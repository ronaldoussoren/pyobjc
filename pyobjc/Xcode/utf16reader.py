__all__ = []

BUFFER_SIZE = 256

def readline_unsized(self, buff):
    while True:
        lines = buff.splitlines(True)
        if len(lines) > 1:
            return (u''.join(lines[1:]), lines[0])
        chunk = self.read(BUFFER_SIZE)
        if not chunk:
            return (u'', buff)
        else:
            buff += chunk
    
def readline_sized(self, buff, size):
    while True:
        lines = buff.splitlines(True)
        if len(lines) > 1:
            rval = lines.pop(0)
            if len(rval) > size:
                lines.insert(0, rval[size:])
                rval = rval[:size]
            return (u''.join(lines), rval)
        bytesread = len(buff)
        if size > bytesread:
            chunk = self.read(min(BUFFER_SIZE, size - bytesread))
            if not chunk:
                return (u'', buff)
            else:
                buff += chunk
        else:
            return (buff[size:], buff[:size])

def readline(self, size=None):
    buff = self._utf16_readline_buffer
    if size is None:
        buff, rval = readline_unsized(self, buff)
    else:
        buff, rval = readline_sized(self, buff, size)
    self._utf16_readline_buffer = buff
    return rval

def install():
    import encodings.utf_16 as utf_16
    import encodings.utf_16_be as utf_16_be
    import encodings.utf_16_le as utf_16_le
    for mod in (utf_16, utf_16_be, utf_16_le):
        mod.StreamReader.readline = readline
        mod.StreamReader._utf16_readline_buffer = u''

def test():
    from StringIO import StringIO
    import codecs
    from itertools import izip
    STRINGS = [
        u'\u304a\u3084\u3059\u307f\u306a\u3055\u3044\n',
        u'Oysasumi nasai\n',
        u'Goodnight\n',
    ] * 500
    for codec in ('utf_16', 'utf_16_le', 'utf_16_be'):
        utxt = u''.join(STRINGS)
        txt = u''.join(STRINGS).encode(codec)
        def testreader():
           return codecs.getreader(codec)(StringIO(txt))
        # test readline()
        for new, orig in izip(testreader(), STRINGS):
            assert new == orig, '%r != %r' % (new, orig,)
        # test readlines()
        assert testreader().readlines() == STRINGS
        # test sized readline()
        idx = 0
        rdr = testreader()
        while idx < len(utxt):
            nextline  = rdr.readline(5)
            assert len(nextline) <= 5, 'len(%r) > 5' % (nextline,)
            if nextline.splitlines()[0] != nextline:
                # there was a newline
                nextchunk = utxt[idx:idx+len(nextline)]
                idx += len(nextline)
                assert nextchunk == nextline, '[a] %r != %r' % (nextline, nextchunk)
            else:
                nextchunk = utxt[idx:idx+5]
                idx += 5
                assert nextline == nextchunk, '[b] %r != %r' % (nextline, nextchunk)

if __name__ == '__main__':
    install()
    try:
        test()
    except:
        import sys, pdb, traceback
        tb = sys.exc_info()[2]
        traceback.print_exc()
        pdb.post_mortem(tb)
