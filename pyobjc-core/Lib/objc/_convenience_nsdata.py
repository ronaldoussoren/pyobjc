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
    b"NSData",
    b"dataWithBytes:length:",
    {
        "arguments": {
            2: {"type": b"^v", "type_modifier": b"n", "c_array_length_in_arg": 3}
        }
    },
)


def nsdata__new__(cls, value=None):
    if value is None:
        return cls.data()

    else:
        return cls.dataWithBytes_length_(value, len(value))


def nsdata__str__(self):
    if len(self) == 0:
        return str(b"")
    return str(self.bytes().tobytes())

def nsdata__bytes__(self):
    return bytes(self.bytes())


# XXX: These NSData helpers should use Cocoa method calls,
#      instead of creating a memoryview/buffer object.
def nsdata__getitem__(self, item):
    buff = self.bytes()
    try:
        return buff[item]
    except TypeError:
        return buff[:][item]


def nsmutabledata__setitem__(self, item, value):
    self.mutableBytes()[item] = value


addConvenienceForClass(
    "NSData",
    (
        ("__new__", staticmethod(nsdata__new__)),
        ("__len__", lambda self: self.length()),
        ("__str__", nsdata__str__),
        ("__getitem__", nsdata__getitem__),
    ),
)
addConvenienceForClass("NSMutableData", (("__setitem__", nsmutabledata__setitem__),))
addConvenienceForClass("NSData", (("__bytes__", nsdata__bytes__),))
