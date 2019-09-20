#! /usr/bin/python
import socket 
ip = raw_input("Enter the Ip address: ")
port = input("Enter the port number: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREM)
if sock.connect_ex((ipport)):
	print "port",port,"is closed"
else:
	print"Port",port,"is open"