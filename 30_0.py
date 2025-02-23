#!/usr/bin/python
# -*- coding: utf-8 -*-

import ipaddress
net = ipaddress.ip_network('192.168.1.0/27')
for a in net:
    print(a)
    
net[0]
net[1]

ip = ipaddress.ip_address('127.45.67.69')
ip in net


from urllib import request, parse

url = 'http://example.com/script.php'

parms = {
    'var1' : 'value1',
    'var2' : 'value2'
}

querystring = parse.urlencode(parms)

u = request.urlopen(url + '?' + querystring)
resp = u.read()


from urllib import request, parse

url = 'http://example.com/script.php'

parms = {
    'name1' : 'value1',
    'name2' : 'value2'
}

querystring = parse.urlencode(parms)

u = request.urlopen(url, querystring.encode('ascii'))
resp = u.read()


from urllib import request, parse
# ...

headers = {
    'User-agent' : 'My Phyton Browser'
}
req = request.Request(url, querystring.encode('ascii'), headers = headers)

u = request.urlopen(req)
resp = u.read()


from socketserver import BaseRequestHandler, TCPServer 

class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Client: ', self.client_address)
        
        while True:
            msg = self.request.recv(8192)
            
            if not msg:
                break
            self.request.send(msg)

if __name__ == '__main__':
    serv = TCPServer((' ', 10000), EchoHandler)
    serv.serve_forever()


from socket import socket, AF_INET, SOCK_STREAM
s = socket(AF_INET, SOCK_STREAM) 
s.connect(('localhost', 10000)) 
s.send(b'12345') 
s.recv(8192)


from socketserver import ThreadingTCPServer 

# ...

if __name__ == '__main__':
    serv = ThreadingTCPServer((' ', 10000), EchoHandler)
    serv.serve_forever()


from multiprocessing.connection import Listener
import traceback 

def echo_client(conn):
    try:
        while True:
            msg = conn.recv()
            conn.send(msg)
    except EOFError:
        print('We Are Closed') 

def my_echo_server(address, authkey):
    serv = Listener(address, authkey=authkey)
    while True:
        try:
            client = serv.accept()
            echo_client(client)            
        except Exception:
            traceback.print_exc() 

my_echo_server((' ', 10000), authkey = b‘peekaboo‘)


from multiprocessing.connection import Client
c = Client(('localhost', 10000), authkey = b'secret')
c.send('12345')
c.recv()
c.send(55)
c.recv()
