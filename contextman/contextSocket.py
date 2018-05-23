import socket
class ContextSocket(socket.socket):
    def __enter__(self):
        print 'entering socket'
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print 'closing'
        self.close()

if __name__ == '__main__':
    with ContextSocket() as sock:
        sock.connect(('google.com',80))
        sock.send('GET / HTTP/1.0\n\n\n')
        print sock.recv(8192)
