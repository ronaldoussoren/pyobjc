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

TODO: Add unittests (in test/test_keyvalue.py)
"""

__all__ = ("getKey", "setKey", "getKeyPath", "setKeyPath")

import objc

def getKey(obj, key):
    """
    Get the attribute referenced by 'key'. The key is used
    to build the name of an attribute, or attribute accessor method.

    The following attributes and accesors at tried (in this order):
    - Accessor 'getKey'
    - Accesoor 'get_key'
    - Attribute 'key'
    - Attribute '_key'

    If none of these exist, raise KeyError
    """
    if isinstance(obj, (objc.objc_object, objc.objc_class)):
        try:
            return obj.valueForKey_(key)
        except ValueError, msg:
            # This is not entirely correct, should check if this
            # is the right kind of ValueError before translating 
            raise KeyError, str(msg)


    try:
        m = getattr(obj, "get" + key.capitalize())
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

    try:
        return getattr(obj, key)
    except AttributeError:
        pass

    try:
        return getattr(obj, "_" + key)
    except AttributeError:
        pass

    raise KeyError, "Key %s does not exist"%(key,)

def setKey(obj, key, value):
    """
    Set the attribute referenced by 'key' to 'value'. The key is used
    to build the name of an attribute, or attribute accessor method.

    The following attributes and accessors are tried (in this order):
    - Accessor 'setKey'
    - Accessor 'set_key'
    - Attribute '_key'
    - Attribute 'key'

    Raises KeyError if the key doesn't exist.
    """
    if isinstance(obj, (objc.objc_object, objc.objc_class)):
        try:
            return obj.takeValue_forKey_(value, key)
        except ValueError, msg:
            raise KeyError, str(msg)

    try:
        m = getattr(obj, 'set' + key.capitalize())
    except AttributeError:
        pass
    else:
        m(value)
        return

    try:
        m = getattr(obj, 'set_' + key)
    except AttributeError:
        pass
    else:
        m(value)
        return

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
        raise KeyError, "Key %s does not exist"%(key,)

def getKeyPath(obj, keypath):
    """
    Get the value for the keypath. Keypath is a string containing a
    path of keys, path elements are seperated by dots.
    """
    if isinstance(obj, (objc.objc_object, objc.objc_class)):
        return obj.valueForKeyPath_(keypath)

    elements = keypath.split('.')
    cur = obj
    for e in elements:
        cur = getKey(cur, e)
    return cur

def setKeyPath(obj, keypath, value):
    """
    Set the value at 'keypath'. The keypath is a string containing a
    path of keys, seperated by dots.
    """
    if isinstance(obj, (objc.objc_object, objc.objc_class)):
        return obj.takeValue_forKeyPath_(value, keypath)

    elements = keypath.split('.')
    cur = obj
    for e in elements[:-1]:
        cur = getKey(cur, e)

    return setKey(cur, elements[-1], value)

class KeyValueCodingMixIn:
    def valueForKey_(self, aKey):
        return getKey(self, aKey)

    def takeValue_forKey_(self, aValue, aKey):
        return setKey(self, aKey, aValue)

    def valueForKeyPath_(self, aKey):
        return getKeyPath(self, aKey)
                    
    def takeValue_forKeyPath_(self, aValue, aKey):
        return setKeyPath(self, aKey, aValue)

