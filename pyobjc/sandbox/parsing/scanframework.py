import os
try:
    set
except NameError:
    from sets import Set as set
import glob
from tokenize_header import *
from macholib.dyld import framework_find
from itertools import *

def framework_header(f, known={}):
    headers = known.get(f)
    if headers is not None:
        return headers
    dylib = framework_find(f)
    framework = os.path.dirname(dylib)
    headers = known[f] = os.path.join(framework, 'Headers')
    return headers

def locate_header(f):
    framework, header = os.path.split(f)
    return os.path.join(framework_header(framework + '.framework'), header)
    
class Dependency(object):
    def __init__(self, header):
        self.header = header

    def infoTuple(self):
        return (self.header,)

    def __repr__(self):
        return '%s%r' % (type(self).__name__, self.infoTuple())
    

class FrameworkScanner(object):
    def __init__(self):
        self._scanner = None

    def scanframework(self, name):
        start = '%s/%s.h' % (name, name)
        startfile = locate_header(start)
        seen = set()
        scanners = []
        if os.path.exists(startfile):
            seen.add(start)
            scanners.append(self.scanfile(startfile))
        else:
            headers = glob.glob(locate_header('%s/*.h' % (name,)))
            for header in headers:
                seen.add(name + '/' + os.path.basename(header))
                scanners.append(self.scanfile(header))
        while scanners:
            try:
                token = scanners[-1].next()
            except StopIteration:
                scanners.pop()
                continue
            if isinstance(token, (AngleImport, StringImport)):
                fn = token['import_file']
                if fn in seen:
                    pass
                elif os.path.dirname(fn) != name:
                    yield Dependency(fn)
                else:
                    seen.add(fn)
                    scanners.append(self.scanfile(locate_header(fn)))
                continue
            yield token
    
    def scanfile(self, fn):
        if self._scanner is None:
            self._scanner = Scanner(LEXICON)
        def deadraise(string, i, j):
            print '-' * len(fn)
            print fn
            print '-' * len(fn)
            s = string[i:].split('\n',1)[0]
            print s
            print
            import pdb
            pdb.Pdb().set_trace()
        return self._scanner.iterscan(file(fn).read(), dead=deadraise)

class EnumCollector(object):
    def __init__(self):
        self.seen = []
        self.code = []

    def add(self, enum):
        value = -1
        for token in enum.matches():
            if isinstance(token, EnumValueMember):
                value = token['value']


if __name__ == '__main__':
    f = FrameworkScanner()
    for token in ifilter(None, f.scanframework('PreferencePanes')):
        if isinstance(token, GlobalThing):
            print token
        else:
            print token
