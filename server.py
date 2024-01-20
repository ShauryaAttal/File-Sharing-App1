import socket
from threading import Thread
from tkinter import *
from tkinter import ttk

IP_ADDRESS = "127.0.0.1"
PORT = "5501"
SERVER = None

clients=[]

def setup():
    global SERVER, PORT, IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS,PORT))
    SERVER.listen()

setup()