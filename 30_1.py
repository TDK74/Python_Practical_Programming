#!/usr/bin/python
# -*- coding: utf-8 -*-

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
