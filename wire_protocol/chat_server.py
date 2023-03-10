import socket 
import threading
import re
from commands import *

mutex_unsent_messages = threading.Lock()
mutex_accounts = threading.Lock()
mutex_active_accounts = threading.Lock()

class ChatServer:
    '''Initializes the Chat Server that sets up the datastructures to store user accounts and messages.'''
    def __init__(self, test=False):
        if not test:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind(ADDR)

        self.unsent_messages = {} # {username: [msg1, msg2, msg3]}
        self.accounts = [] # [username1, username2, username3]
        self.active_accounts = {} # {username: addr}

    '''Logins the user by checking the list of accounts stored in the server session.'''
    def login_user(self, conn, username, addr):
        logged_in = False
        
        print(f"[{addr}] {username}")

        if username not in self.accounts:
            self.send(conn, NOTIFY, "Username does not exist.")
            return (None, None)
        
        # Checks if user is logged in already
        if username in self.active_accounts:
            self.send(conn, NOTIFY, "User is already logged in.")
            return (None, None)

        # Log in user
        mutex_active_accounts.acquire()
        self.active_accounts[username] = addr
        mutex_active_accounts.release()

        logged_in = True
        
        self.send(conn, NOTIFY, LOGIN_SUCCESSFUL)
        return (username, logged_in)

    '''Registers user given the client's input and compares with existing account stores.'''
    def register_user(self, conn, username, addr):
        registered = False
        
        print(f"[{addr}] {username}")

        if username in self.accounts:
            self.send(conn, NOTIFY, "Username already exists.")
            return (None, None)
        
        mutex_active_accounts.acquire()
        self.active_accounts[username] = addr
        mutex_active_accounts.release()

        mutex_accounts.acquire()
        self.accounts.append(username)
        mutex_accounts.release()

        mutex_unsent_messages.acquire()
        self.unsent_messages[username] = []
        mutex_unsent_messages.release()

        registered = True

        self.send(conn, NOTIFY, LOGIN_SUCCESSFUL)
        return (username, registered)

    '''Handles the clients sending messages to other clients. Assumes recipient is already registered.'''
    def record_chat_message(self, conn, sender, recipient, msg):
        mutex_unsent_messages.acquire()
        self.unsent_messages[recipient].append((sender, msg))
        mutex_unsent_messages.release()
        self.send(conn, NOTIFY, "Message sent!")
    

    '''Handles the clients receiving messages sent to them. Delivers the message to the clients then clears sent messages'''
    def send_unsent_messages(self, conn, addr):
        for recipient in self.unsent_messages:
            messages = self.unsent_messages[recipient]

            if recipient in self.active_accounts:
                recipient_addr = self.active_accounts[recipient]
                if recipient_addr == addr:
                    print("waiting for mutex")
                    mutex_unsent_messages.acquire()
                    print("got mutex")
                    for message in messages:
                        text = message[0] + " sends: " + message[1]
                        self.send(conn, NOTIFY, text)
                    self.unsent_messages[recipient] = []
                    print("mutex released")
                    mutex_unsent_messages.release()

                    # Assumes user is only logged into one terminal
                    self.send(conn, NO_MORE_DATA, " ")

    '''Deletes the account for the client requesting the deletion. Precondition: we have already checked that the username corresponds to the user who was logged in at the time'''
    def delete_account(self, conn, username):
        mutex_active_accounts.acquire()
        del self.active_accounts[username]
        mutex_active_accounts.release()

        mutex_unsent_messages.acquire()
        del self.unsent_messages[username]
        mutex_unsent_messages.release()

        mutex_accounts.acquire()
        self.accounts.remove(username)
        mutex_accounts.release()

        self.send(conn, NOTIFY, DELETION_SUCCESSFUL)
    

    '''Logs out the user. Assumes that the user is already logged in and is displayed as an active account. Precondition: we have already checked that the username corresponds to the user who was logged in at the time'''
    def logout(self, conn, username):

        mutex_active_accounts.acquire()
        del self.active_accounts[username]
        mutex_active_accounts.release()

        self.send(conn, NOTIFY, LOGOUT_SUCCESSFUL)
    
    '''Includes the core logic to handle all messages sent by the client'''
    def handle_client(self, conn, addr):
        print(f"[NEW CONNECTION] {addr} connected.")
        logged_in = False

        while True:
            parsed_message = self.receive(conn)

            print(parsed_message)
            purpose = parsed_message[PURPOSE]
            if purpose == LOGIN:
                username = parsed_message[BODY]
                username, logged_in = self.login_user(conn, username, addr)
            elif purpose == REGISTER:
                username = parsed_message[BODY]
                username, logged_in = self.register_user(conn, username, addr)
            elif purpose == SEND_MESSAGE:
                if not logged_in:
                    self.send(conn, NOTIFY, "You must be logged in to send a message.")
                    continue
                sender = parsed_message[SENDER]
                recipient = parsed_message[RECIPIENT]
                msg = parsed_message[BODY]
                self.record_chat_message(conn, sender, recipient, msg)
            elif purpose == PULL_MESSAGE:
                if not logged_in:
                    self.send(conn, NOTIFY, "You must be logged in to receive messages.")
                    continue

                self.send_unsent_messages(conn, addr)
            elif purpose == CHECK_USER_EXISTS:
                username = parsed_message[BODY]
                if username in self.accounts:
                    self.send(conn, NOTIFY, "User exists.")
                else:
                    self.send(conn, NOTIFY, USER_DOES_NOT_EXIST)
            
            elif purpose == DELETE_ACCOUNT:
                if not logged_in:
                    self.send(conn, NOTIFY, "You must be logged in to delete an account.")
                    continue
                username = parsed_message[BODY]

                self.delete_account(conn, username)
            
            elif purpose == SHOW_ACCOUNTS:
                username = parsed_message[BODY]
                matched_accounts = "\nUsers:\n"
                no_accounts_found_length = len(matched_accounts)
            
                for account in self.accounts:
                    if account.startswith(username):
                        matched_accounts += account + "\n"
                
                if len(matched_accounts) == no_accounts_found_length:
                    self.send(conn, NOTIFY, USER_DOES_NOT_EXIST)
                else:
                    self.send(conn, NOTIFY, matched_accounts)

            elif purpose == LOGOUT:
                if not logged_in:
                    self.send(conn, NOTIFY, "You must be logged in to log out.")
                    continue

                username = parsed_message[BODY]
                self.logout(conn, username)
                logged_in = False

    '''Creates the message to be parsed according to the designed wire protocol'''
    def create_message(self, purpose, body, recipient=None, sender=None):
        data=PURPOSE + SEPARATOR + purpose
        if recipient and sender:
            data += SEPARATOR + RECIPIENT + SEPARATOR + recipient
            data += SEPARATOR + SENDER + SEPARATOR + sender
        if body:
            length = len(body)
            data += SEPARATOR + LENGTH + SEPARATOR + str(length)
            data += SEPARATOR + BODY + SEPARATOR + body
        
        return data
    
    '''Sends the message to the client.'''
    def send(self, conn, purpose, body, recipient=None, sender=None):
        msg = self.create_message(purpose, body, recipient, sender)
        try:
            encoded_message = msg.encode(FORMAT)
            if len(encoded_message) > MAX_BANDWIDTH:
                return False
            
            encoded_message = encoded_message.ljust(MAX_BANDWIDTH, b'0')
            conn.send(encoded_message)
        except:
            raise ValueError
        
        return True

    '''Receives and parses the message from clients per the designed wire protocol.'''
    def parse_message(self, full_message):
        split_message = full_message.split("/")
        parsed_message = {}
        i = 0
        while i < len(split_message):
            part = split_message[i]
            if BODY != part:
                parsed_message[part] = split_message[i+1]
                i += 1
            else:
                body = "/".join(split_message[i+1:])
                length = int(parsed_message[LENGTH])
                parsed_message[part] = body[:length]
                break
            i += 1
        print(parsed_message)
        return parsed_message
    

    '''Return a dictionary representation of the message'''
    def receive(self, conn):
        try:
            full_message = conn.recv(MAX_BANDWIDTH).decode(FORMAT)
            return self.parse_message(full_message)
        except:
            return self.receive(conn)

        
    '''Runs the server and launches the threads for all new client connections.'''
    def start(self):
        self.server.listen()
        print(f"[LISTENING] Server is listening on {SERVER}")
        while True:
            conn, addr = self.server.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
