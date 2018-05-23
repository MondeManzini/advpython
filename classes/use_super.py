import collections
import logging

logging.basicConfig(level='INFO')

class LoggingDict(dict):
    # Simple example of extending a builtin class
    def __setitem__(self, key, value):
        logging.info('Setting %r to %r' % (key, value))
        super(LoggingDict, self).__setitem__(key, value)

class LoggingOD(LoggingDict, collections.OrderedDict):
    # Build new functionality by reordering the MRO
    pass

ld = LoggingDict([('red', 1), ('green', 2), ('blue', 3)])
print ld
ld['red'] = 10

ld = LoggingOD([('red', 1), ('green', 2), ('blue', 3)])
print ld
ld['red'] = 10
print '-' * 20

