"""
Implements class dupfile. This is a variant on file that won't actually change
the fs representation of a file unless you write a different contents, used
to avoid rebuilding the bridge on every call to setup.py
"""
import os

def cmpfile(fn1, fn2):
    return open(fn1).read() == open(fn2).read()

class dupfile:
    def __init__(self, fname, mode):
        self.fname = fname
        self.done = 0
        self.tfile = fname + ".wrk"
        self.mode = mode

        if mode == 'w':
            self.fp = open(self.tfile, "w")
        else:
            self.fp = open(self.fname, mode)


    def read(self, bytes=None):
        if bytes is None:
            return self.fp.read()
        else:
            return self.fp.read(bytes)

    def write(self, bytes):
        self.fp.write(bytes)

    def flush(self):
        self.fp.flush()

    def close(self):
        self.fp.close()
        self.fp = None
        if self.mode == 'w':
            if os.path.exists(self.fname) and cmpfile(self.tfile, self.fname):
                os.unlink(self.tfile)
            else:
                os.rename(self.tfile, self.fname)
        self.done = 1

    def __del__(self):
        if self.done:
            return
        if self.mode == 'w':
            if self.fp is not None:
                self.fp.close()
                self.fp = None
            if os.path.exists(self.fname) and cmpfile(self.tfile, self.fname):
                os.unlink(self.tfile)
            else:
                os.rename(self.tfile, self.fname)
