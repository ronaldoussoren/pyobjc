"""
This module implements a callback function that is used by the C code to
add Python special methods to Objective-C classes with a suitable interface.

This module contains no user callable code.

TODO:
- Add external interface: Framework specific modules may want to add to this.

- These are candidates for implementation:

    >>> from Foundation import *
    >>> set(dir(list)) - set(dir(NSMutableArray))
    set(['__delslice__', '__imul__', '__getslice__', '__setslice__',
        '__iadd__', '__mul__', '__add__', '__rmul__'])
    >>> set(dir(dict)) - set(dir(NSMutableDictionary))
    set(['__cmp__'])

"""
from _objc import setClassExtender, selector, lookUpClass, currentBundle, repythonify, splitSignature
from itertools import imap
import sys

__all__ = ( 'addConvenienceForSelector', 'addConvenienceForClass' )


CONVENIENCE_METHODS = {}
CLASS_METHODS = {}

def addConvenienceForSelector(selector, methods):
    """
    Add the list with methods to every class that has a selector with the
    given name.
    """
    CONVENICENCE_METHODS[selector] = methods

def addConvenienceForClass(classname, methods):
    """
    Add the list with methods to the class with the specified name
    """
    CLASS_METHODS[classname] = methods

NSObject = lookUpClass('NSObject')

def isNative(sel):
    return not hasattr(sel, 'callable')

def add_convenience_methods(super_class, name, type_dict):
    try:
        return _add_convenience_methods(super_class, name, type_dict)
    except:
        import traceback
        traceback.print_exc()
        raise

def _add_convenience_methods(super_class, name, type_dict):
    """
    Add additional methods to the type-dict of subclass 'name' of
    'super_class'.

    CONVENIENCE_METHODS is a global variable containing a mapping from
    an Objective-C selector to a Python method name and implementation.

    CLASS_METHODS is a global variable containing a mapping from
    class name to a list of Python method names and implementation.

    Matching entries from both mappings are added to the 'type_dict'.
    """
    if type_dict.get('__objc_python_subclass__'):
        if 'bundleForClass' not in type_dict:
            cb = currentBundle()
            def bundleForClass(cls):
                return cb
            type_dict['bundleForClass'] = selector(bundleForClass, isClassMethod=True)
            if ('__useKVO__' not in type_dict and
                    isNative(type_dict.get('willChangeValueForKey_')) and
                    isNative(type_dict.get('didChangeValueForKey_'))):
                useKVO = issubclass(super_class, NSObject)
                type_dict['__useKVO__'] = useKVO
        if '__bundle_hack__' in type_dict:
            import warnings
            warnings.warn(
                "__bundle_hack__ is not necessary in PyObjC 1.3+ / py2app 0.1.8+",
                DeprecationWarning)

    for k, sel in type_dict.items():
        if not isinstance(sel, selector):
            continue

        # 
        # Handle some common exceptions to the usual rules:
        #

        sel = sel.selector

        if sel in CONVENIENCE_METHODS:
            v = CONVENIENCE_METHODS[sel]
            for nm, value in v:
                if nm in type_dict and isinstance(type_dict[nm], selector):

                    # Clone attributes of already existing version

                    t = type_dict[nm]
                    v = selector(value, selector=t.selector,
                        signature=t.signature, isClassMethod=t.isClassMethod)

                    type_dict[nm] = v
                else:
                    type_dict[nm] = value

    if name in CLASS_METHODS:
        for nm, value in CLASS_METHODS[name]:
            type_dict[nm] = value


    if name == 'NSObject':
        class kvc (object):
            """
            Key-Value-Coding accessor for Cocoa objects. 
            
            Both attribute access and dict-like indexing will attempt to 
            access the requested item through Key-Value-Coding.
            """
            __slots__ = ('__object',)
            def __init__(self, value):
                self.__object = value

            def __repr__(self):
                return "<KVC accessor for %r>"%(self.__object,)

            def __getattr__(self, key):
                try:
                    return self.__object.valueForKey_(key)
                except KeyError, msg:
                    if hasattr(msg, '_pyobjc_info_') and msg._pyobjc_info_['name'] == 'NSUnknownKeyException':
                        raise AttributeError(key)

                    raise
            def __setattr__(self, key, value):
                if not key.startswith('_'):
                    return self.__object.setValue_forKey_(value, key)
                else:
                    super(kvc, self).__setattr__(key, value)

            def __getitem__(self, key):
                if not isinstance(key, (str, unicode)):
                    raise TypeError("Key must be string")
                return self.__object.valueForKey_(key)

            def __setitem__(self, key, value):
                if not isinstance(key, (str, unicode)):
                    raise TypeError("Key must be string")
                return self.__object.setValue_forKey_(value, key)

        type_dict['_'] = property(kvc)

setClassExtender(add_convenience_methods)


#
# The following conveniences should strictly speaking be in 
# in pyobjc-framework-Foundation, but as they are very fundamental
# we're keeping them here.
#

def __getitem__objectForKey_(self, key):
    res = self.objectForKey_(container_wrap(key))
    return container_unwrap(res, KeyError, key)

def has_key_objectForKey_(self, key):
    res = self.objectForKey_(container_wrap(key))
    return res is not None

def get_objectForKey_(self, key, dflt=None):
    res = self.objectForKey_(container_wrap(key))
    if res is None:
        res = dflt
    return res

CONVENIENCE_METHODS['objectForKey:'] = (
    ('__getitem__', __getitem__objectForKey_),
    ('has_key', has_key_objectForKey_),
    ('get', get_objectForKey_),
    ('__contains__', has_key_objectForKey_),
)

def __delitem__removeObjectForKey_(self, key):
    self.removeObjectForKey_(container_wrap(key))

CONVENIENCE_METHODS['removeObjectForKey:'] = (
    ('__delitem__', __delitem__removeObjectForKey_),
)

def update_setObject_forKey_(self, other):
    # XXX - should this be more flexible?
    for key, value in other.items():
        self[key] = value

def setdefault_setObject_forKey_(self, key, dflt=None):
    try:
        return self[key]
    except KeyError:
        self[key] = dflt
        return dflt

def __setitem__setObject_forKey_(self, key, value):
    self.setObject_forKey_(container_wrap(value), container_wrap(key))
    
def pop_setObject_forKey_(self, key, dflt=None):
    try:
        res = self[key]
    except KeyError:
        res = dflt
    else:
        del self[key]
    return res

def popitem_setObject_forKey_(self):
    try:
        k = self[iter(self).next()]
    except StopIteration:
        raise KeyError, "popitem on an empty %s" % (type(self).__name__,)
    else:
        return (k, self[k])

CONVENIENCE_METHODS['setObject:forKey:'] = (
    ('__setitem__', __setitem__setObject_forKey_),
    ('update', update_setObject_forKey_),
    ('setdefault', setdefault_setObject_forKey_),
    ('pop', pop_setObject_forKey_),
    ('popitem', popitem_setObject_forKey_),
)


CONVENIENCE_METHODS['count'] = (
    ('__len__', lambda self: self.count()),
)

CONVENIENCE_METHODS['containsObject:'] = (
    ('__contains__', lambda self, elem: bool(self.containsObject_(container_wrap(elem)))),
)



def objc_hash(self, _max=sys.maxint, _const=((sys.maxint + 1L) * 2L)):
    rval = self.hash()
    if rval > _max:
        rval -= _const
        # -1 is not a valid hash in Python and hash(x) will
        # translate a hash of -1 to -2, so we might as well
        # do it here so that it's not too surprising..
        if rval == -1:
            rval = -2
    return int(rval)
CONVENIENCE_METHODS['hash'] = (
    ('__hash__', objc_hash),
)

CONVENIENCE_METHODS['isEqualTo:'] = (
    ('__eq__', lambda self, other: bool(self.isEqualTo_(other))),
)

CONVENIENCE_METHODS['isEqual:'] = (
    ('__eq__', lambda self, other: bool(self.isEqual_(other))),
)

CONVENIENCE_METHODS['isGreaterThan:'] = (
    ('__gt__', lambda self, other: bool(self.isGreaterThan_(other))),
)

CONVENIENCE_METHODS['isGreaterThanOrEqualTo:'] = (
    ('__ge__', lambda self, other: bool(self.isGreaterThanOrEqualTo_(other))),
)

CONVENIENCE_METHODS['isLessThan:'] = (
    ('__lt__', lambda self, other: bool(self.isLessThan_(other))),
)

CONVENIENCE_METHODS['isLessThanOrEqualTo:'] = (
    ('__le__', lambda self, other: bool(self.isLessThanOrEqualTo_(other))),
)

CONVENIENCE_METHODS['isNotEqualTo:'] = (
    ('__ne__', lambda self, other: bool(self.isNotEqualTo_(other))),
)

CONVENIENCE_METHODS['length'] = (
    ('__len__', lambda self: self.length()),
)

CONVENIENCE_METHODS['addObject:'] = (
    ('append', lambda self, item: self.addObject_(container_wrap(item))),
)

def reverse_exchangeObjectAtIndex_withObjectAtIndex_(self):
    begin = 0
    end = len(self) - 1
    while begin < end:
        self.exchangeObjectAtIndex_withObjectAtIndex_(begin, end)
        begin += 1
        end -= 1

CONVENIENCE_METHODS['exchangeObjectAtIndex:withObjectAtIndex:'] = (
    ('reverse', reverse_exchangeObjectAtIndex_withObjectAtIndex_),
)

def ensureArray(anArray):
    if not isinstance(anArray, (NSArray, list, tuple)):
        anArray = list(anArray)
    return anArray
    

def extend_addObjectsFromArray_(self, anArray):
    self.addObjectsFromArray_(ensureArray(anArray))

CONVENIENCE_METHODS['addObjectsFromArray:'] = (
    ('extend', extend_addObjectsFromArray_),
)

def index_indexOfObject_(self, item):
    from Foundation import NSNotFound
    res = self.indexOfObject_(container_wrap(item))
    if res == NSNotFound:
        raise ValueError, "%s.index(x): x not in list" % (type(self).__name__,)
    return res

CONVENIENCE_METHODS['indexOfObject:'] = (
    ('index', index_indexOfObject_),
)

def insert_insertObject_atIndex_(self, idx, item):
    if idx < 0: 
        idx += len(self)
        if idx < 0:
            raise IndexError("list index out of range")
    self.insertObject_atIndex_(container_wrap(item), idx)

CONVENIENCE_METHODS['insertObject:atIndex:'] = (
    ( 'insert', insert_insertObject_atIndex_),
)

def __getitem__objectAtIndex_(self, idx):
    if isinstance(idx, slice):
        start, stop, step = idx.indices(len(self))
        #if step == 1:
        #    m = getattr(self, 'subarrayWithRange_', None)
        #    if m is not None:
        #        return m((start, stop - start))
        return [self[i] for i in xrange(start, stop, step)]
    if idx < 0:
        idx += len(self)
        if idx < 0:
            raise IndexError("list index out of range")

    return container_unwrap(self.objectAtIndex_(idx), RuntimeError)

CONVENIENCE_METHODS['objectAtIndex:'] = (
    ('__getitem__', __getitem__objectAtIndex_),
)

def __delitem__removeObjectAtIndex_(self, idx):
    if isinstance(idx, slice):
        start, stop, step = idx.indices(len(self))
        if step == 1:
            if start > stop:
                start, stop = stop, start
            m = getattr(self, 'removeObjectsInRange_', None)
            if m is not None:
                m((start, stop - start))
                return
        r = range(start, stop, step)
        r.sort()
        r.reverse()
        for i in r:
            self.removeObjectAtIndex_(i)
        return
    if idx < 0:
        idx += len(self)
        if idx < 0:
            raise IndexError("list index out of range")
        
    self.removeObjectAtIndex_(idx)
    
def pop_removeObjectAtIndex_(self, idx=-1):
    length = len(self)
    if length <= 0:
        raise IndexError("pop from empty list")
    elif idx >= length or (idx + length) < 0:
        raise IndexError("pop index out of range")
    elif idx < 0:
        idx += len(self)
        if idx < 0:
            raise IndexError("list index out of range")
    rval = self[idx]
    self.removeObjectAtIndex_(idx)
    return rval

def remove_removeObjectAtIndex_(self, obj):
    idx = self.index(obj)
    self.removeObjectAtIndex_(idx)

CONVENIENCE_METHODS['removeObjectAtIndex:'] = (
    ('remove', remove_removeObjectAtIndex_),
    ('pop', pop_removeObjectAtIndex_),
    ('__delitem__', __delitem__removeObjectAtIndex_),
)

def __setitem__replaceObjectAtIndex_withObject_(self, idx, anObject):
    if isinstance(idx, slice):
        start, stop, step = idx.indices(len(self))
        if step == 1:
            m = getattr(self, 'replaceObjectsInRange_withObjectsFromArray_', None)
            if m is not None:
                m((start, stop - start), ensureArray(anObject))
                return
        # XXX - implement this..
        raise NotImplementedError
    if idx < 0:
        idx += len(self)
        if idx < 0:
            raise IndexError("list index out of range")

    self.replaceObjectAtIndex_withObject_(idx, anObject)

CONVENIENCE_METHODS['replaceObjectAtIndex:withObject:'] = (
    ('__setitem__', __setitem__replaceObjectAtIndex_withObject_),
)

def enumeratorGenerator(anEnumerator):
    while True:
        yield container_unwrap(anEnumerator.nextObject(), StopIteration)

def dictItems(aDict):
    """
    NSDictionary.items()
    """
    keys = aDict.allKeys()
    return zip(keys, imap(aDict.__getitem__, keys))

CONVENIENCE_METHODS['allKeys'] = (
    ('keys', lambda self: self.allKeys()),
    ('items', lambda self: dictItems(self)),
)

CONVENIENCE_METHODS['allValues'] = (
    ('values', lambda self: self.allValues()),
)

def itemsGenerator(aDict):
    for key in aDict:
        yield (key, aDict[key])

def __iter__objectEnumerator_keyEnumerator(self):
    meth = getattr(self, 'keyEnumerator', None)
    if meth is None:
        meth = self.objectEnumerator
    return iter(meth())

CONVENIENCE_METHODS['keyEnumerator'] = (
    ('__iter__', __iter__objectEnumerator_keyEnumerator),
    ('iterkeys', lambda self: iter(self.keyEnumerator())),
    ('iteritems', lambda self: itemsGenerator(self)),
)

CONVENIENCE_METHODS['objectEnumerator'] = (
    ('__iter__', __iter__objectEnumerator_keyEnumerator),
    ('itervalues', lambda self: iter(self.objectEnumerator())),
)

CONVENIENCE_METHODS['reverseObjectEnumerator'] = (
    ('__reversed__', lambda self: iter(self.reverseObjectEnumerator())),
)

CONVENIENCE_METHODS['removeAllObjects'] = (
    ('clear', lambda self: self.removeAllObjects()),
)

CONVENIENCE_METHODS['dictionaryWithDictionary:'] = (
    ('copy', lambda self: type(self).dictionaryWithDictionary_(self)),
)

CONVENIENCE_METHODS['nextObject'] = (
    ('__iter__', enumeratorGenerator),
)

#
# NSNumber seems to be and abstract base-class that is implemented using
# NSCFNumber, a CoreFoundation 'proxy'.
#
NSNull = lookUpClass('NSNull')
NSArray = lookUpClass('NSArray')
#null = NSNull.null()

number_wrap = repythonify

def container_wrap(v):
    if v is None:
        return NSNull.null()
    return v

def container_unwrap(v, exc_type, *exc_args):
    if v is None:
        raise exc_type(*exc_args)
    elif v is NSNull.null():
        return None
    return v


def fromkeys_dictionaryWithObjects_forKeys_(cls, keys, values=None):
    if not isinstance(keys, (list, tuple)):
        keys = list(keys)
    if values is None:
        values = (None,) * len(keys)
    elif not isinstance(values, (list, tuple)):
        values = list(values)
    return cls.dictionaryWithObjects_forKeys_(values, keys)

CONVENIENCE_METHODS['dictionaryWithObjects:forKeys:'] = (
    ('fromkeys',
        classmethod(fromkeys_dictionaryWithObjects_forKeys_)),
)


def sort(self, key=None, reverse=False, cmpfunc=cmp):
    # NOTE: cmpfunc argument is for backward compatibility.
    if key is None:
        if reverse:
            def doCmp(a, b, cmpfunc):
                return -cmpfunc(a, b)
        else:
            def doCmp(a, b, cmpfunc):
                return cmpfunc(a, b)
    else:
        # This is (a lot) slower than the algoritm used for
        # list.sort, but so be it.
        if reverse:
            def doCmp(a, b, cmpfunc):
                return -cmpfunc(key(a), key(b))
        else:
            def doCmp(a, b, cmpfunc):
                return cmpfunc(key(a), key(b))

    self.sortUsingFunction_context_(doCmp, cmpfunc)



CONVENIENCE_METHODS['sortUsingFunction:context:'] = (
    ('sort', sort),
)

CONVENIENCE_METHODS['hasPrefix:'] = (
    ('startswith', lambda self, pfx: self.hasPrefix_(pfx)),
)

CONVENIENCE_METHODS['hasSuffix:'] = (
    ('endswith', lambda self, pfx: self.hasSuffix_(pfx)),
)

CLASS_METHODS['NSNull'] = (
    ('__nonzero__',  lambda self: False ),
)

NSDecimalNumber = lookUpClass('NSDecimalNumber')
def _makeD(v):
    if isinstance(v, NSDecimalNumber):
        return v
    return NSDecimalNumber.decimalNumberWithDecimal_(v)

CLASS_METHODS['NSDecimalNumber'] = (
    ('__add__', lambda self, other: _makeD(self.decimalValue() + other)),
    ('__radd__', lambda self, other: _makeD(other + self.decimalValue())),
    ('__sub__', lambda self, other: _makeD(self.decimalValue() - other)),
    ('__rsub__', lambda self, other: _makeD(other - self.decimalValue())),
    ('__mul__', lambda self, other: _makeD(self.decimalValue() * other)),
    ('__rmul__', lambda self, other: _makeD(other * self.decimalValue())),
    ('__div__', lambda self, other: _makeD(self.decimalValue() / other)),
    ('__rdiv__', lambda self, other: _makeD(other / self.decimalValue())),
    ('__mod__', lambda self, other: _makeD(self.decimalValue() % other)),
    ('__rmod__', lambda self, other: _makeD(other % self.decimalValue())),
    ('__neg__', lambda self: _makeD(-(self.decimalValue()))),
    ('__pos__', lambda self: _makeD(+(self.decimalValue()))),
    ('__abs__', lambda self: _makeD(abs(self.decimalValue()))),
)

def NSData__getslice__(self, i, j):
    return self.bytes()[i:j]

def NSData__getitem__(self, item):
    buff = self.bytes()
    try:
        return buff[item]
    except TypeError:
        return buff[:][item]

CLASS_METHODS['NSData'] = (
    ('__str__', lambda self: self.bytes()[:]),
    ('__getitem__', NSData__getitem__),
    ('__getslice__', NSData__getslice__),
)

def NSMutableData__setslice__(self, i, j, sequence):
    # XXX - could use replaceBytes:inRange:, etc.
    self.mutableBytes()[i:j] = sequence
    
def NSMutableData__setitem__(self, item, value):
    self.mutableBytes()[item] = value

CLASS_METHODS['NSMutableData'] = (
    ('__setslice__', NSMutableData__setslice__),
    ('__setitem__', NSMutableData__setitem__),
)
