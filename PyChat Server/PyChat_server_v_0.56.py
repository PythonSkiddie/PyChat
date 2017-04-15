import socket

print("Welcome to PyChat Server version 0.60. Type 'help' for commands or 'setup' when ready to start server.\n")
choice = input(">>>")

if choice == "help" | "help".upper():
	help()
	
def Main():
	s = socket.socket()
	
		
	host = input("Enter the host IP address: ")							  
	stport = int(input("Enter the starting point for the port range: "))  
	enport = int(input("Enter the end point for the port range: "))		  
	port = range(stport, enport)										  
	clinumber = int(input("Enter the max number of clients allowed: "))
	
	# Defining server IP address, port range, and max connections allowed.
	
	s.bind((host, port))
	s.listen(clinumber)
	
	c, addr = s.accept()
	username = s.recv(1024).decode("utf-8")
	print('Got connection from {}, {}'.format(host, port))
	
def help():
	print("Commands:\n")
	print("kick [username] [ip address]\tKick a user")
	print("ban [\"username\"] [\"ip address\"] [time in hours]\tBan a user")
	print("announce [\"message\"]\tAnnounce a message with the username \"ADMIN\"")
	print("ip [\"username\"]\tshow username")

	
	# use this code to build new code
	
#print ('Welcome to PyChat Server v 0.56. When a client connects, their \nIP address is shown, along with the port number they connected through.')
#
#def Main():
#    host = '127.0.0.1'
#    port = 5000
#
#    s = socket.socket()
#    s.bind((host, port))
#    
#	connumber = int(input('Number of clients allowed: '))
#	
#    s.listen(connumber)
#    
#    c, addr = s.accept()
#    username = c.recv(1024).decode('utf-8')					# Recieve username of connected client
#    print ('Got connection from: ' + str(addr))				# print the IP address and connected port of client
#    if True:									 
#        print ('Username: ' + username)					# Show connected client's username
#    while True:								
#        data = c.recv(1024).decode('utf-8')					# Recieve data from client(s)
#        if not data:
#            break
#        print (username + ': '  + data)
#        data = '+'								# Sending confirmation to the client that a message was recieved
#        c.send(data.encode('utf-8'))
#    c.close()
#
#if __name__ == '__main__':
#    Main()
	
	
	# Todo:
	# 
	# -Add simple admin commands (i.e: kick [username], ban [username] [time], help, broadcast, etc...)
	#
	# Admin commands so far:
	# 
	# ban [username], [time] (time is in hours)
	# kick [username] (might have to add _thread module)
	# help([topic])
	# broadcast "[text]" (have to make it noticable, maybe ADMIN: or ADMINBROADCAST: for username)
	# ip [username] (show IP of user)
	# port [port number] (add a port that can be connected to)
	
	# Tasks done:
	#
	# -Add a 'Number of connections allowed' option when starting a server.
