# -*- coding: utf-8 -*-
import traceback
import socket
import json
import time

class Machine:

    last_call = None
    last_status = None

    def __init__(self, host, port):
        self.host = host
        self.port = port
        
    def __recv_end(self, the_socket):
    # Recipe from http://code.activestate.com/recipes/408859-socketrecv-three-ways-to-turn-it-into-recvall/
    
        End = '\x00'
        total_data = []
        data = ''
        while True:
            data = the_socket.recv(8192)
            if End in data:
                total_data.append(data[:data.find(End)])
                break
            total_data.append(data)
            if len(total_data) > 1:
                #check if end_of_data was split
                last_pair = total_data[-2] + total_data[-1]
                if End in last_pair:
                    total_data[-2] = last_pair[:last_pair.find(End)]
                    total_data.pop()
                    break
        return ''.join(total_data)

    def call(self, cmd, param=''):
        command = json.dumps({'command': cmd, 'parameter': param})
        with SocketConnection(self.host,self.port) as skt:
            skt.sendall(command)
            resp = self.__recv_end(skt)
            data = json.loads(resp)
        self.last_status = data['STATUS'][0]
        self.last_call = time.localtime(self.last_status['When'])
        return data

class SocketConnection:
    skt = None
    
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def __enter__(self):
        self.skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.skt.connect((self.host, self.port))
        return self.skt
        
    def __exit__(self, type, value, traceback):
        self.skt.close()

