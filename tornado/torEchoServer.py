from tornado.tcpserver import TCPServer
from tornado.ioloop  import IOLoop
from tornado.httpclient import AsyncHTTPClient
from tornado.httpclient import HTTPRequest
from tornado import gen 
from trollius import From
from functools import partial
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s'+logging.BASIC_FORMAT, filename='torecho.log')
logger = logging.getLogger(__name__)

class EchoServer(TCPServer):
    def handle_stream(self, stream, address):
        self.stream = stream
        logger.debug('new connection' + str(address))
        self._read_line()

    def _read_line(self):
        self.stream.read_until('\n', self._handle_read)

    def _handle_read(self, data_in):
	stream = self.stream
        stream.write(data_in.upper())
        self._read_line()

if __name__ == '__main__':
    EchoServer().listen(8001)
    IOLoop.current().start()
