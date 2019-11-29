import socket
from threading import Thread
import logging as log
RUNNING = True


class TCPServer(Thread):
    def __init__(self):
        super(TCPServer, self).__init__()
        self.setDaemon(1)
        self.start()
        raw_input('press enter to quit')

    def run(self):
        server_sock = socket.socket()
        try:
            server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_sock.bind(('localhost', 10001))
            server_sock.listen(5)
            while RUNNING:
                (sock, ip) = server_sock.accept()
                TCPWorker(sock)
        except:
            log.exception('main loop')
        finally:
            server_sock.close()


class TCPWorker(Thread):
    def __init__(self, sock):
        super(TCPWorker, self).__init__()
        self.sock = sock
        self.setDaemon(1)
        self.start()

    def run(self):
        sock = self.sock
        sock.send('Welcome to the ultimate server\n\n')
        while RUNNING:
            line = sock.recv(8192)
            print line.upper()
            if line.startswith('quit'):
                break
        sock.close()


if __name__ == '__main__':
    TCPServer()
