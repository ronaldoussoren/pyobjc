"""
This module implements a callback function that is used by the C code to
add Python special methods to Objective-C classes with a suitable interface.

This module contains no user callable code.

TODO:
- Add external interface: Framework specific modules may want to add to this.
"""
from _objc import setClassExtender, selector, lookUpClass, currentBundle, ivar
from itertools import imap

__all__ = ['CONVENIENCE_METHODS', 'CLASS_METHODS']

CONVENIENCE_METHODS = {}
CLASS_METHODS = {}

NSObject = lookUpClass('NSObject')

def add_convenience_methods(super_class, name, type_dict):
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
            if '__useKVO__' not in type_dict:
                if not (
                        'willChangeValueForKey_' in type_dict
                        or 'didChangeValueForKey_' in type_dict):
                    type_dict['__useKVO__'] = issubclass(super_class, NSObject)
        if '__bundle_hack__' in type_dict:
            import warnings
            warnings.warn(
                "__bundle_hack__ is not necessary in PyObjC 1.3+ / py2app 0.1.8+",
                DeprecationWarning)

    for k, sel in type_dict.items():
        if not isinstance(sel, selector):
            continue

        if sel.selector == "alloc" or sel.selector == "allocWithZone:":
            sel.isAlloc = 1

        if sel.selector in ( 'copy', 'copyWithZone:',
                      'mutableCopy', 'mutableCopyWithZone:'):
            # These methods transfer ownership to the caller, the runtime uses
            # this information to adjust the reference count.
            sel.doesDonateReference = 1

        sel = sel.selector

        if sel in CONVENIENCE_METHODS:
            v = CONVENIENCE_METHODS[sel]
            for name, value in v:
                if name in type_dict and isinstance(type_dict[name], selector):

                    # Clone attributes of already existing version

                    t = type_dict[name]
                    v = selector(value, selector=t.selector,
                        signature=t.signature, isClassMethod=t.isClassMethod)
                    v.isAlloc = t.isAlloc

                    type_dict[name] = v
                else:
                    type_dict[name] = value

    if name in CLASS_METHODS:
        for name, value in CLASS_METHODS[name]:
            type_dict[name] = value

setClassExtender(add_convenience_methods)

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

CONVENIENCE_METHODS['removeObject:'] = (
    ('discard', lambda self, elem: self.removeObject_(container_wrap(elem))),
)

CONVENIENCE_METHODS['hash'] = (
    ('__hash__', lambda self: self.hash()),
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
    ( 'append', lambda self, item: self.addObject_(container_wrap(item))),
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
    idx = slice(idx, None, None).indices(len(self)).start
    self.insertObject_atIndex_(container_wrap(item), idx)

CONVENIENCE_METHODS['insertObject:atIndex:'] = (
    ( 'insert', insert_insertObject_atIndex_),
)

def __getitem__objectAtIndex_(self, idx):
    length = len(self)
    if isinstance(idx, slice):
        start, stop, step = idx.indices(length)
        #if step == 1:
        #    m = getattr(self, 'subarrayWithRange_', None)
        #    if m is not None:
        #        return m((start, stop - start))
        return [self[i] for i in xrange(start, stop, step)]
    if idx < 0:
        idx += length
        if idx < 0:
            raise IndexError, "index out of range"
    elif idx >= length:
        raise IndexError, "index out of range"
    return container_unwrap(self.objectAtIndex_(idx), RuntimeError)

CONVENIENCE_METHODS['objectAtIndex:'] = (
    ('__getitem__', __getitem__objectAtIndex_),
)

def __delitem__removeObjectAtIndex_(self, idx):
    length = len(self)
    if isinstance(idx, slice):
        start, stop, step = idx.indices(length)
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
        idx += length
        if idx < 0:
            raise IndexError, "index out of range"
    elif idx >= length:
        raise IndexError, "index out of range"
    self.removeObjectAtIndex_(idx)
    
CONVENIENCE_METHODS['removeObjectAtIndex:'] = (
    ('__delitem__', __delitem__removeObjectAtIndex_),
)

def __setitem__replaceObjectAtIndex_withObject_(self, idx, anObject):
    length = len(self)
    if isinstance(idx, slice):
        start, stop, step = idx.indices(length)
        if step == 1:
            m = getattr(self, 'replaceObjectsInRange_withObjectsFromArray_', None)
            if m is not None:
                m((start, stop - start), ensureArray(anObject))
                return
        # XXX - implement this..
        raise NotImplementedError
    if idx < 0:
        idx += length
        if idx < 0:
            raise IndexError, "index out of range"
    elif idx >= length:
        raise IndexError, "index out of range"
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
NSDecimalNumber = lookUpClass('NSDecimalNumber')
NSNull = lookUpClass('NSNull')
NSArray = lookUpClass('NSArray')
null = NSNull.null()

class PyObjCUtilWrap(NSObject):
    __useKVO__ = False
    __slots__ = ()
    tmp = ivar('tmp')
    def wrap_(self, anObject):
        self.tmp = anObject
        return self.tmp

def number_wrap(v):
    # we should have a nicer way to cross the bridge
    return PyObjCUtilWrap.alloc().init().wrap_(v)

def container_wrap(v):
    if v is None:
        return null
    return v

def container_unwrap(v, exc_type, *exc_args):
    if v is null:
        return None
    elif v is None:
        raise exc_type(*exc_args)
    return v

def _numberForDecimal(v):
    # make sure we have a NSDecimal type around
    import Foundation
    return v.decimalValue()

def _num_to_python(v):
    """
    Magic method that converts NSNumber values to Python, see
    <CoreFoundation/CFNumber.h> for the magic numbers
    """
    if isinstance(v, NSDecimalNumber):
        return _numberForDecimal(v)
    # XXX - this only works for Mac OS X
    #       GNUstep and Mac OS X can both use objCType
    if hasattr(v, '_cfNumberType'):
        tp = v._cfNumberType()
        if tp in [ 1, 2, 3, 7, 8, 9, 10 ]:
            v = v.longValue()
        elif tp in [ 4, 11 ]:
            v = v.longlongValue()
        elif tp in [ 5, 6, 12, 13 ]:
            v = v.doubleValue()
        else:
            import warnings
            warnings.warn(RuntimeWarning, "Unhandled numeric type: %r" % (tp,))

    return v

def __abs__CFNumber(numA):
    return number_wrap(abs(_num_to_python(numA)))

def __add__CFNumber(numA, numB):
    return number_wrap(_num_to_python(numA) + _num_to_python(numB))

def __and__CFNumber(numA, numB):
    return number_wrap(_num_to_python(numA) & _num_to_python(numB))

def __div__CFNumber(numA, numB):
    return number_wrap(_num_to_python(numA) / _num_to_python(numB))

def __divmod__CFNumber(numA, numB):
    return number_wrap(divmod(_num_to_python(numA), _num_to_python(numB)))

def __float__CFNumber(numA):
    return numA.doubleValue()

def __floordiv__CFNumber(numA, numB):
    return number_wrap(_num_to_python(numA) // _num_to_python(numB))

def __hex__CFNumber(numA):
    return hex(_num_to_python(numA))

def __int__CFNumber(numA):
    return numA.longValue()

def __invert__CFNumber(numA):
    return number_wrap(~_num_to_python(numA))

def __long__CFNumber(numA):
    return numA.longLongValue()

def __lshift__CFNumber(numA, numB):
    return number_wrap(_num_to_python(numA) << _num_to_python(numB))

def __rshift__CFNumber(numA, numB):
    return number_wrap(_num_to_python(numA) >> _num_to_python(numB))

def __mod__CFNumber(numA, numB):
    return number_wrap(_num_to_python(numA) % _num_to_python(numB))

def __mul__CFNumber(numA, numB):
    return number_wrap(_num_to_python(numA) * _num_to_python(numB))

def __neg__CFNumber(numA):
    return number_wrap(-_num_to_python(numA))

def __oct__CFNumber(numA):
    return oct(_num_to_python(numA))

def __or__CFNumber(numA, numB):
    return number_wrap(_num_to_python(numA)  | _num_to_python(numB))

def __pos__CFNumber(numA):
    return +number_wrap(_num_to_python(numA))

def __pow__CFNumber(numA, numB, modulo=None):
    if modulo is None:
        return number_wrap(_num_to_python(numA)  ** _num_to_python(numB))
    else:
        return number_wrap(pow(_num_to_python(numA), _num_to_python(numB), modulo))

def __sub__CFNumber(numA, numB):
    return number_wrap(_num_to_python(numA)  - _num_to_python(numB))

def __truediv__CFNumber(numA, numB):
    return number_wrap(_num_to_python(numA) / _num_to_python(numB))

def __xor__CFNumber(numA, numB):
    return number_wrap(_num_to_python(numA)  ^ _num_to_python(numB))

def __nonzero__CFNumber(numA):
    return bool(numA.boolValue())

CONVENIENCE_METHODS['_cfNumberType'] = (
    ('__abs__', __abs__CFNumber),
    ('__add__', __add__CFNumber),
    ('__and__', __and__CFNumber),
    ('__div__', __div__CFNumber),
    ('__divmod__', __divmod__CFNumber),
    ('__float__', __float__CFNumber),
    ('__floordiv__', __floordiv__CFNumber),
    ('__hex__', __hex__CFNumber),
    ('__int__', __int__CFNumber),
    ('__invert__', __invert__CFNumber),
    ('__long__', __long__CFNumber),
    ('__lshift__', __lshift__CFNumber),
    ('__mod__', __mod__CFNumber),
    ('__mul__', __mul__CFNumber),
    ('__neg__', __neg__CFNumber),
    ('__oct__', __oct__CFNumber),
    ('__or__', __or__CFNumber),
    ('__pos__', __pos__CFNumber),
    ('__pow__', __pow__CFNumber),
    ('__radd__', lambda x, y: __add__CFNumber(y, x)),
    ('__rand__', lambda x, y: __and__CFNumber(y, x)),
    ('__rdiv__', lambda x, y: __div__CFNumber(y, x)),
    ('__rdivmod__', lambda x, y: __divmod__CFNumber(y, x)),
    ('__rfloordiv__', lambda x, y: _rfloordiv__CFNumber(y, x)),
    ('__rlshift__', lambda x, y: __lshift__CFNumber(y, x)),
    ('__rmod__', lambda x, y: __mod__CFNumber(y, x)),
    ('__rmul__', lambda x, y: __mul__CFNumber(y, x)),
    ('__ror__', lambda x, y: __or__CFNumber(y, x)),
    ('__rpow__', lambda x, y, z=None: __pow__CFNumber(y, x, z)),
    ('__rrshift__', lambda x, y: __rshift__CFNumber(y, x)),
    ('__rshift__', lambda x, y: __shift__CFNumber(y, x)),
    ('__rsub__', lambda x, y: __sub__CFNumber(y, x)),
    ('__rtruediv__', lambda x, y: __truediv__CFNumber(y, x)),
    ('__rxor__', lambda x, y: __xor__CFNumber(y, x)),
    ('__sub__', __sub__CFNumber),
    ('__truediv__', __truediv__CFNumber),
    ('__xor__', __xor__CFNumber),
    ('__nonzero__', __nonzero__CFNumber),
)
CONVENIENCE_METHODS['decimalNumberByAdding:'] = CONVENIENCE_METHODS['_cfNumberType']

#CONVENIENCE_METHODS['boolValue'] = (
#    ('__nonzero__', lambda (self): self.boolValue() != 0),
#)


#
# Special wrappers for a number of varargs functions (constructors)
#

def initWithObjects_(self, *args):
    if args[-1] is not None:
        raise ValueError, "Need None as the last argument"
    return self.initWithArray_(args[:-1])

CONVENIENCE_METHODS['initWithObjects:'] = (
    ('initWithObjects_', initWithObjects_),
)

def arrayWithObjects_(self, *args):
    if args[-1] is not None:
        raise ValueError, "Need None as the last argument"
    return self.arrayWithArray_(args[:-1])

CONVENIENCE_METHODS['arrayWithObjects:'] = (
    ('arrayWithObjects_', selector(arrayWithObjects_, signature='@@:@', isClassMethod=1)),
)


def setWithObjects_(self, *args):
    if args[-1] is not None:
        raise ValueError, "Need None as the last argument"
    return self.setWithArray_(args[:-1])

CONVENIENCE_METHODS['setWithObjects:'] = (
    ('setWithObjects_', selector(setWithObjects_, signature='@@:@', isClassMethod=1)),
)

def setWithObjects_count_(self, args, count):
    return self.setWithArray_(args[:count])

CONVENIENCE_METHODS['setWithObjects:count:'] = (
    ('setWithObjects_count_', selector(setWithObjects_count_, signature='@@:^@i', isClassMethod=1)),
)

def splitObjectsAndKeys(values):
    if values[-1] is not None:
        raise ValueError, "Need None as the last argument"
    if len(values) % 2 != 1:
        raise ValueError, "Odd number of arguments"

    objects = []
    keys = []
    for i in range(0, len(values)-1, 2):
        objects.append(container_wrap(values[i]))
        keys.append(container_wrap(values[i+1]))
    return objects, keys

def dictionaryWithObjectsAndKeys_(self, *values):
    objects, keys = splitObjectsAndKeys(values)
    return self.dictionaryWithObjects_forKeys_(objects, keys)

CONVENIENCE_METHODS['dictionaryWithObjectsAndKeys:'] = (
    ('dictionaryWithObjectsAndKeys_',
      selector(dictionaryWithObjectsAndKeys_, signature='@@:@',isClassMethod=1)),
)

def initWithObjectsAndKeys_(self, *values):
    objects, keys = splitObjectsAndKeys(values)
    return self.initWithObjects_forKeys_(objects, keys)

CONVENIENCE_METHODS['initWithObjectsAndKeys:'] = (
    ( 'initWithObjectsAndKeys_', initWithObjectsAndKeys_ ),
)

def UnsupportedMethod(self, *args):
    raise ValueError, "Unsupported method"

CONVENIENCE_METHODS['poseAsClass:'] = (
    ('poseAsClass_', (UnsupportedMethod)),
)

def sort(self, cmpfunc=cmp):
    def doCmp(a, b, cmpfunc):
        return cmpfunc(a, b)

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
        (   '__nonzero__',  lambda self: False ),
)
