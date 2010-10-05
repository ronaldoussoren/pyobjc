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
from objc._objc import _setClassExtender, selector, lookUpClass, currentBundle, repythonify, splitSignature, _block_call
from objc._objc import registerMetaDataForSelector
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
    CONVENIENCE_METHODS[selector] = methods

def addConvenienceForClass(classname, methods):
    """
    Add the list with methods to the class with the specified name
    """
    CLASS_METHODS[classname] = methods

NSObject = lookUpClass('NSObject')

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
        if '__bundle_hack__' in type_dict:
            import warnings
            warnings.warn(
                "__bundle_hack__ is not necessary in PyObjC 1.3+ / py2app 0.1.8+",
                DeprecationWarning)

    look_at_super = (super_class is not None and super_class.__name__ != 'Object')

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

                elif look_at_super and hasattr(super_class, nm):
                    # Skip, inherit the implementation from a super_class
                    pass

                elif nm not in type_dict:
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

_setClassExtender(add_convenience_methods)


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

CONVENIENCE_METHODS[b'objectForKey:'] = (
    ('__getitem__', __getitem__objectForKey_),
    ('has_key', has_key_objectForKey_),
    ('get', get_objectForKey_),
    ('__contains__', has_key_objectForKey_),
)

def __delitem__removeObjectForKey_(self, key):
    self.removeObjectForKey_(container_wrap(key))

CONVENIENCE_METHODS[b'removeObjectForKey:'] = (
    ('__delitem__', __delitem__removeObjectForKey_),
)

def update_setObject_forKey_(self, *args, **kwds):
    # XXX - should this be more flexible?
    if len(args) == 0:
        pass
    elif len(args) != 1:
        raise TypeError("update expected at most 1 arguments, got {0}".format(
            len(args)))


    else:
        other = args[0]
        if hasattr(other, 'keys'):
            # This mirrors the implementation of dict.update, but seems
            # wrong for Python3 (with collectons.Dict)
            for key in other.keys():
                self[key] = other[key]

        else:
            for key, value in other:
                self[key] = value

    for k, v in kwds.iteritems():
        self[k] = v

def setdefault_setObject_forKey_(self, key, dflt=None):
    try:
        return self[key]
    except KeyError:
        self[key] = dflt
        return dflt

def __setitem__setObject_forKey_(self, key, value):
    self.setObject_forKey_(container_wrap(value), container_wrap(key))
   
pop_setObject_dflt=object()
def pop_setObject_forKey_(self, key, dflt=pop_setObject_dflt):
    try:
        res = self[key]
    except KeyError:
        if dflt == pop_setObject_dflt:
            raise KeyError(key)
        res = dflt
    else:
        del self[key]
    return res

NSAutoreleasePool = lookUpClass('NSAutoreleasePool')

def popitem_setObject_forKey_(self):
    try:
        it = self.keyEnumerator()
        k = container_unwrap(it.nextObject(), StopIteration)
    except (StopIteration, IndexError):
        raise KeyError, "popitem on an empty %s" % (type(self).__name__,)
    else:
        result = (k, container_unwrap(self.objectForKey_(k), KeyError))
        self.removeObjectForKey_(k)
        return result

CONVENIENCE_METHODS[b'setObject:forKey:'] = (
    ('__setitem__', __setitem__setObject_forKey_),
    ('update', update_setObject_forKey_),
    ('setdefault', setdefault_setObject_forKey_),
    ('pop', pop_setObject_forKey_),
    ('popitem', popitem_setObject_forKey_),
)


CONVENIENCE_METHODS[b'count'] = (
    ('__len__', lambda self: self.count()),
)

CONVENIENCE_METHODS[b'containsObject:'] = (
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
CONVENIENCE_METHODS[b'hash'] = (
    ('__hash__', objc_hash),
)

CONVENIENCE_METHODS[b'isEqualTo:'] = (
    ('__eq__', lambda self, other: bool(self.isEqualTo_(other))),
)

CONVENIENCE_METHODS[b'isEqual:'] = (
    ('__eq__', lambda self, other: bool(self.isEqual_(other))),
)

CONVENIENCE_METHODS[b'isGreaterThan:'] = (
    ('__gt__', lambda self, other: bool(self.isGreaterThan_(other))),
)

CONVENIENCE_METHODS[b'isGreaterThanOrEqualTo:'] = (
    ('__ge__', lambda self, other: bool(self.isGreaterThanOrEqualTo_(other))),
)

CONVENIENCE_METHODS[b'isLessThan:'] = (
    ('__lt__', lambda self, other: bool(self.isLessThan_(other))),
)

CONVENIENCE_METHODS[b'isLessThanOrEqualTo:'] = (
    ('__le__', lambda self, other: bool(self.isLessThanOrEqualTo_(other))),
)

CONVENIENCE_METHODS[b'isNotEqualTo:'] = (
    ('__ne__', lambda self, other: bool(self.isNotEqualTo_(other))),
)

CONVENIENCE_METHODS[b'length'] = (
    ('__len__', lambda self: self.length()),
)

CONVENIENCE_METHODS[b'addObject:'] = (
    ('append', lambda self, item: self.addObject_(container_wrap(item))),
)

def reverse_exchangeObjectAtIndex_withObjectAtIndex_(self):
    begin = 0
    end = len(self) - 1
    while begin < end:
        self.exchangeObjectAtIndex_withObjectAtIndex_(begin, end)
        begin += 1
        end -= 1

CONVENIENCE_METHODS[b'exchangeObjectAtIndex:withObjectAtIndex:'] = (
    ('reverse', reverse_exchangeObjectAtIndex_withObjectAtIndex_),
)

def ensureArray(anArray):
    if not isinstance(anArray, (NSArray, list, tuple)):
        anArray = list(anArray)
    return anArray
    

def extend_addObjectsFromArray_(self, anArray):
    self.addObjectsFromArray_(ensureArray(anArray))

CONVENIENCE_METHODS[b'addObjectsFromArray:'] = (
    ('extend', extend_addObjectsFromArray_),
)

_index_sentinel=object()
def index_indexOfObject_inRange_(self, item, start=0, stop=_index_sentinel):
    #from Foundation import NSNotFound
    NSNotFound = sys.maxsize
    if start == 0 and stop is _index_sentinel:
        res = self.indexOfObject_(container_wrap(item))
        if res == NSNotFound:
            raise ValueError("%s.index(x): x not in list" % (type(self).__name__,))
    else:
        l = len(self)
        if start < 0:
            start = l + start
            if start < 0:
                start = 0

        if stop is not _index_sentinel:
            if stop < 0:
                stop = l + stop
                if stop < 0:
                    stop = 0
        else:
            stop = l

        itemcount = len(self)

        if itemcount == 0:
            raise ValueError("%s.index(x): x not in list" % (type(self).__name__,))
           
        else:
            if start >= itemcount:
                start = itemcount - 1
            if stop >= itemcount:
                stop = itemcount - 1

            if stop <= start:
                ln = 0 
            else:

                ln = stop - start


            if ln == 0:
                raise ValueError("%s.index(x): x not in list" % (type(self).__name__,))
            
            if ln > sys.maxint:
                ln = sys.maxint

            res = self.indexOfObject_inRange_(item, (start, ln))
            if res == NSNotFound:
                raise ValueError("%s.index(x): x not in list" % (type(self).__name__,))
    return res

CONVENIENCE_METHODS[b'indexOfObject:inRange:'] = (
    ('index', index_indexOfObject_inRange_),
)

def insert_insertObject_atIndex_(self, idx, item):
    if idx < 0: 
        idx += len(self)
        if idx < 0:
            raise IndexError("list index out of range")
    self.insertObject_atIndex_(container_wrap(item), idx)

CONVENIENCE_METHODS[b'insertObject:atIndex:'] = (
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
    
    elif not isinstance(idx, (int, long)):
        raise TypeError("index must be a number")
    
    if idx < 0:
        idx += len(self)
        if idx < 0:
            raise IndexError("list index out of range")

    return container_unwrap(self.objectAtIndex_(idx), RuntimeError)

def __getslice__objectAtIndex_(self, i, j):
    i = max(i, 0); j = max(j, 0)
    return __getitem__objectAtIndex_(self, slice(i, j))

CONVENIENCE_METHODS[b'objectAtIndex:'] = (
    ('__getitem__', __getitem__objectAtIndex_),
    ('__getslice__', __getslice__objectAtIndex_),
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

def __delslice__removeObjectAtIndex_(self, i, j):
    __delitem__removeObjectAtIndex_(self, slice(i, j))
    
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

CONVENIENCE_METHODS[b'removeObjectAtIndex:'] = (
    ('remove', remove_removeObjectAtIndex_),
    ('pop', pop_removeObjectAtIndex_),
    ('__delitem__', __delitem__removeObjectAtIndex_),
    ('__delslice__', __delslice__removeObjectAtIndex_),
)

def __setitem__replaceObjectAtIndex_withObject_(self, idx, anObject):
    if isinstance(idx, slice):
        start, stop, step = idx.indices(len(self))
        if step >=0:
            if stop <= start:
                # Empty slice: insert values
                stop = start
        elif start <= stop:
            start = stop

        if step == 1:
            m = getattr(self, 'replaceObjectsInRange_withObjectsFromArray_', None)
            if m is not None:
                m((start, stop - start), ensureArray(anObject))
                return

        if not isinstance(anObject, (NSArray, list, tuple)):
            anObject = list(anObject)

        slice_len = len(xrange(start, stop, step))
        if slice_len != len(anObject):
            raise ValueError("Replacing extended slice with %d elements by %d elements"%(
                slice_len, len(anObject)))

        if step > 0:
            if anObject is self:
                toAssign = list(anObject)
            else:
                toAssign = anObject
            for inIdx, outIdx in enumerate(xrange(start, stop, step)): 
                self.replaceObjectAtIndex_withObject_(outIdx, toAssign[inIdx])

        elif step == 0:
            raise ValueError("Step 0")

        else:
            if anObject is self:
                toAssign = list(anObject)
            else:
                toAssign = anObject
            #for inIdx, outIdx in reversed(enumerate(reversed(range(start, stop, step)))):
            for inIdx, outIdx in enumerate(xrange(start, stop, step)): 
                self.replaceObjectAtIndex_withObject_(outIdx, toAssign[inIdx])


    elif not isinstance(idx, (int, long)):
        raise TypeError("index is not an integer")

    else:

        if idx < 0:
            idx += len(self)
            if idx < 0:
                raise IndexError("list index out of range")

        self.replaceObjectAtIndex_withObject_(idx, anObject)

def __setslice__replaceObjectAtIndex_withObject_(self, i, j, seq):
    i = max(i, 0)
    j = max(j, 0)
    __setitem__replaceObjectAtIndex_withObject_(self, slice(i, j), seq)

CONVENIENCE_METHODS[b'replaceObjectAtIndex:withObject:'] = (
    ('__setitem__', __setitem__replaceObjectAtIndex_withObject_),
    ('__setslice__', __setslice__replaceObjectAtIndex_withObject_),
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

#CONVENIENCE_METHODS[b'allKeys'] = (
#    ('keys', lambda self: self.allKeys()),
#    ('items', lambda self: dictItems(self)),
#)

#CONVENIENCE_METHODS[b'allValues'] = (
    #('values', lambda self: self.allValues()),
#)

def itemsGenerator(aDict):
    for key in aDict:
        yield (key, aDict[key])

def __iter__objectEnumerator_keyEnumerator(self):
    meth = getattr(self, 'keyEnumerator', None)
    if meth is None:
        meth = self.objectEnumerator
    return iter(meth())

CONVENIENCE_METHODS[b'keyEnumerator'] = (
    ('__iter__', __iter__objectEnumerator_keyEnumerator),
    ('iterkeys', lambda self: iter(self.keyEnumerator())),
    ('iteritems', lambda self: itemsGenerator(self)),
)

CONVENIENCE_METHODS[b'objectEnumerator'] = (
    ('__iter__', __iter__objectEnumerator_keyEnumerator),
    ('itervalues', lambda self: iter(self.objectEnumerator())),
)

CONVENIENCE_METHODS[b'reverseObjectEnumerator'] = (
    ('__reversed__', lambda self: iter(self.reverseObjectEnumerator())),
)

CONVENIENCE_METHODS[b'removeAllObjects'] = (
    ('clear', lambda self: self.removeAllObjects()),
)

CONVENIENCE_METHODS[b'dictionaryWithDictionary:'] = (
    ('copy', lambda self: type(self).dictionaryWithDictionary_(self)),
)

CONVENIENCE_METHODS[b'nextObject'] = (
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

#CONVENIENCE_METHODS[b'dictionaryWithObjects:forKeys:'] = (
    #('fromkeys',
        #classmethod(fromkeys_dictionaryWithObjects_forKeys_)),
#)

if sys.version_info[0] == 3:
    def cmp(a, b):
        if a == b:
            return 0
        elif a < b:
            return -1
        else:
            return 1

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


registerMetaDataForSelector(b"NSObject", b"sortUsingFunction:context:",
        dict(
            arguments={
                2:  { 
                        'callable': {
                            'reval': 'i',
                            'arguments': {
                                0: { 'type': '@' },
                                1: { 'type': '@' },
                                2: { 'type': '@' },
                            }
                        },
                        'callable_retained': False,
                },
                3:  { 'type': '@' },
            },
        ))


CONVENIENCE_METHODS[b'sortUsingFunction:context:'] = (
    ('sort', sort),
)

CONVENIENCE_METHODS[b'hasPrefix:'] = (
    ('startswith', lambda self, pfx: self.hasPrefix_(pfx)),
)

CONVENIENCE_METHODS[b'hasSuffix:'] = (
    ('endswith', lambda self, pfx: self.hasSuffix_(pfx)),
)


CONVENIENCE_METHODS[b'copyWithZone:'] = (
    ('__copy__', lambda self: self.copyWithZone_(None)),
)

# This won't work:
#NSKeyedArchiver = lookUpClass('NSKeyedArchiver')
#NSKeyedUnarchiver = lookUpClass('NSKeyedUnarchiver')
#def coder_deepcopy(self, memo):
#   buf = NSKeyedArchiver.archivedDataWithRootObject_(self)
#   result = NSKeyedUnarchiver.unarchiveObjectWithData_(buf)
#   return result
#
#CONVENIENCE_METHODS['encodeWithCoder:'] = (
#   ('__deepcopy__', coder_deepcopy ),
#)

CLASS_METHODS['NSNull'] = (
    ('__nonzero__',  lambda self: False ),
    ('__bool__',  lambda self: False ),
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


if sys.version_info[:2] <= (2,6):
    def NSData__str__(self):
        return self.bytes()[:]

elif sys.version_info[0] == 2:
    def NSData__str__(self):
        return str(self.bytes().tobytes())

else:
    def NSData__str__(self):
        return str(self.bytes().tobytes())


CLASS_METHODS['NSData'] = (
    ('__str__', NSData__str__),
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


def __call__(self, *args, **kwds):
    return _block_call(self, self.__block_signature__, args, kwds)

CLASS_METHODS['NSBlock'] = (
    ('__call__', __call__),
)


if sys.version_info[0] == 3 or (sys.version_info[0] == 2 and sys.version_info[1] >= 6):
    import collections

    def all_contained_in(inner, outer):
        """
        Return True iff all items in ``inner`` are also in ``outer``.
        """
        for v in inner:
            if v not in outer:
                return False

        return True

    class nsdict_view (object):
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
    
    collections.Set.register(nsdict_view)

    class nsdict_keys(nsdict_view):
        __slots__=('__value')
        def __init__(self, value):
            self.__value =  value

        def __repr__(self):
            keys = list(self.__value)
            keys.sort()

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



    NSDictionary = lookUpClass('NSDictionary')
    def nsdict_fromkeys(cls, keys, value=None):
        keys = [container_wrap(k) for k in keys]
        values = [container_wrap(value)]*len(keys)

        return NSDictionary.dictionaryWithObjects_forKeys_(values, keys)

    NSMutableDictionary = lookUpClass('NSMutableDictionary')
    def nsmutabledict_fromkeys(cls, keys, value=None):
        result = NSMutableDictionary.dictionary()
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
                items = args[0].iteritems()
            else:
                items = args[0]
            for k , v in items:
                d[container_wrap(k)] = container_wrap(v)

            for k, v in kwds.iteritems():
                d[container_wrap(k)] = container_wrap(v)

            return cls.dictionaryWithDictionary_(d)

        else:
            raise TypeError(
                    "dict expected at most 1 arguments, got {0}".format(
                        len(args)))
        if kwds:
            d = dict()
            for k, v in kwds.iteritems():
                d[container_wrap(k)] = container_wrap(v)

            return cls.dictionaryWithDictionary_(d)

        return cls.dictionary()

    def nsdict_new(cls, *args, **kwds):
        return dict_new(NSDictionary, args, kwds)

    def nsmutabledict_new(cls, *args, **kwds):
        return dict_new(NSMutableDictionary, args, kwds)


    def nsdict__eq__(self, other):
        if not isinstance(other, collections.Mapping):
            return False

        return self.isEqualToDictionary_(other)

    def nsdict__ne__(self, other):
        return not nsdict__eq__(self, other)

    def nsdict__richcmp__(self, other):
        return NotImplemented
        

    if sys.version_info[0] == 3:
        CLASS_METHODS['NSDictionary'] = (
            ('fromkeys', classmethod(nsdict_fromkeys)),
            ('keys', lambda self: nsdict_keys(self)),
            ('values', lambda self: nsdict_values(self)),
            ('items', lambda self: nsdict_items(self)),
        )

        CLASS_METHODS['NSMutableDictionary'] = (
            ('fromkeys', classmethod(nsmutabledict_fromkeys)),
        )

    else:
        CLASS_METHODS['NSDictionary'] = (
            ('fromkeys', classmethod(nsdict_fromkeys)),
            ('viewkeys', lambda self: nsdict_keys(self)),
            ('viewvalues', lambda self: nsdict_values(self)),
            ('viewitems', lambda self: nsdict_items(self)),
            ('keys', lambda self: self.allKeys()),
            ('items', lambda self: dictItems(self)),
            ('values', lambda self: self.allValues()),
        )

    CLASS_METHODS['NSDictionary'] += (
        ('__eq__', nsdict__eq__),
        ('__ne__', nsdict__ne__),
        ('__lt__', nsdict__richcmp__),
        ('__le__', nsdict__richcmp__),
        ('__gt__', nsdict__richcmp__),
        ('__ge__', nsdict__richcmp__),
    )

    NSDictionary.__new__ = nsdict_new
    NSMutableDictionary.__new__ = nsmutabledict_new

    NSMutableDictionary.dictionary()

    #FIXME: This shouldn't be necessary

NSMutableArray = lookUpClass('NSMutableArray')
def nsarray_add(self, other):
    result = NSMutableArray.arrayWithArray_(self)
    result.extend(other)
    return result

def nsarray_radd(self, other):
    result = NSMutableArray.arrayWithArray_(other)
    result.extend(self)
    return result

def nsarray_mul(self, other):
    """
    This tries to implement anNSArray * N
    somewhat efficently (and definitely more
    efficient that repeated appending).
    """
    result = NSMutableArray.array()

    if other <= 0:
        return result

    n = 1
    tmp = self
    while other:
        if other & n != 0:
            result.extend(tmp)
            other -= n

        if other:
            n <<= 1
            tmp = tmp.arrayByAddingObjectsFromArray_(tmp)

    #for n in xrange(other):
        #result.extend(self)
    return result



def nsarray_new(cls, sequence=None):
    if not sequence:
        return NSArray.array()

    elif isinstance(sequence, (str, unicode)):
        return NSArray.arrayWithArray_(list(sequence))

    else:
        if not isinstance(sequence, (list, tuple)):
            # FIXME: teach bridge to treat range and other list-lik
            # types correctly
            return NSArray.arrayWithArray_(list(sequence))

        return NSArray.arrayWithArray_(sequence)

def nsmutablearray_new(cls, sequence=None):
    if not sequence:
        return NSMutableArray.array()

    elif isinstance(sequence, (str, unicode)):
        return NSMutableArray.arrayWithArray_(list(sequence))

    else:
        if not isinstance(sequence, (list, tuple)):
            # FIXME: teach bridge to treat range and other list-lik
            # types correctly
            return NSMutableArray.arrayWithArray_(list(sequence))

        return NSMutableArray.arrayWithArray_(sequence)

CLASS_METHODS['NSArray'] = (
    ('__add__', nsarray_add),
    ('__radd__', nsarray_radd),
    ('__mul__', nsarray_mul),
    ('__rmul__', nsarray_mul),
)

# Force scans to ensure __new__ is set correctly
# FIXME: This shouldn't be necessary!
NSArray.__new__ = nsarray_new
NSMutableArray.__new__ = nsmutablearray_new
NSMutableArray.alloc().init()
#NSMutableSet.set()

NSSet = lookUpClass('NSSet')
NSMutableSet = lookUpClass('NSMutableSet')

try:
    from collections import Set
    Set.register(NSSet)
except:
    Set = (set, frozenset, NSSet)

def nsset_isdisjoint(self, other):
    for item in self:
        if item in other:
            return False
    return True

def nsset_union(self, *other):
    result = NSMutableSet()
    result.unionSet_(self)
    for val in other:
        if isinstance(val, Set):
            result.unionSet_(val)
        else:
            result.unionSet_(set(val))
    return result

def nsset_intersection(self, *others):
    if len(others) == 0:
        return self.mutableCopy()
    result = NSMutableSet()
    for item in self:
        for o in others:
            if item not in o:
                break
        else:
            result.add(item)
    return result

def nsset_difference(self, *others):
    result = self.mutableCopy()

    for value in others:
        if isinstance(value, Set):
            result.minusSet_(value)
        else:
            result.minusSet_(set(value))

    return result

def nsset_symmetric_difference(self, other):
    result = NSMutableSet()
    for item in self:
        if item not in other:
            result.add(item)
    for item in other:
        if item not in self:
            result.add(item)
    return result
    

def nsset__contains__(self, value):
    hash(value) # Force error for non-hashable values
    return self.containsObject_(value)

def nsset__or__(self, other):
    if not isinstance(self, Set):
        raise TypeError("NSSet|value where value is not a set")
    if not isinstance(other, Set):
        raise TypeError("NSSet|value where value is not a set")
    return nsset_union(self, other)

def nsset__ror__(self, other):
    if not isinstance(self, Set):
        raise TypeError("value|NSSet where value is not a set")
    if not isinstance(other, Set):
        raise TypeError("value|NSSet where value is not a set")
    return nsset_union(other, self)

def nsset__and__(self, other):
    if not isinstance(self, Set):
        raise TypeError("NSSet&value where value is not a set")
    if not isinstance(other, Set):
        raise TypeError("NSSet&value where value is not a set")
    return nsset_intersection(self, other)

def nsset__rand__(self, other):
    if not isinstance(self, Set):
        raise TypeError("value&NSSet where value is not a set")
    if not isinstance(other, Set):
        raise TypeError("value&NSSet where value is not a set")
    return nsset_intersection(other, self)

def nsset__sub__(self, other):
    if not isinstance(self, Set):
        raise TypeError("NSSet-value where value is not a set")
    if not isinstance(other, Set):
        raise TypeError("NSSet-value where value is not a set")
    return nsset_difference(self, other)

def nsset_rsub__(self, other):
    if not isinstance(self, Set):
        raise TypeError("NSSet-value where value is not a set")
    if not isinstance(other, Set):
        raise TypeError("NSSet-value where value is not a set")
    return nsset_difference(other, self)

def nsset__xor__(self, other):
    if not isinstance(self, Set):
        raise TypeError("NSSet-value where value is not a set")
    if not isinstance(other, Set):
        raise TypeError("NSSet-value where value is not a set")
    return nsset_symmetric_difference(other, self)

def nsset_issubset(self, other):
    if isinstance(other, Set):
        return self.isSubsetOfSet_(other)

    else:
        return self.isSubsetOfSet_(set(other))

def nsset__le__(self, other):
    if not isinstance(other, Set):
        raise TypeError()
    return nsset_issubset(self, other)

def nsset__eq__(self, other):
    if not isinstance(other, Set):
        return False

    return self.isEqualToSet_(other)

def nsset__ne__(self, other):
    if not isinstance(other, Set):
        return True

    return not self.isEqualToSet_(other)

def nsset__lt__(self, other):
    if not isinstance(other, Set):
        raise TypeError()

    return (self <= other) and (self != other)

def nsset_issuperset(self, other):
    if not isinstance(other, Set):
        other = set(other)

    for item in other:
        if item not in self:
            return False

    return True

def nsset__ge__(self, other):
    if not isinstance(other, Set):
        raise TypeError()
    return nsset_issuperset(self, other)

def nsset__gt__(self, other):
    if not isinstance(other, Set):
        raise TypeError()
    return (self >= other) and (self != other)

if sys.version_info[0] == 2:
    def nsset__cmp__(self, other):
        try:
            if self < other:
                return -1
            elif self == other:
                return 0
            else:
                return 1
        except TypeError:
            return cmp(id(self), id(other))

def nsset__length_hint__(self):
    return len(self)

def nsset_update(self, *others):
    for other in others:
        if isinstance(other, Set):
            self.unionSet_(other)
        else:
            self.unionSet_(set(other))

def nsset_intersection_update(self, *others):
    for other in others:
        if isinstance(other, Set):
            self.intersectSet_(other)
        else:
            self.intersectSet_(set(other))

def nsset_difference_update(self, *others):
    for other in others:
        if isinstance(other, Set):
            self.minusSet_(other)
        else:
            self.minusSet_(set(other))

def nsset_symmetric_difference_update(self, other):
    toadd = set()
    toremove = set()

    if isinstance(other, Set):
        totest = other
    else:
        totest = set(other)

    for value in self:
        if value in totest:
            toremove.add(value)
    for value in totest:
        if value not in self:
            toadd.add(value)

    self.minusSet_(toremove)
    self.unionSet_(toadd)

def nsset_pop(self):
    if len(self) == 0:
        raise KeyError()

    v = self.anyObject()
    self.removeObject_(v)
    return container_unwrap(v, KeyError)

def nsset_remove(self, value):
    hash(value)
    value = container_wrap(value)
    if value not in self:
        raise KeyError(value)
    self.removeObject_(value)

def nsset_discard(self, value):
    hash(value)
    self.removeObject_(container_wrap(value))

def nsset_add(self, value):
    hash(value)
    self.addObject_(container_wrap(value))

class nsset__iter__ (object):
    def __init__(self, value):
        self._size = len(value)
        self._enum = value.objectEnumerator()

    def __length_hint__(self):
        return self._size

    def __iter__(self):
        return self

    def next(self):
        self._size -= 1
        return container_unwrap(self._enum.nextObject(), StopIteration)


CLASS_METHODS['NSSet'] = (
    ('__iter__', lambda self: nsset__iter__(self)),
    ('__length_hint__', nsset__length_hint__),
    ('__contains__',  nsset__contains__),
    ('isdisjoint',  nsset_isdisjoint),
    ('union',  nsset_union),
    ('intersection',  nsset_intersection),
    ('difference',  nsset_difference),
    ('symmetric_difference',  nsset_symmetric_difference),
    ('issubset', nsset_issubset),
    ('__eq__', nsset__eq__),
    ('__ne__', nsset__ne__),
    ('__le__', nsset__le__),
    ('__lt__', nsset__lt__),
    ('issuperset', nsset_issuperset),
    ('__ge__', nsset__ge__),
    ('__gt__', nsset__gt__),
    ('__or__', nsset__or__),
    ('__ror__', nsset__ror__),
    ('__and__', nsset__and__),
    ('__rand__', nsset__rand__),
    ('__xor__', nsset__xor__),
    ('__rxor__', nsset__xor__),
    ('__sub__', nsset__sub__),
)

if sys.version_info[0] == 2:
    CLASS_METHODS['NSSet'] += (
        ('__cmp__', 'nsset__cmp__'),
    )

CLASS_METHODS['NSMutableSet'] = (
    ('add',  nsset_add), 
    ('remove',  nsset_remove),
    ('discard',  nsset_discard),
    ('update', nsset_update),
    ('intersection_update', nsset_intersection_update),
    ('difference_update', nsset_difference_update),
    ('symmetric_difference_update', nsset_symmetric_difference_update),
    ('clear', lambda self: self.removeAllObjects()),
    ('pop', nsset_pop),
)

def nsset_new(cls, sequence=None):
    if not sequence:
        return NSSet.set()

    if isinstance(sequence, (NSSet, set, frozenset)):
        return NSSet.set().setByAddingObjectsFromSet_(sequence)

    else:
        return NSSet.set().setByAddingObjectsFromSet_(set(sequence))

def nsmutableset_new(cls, sequence=None):
    if not sequence:
        value = NSMutableSet.set()

    elif isinstance(sequence, (NSSet, set, frozenset)):
        value = NSMutableSet.set()
        value.unionSet_(sequence)

    else:
        value = NSMutableSet.set()
        value.unionSet_(set(sequence))

    return value

NSSet.__new__ = nsset_new
NSMutableSet.__new__ = nsmutableset_new

NSMutableSet.alloc().init()
