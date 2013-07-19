"""
Convenience interface for NSArray/NSMutableArray
"""
__all__ = ()

from objc._convenience import addConvenienceForClass, container_wrap, container_unwrap
from objc._objc import lookUpClass, registerMetaDataForSelector
from objc._objc import _NSNotFound as NSNotFound

import collections
import sys

NSArray = lookUpClass('NSArray')
NSMutableArray = lookUpClass('NSMutableArray')

collections.Sequence.register(NSArray)
collections.MutableSequence.register(NSMutableArray)

if sys.version_info[0] == 2:
    INT_TYPES = (int, long)
    STR_TYPES = (str, unicode)
else:
    INT_TYPES = int
    STR_TYPES = str

def reverse_exchangeObjectAtIndex_withObjectAtIndex_(self):
    begin = 0
    end = len(self) - 1
    while begin < end:
        self.exchangeObjectAtIndex_withObjectAtIndex_(begin, end)
        begin += 1
        end -= 1

def ensureArray(anArray):
    if not isinstance(anArray, (NSArray, list, tuple)):
        anArray = list(anArray)
    return anArray


def extend_addObjectsFromArray_(self, anArray):
    self.addObjectsFromArray_(ensureArray(anArray))

_index_sentinel=object()
def index_indexOfObject_inRange_(self, item, start=0, stop=_index_sentinel):
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

        if ln > sys.maxsize:
            ln = sys.maxsize

        res = self.indexOfObject_inRange_(item, (start, ln))
        if res == NSNotFound:
            raise ValueError("%s.index(x): x not in list" % (type(self).__name__,))
    return res

def insert_insertObject_atIndex_(self, idx, item):
    if idx < 0:
        idx += len(self)
        if idx < 0:
            raise IndexError("list index out of range")
    self.insertObject_atIndex_(container_wrap(item), idx)


def __getitem__objectAtIndex_(self, idx):
    if isinstance(idx, slice):
        start, stop, step = idx.indices(len(self))
        #if step == 1:
        #    m = getattr(self, 'subarrayWithRange_', None)
        #    if m is not None:
        #        return m((start, stop - start))
        return [self[i] for i in range(start, stop, step)]

    elif not isinstance(idx, INT_TYPES):
        raise TypeError("index must be a number")

    if idx < 0:
        idx += len(self)
        if idx < 0:
            raise IndexError("list index out of range")

    return container_unwrap(self.objectAtIndex_(idx), RuntimeError)

def __getslice__objectAtIndex_(self, i, j):
    i = max(i, 0); j = max(j, 0)
    return __getitem__objectAtIndex_(self, slice(i, j))

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
        r = reversed(range(start, stop, step))
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

        slice_len = len(range(start, stop, step))
        if slice_len != len(anObject):
            raise ValueError("Replacing extended slice with %d elements by %d elements"%(
                slice_len, len(anObject)))

        if step > 0:
            if anObject is self:
                toAssign = list(anObject)
            else:
                toAssign = anObject
            for inIdx, outIdx in enumerate(range(start, stop, step)):
                self.replaceObjectAtIndex_withObject_(outIdx, toAssign[inIdx])

        elif step == 0:
            raise ValueError("Step 0")

        else:
            if anObject is self:
                toAssign = list(anObject)
            else:
                toAssign = anObject
            for inIdx, outIdx in enumerate(range(start, stop, step)):
                self.replaceObjectAtIndex_withObject_(outIdx, toAssign[inIdx])


    elif not isinstance(idx, INT_TYPES):
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



registerMetaDataForSelector(b"NSObject", b"sortUsingFunction:context:",
        dict(
            arguments={
                2:  {
                        'callable': {
                            'reval': 'i',
                            'arguments': {
                                0: { 'type': b'@' },
                                1: { 'type': b'@' },
                                2: { 'type': b'@' },
                            }
                        },
                        'callable_retained': False,
                },
                3:  { 'type': b'@' },
            },
        ))


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

    return result



def nsarray_new(cls, sequence=None):
    if not sequence:
        return NSArray.array()

    elif isinstance(sequence, STR_TYPES):
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

    elif isinstance(sequence, STR_TYPES):
        return NSMutableArray.arrayWithArray_(list(sequence))

    else:
        if not isinstance(sequence, (list, tuple)):
            # FIXME: teach bridge to treat range and other list-lik
            # types correctly
            return NSMutableArray.arrayWithArray_(list(sequence))

        return NSMutableArray.arrayWithArray_(sequence)


def containsObject_has_key(self, elem):
    return bool(self.containsObject_(container_wrap(elem)))


addConvenienceForClass('NSArray', (
    ('__add__', nsarray_add),
    ('__radd__', nsarray_radd),
    ('__mul__', nsarray_mul),
    ('__rmul__', nsarray_mul),
    ('__new__', staticmethod(nsarray_new)),
    ('__len__', lambda self: self.count()),
    ('__contains__', containsObject_has_key),
    ('index', index_indexOfObject_inRange_),
    ('remove', remove_removeObjectAtIndex_),
    ('pop', pop_removeObjectAtIndex_),
    ('__delitem__', __delitem__removeObjectAtIndex_),
    ('__delslice__', __delslice__removeObjectAtIndex_), # Python 2
    ('__copy__', lambda self: self.copy()),
    ('__getitem__', __getitem__objectAtIndex_),
    ('__getslice__', __getslice__objectAtIndex_),
))

addConvenienceForClass('NSMutableArray', (
    ('__setitem__', __setitem__replaceObjectAtIndex_withObject_),
    ('__setslice__', __setslice__replaceObjectAtIndex_withObject_),
    ('__new__', staticmethod(nsmutablearray_new)),
    ('extend', extend_addObjectsFromArray_),
    ('append', lambda self, item: self.addObject_(container_wrap(item))),
    #('sort', sort),
    ('insert', insert_insertObject_atIndex_),
    ('reverse', reverse_exchangeObjectAtIndex_withObjectAtIndex_),
    ('clear', lambda self: self.removeAllObjects()),
    ('__copy__', lambda self: self.mutableCopy()),
))
