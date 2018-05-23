Tornado is simple,
fast 

Revolves around the ioloop registers itself with os

select, poll kqueue

callback style

def step(ca):
    #do stuff
    
cross platftom on various Unix like operating systems
runs on windows,but not a supported platform

iostream convenient utility class each connection that you create can be an instance of iostream, register with ioloop

read_until_regex(regex, callback)

read_until(delimiter, callback)
read(num_bytes, callback, streaming_callback=None)
read_until_close(callback, streaming_callback=None)

ampq ?

SSLIOStream drop in replacement for IOStream

tornado.stack_context.StackContext

IOLoop.instance()
 	.add_handler(fdm handler,events)a #events are read write error, which of these do I want to be notified of
        .update_handler #change which events notify
         remove_handler

multiprocessing.reduction
   pickle socket and pass ir to another process.

#main process
from multiprocessing.reduction import reduce_handle

h = reduce_handle(client_socket.fileno())

pipe_to_worker.send(h) #instance of multiprocessing.Pipe()

# worker
from multiprocessing.reduction import reduce_handle
client_socket = socket.fromfd(fd, socket.AF_INET, socket.SOC_STREAM)
client_socket.send("hello from the worker process\r\n")

h = pipe.recv()

