import itertools

def as_unicode(s, encoding='utf-8'):
    typ = type(s)
    if typ is unicode:
        pass
    elif issubclass(typ, unicode):
        s = unicode(s)
    elif issubclass(typ, str):
        s = unicode(s, encoding, 'replace')
    else:
        raise TypeError, 'expecting basestring, not %s' % (typ.__name__,)
    return s


def as_str(s, encoding='utf-8'):
    typ = type(s)
    if typ is str:
        pass
    elif issubclass(typ, str):
        s = str(s)
    elif issubclass(typ, unicode):
        s = s.encode(encoding)
    else:
        raise TypeError, 'expecting basestring, not %s' % (typ.__name__,)
    return s


class RemotePipe(object):
    def __init__(self, runcode, clientfile, netReprCenter, namespace, pool):
        self.runcode = runcode
        self.pool = pool
        self.clientfile = clientfile
        self.namespace = namespace
        self.result = self.namespace['__result__'] = {}
        self.netReprCenter = netReprCenter
        self.netrepr_list = netReprCenter.netrepr_list
        self.sequence = itertools.count()
        self.stdin = RemoteFileLike(self, 'stdin')
        self.stdout = RemoteFileLike(self, 'stdout')
        self.stderr = RemoteFileLike(self, 'stderr')

    def send(self, *args):
        self.clientfile.write(self.netrepr_list(args) + '\n')
        self.clientfile.flush()

    def respond(self, *args):
        self.send('respond', *args)
        
    def expect(self, *args):
        self.pool.push()
        try:
            return self._expect(*args)
        finally:
            self.pool.pop()

    def _expect(self, *args):
        ident = self.sequence.next()
        self.send('expect', ident, *args)
        while ident not in self.result:
            self.runcode(self.clientfile, self.namespace)
        return self.result.pop(ident)


class RemoteFileLike(object):
    softspace = 0
    closed = False
    encoding = 'utf-8'

    def __init__(self, pipe, ident):
        self.pipe = pipe
        self.ident = ident

    def __iter__(self):
        while True:
            rval = self.readline()
            if not rval:
                break
            yield rval

    def write(self, s):
        s = as_unicode(s, self.encoding)
        self.pipe.expect('RemoteFileLike.write', self.ident, s)

    def writelines(self, lines):
        for line in lines:
            self.write(line)
    
    def close(self):
        self.closed = True

    def flush(self):
        pass

    def isatty(self):
        return True

    def read(self, size=-1):
        return as_str(
            self.pipe.expect('RemoteFileLike.read', self.ident, size),
            self.encoding,
        )

    def readline(self, size=-1):
        return as_str(
            self.pipe.expect('RemoteFileLike.readline', self.ident, size),
            self.encoding,
        )

    def readlines(self):
        return list(self)
