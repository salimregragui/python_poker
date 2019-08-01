#!/usr/bin/env python3
"""Script for client."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import os
import player
import json

first_receive = True
msg_list = []
def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.append(msg)
            os.system("cls")
            for i,msg in enumerate(msg_list):
                print(msg)
        except OSError:  # Possibly client has left the chat.
            break


def send():  # event is passed by binders.
    """Handles sending of messages."""
    data = {
        "name" : p.name,
        "money" : p.money,
        "status" : p.status
    }
    data_string = json.dumps(data) #data serialized
    print(data_string)

    while True:
        try:
            client_socket.send(bytes(data, "utf8"))
        except:
            print(data_string)
            os.system("exit")
        # if msg == "quit":
        #     client_socket.close()
        #     break


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    send()

#----Now comes the sockets part----
HOST = input('Enter host: ')
PORT = input('Enter port: ')
NAME = input("Your name : ")
p = player.Player(1000, NAME)
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
send()