import socket 
import select
import sys

TCP_IP = 'localhost' 
TCP_PORT = 5005 
BUFFER_SIZE = 1024
#chatClient is created using a socket. SOCK_STREAM is used in TCP for constant flow
chatClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connects using given TCP_IP and TCP_PORT variables
chatClient.connect((TCP_IP,TCP_PORT)) 

print('Enter username')
name = input()
while True:
    #This holds input streams
    sockets_list = [sys.stdin, chatClient] 
    read_sockets,write_socket,error_socket = select.select(sockets_list,[],[])

    
    for socks in read_sockets:

        #Client receives message from server, usually from broadcast
        if socks == chatClient: 
            message = socks.recv(BUFFER_SIZE) 
            print(message.decode())
        else:
            #User sends message to server, which broadcasts to other clients
            message = sys.stdin.readline() 
            chatClient.send(message.encode()) 
            sys.stdout.write("<" + name + ">")

            #A copy of user's input is displayed
            sys.stdout.write(message) 
            sys.stdout.flush() 
chatClient.close() 
