import sys


class Logger(object):
    def __init__(self, filename, new=False):
        print("\n I am inside Logger class  constructor def __init__(self, filename, new=False)")
        self.terminal = sys.stdout
        self.filename = filename
        if new:
            self.logfile = open(filename, "w")
        else:
            self.logfile = open(filename, "a")

    def write(self, message):
         self.terminal.write(message)
         self.logfile.write(message)

    #AttributeError: 'Logger' object has no attribute 'flush'
    #sys.stdout.flush()
    def flush(self):
         pass

    def close(self):
         print("\n I am inside logger class def close(self)")
         self.logfile = open(self.filename, "w")
         # ValueError: I/O operation on closed file
         # self.logfile.close()
