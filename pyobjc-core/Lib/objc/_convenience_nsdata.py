"""
Specific support for NSData.

NSData needs to be handles specially for correctness reasons,
and is therefore in the core instead of the Foundation
framework wrappers.
"""
from objc._objc import registerMetaDataForSelector
from objc._convenience import addConvenienceForClass
import sys

registerMetaDataForSelector(
    b'NSData', b'dataWithBytes:length:',
    {
        'arguments': {
            2: { 'type': b'^v', 'type_modifier': b'n', 'c_array_length_in_arg': 3 }
        }
    })


def nsdata__new__(cls, value=None):
    if value is None:
        return cls.data()

    else:
        return cls.dataWithBytes_length_(value, len(value))

if sys.version_info[:2] <= (2,6):  # pragma: no 3.x cover
    def nsdata__str__(self):
        return self.bytes()[:]

elif sys.version_info[0] == 2:  # pragma: no 3.x cover
    def nsdata__str__(self):
        if len(self) == 0:
            return str(b"")
        return str(self.bytes().tobytes())

else:
    def nsdata__str__(self):
        if len(self) == 0:
            return str(b"")
        return str(self.bytes().tobytes())

    def nsdata__bytes__(self):
        return bytes(self.bytes())

addConvenienceForClass('NSData', (
    ('__new__', nsdata__new__),
    ('__len__', lambda self: self.length()),
    ('__str__', nsdata__str__),
))

if sys.version_info[0] == 3:  # pragma: no 2.x cover; pragma: no branch
    addConvenienceForClass('NSData', (
        ('__bytes__', nsdata__bytes__),
    ))
