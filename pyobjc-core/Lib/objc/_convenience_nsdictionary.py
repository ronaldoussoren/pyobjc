"""
Convenience interface for NSDictionary/NSMutableDictionary
"""
__all__ = ()

from objc._convenience_mapping import addConvenienceForBasicMapping
from objc._convenience import container_wrap, container_unwrap, addConvenienceForClass
from objc._objc import lookUpClass

import collections
import sys

addConvenienceForBasicMapping('NSDictionary', True)
addConvenienceForBasicMapping('NSMutableDictionary', False)

def dict_items(aDict):
    """
    NSDictionary.items()
    """
    keys = aDict.allKeys()
    return zip(keys, map(aDict.__getitem__, keys))

def itemsGenerator(aDict):
    for key in aDict:
        yield (key, aDict[key])

def __iter__objectEnumerator_keyEnumerator(self):
    meth = getattr(self, 'keyEnumerator', None)
    if meth is None:
        meth = self.objectEnumerator
    return iter(meth())

def fromkeys_dictionaryWithObjects_forKeys_(cls, keys, values=None):
    if not isinstance(keys, (list, tuple)):
        keys = list(keys)
    if values is None:
        values = (None,) * len(keys)
    elif not isinstance(values, (list, tuple)):
        values = list(values)
    return cls.dictionaryWithObjects_forKeys_(values, keys)

if sys.version_info[0] == 3:
    def cmp(a, b):
        if a == b:
            return 0
        elif a < b:
            return -1
        else:
            return 1

#

def all_contained_in(inner, outer):
    """
    Return True iff all items in ``inner`` are also in ``outer``.
    """
    for v in inner:
        if v not in outer:
            return False

    return True

class nsdict_view (collections.Set):
    __slots__ = ()

    def __eq__(self, other):
        if not isinstance(other, collections.Set):
            return NotImplemented

        if len(self) == len(other):
            return all_contained_in(self, other)

        else:
            return False

    def __ne__(self, other):
        if not isinstance(other, collections.Set):
            return NotImplemented

        if len(self) == len(other):
            return not all_contained_in(self, other)

        else:
            return True

    def __lt__(self, other):
        if not isinstance(other, collections.Set):
            return NotImplemented

        if len(self) < len(other):
            return all_contained_in(self, other)

        else:
            return False

    def __le__(self, other):
        if not isinstance(other, collections.Set):
            return NotImplemented

        if len(self) <= len(other):
            return all_contained_in(self, other)

        else:
            return False

    def __gt__(self, other):
        if not isinstance(other, collections.Set):
            return NotImplemented

        if len(self) > len(other):
            return all_contained_in(other, self)

        else:
            return False

    def __ge__(self, other):
        if not isinstance(other, collections.Set):
            return NotImplemented

        if len(self) >= len(other):
            return all_contained_in(other, self)

        else:
            return False

    def __and__(self, other):
        if not isinstance(other, collections.Set):
            return NotImplemented
        result = set(self)
        result.intersection_update(other)
        return result

    def __or__(self, other):
        if not isinstance(other, collections.Set):
            return NotImplemented
        result = set(self)
        result.update(other)
        return result

    def __ror__(self, other):
        if not isinstance(other, collections.Set):
            return NotImplemented
        result = set(self)
        result.update(other)
        return result

    def __sub__(self, other):
        if not isinstance(other, collections.Set):
            return NotImplemented
        result = set(self)
        result.difference_update(other)
        return result

    def __xor__(self, other):
        if not isinstance(other, collections.Set):
            return NotImplemented
        result = set(self)
        result.symmetric_difference_update(other)
        return result

#collections.Set.register(nsdict_view)

class nsdict_keys(nsdict_view):
    __slots__=('__value')
    def __init__(self, value):
        self.__value =  value

    def __repr__(self):
        keys = list(self.__value)
        #keys.sort()

        return "<nsdict_keys({0})>".format(keys)


    def __len__(self):
        return len(self.__value)

    def __iter__(self):
        return iter(self.__value)

    def __contains__(self, value):
        return value in self.__value

class nsdict_values(nsdict_view):
    __slots__=('__value')
    def __init__(self, value):
        self.__value =  value

    def __repr__(self):
        values = list(self)
        values.sort()

        return "<nsdict_values({0})>".format(values)

    def __len__(self):
        return len(self.__value)

    def __iter__(self):
        return iter(self.__value.objectEnumerator())

    def __contains__(self, value):
        for v in iter(self):
            if value == v:
                return True
        return False

class nsdict_items(nsdict_view):
    __slots__=('__value')

    def __init__(self, value):
        self.__value =  value

    def __repr__(self):
        values = list(self)
        values.sort()

        return "<nsdict_items({0})>".format(values)

    def __len__(self):
        return len(self.__value)

    def __iter__(self):
        for k in self.__value:
            yield (k, self.__value[k])

    def __contains__(self, value):
        for v in iter(self):
            if value == v:
                return True
        return False

collections.KeysView.register(nsdict_keys)
collections.ValuesView.register(nsdict_values)
collections.ItemsView.register(nsdict_items)

collections.Mapping.register(lookUpClass('NSDictionary'))
collections.MutableMapping.register(lookUpClass('NSMutableDictionary'))



def nsdict_fromkeys(cls, keys, value=None):
    keys = [container_wrap(k) for k in keys]
    values = [container_wrap(value)]*len(keys)

    return cls.dictionaryWithObjects_forKeys_(values, keys)

def nsmutabledict_fromkeys(cls, keys, value=None):
    result = cls.dictionary()
    value = container_wrap(value)
    for k in keys:
        result[container_wrap(k)] = value

    return result

def dict_new(cls, args, kwds):
    if len(args) == 0:
        pass

    elif len(args) == 1:
        d = dict()
        if isinstance(args[0], collections.Mapping):
            items = args[0].items()
        else:
            items = args[0]
        for k , v in items:
            d[container_wrap(k)] = container_wrap(v)

        for k, v in kwds.items():
            d[container_wrap(k)] = container_wrap(v)

        return cls.dictionaryWithDictionary_(d)

    else:
        raise TypeError(
                "dict expected at most 1 arguments, got {0}".format(
                    len(args)))
    if kwds:
        d = dict()
        for k, v in kwds.items():
            d[container_wrap(k)] = container_wrap(v)

        return cls.dictionaryWithDictionary_(d)

    return cls.dictionary()

def nsdict_new(cls, *args, **kwds):
    return dict_new(cls, args, kwds)

def nsmutabledict_new(cls, *args, **kwds):
    return dict_new(cls, args, kwds)


def nsdict__eq__(self, other):
    if not isinstance(other, collections.Mapping):
        return False

    return self.isEqualToDictionary_(other)

def nsdict__ne__(self, other):
    return not nsdict__eq__(self, other)

if sys.version_info[0] == 3:
    def nsdict__lt__(self, other):
        return NotImplemented

    def nsdict__le__(self, other):
        return NotImplemented

    def nsdict__ge__(self, other):
        return NotImplemented

    def nsdict__gt__(self, other):
        return NotImplemented

else:
    def nsdict__cmp__(self, other):
        if not isinstance(other, collections.Mapping):
            return NotImplemented

        if len(self) < len(other):
            return -1

        elif len(self) > len(other):
            return 1

        sentinel = object()

        for a_key in sorted(self):
            try:
                if self[a_key] != other[a_key]:
                    break

            except KeyError:
                break

        else:
            a_key = sentinel

        for b_key in sorted(self):
            try:
                if self[b_key] != other[b_key]:
                    break

            except KeyError:
                break
        else:
            b_key = sentinel

        r = cmp(a_key, b_key)
        if r == 0 and a_key is not sentinel:
            r =  cmp(self[a_key], other[a_key])

        return r

    def nsdict__lt__(self, other):
        return nsdict_cmp(self, other) < 0

    def nsdict__le__(self, other):
        return nsdict_cmp(self, other) <= 0

    def nsdict__ge__(self, other):
        return nsdict_cmp(self, other) >= 0

    def nsdict__gt__(self, other):
        return nsdict_cmp(self, other) > 0

if sys.version_info[0] == 3:
    addConvenienceForClass('NSDictionary', (
        ('fromkeys', classmethod(nsdict_fromkeys)),
        ('keys', lambda self: nsdict_keys(self)),
        ('values', lambda self: nsdict_values(self)),
        ('items', lambda self: nsdict_items(self)),
    ))

    addConvenienceForClass('NSMutableDictionary', (
        ('fromkeys', classmethod(nsmutabledict_fromkeys)),
    ))

else:
    addConvenienceForClass('NSDictionary', (
        ('fromkeys', classmethod(nsdict_fromkeys)),
        ('viewkeys', lambda self: nsdict_keys(self)),
        ('viewvalues', lambda self: nsdict_values(self)),
        ('viewitems', lambda self: nsdict_items(self)),
        ('keys', lambda self: self.allKeys()),
        ('items', lambda self: dictItems(self)),
        ('values', lambda self: self.allValues()),
        ('__getitem__', __getitem__objectForKey_),
        ('iterkeys', lambda self: iter(self.keyEnumerator())),
        ('iteritems', lambda self: itemsGenerator(self)),
        ('itervalues', lambda self: iter(self.objectEnumerator())),
    ))

addConvenienceForClass('NSDictionary', (
    ('__eq__', nsdict__eq__),
    ('__ne__', nsdict__ne__),
    ('__lt__', nsdict__lt__),
    ('__le__', nsdict__le__),
    ('__gt__', nsdict__gt__),
    ('__ge__', nsdict__ge__),
    ('__new__', staticmethod(nsdict_new)),
    ('__len__', lambda self: self.count()),
    ('__iter__', __iter__objectEnumerator_keyEnumerator),
))

addConvenienceForClass('NSMutableDictionary', (
    ('clear',     lambda self: self.removeAllObjects()),
))

if sys.version_info[0] == 2:
    addConvenienceForClass('NSDictionary', (
        ('__cmp__', nsdict__cmp__),
    ))

addConvenienceForClass('NSMutableDictionary', (
    ('__new__', staticmethod(nsmutabledict_new)),
))
