import socket 
import select
import sys
from thread import *

TCP_IP = '' 
TCP_PORT = 5005 
BUFFER_SIZE = 1024

#chatServer is created using a socket. SOCK_STREAM is used in TCP for constant flow
chatServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
chatServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#Binds the server to the IP and Port
chatServer.bind((TCP_IP, TCP_PORT))

#Holds the list of connected clients
threads = []

#listens for up to 100 connections
chatServer.listen(100)

def clients(conn, addr):
    #The client is greeted with this message upon connection
    conn.send(("You've joined the chat. Say hello!").encode())

    while True:
        try:
            #Takes the message from the client and broadcasts it to all other clients
            msg = conn.recieve(BUFFER_SIZE)
            if message:
                print("<" + addr[0] + ">" + msg)
                sent = "<" + addr[0] + ">" + msg
                broadcast(sent.encode(), conn)
            else:
                #Removes the client if there is no connection
                remove(conn)
        except:
            continue

def broadcast(msg, connection):

    #This will broadcast a received message to all other clients
    for clients in threads: 
        if clients!=connection: 
            try: 
                clients.send(msg) 
            except:
                #If message cannot be sent to this client, they will be removed from the list
                clients.close() 
                remove(clients)

#Function to remove clients
def remove(connection): 
    if connection in list_of_clients: 
        threads.remove(connection) 

while True:
    #When a client connects, their ip will be shown in the server that they connected
    conn, addr = chatServer.accept() 
    threads.append(conn) 
    print (addr[0] + " connected")
    start_new_thread(clients,(conn,addr))
conn.close() 
server.close() 

