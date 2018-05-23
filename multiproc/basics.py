import multiprocessing
import os

def worker():
    """worker function"""
    print 'Worker', os.getpid()
    return

print 'test=-----'
if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()
