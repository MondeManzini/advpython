#main process
from multiprocessing.reduction import reduce_handle

h = reduce_handle(client_socket.fileno())

pipe_to_worker.send(h) #instance of multiprocessing.Pipe()

# worker
from multiprocessing.reduction import reduce_handle
client_socket = socket.fromfd(fd, socket.AF_INET, socket.SOC_STREAM)
client_socket.send("hello from the worker process\r\n")

h = pipe.recv()

