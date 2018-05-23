from tornado.tcpserver import TCPServer
from tornado.ioloop  import IOLoop
from tornado.httpclient import AsyncHTTPClient
from tornado.httpclient import HTTPRequest
from tornado import gen 
from trollius import From
from functools import partial
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s'+logging.BASIC_FORMAT)
logger = logging.getLogger(__name__)

class UrlServer(TCPServer):
    def handle_stream(self, stream, address):
        logger.debug('new connection' + str(address))
        self._read_line(stream)

    def _read_line(self,stream):
        handle = partial(self._handle_read, stream)
        stream.read_until('\n', handle)

    @gen.coroutine
    def _handle_read(self, stream, data_in):
        stream.write(data_in.upper())
        http_client = AsyncHTTPClient()
        try:
            response = yield From(http_client.fetch("http://" + data_in.strip()))
            logger.debug(response)
            stream.write(bytes(response) + "\n")
        except:
            logger.exception('hndle error')
        self._read_line(stream)

if __name__ == '__main__':
    UrlServer().listen(8001)
    IOLoop.current().start()
