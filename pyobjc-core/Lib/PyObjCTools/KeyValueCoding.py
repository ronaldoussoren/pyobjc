"""
Support for Key-Value Coding in Python. This provides a simple functional
interface to Cocoa's Key-Value coding that also works for regular Python
objects.

Public API:

    setKey(obj, key, value) -> None
    setKeyPath (obj, keypath, value) -> None

    getKey(obj, key) -> value
    getKeyPath (obj, keypath) -> value

A keypath is a string containing a sequence of keys seperated by dots. The
path is followed by repeated calls to 'getKey'. This can be used to easily
access nested attributes.

This API is mirroring the 'getattr' and 'setattr' APIs in Python, this makes
it more natural to work with Key-Value coding from Python. It also doesn't
require changes to existing Python classes to make use of Key-Value coding,
making it easier to build applications as a platform independent core with
a Cocoa GUI layer.

See the Cocoa documentation on the Apple developer website for more
information on Key-Value coding. The protocol is basicly used to enable
weaker coupling between the view and model layers.
"""

__all__ = ("getKey", "setKey", "getKeyPath", "setKeyPath")

import objc
import types
from itertools import imap
try:
    set
except NameError:
    from sets import Set as set

if objc.lookUpClass('NSObject').alloc().init().respondsToSelector_('setValue:forKey:'):
    SETVALUEFORKEY = 'setValue_forKey_'
    SETVALUEFORKEYPATH = 'setValue_forKeyPath_'
else:
    SETVALUEFORKEY = 'takeValue_forKey_'
    SETVALUEFORKEYPATH = 'takeValue_forKeyPath_'

def keyCaps(s):
    return s[:1].capitalize() + s[1:]

# From http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/393090
# Title: Binary floating point summation accurate to full precision
# Version no: 2.2

def msum(iterable):
    "Full precision summation using multiple floats for intermediate values"
    # sorted, non-overlapping partial sums
    partials = []
    for x in iterable:
        i = 0
        for y in partials:
            if abs(x) < abs(y):
                x, y = y, x
            hi = x + y
            lo = y - (hi - x)
            if lo:
                partials[i] = lo
                i += 1
            x = hi
        partials[i:] = [x]
    return sum(partials, 0.0)

class ArrayOperators(object):
    def avg(self, obj, segments):
        path = u'.'.join(segments)
        lst = getKeyPath(obj, path)
        count = len(lst)
        if count == 0:
            return 0.0
        return msum(imap(float, lst)) / count
    
    def count(self, obj, segments):
        return len(obj)
    
    def distinctUnionOfArrays(self, obj, segments):
        path = u'.'.join(segments)
        rval = []
        s = set()
        lists = getKeyPath(obj, path)
        for lst in lists:
            for item in lst:
                if item in s:
                    continue
                rval.append(item)
                s.add(item)
        return rval

    def distinctUnionOfObjects(self, obj, segments):
        path = u'.'.join(segments)
        rval = []
        s = set()
        lst = getKeyPath(obj, path)
        for item in lst:
            if item in s:
                continue
            rval.append(item)
            s.add(item)
        return rval
        
    def max(self, obj, segments):
        path = u'.'.join(segments)
        return max(getKeyPath(obj, path))
    
    def min(self, obj, segments):
        path = u'.'.join(segments)
        return min(getKeyPath(obj, path))
    
    def sum(self, obj, segments):
        path = u'.'.join(segments)
        lst = getKeyPath(obj, path)
        return msum(imap(float, lst))

    def unionOfArrays(self, obj, segments):
        path = u'.'.join(segments)
        rval = []
        lists = getKeyPath(obj, path)
        for lst in lists:
            rval.extend(lst)
        return rval

    def unionOfObjects(self, obj, segments):
        path = u'.'.join(segments)
        return getKeyPath(obj, path)

arrayOperators = ArrayOperators()

def getKey(obj, key):
    """
    Get the attribute referenced by 'key'. The key is used
    to build the name of an attribute, or attribute accessor method.

    The following attributes and accesors are tried (in this order):

    - Accessor 'getKey'
    - Accesoor 'get_key'
    - Accessor or attribute 'key'
    - Accessor or attribute 'isKey'
    - Attribute '_key'

    If none of these exist, raise KeyError
    """
    if obj is None:
        return None
    if isinstance(obj, (objc.objc_object, objc.objc_class)):
        try:
            return obj.valueForKey_(key)
        except ValueError, msg:
            # This is not entirely correct, should check if this
            # is the right kind of ValueError before translating
            raise KeyError, str(msg)
    
    # check for dict-like objects
    getitem = getattr(obj, '__getitem__', None)
    if getitem is not None:
        try:
            return getitem(key)
        except (KeyError, IndexError, TypeError):
            pass

    # check for array-like objects
    if not isinstance(obj, basestring):
        try:
            itr = iter(obj)
        except TypeError:
            pass
        else:
            return [getKey(obj, key) for obj in itr]

    try:
        m = getattr(obj, "get" + keyCaps(key))
    except AttributeError:
        pass
    else:
        return m()

    try:
        m = getattr(obj, "get_" + key)
    except AttributeError:
        pass
    else:
        return m()

    for keyName in (key, "is" + keyCaps(key)):
        try:
            m = getattr(obj, keyName)
        except AttributeError:
            continue

        if isinstance(m, types.MethodType) and m.im_self is obj:
            return m()

        elif isinstance(m, types.BuiltinMethodType):
            # Can't access the bound self of methods of builtin classes :-(
            return m()

        elif isinstance(m, objc.selector) and m.self is obj:
            return m()

        else:
            return m

    try:
        return getattr(obj, "_" + key)
    except AttributeError:
        raise KeyError, "Key %s does not exist" % (key,)


def setKey(obj, key, value):
    """
    Set the attribute referenced by 'key' to 'value'. The key is used
    to build the name of an attribute, or attribute accessor method.

    The following attributes and accessors are tried (in this order):
    - Accessor 'setKey_'
    - Accessor 'setKey'
    - Accessor 'set_key'
    - Attribute '_key'
    - Attribute 'key'

    Raises KeyError if the key doesn't exist.
    """
    if obj is None:
        return
    if isinstance(obj, (objc.objc_object, objc.objc_class)):
        try:
            getattr(obj, SETVALUEFORKEY)(value, key)
            return
        except ValueError, msg:
            raise KeyError, str(msg)

    aBase = 'set' + keyCaps(key)
    for accessor in (aBase + '_', aBase, 'set_' + key):
        m = getattr(obj, accessor, None)
        if m is None:
            continue
        try:
            m(value)
            return
        except TypeError:
            pass

    try:
        o = getattr(obj, "_" + key)
    except AttributeError:
        pass
    else:
        setattr(obj, "_" + key, value)
        return

    try:
        setattr(obj, key, value)
    except AttributeError:
        raise KeyError, "Key %s does not exist" % (key,)

def getKeyPath(obj, keypath):
    """
    Get the value for the keypath. Keypath is a string containing a
    path of keys, path elements are seperated by dots.
    """
    if obj is None:
        return None
        
    if isinstance(obj, (objc.objc_object, objc.objc_class)):
        return obj.valueForKeyPath_(keypath)

    elements = keypath.split('.')
    cur = obj
    elemiter = iter(elements)
    for e in elemiter:
        if e[:1] == u'@':
            try:
                oper = getattr(arrayOperators, e[1:])
            except AttributeError:
                raise KeyError, "Array operator %s not implemented" % (e,)
            return oper(cur, elemiter)
        cur = getKey(cur, e)
    return cur

def setKeyPath(obj, keypath, value):
    """
    Set the value at 'keypath'. The keypath is a string containing a
    path of keys, seperated by dots.
    """
    if obj is None:
        return
        
    if isinstance(obj, (objc.objc_object, objc.objc_class)):
        return getattr(obj, SETVALUEFORKEYPATH)(value, keypath)

    elements = keypath.split('.')
    cur = obj
    for e in elements[:-1]:
        cur = getKey(cur, e)

    return setKey(cur, elements[-1], value)

        
class kvc(object):
    def __init__(self, obj):
        self.__pyobjc_object__ = obj
    
    def __getattr__(self, attr):
        return getKey(self.__pyobjc_object__, attr)

    def __repr__(self):
        return repr(self.__pyobjc_object__)

    def __setattr__(self, attr, value):
        if not attr.startswith('_'):
            setKey(self.__pyobjc_object__, attr, value)
        object.__setattr__(self, attr, value)

    def __getitem__(self, item):
        if not isinstance(item, basestring):
            raise TypeError, 'Keys must be strings'
        return getKeyPath(self.__pyobjc_object__, item)

    def __setitem__(self, item, value):
        if not isinstance(item, basestring):
            raise TypeError, 'Keys must be strings'
        setKeyPath(self.__pyobjc_object__, item, value)
