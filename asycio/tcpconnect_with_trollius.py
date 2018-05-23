import socket
import select
import logging as log
import trollius as asyncio
from trollius import From, Return, Future
from functools import partial

log.basicConfig(level=log.DEBUG, format='%(asctime)s:'+log.BASIC_FORMAT)
logger = log.getLogger(__name__)

@asyncio.coroutine
def selector(fno, i, fn, *args, **kwargs):
    while True:
        if fno in select.select([fno], [fno], [fno])[i]:
            raise Return(fn(*args, **kwargs))
        else: yield

@asyncio.coroutine
def connect_coro(future, url):
    sock = socket.socket()
    fno = sock.fileno()
    logger.debug(fno)
    sock.connect((url,80))
    sock.setblocking(0) 
    yield From(selector( fno, 1, sock.send,'GET / HTTP/1.0\n\n\n'))
    result = yield From(selector(fno, 0, sock.recv,2000))
    future.set_result(result)

def got_result(future):
    print future.result()

future1 = Future()
future2 = Future()


jobs = [
    connect_coro(future1,'ledge.co.za'),
    connect_coro(future2, 'google.com')
]

future1.add_done_callback(got_result)
future2.add_done_callback(got_result)

loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.wait(jobs)
)
loop.close()
