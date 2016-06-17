#!/usr/bin/python
# Echo client program
import socket

HOST = '10.1.1.1'    # The remote host
PORT = 1337              # The same port as used by the server

def talkWithServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    try:
        while True:
            #msg = raw_input(">")
            #s.sendall(msg)
            data = s.recv(2048)
            print 'Received', repr(data)
    except KeyboardInterrupt:
        s.close()
    finally:
        s.close()

if __name__ == "__main__":
    talkWithServer()
