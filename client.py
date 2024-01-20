import socket
from threading import Thread
from tkinter import *
from tkinter import ttk

IP_ADDRESS = "127.0.0.1"
PORT = "5501"
SERVER = None
bufferSize = 2048
name = None
listBox = None
textArea = None
labelChat = None
textMessage = None


def openChatWindow():
    window = Tk()
    window.title("Messenger")
    window.geometry("550x400")

    namelabel = Label(window, text="Enter your name", font=("Helvetica", 12))
    namelabel.place(x=10,y=10)

    nameEntry = Entry(window, width=20, font=("Helvetica", 12))
    nameEntry.place(x=140,y=10)
    nameEntry.focus()

    connect = Button(window, text="Connect to server", font=("Helvetica",10))
    connect.place(x=350,y=10)

    line = ttk.Separator(window,orient="horizontal")
    line.place(x=0,y=40, relwidth=1, height=0.25)

    activeuser = Label(window, text="Active Users", font=("Helvetica", 12))
    activeuser.place(x=10, y = 50)

    listBox = Listbox(window, height = 6, width=58, activestyle="dotbox", font=("Helvetica", 12))
    listBox.place(x=10,y=70)

    sc1 = Scrollbar(listBox)
    sc1.place(relheight=1, relwidth=0.02, relx = 0.98)
    sc1.config(command=listBox.yview)

    connectuser = Button(window, text="Connect to user", font=("Helvetica",10))
    connectuser.place(x=230,y=190)

    disconnect = Button(window, text="Disconnect from User", font=("Helvetica",10))
    disconnect.place(x=340,y=190)

    refresh = Button(window, text="Refresh", font=("Helvetica",10))
    refresh.place(x=480,y=190)

    chatwindow = Label(window, text="Chat Window", font=("Helvetica", 12))
    chatwindow.place(x=10, y=210)
    
    chatBox = Text(window, height = 6, width=58, font=("Helvetica", 12))
    chatBox.place(x=10,y=230)

    sc2 = Scrollbar(chatBox)
    sc2.place(relheight=1, relwidth=0.02, relx = 0.98)
    sc2.config(command=chatBox.yview)

    attach = Button(window, text="Attach File and Send", font=("Helvetica",10))
    attach.place(x=10,y=350)

    fileEntry = Entry(window, width=20, font=("Helvetica", 12))
    fileEntry.place(x=160,y=352)
    fileEntry.focus()

    send = Button(window, text="Send", font=("Helvetica",10))
    send.place(x=380,y=350)

    filePath = Label(window,text="", fg="blue", bg="yellow", font=("Helvetica",12))
    filePath.place(x=10,y=380)

    window.mainloop()

def setup():
    global SERVER, PORT, IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS,PORT))
    
    openChatWindow()

setup()
