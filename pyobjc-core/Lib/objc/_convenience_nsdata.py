"""
Specific support for NSData.

NSData needs to be handles specially for correctness reasons,
and is therefore in the core instead of the Foundation
framework wrappers.
"""
from objc._convenience import addConvenienceForClass
import sys

def NSData__getitem__(self, item):
    # XXX: deal with slices
    buff = self.bytes()
    try:
        return buff[item]
    except TypeError:
        return buff[:][item]


if sys.version_info[:2] <= (2,6):
    def NSData__str__(self):
        return self.bytes()[:]

elif sys.version_info[0] == 2:  # pragma: no 3.x cover
    def NSData__str__(self):
        if len(self) == 0:
            return str(b"")
        return str(self.bytes().tobytes())

else:
    def NSData__str__(self):
        if len(self) == 0:
            return str(b"")
        return str(self.bytes().tobytes())

    def NSData__bytes__(self):
        return bytes(self.bytes())

addConvenienceForClass('NSData', (
    ('__len__', lambda self: self.length()),
    ('__str__', NSData__str__),
    ('__getitem__', NSData__getitem__),
))

if sys.version_info[0] == 2:  # pragma: no 3.x cover
    def NSData__getslice__(self, i, j):
        return self.bytes()[i:j]

    addConvenienceForClass('NSData', (
        ('__getslice__', NSData__getslice__),
    ))

else:
    addConvenienceForClass('NSData', (
        ('__bytes__', NSData__bytes__),
    ))


def NSMutableData__setitem__(self, item, value):
    # XXX: deal with slices
    self.mutableBytes()[item] = value

addConvenienceForClass('NSMutableData', (
    ('__setitem__', NSMutableData__setitem__),
))

if sys.version_info[0] == 2:  # pragma: no 3.x cover
    def NSMutableData__setslice__(self, i, j, sequence):
        start, stop = slice(i, j).indices(self.length())
        try:
            buf = buffer(sequence)
        except TypeError:
            buf = list(sequence)
        self.replaceBytes_inRange_withBytes_length_(
            (start, stop), buf, len(buf))
        self.mutableBytes()[i:j] = sequence

    addConvenienceForClass('NSMutableData', (
        ('__setslice__', NSMutableData__setslice__),
    ))
