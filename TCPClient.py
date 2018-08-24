
"""Script for Tkinter GUI chat client."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter


def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = clientSocket.recv(BUFSIZ).decode("utf8")
            msgList.insert(tkinter.END, msg)
        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = myMsg.get()
    myMsg.set("")  # Clears input field.
    clientSocket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        clientSocket.close()
        top.quit()


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    myMsg.set("{quit}")
    send()


top = tkinter.Tk()
top.title("Chatter")

msgsFrame = tkinter.Frame(top)
myMsg = tkinter.StringVar()  # For the messages to be sent.
myMsg.set("Type your messages here.")
# To navigate through past messages.
scrollbar = tkinter.Scrollbar(msgsFrame)
# Following will contain the messages.
msgList = tkinter.Listbox(msgsFrame, height=15,
                           width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msgList.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msgList.pack()
msgsFrame.pack()

entryField = tkinter.Entry(top, textvariable=myMsg)
entryField.bind("<Return>", send)
entryField.pack()
sendButton = tkinter.Button(top, text="Send", command=send)
sendButton.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)

# ----Now comes the sockets part----
HOST = input('Enter host: ')
PORT = input('Enter port: ')
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(ADDR)

receiverThread = Thread(target=receive)
receiverThread.start()
tkinter.mainloop()  # Starts GUI execution.
