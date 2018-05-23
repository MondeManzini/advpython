from tornado.tcpserver import TCPServer
from tornado.ioloop  import IOLoop
from tornado.httpclient import AsyncHTTPClient
from tornado.httpclient import HTTPRequest
from tornado import gen
import json
import logging

logging.basicConfig(level=logging.DEBUG, BASIC_FORMAT='%(asctimes):' + logging.BASIC_FORMAT)
logger = logging.getLogger(__name__)

class UrlServer(TCPServer):
    def handle_stream(self, stream, address):
        self._stream = stream
        self._read_line()

    def _read_line(self):
        self._stream.read_until('\n', self._handle_read)

    @gen.coroutine
    def _handle_read(self, data_in):
        self._stream.write(data_in.upper())
        request = HTTPRequest(
            url='http://' + data_in,
            method="GET"
        )
        response = yield gen.Task(
            AsyncHTTPClient().fetch,request)
        logger.debug(response)
        try:
            self._stream.write(bytes(response.body)+'\n')
        except:
            logger.exception('Exception while writing')
        self._read_line()

if __name__ == '__main__':
    UrlServer().listen(8888)
    IOLoop.current().start()
