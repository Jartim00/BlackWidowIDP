#!/usr/bin/python
import socket
import threading
import json
from servo import Servo
from time import sleep

## App Server for sending diagnostic data
class AppServer(object):
    #  @param host The host address to bind to. Leave empty for letting in anyone
    #  @param port The port for the server
    def __init__(self,host,port):
        self.HOST = host                 # Symbolic name meaning all available interfaces
        self.PORT = port              # Arbitrary non-privileged port
        self.clients = []
        self.servos = []

    ## Starts the socket and accepts clients
    def start(self):
        self.running = True
        #start server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((self.HOST, self.PORT))
        s.listen(5)
        #start accepting clients
        while self.running:
            self.acceptClient(s)

    ## Disconnects the clients and stops the server
    def stop(self):
        self.disconnectClients()
        self.running = False

    ## Accepts a client
    #  @param serverSocket The socket for accepting the client.
    def acceptClient(self,serverSocket):
        conn, addr = serverSocket.accept()
        # worker = threading.Thread(target=self.communicate,args=(conn,))
        self.clients.append({'clientId':len(self.clients) + 1,
                            'conn': conn,
                            'addr': addr#,
                            # 'worker': worker
                            })
        print 'Connected by', addr
        # worker.start()

    ## Closes all client sockets
    def disconnectClients(self):
        for client in self.clients:
            conn = client['conn']
            conn.close()

    ## Sends a JSON message to all clients.
    #  @param appJSON a JSON string
    def sendJSONToAll(self,appJSON):
        for client in self.clients:
            conn = client['conn']
            try:
                conn.sendall(appJSON + "\n")
            except:
                print "can't send app JSON to client"
        # while self.running:
        #     # data = conn.recv(1024)
        #     # if not data: break
        #     print "appserver sending...."
        #     jsonData = self.getServoJSON()
        #     conn.sendall(jsonData)
        #     print "appserver sent...."
        #     for servo in self.servos:
        #         servo.updateVariables()
        #     print "updated servos..."
        #     sleep(0.1)
        # conn.close()

    # def setServos(self,servos):
    #     self.servos = servos

if __name__ == "__main__":
    appcomm = AppServer("",1337)
    appcomm.start()
