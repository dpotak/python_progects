from wsgiref.simple_server import server_version
import socket

socket_server = socket.socket()

name = input()
socket_server.connect(())