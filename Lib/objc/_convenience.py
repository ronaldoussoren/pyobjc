from __future__ import generators

"""
This module implements a callback function that is used by the C code to
add Python special methods to Objective-C classes with a suitable interface.

This module contains no user callable code.

TODO:
- Add external interface: Framework specific modules may want to add to this.
"""
from objc import set_class_extender, selector, runtime

CONVENIENCE_METHODS = {}
CLASS_METHODS = {}

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
    for sel in type_dict.values():
        if not isinstance(sel, selector):
            continue

        
        if sel.selector.startswith('init') and not sel.isClassMethod:
            # Instance methods that start with 'init*' are constructors. These
            # return 'self'. If they don't they reallocated the previous 
            # value, don't use that afterwards.
            sel.returnsSelf = 1
            sel.isInitializer = 1
        elif sel.selector == "alloc" or sel.selector == "allocWithZone:":
            sel.isAlloc = 1

        if sel.selector in ( 'copy', 'copyWithZone:', 
                      'mutableCopy', 'mutableCopyWithZone:'):
            # These methods transfer ownership to the caller, the runtime uses
            # this information to adjust the reference count.
            sel.doesDonateReference = 1

        sel = sel.selector

        if CONVENIENCE_METHODS.has_key(sel):
            v = CONVENIENCE_METHODS[sel]
            for name, value in v:
                if name in type_dict and isinstance(type_dict[name], selector):

                    # Clone attributes of already existing version

                    t = type_dict[name]
                    v = selector(value, selector=t.selector, 
                        signature=t.signature, isClassMethod=t.isClassMethod)
                    v.isInitializer = t.isInitializer
                    v.returnsSelf = t.returnsSelf
                    v.isAlloc = t.isAlloc

                    #if t.selector.startswith('init'):
                    #    v.isInitializer = 1
                    #    v.returnsSelf = 1
                    #elif sel.selector == "alloc" \
                    #        or sel.selector == "allocWithZone:":
                    #    sel.isAlloc = 1

                    type_dict[name] = v
                else:
                    type_dict[name] = value

    if CLASS_METHODS.has_key(name):
        for name, value in CLASS_METHODS[name]:
            type_dict[name] = value

set_class_extender(add_convenience_methods)

# NOTE: the '!= 0' in the definition of the comparison function
# is there to force conversion to type 'bool' on Python releases
# that have such a type.

def __getitem__objectForKey(self, key):
    res = self.objectForKey_(key)
    if res is None:
        raise KeyError, key
    return res
def has_key_objectForKey(self, key):
    res = self.objectForKey_(key)
    return res is not None
def get_objectForKey(self, key, dflt=None):
    res = self.objectForKey_(key)
    if res is None: 
        res = dflt
    return res

CONVENIENCE_METHODS['objectForKey:'] = (
    ('__getitem__', __getitem__objectForKey),
    ('has_key', has_key_objectForKey),
    ('get', get_objectForKey),
    ('__contains__', lambda self, elem: (self.objectForKey_(elem) is not None)),
)

CONVENIENCE_METHODS['removeObjectForKey:'] = (
    ('__delitem__', lambda self, key: self.removeObjectForKey_(key)), 
)

def dict_update(self, other):
    for key, value in other.items():
        self.setObject_forKey_(value, key)

def dict_setdefault(self, key, dflt=None):
    res = self.objectForKey_(key)
    if res is None:
        res = dflt
        self.setObject_forKey_(dflt, key)
    return res

def dict_pop(self, key, dflt=None):
    res = self.objectForKey_(key)
    if res is None:
        if dflt is None:
            raise KeyError, key
        res = dflt
    else:
        self.removeObjectForKey_(key)
    return res


def dict_popitem(self):
    o = self.keyEnumerator().nextItem()
    if o is None:
        raise KeyError, "popitem on an empty dict"
    v = self.objectForKey_(o)
    if v is None:
        raise KeyError, "popitem on an empty dict"
    return (o, v)

CONVENIENCE_METHODS['setObject:forKey:'] = (
    ('__setitem__', lambda self, key, value: self.setObject_forKey_(value, key)), 
    ('update', dict_update),
    ('setdefault', dict_setdefault),
    ('pop', dict_pop),
    ('popitem', dict_popitem),
)


CONVENIENCE_METHODS['count'] = (
    ('__len__', lambda self: self.count()),
)

CONVENIENCE_METHODS['description'] = (
    # Don't do '__repr__', if the object is not yet initialized this may
    # cause coredumps (and __repr__ is used by the interpreter to print
    # objects in interactive mode)
    #('__repr__', lambda self: self.description()),
    ('__str__', lambda self: self.description()),
)

CONVENIENCE_METHODS['containsObject:'] = (
    ('__contains__', lambda self, elem: bool(self.containsObject_(elem))),
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

def __getitem__objectAtIndexWithSlice(self, x, y):
    l = len(self)
    r = y - x
    if r < 0:
        return []
    if (r - x) > l:
        r = l - x
    res =  self.subarrayWithRange_( (x, r) )
    return res

def __getitem__objectAtIndex(self, idx):
    if idx < 0:
        idx = len(self) + idx
        if idx < 0:
            raise IndexError, "index out of range"
    elif idx >= len(self):
            raise IndexError, "index out of range"
    return self.objectAtIndex_(idx)

CONVENIENCE_METHODS['addObject:'] = (
    ( 'append', lambda self, item: self.addObject_(item) ),
)

CONVENIENCE_METHODS['addObjectsFromArray:'] = (
    ('extend', lambda self, item: self.addObjectsFromArray_(item)),
)

def index_indexOfObject(self, item):
    import Foundation

    res = self.indexOfObject_(item)
    if res == Foundation.NSNotFound:
        raise ValueError, "NSArray.index(x): x not in list"

CONVENIENCE_METHODS['indexOfObject:'] = (
    ('index', index_indexOfObject),
)

CONVENIENCE_METHODS['insertObject:atIndex:'] = (
    ( 'insert', lambda self, idx, item: self.insertObject_atIndex(item,idx)),
)

CONVENIENCE_METHODS['objectAtIndex:'] = (
    ('__getitem__', __getitem__objectAtIndex),
    ('__getslice__', __getitem__objectAtIndexWithSlice),
)

def __delslice__removeObjectAtIndex(self, x, y):
    l = len(self)
    r = y - x
    if r < 0:
        return
    if (r - x) > l:
        r = l - x
    return self.removeObjectsInRange_( (x, r) )
    
CONVENIENCE_METHODS['removeObjectAtIndex:'] = (
    ('__delitem__', lambda self, index: self.removeObjectAtIndex_(index)),
    ('__delslice__', __delslice__removeObjectAtIndex),
)

CONVENIENCE_METHODS['replaceObjectAtIndex:withObject:'] = (
    ('__setitem__', lambda self, index, anObject: self.replaceObjectAtIndex_withObject_(index, anObject)),
)

def __setslice__replaceObjectAtIndex_withObject(self, x, y, v):
    l = len(self)
    r = y - x
    if r < 0:
        return
    if (r - x) > l:
        r = l - x
    return self.replaceObjectsInRange_withObjectsFromArray_( (x, r), v )

CONVENIENCE_METHODS['replaceObjectsInRange:withObjectsFromArray:'] = (
    ('__setslice__', __setslice__replaceObjectAtIndex_withObject), 
)

# Mapping protocol

# Mappings (e.g. like dict)
# TODO (not all are needed or even possible): 
#   iter*, update, pop, popitem, setdefault
# __str__ would be nice (as obj.description()),

def enumeratorGenerator(anEnumerator):
    nextObject = anEnumerator.nextObject()
    while nextObject is not None:
        yield nextObject
        nextObject = anEnumerator.nextObject()

def dictItems(aDict):
    """
    NSDictionary.items()
    """
    keys = aDict.allKeys()
    values = aDict.objectsForKeys_notFoundMarker_(keys, runtime.NSNull.null())
    return zip(keys, values)


CONVENIENCE_METHODS['allKeys'] = (
    ('keys', lambda self: self.allKeys()),
    ('items', lambda self: dictItems(self)),
)

CONVENIENCE_METHODS['allValues'] = (
    ('values', lambda self: self.allValues()),
)

def itemsGenerator(aDict):
    anEnumerator = aDict.keyEnumerator()
    nextObject = anEnumerator.nextObject()
    while nextObject is not None:
        yield (nextObject, aDict.objectForKey_(nextObject))
        nextObject = anEnumerator.nextObject()

CONVENIENCE_METHODS['keyEnumerator'] = (
    ('__iter__', lambda self: enumeratorGenerator(self.keyEnumerator())),
    ('iterkeys', lambda self: enumeratorGenerator( self.keyEnumerator())),
    ('iteritems', lambda self: itemsGenerator(self)),
)

CONVENIENCE_METHODS['objectEnumerator'] = (
    ('__iter__', lambda self: enumeratorGenerator(self.objectEnumerator())),
    ('itervalues', lambda self: enumeratorGenerator( self.objectEnumerator())),
)

# Ronald: I don't think you want this!
#CONVENIENCE_METHODS['reverseObjectEnumerator'] = (
#    ('__iter__', lambda self: enumeratorGenerator(self.reverseObjectEnumerator())),
#    ('itervalues', lambda self: enumeratorGenerator(self.reverseObjectEnumerator()))
#)

CONVENIENCE_METHODS['removeAllObjects'] = (
    ('clear', lambda self: self.removeAllObjects()),
)

CONVENIENCE_METHODS['dictionaryWithDictionary:'] = (
    ('copy', lambda self: type(self).dictionaryWithDictionary_(self)),
)

CONVENIENCE_METHODS['nextObject'] = (
    ('__iter__', lambda self: enumeratorGenerator(self)),
    ('itervalues', lambda self: enumeratorGenerator(self)),
)

#
# NSNumber seems to be and abstract base-class that is implemented using
# NSCFNumber, a CoreFoundation 'proxy'.
#
def _num_to_python(v):
    """
    Magic method that converts NSNumber values to Python, see 
    <Foundation/CFNumber.h> for the magic numbers
    """
    if hasattr(v, '_cfNumberType'):
        tp = v._cfNumberType()
        if tp in [ 1, 2, 3, 7, 8, 9, 10 ]:
            v = v.longValue()
        elif tp in [ 4, 11 ]:
            v = v.longlongValue()
        elif tp in [ 5, 6, 12, 13 ]:
            v = v.doubleValue()
        else:
            print "Unhandled numeric type: %s"%tp

    return v

def __abs__CFNumber(numA):
    return abs(_num_to_python(numA))

def __add__CFNumber(numA, numB):
    return _num_to_python(numA) + _num_to_python(numB)

def __and__CFNumber(numA, numB):
    return _num_to_python(numA) & _num_to_python(numB)

def __div__CFNumber(numA, numB):
    return _num_to_python(numA) / _num_to_python(numB)

def __divmod__CFNumber(numA, numB):
    return divmod(_num_to_python(numA), _num_to_python(numB))

def __float__CFNumber(numA):
    return float(_num_to_python(numA))

def __floordiv__CFNumber(numA, numB):
    return _num_to_python(numA) // _num_to_python(numB)

def __hex__CFNumber(numA):
    return hex(_num_to_python(numA))

def __int__CFNumber(numA):
    return int(_num_to_python(numA))

def __invert__CFNumber(numA):
    return ~_num_to_python(numA)

def __long__CFNumber(numA):
    return long(_num_to_python(numA))

def __lshift__CFNumber(numA, numB):
    return _num_to_python(numA) << _num_to_python(numB)

def __rshift__CFNumber(numA, numB):
    return _num_to_python(numA) >> _num_to_python(numB)

def __mod__CFNumber(numA, numB):
    return _num_to_python(numA) % _num_to_python(numB)

def __mul__CFNumber(numA, numB):
    return _num_to_python(numA) * _num_to_python(numB)

def __neg__CFNumber(numA):
    return -_num_to_python(numA)

def __oct__CFNumber(numA):
    return oct(_num_to_python(numA))

def __or__CFNumber(numA, numB):
    return _num_to_python(numA)  | _num_to_python(numB)

def __pos__CFNumber(numA):
    return +_num_to_python(numA)

def __pow__CFNumber(numA, numB, modulo=None):
    if modulo is None:
        return _num_to_python(numA)  ** _num_to_python(numB)
    else:
        return pow(_num_to_python(numA), _num_to_python(numB), modulo)

def __sub__CFNumber(numA, numB):
    return _num_to_python(numA)  - _num_to_python(numB)

def __truediv__CFNumber(numA, numB):
    return _num_to_python(numA) / _num_to_python(numB)

def __xor__CFNumber(numA, numB):
    return _num_to_python(numA)  ^ _num_to_python(numB)

import __builtin__
if not hasattr(__builtin__, 'bool'):
    def bool(x):
        if x:
            return 1
        else:
            return 0

def __nonzero__CFNumber(numA):
    return bool(_num_to_python(numA))

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
        objects.append(values[i])
        keys.append(values[i+1])
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
