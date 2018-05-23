import socket
import select
import logging as log
log.basicConfig(level=log.DEBUG, format='%(asctime)s:'+log.BASIC_FORMAT)
logger = log.getLogger(__name__)

def connect_coro(url):
    sock = socket.socket()
    fno = sock.fileno()
    logger.debug(fno)
    sock.connect((url,80))
    sock.setblocking(0) 
    while True:
    	yield
    	if fno in select.select([fno], [fno], [fno])[1]:
	    logger.debug('sending to ' + url)
	    sock.send('GET / HTTP/1.0\n\n\n')
            break
    while True:
        yield
        log.debug(select.select([fno], [fno], [fno]))
        if fno in select.select([fno], [fno], [fno])[0]:
            print sock.recv(2000)
            break
jobs = [
    connect_coro('ledge.co.za'),
    connect_coro('google.com')
]
while jobs:
    for job in jobs:
        try: 
            next(job)
        except StopIteration:
            jobs.remove(job)
