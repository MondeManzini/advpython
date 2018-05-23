import socket
from contextlib import contextmanager

@contextmanager
def ContextSocket():
    print 'entering socket'
    sock = socket.socket()
    try:
        yield sock
    finally:
        print 'closing'
        sock.close()

if __name__ == '__main__':
    with ContextSocket() as sock:
        sock.connect(('google.com',80))
        sock.send('GET / HTTP/1.0\n\n\n')
        raise Exception, 'blah'
        print sock.recv(8192)
