#C:\Users\Logan\Desktop

import socket

print ("Welcome to PyChat v 0.56.\nCommands:\n\n-Type q to quit.\n\nKnown bugs:\n-Entering your username before the server is activated will cause the shell to crash\n-Entering a blank line in chat will cause you to be unable to type anything.")

print ('\nEnter username\n')                  
username = input("->>")                     # input username

def Main():
    host = '127.0.0.1'                      # declare server
    port = 5000                             # declare port

    s = socket.socket()                     # bind a variable to create a socket
    s.connect((host, port))                 # connect to server

    s.send(username.encode('utf-8'))        # send username

    message = input(username + ': ')        # input message with username as a prompt
    while message != 'q':                   # if message == q then quit
        s.send(message.encode('utf-8'))     # send UTF-8 encoded message
        data = s.recv(1024).decode('utf-8') # recieve message from server and set it to 'data'
        print (data + '\n')                 # print message from server
        message = input(username + ": ")    # input another message
    s.close                                 # close connection
    
Main()
	
if __name__ == '__main__':                  # loop program
    Main()

