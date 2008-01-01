# Ideally we'd probably be using something like the PyObjC runtime
# rather than the struct module to get by here.  However, this is
# good enough for now.

import struct
from itertools import *

__all__ = """
sizeof
Structure
pypackable
p_char
p_byte
p_ubyte
p_short
p_ushort
p_int
p_uint
p_long
p_ulong
p_float
p_double
p_ptr
p_longlong
p_ulonglong
""".split()

def sizeof(s):
    """
    Return the size of an object when packed
    """
    if hasattr(s, '_size_'):
        return s._size_
    return len(s)

class MetaPackable(type):
    """
    Fixed size struct.unpack-able types use from_tuple as their designated initializer
    """
    def from_mmap(cls, mm, ptr, **kw):
        return cls.from_str(mm[ptr:ptr+cls._size_], **kw)

    def from_fileobj(cls, f, **kw):
        return cls.from_str(f.read(cls._size_), **kw)

    def from_str(cls, s, **kw):
        endian = kw.get('_endian_', cls._endian_)
        return cls.from_tuple(struct.unpack(endian + cls._format_, s), **kw)

    def from_tuple(cls, tpl, **kw):
        return cls(tpl[0], **kw)

class BasePackable(object):
    # XXX - use big endian everywhere, because we're only parsing Mach-O
    _endian_ = '>'

    def to_str(self, s):
        raise NotImplementedError

    def to_fileobj(self, f):
        f.write(self.to_str())

    def to_mmap(self, mm, ptr):
        mm[ptr:ptr+self._size_] = self.to_str()

class Packable(BasePackable):
    """
    Fixed size single object that is (un)packable by a struct format
    """
    __metaclass__ = MetaPackable

    def to_str(self):
        cls = type(self)
        endian = getattr(self, '_endian_', cls._endian_)
        return struct.pack(endian + cls._format_, self)

def pypackable(name, pytype, format):
    """
    Create a "mix-in" class with a python type and a
    Packable with the given struct format
    """
    size, items = formatinfo(format)
    return type(Packable)(name, (pytype, Packable), {
        '_format_': format,
        '_size_': size,
        '_items_': items,
    })

def formatinfo(format):
    """
    Calculate the size and number of items in a struct format.
    """
    size = struct.calcsize(format)
    return size, len(struct.unpack(format, '\x00' * size))

class MetaStructure(MetaPackable):
    """
    The metaclass of Structure objects that does all the magic.

    Since we can assume that all Structures have a fixed size,
    we can do a bunch of calculations up front and pack or
    unpack the whole thing in one struct call.
    """
    def __new__(cls, clsname, bases, dct):
        fields = dct['_fields_']
        names = []
        types = []
        structmarks = []
        format = ''
        items = 0
        size = 0

        def struct_property(name, typ):
            def _get(self):
                return self._objects_[name]
            def _set(self, obj):
                if type(obj) is not typ:
                    obj = typ(obj)
                self._objects_[name] = obj
            return property(_get, _set, typ.__name__)

        for name, typ in fields:
            dct[name] = struct_property(name, typ)
            names.append(name)
            types.append(typ)
            format += typ._format_
            size += typ._size_
            if (typ._items_ > 1):
                structmarks.append((items, typ._items_, typ))
            items += typ._items_

        dct['_structmarks_'] = structmarks
        dct['_names_'] = names
        dct['_types_'] = types
        dct['_size_'] = size
        dct['_items_'] = items
        dct['_format_'] = format
        return super(MetaStructure, cls).__new__(cls, clsname, bases, dct)

    def from_tuple(cls, tpl, **kw):
        values = []
        current = 0
        for begin, length, typ in cls._structmarks_:
            if begin > current:
                values.extend(tpl[current:begin])
            current = begin + length
            values.append(typ.from_tuple(tpl[begin:current], **kw))
        values.extend(tpl[current:])
        return cls(*values, **kw)

class Structure(BasePackable):
    __metaclass__ = MetaStructure
    _fields_ = ()

    def __init__(self, *args, **kwargs):
        if len(args) == 1 and not kwargs and type(args[0]) is type(self):
            kwargs = args[0]._objects_
            args = ()
        self._objects_ = {}
        iargs = chain(izip(self._names_, args), kwargs.iteritems())
        for key, value in iargs:
            if key not in self._names_ and key != "_endian_":
                raise TypeError
            setattr(self, key, value)
        for key, typ in izip(self._names_, self._types_):
            if key not in self._objects_:
                self._objects_[key] = typ()

    def _get_packables(self):
        for obj in imap(self._objects_.__getitem__, self._names_):
            if obj._items_ == 1:
                yield obj
            else:
                for obj in obj._get_packables():
                    yield obj

    def to_str(self):
        return struct.pack(self._endian_ + self._format_, *self._get_packables())

    def __cmp__(self, other):
        if not type(other) is type(self):
            raise TypeError, 'Cannot compare objects of type %r to objects of type %r' % (type(other), type(self))
        for cmpval in starmap(cmp, izip(self._get_packables(), other._get_packables())):
            if cmpval != 0:
                return cmpval
        return 0

# export common packables with predictable names
p_char = pypackable('p_char', str, 'c')
p_byte = pypackable('p_byte', int, 'b')
p_ubyte = pypackable('p_ubyte', int, 'B')
p_short = pypackable('p_short', int, 'h')
p_ushort = pypackable('p_ushort', int, 'H')
p_int = pypackable('p_int', int, 'i')
p_uint = pypackable('p_uint', long, 'I')
p_long = pypackable('p_long', int, 'l')
p_ulong = pypackable('p_ulong', long, 'L')
p_float = pypackable('p_float', float, 'f')
p_double = pypackable('p_double', float, 'd')
p_ptr = pypackable('p_ptr', long, 'P')
p_longlong = pypackable('p_longlong', long, 'q')
p_ulonglong = pypackable('p_ulonglong', long, 'Q')

def test_ptypes():
    from cStringIO import StringIO
    import mmap

    class MyStructure(Structure):
        _fields_ = (
            ('foo', p_int),
            ('bar', p_ubyte),
        )

    class MyFunStructure(Structure):
        _fields_ = (
            ('fun', p_char),
            ('mystruct', MyStructure),
        )

    for endian in '><':
        kw = dict(_endian_=endian)
        MYSTRUCTURE = '\x00\x11\x22\x33\xFF'
        for fn, args in [
                    ('from_str', (MYSTRUCTURE,)),
                    ('from_mmap', (MYSTRUCTURE, 0)),
                    ('from_fileobj', (StringIO(MYSTRUCTURE),)),
                ]:
            myStructure = getattr(MyStructure, fn)(*args, **kw)
            if endian == '>':
                assert myStructure.foo == 0x00112233
            else:
                assert myStructure.foo == 0x33221100
            assert myStructure.bar == 0xFF
            assert myStructure.to_str() == MYSTRUCTURE

        MYFUNSTRUCTURE = '!' + MYSTRUCTURE
        for fn, args in [
                    ('from_str', (MYFUNSTRUCTURE,)),
                    ('from_mmap', (MYFUNSTRUCTURE, 0)),
                    ('from_fileobj', (StringIO(MYFUNSTRUCTURE),)),
                ]:
            myFunStructure = getattr(MyFunStructure, fn)(*args, **kw)
            assert myFunStructure.mystruct == myStructure
            assert myFunStructure.fun == '!'
            assert myFunStructure.to_str() == MYFUNSTRUCTURE

        sio = StringIO()
        myFunStructure.to_fileobj(sio)
        assert sio.getvalue() == MYFUNSTRUCTURE

        mm = mmap.mmap(-1, sizeof(MyFunStructure) * 2, mmap.MAP_ANONYMOUS)
        mm[:] = '\x00' * (sizeof(MyFunStructure) * 2)
        myFunStructure.to_mmap(mm, 0)
        assert MyFunStructure.from_mmap(mm, 0, **kw) == myFunStructure
        assert mm[:sizeof(MyFunStructure)] == MYFUNSTRUCTURE
        assert mm[sizeof(MyFunStructure):] == '\x00' * sizeof(MyFunStructure)
        myFunStructure.to_mmap(mm, sizeof(MyFunStructure))
        assert mm[:] == MYFUNSTRUCTURE + MYFUNSTRUCTURE
        assert MyFunStructure.from_mmap(mm, sizeof(MyFunStructure), **kw) == myFunStructure

if __name__ == '__main__':
    test_ptypes()
