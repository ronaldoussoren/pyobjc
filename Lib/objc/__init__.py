"""
Python <-> Objective-C bridge (PyObjC)

This module defines the core interfaces of the Python<->Objective-C bridge.
"""

# Aliases for some common Objective-C constants
nil = None
YES = True
NO = False

def _update(g=globals()):
    import _objc
    for k,v in _objc.__dict__.iteritems():
        g.setdefault(k,v)
_update()
del _update
import _FoundationSignatures

# Add useful utility functions below
if platform == 'MACOSX':
    from _dyld import *
else:
    from _gnustep import *

class _runtime:
    """
    Backward compatibility interface.

    This class provides (partial) support for the interface of
    older versions of PyObjC.
    """
    def __getattr__(self, name):
        import warnings
        warnings.warn("Deprecated: use objc.lookUpClass",
            DeprecationWarning)
        if name == '__objc_classes__':
            return getClassList()
        elif name == '__kind__':
            return 'python'

        try:
            return lookUpClass(name)
        except nosuchclass_error:
            raise AttributeError, name

    def __eq__(self, other):
        return self is other

    def __repr__(self):
        return "objc.runtime"
runtime = _runtime()
del _runtime

from _descriptors import *

_PLUGINS = {}
def registerPlugin(pluginName):
    """
    Deprecated: use currentBundle()

    Register the current py2app plugin by name and return its bundle
    """
    import os
    import sys
    path = os.path.dirname(os.path.dirname(os.environ['RESOURCEPATH']))
    if not isinstance(path, unicode):
        path = unicode(path, sys.getfilesystemencoding())
    _PLUGINS[pluginName] = path
    return pluginBundle(pluginName)

def pluginBundle(pluginName):
    """
    Deprecated: use currentBundle()

    Return the main bundle for the named plugin. This should be used
    only after it has been registered with registerPlugin
    """
    import warnings
    warnings.warn("Deprecated: use currentBundle()", DeprecationWarning)
    return lookUpClass('NSBundle').bundleWithPath_(_PLUGINS[pluginName])

from _convenience import CONVENIENCE_METHODS, CLASS_METHODS

# Some special modules needed to correctly wrap all
# methods in the Foundation framework. Doing it here
# is ugly, but it is also something that would be very
# hard to avoid...

def classAddMethod(cls, name, method):
    """
    Add a single method to a class. 'name' is the ObjC selector
    """
    import types

    if isinstance(method, selector):
        sel = selector(method.callable,
                    selector=name,
                    signature=method.signature,
                    isClassMethod=method.isClassMethod)
    else:
        sel = selector(method, selector=name)

    return classAddMethods(cls, [sel])


#
# Syntactic support for categories
#

class _CategoryMeta (type):
    """
    Meta class for categories.
    """
    __slots__ = ()
    _IGNORENAMES = ('__module__', '__name__')
    def _newSubclass(cls, name, bases, methods):
        return type.__new__(cls, name, bases, methods)
    _newSubclass = classmethod(_newSubclass)

    def __new__(cls, name, bases, methods):
        if len(bases) != 1:
            raise TypeError, "Cannot have multiple inheritance with Categories"

        c = bases[0].real_class

        if c.__name__ != name:
            raise TypeError, "Category name must be same as class name"

        m = [ x[1] for x in methods.items() if x[0] not in cls._IGNORENAMES ]
        classAddMethods(c, m)
        return c

def Category(cls):
    """
    Create a category on ``cls``. 

    Usage:
        class SomeClass (Category(SomeClass)):
            def method(self):
                pass

    ``SomeClass`` is an existing class that will be rebound to the same
    value. The side-effect of this class definition is that the methods
    in the class definition will be added to the existing class.
    """
    if not isinstance(cls, objc_class):
        raise TypeError, "Category can only be used on Objective-C classes"
    retval = _CategoryMeta._newSubclass('Category', (), dict(real_class=cls))
    return retval

def _subclass_extender(name, base, protocols, dct):
    """
    used internally by the class builder

    This is the rough equivalent to a metaclass for a
    Python subclass of an Objective-C class.

    Typically it will just modify the class dct, but may choose
    to raise an exception.
    """
    if 'bundleForClass' not in dct:
        cb = currentBundle()
        def bundleForClass(cls):
            return cb
        dct['bundleForClass'] = selector(bundleForClass, isClassMethod=True)
    if '__bundle_hack__' in dct:
        import warnings
        warnings.warn(
            "__bundle_hack__ is not necessary in PyObjC 1.3+ / py2app 0.1.8+",
            DeprecationWarning)

###
# This can be usefull to hunt down memory problems in the testsuite.
#import atexit
#atexit.register(recycleAutoreleasePool)

###
# Do the written-in-Python object bridges
from _bridges import *
