"""
Python <-> Objective-C bridge (PyObjC)

This module defines the core interfaces of the Python<->Objective-C bridge.
"""

# Aliases for some common Objective-C constants
nil = None
YES = True
NO = False

# Import the namespace from the _objc extension
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

from _descriptors import *
from _convenience import *
from _category import *

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

from _bridges import *
from _compat import *

###
# This can be usefull to hunt down memory problems in the testsuite.
#import atexit
#atexit.register(recycleAutoreleasePool)
