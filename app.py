#Import library
import socket

#Creates instance of 'Socket'
sock = socket.socket()

hostname = 'hostname' #Server IP/Hostname
port = 6969 #Server Port
BUFFER_SIZE = 1024 #Buffer size for data to be received

sock.connect((hostname,port)) #Connects to server

while True:
    x = input("Enter message: ")
    sock.send(x.encode()) #Encodes and sends message (x)
    data = sock.recv(BUFFER_SIZE) #Receive incoming data and store in buffer
    print(f"Received data {data}")
