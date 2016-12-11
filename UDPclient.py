from socket import *
serverName = str(raw_input('Enter server IP: '))
serverPort = int(input('Enter server port: '))
clientSocket = socket(AF_INET, SOCK_DGRAM)
print('Connecting to: ' + serverName)
while True:
	message = raw_input('> ')
	if message == exit:
		clientSocket.close()
	clientSocket.sendto(message, (serverName, serverPort))
	reply, serverAddress = clientSocket.recvfrom(2048)
	print('# ' + reply)

