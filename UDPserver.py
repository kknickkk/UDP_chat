from socket import *
serverPort = int(input('Enter server port: '))
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
flag = 0
while True:
	message, clientAddress = serverSocket.recvfrom(2048)
	if flag == 0:
		print('Connected to: ' + clientAddress[0])
		flag = 1
	print('# ' + message)
	reply = raw_input('> ')
	serverSocket.sendto(reply, clientAddress)
