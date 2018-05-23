import re
FILENAME = 'config.text'

def file_to_dict(filename):
    return dict(re.findall(
        r'^\s*(\w+)\s*=\s*(\w+)\s*$', 
        open(filename).read(),
        re.M))

class Config(object):

    def __init__(self, filename = FILENAME, read=True):
        self.filename = filename
        if read:
            self.read_config()

    @classmethod
    def from_dict(cls,d, filename = FILENAME):
        instance = cls(filename = FILENAME, read=False)
        instance.config=d
        return instance

    def read_config(self):
        self.config = file_to_dict(self.filename)

    def getval(self,val):
        return self.config.get(val)

    def setval(self,key,val):
        self.config[key]= val

    def write_config(self):
        f = open(self.filename, 'w')
        for item in self.config.items():
            f.write('%s = %s\n' % item)
        f.close()

if __name__ == '__main__':
    print(Config().getval('port'))
