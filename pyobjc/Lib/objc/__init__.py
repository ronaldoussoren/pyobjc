"""
Python <-> Objective-C bridge (PyObjC)

This module defines the core interfaces of the Python<->Objective-C bridge.
"""

##
## Disable gc -- blows up w/Python 2.2.0
##
import sys
if sys.version_info[:3] == (2,2,0):
    import gc
    gc.disable()

# Aliases for some common Objective-C constants
nil=None

from _objc import *
from _objc import __version__
import _FoundationSignatures

try:
    import _Foundation
except ImportError:
    pass

_objc_bool = type(YES)

# Import values used to define signatures
import _objc
gl = globals()
for nm in [ x for x in dir(_objc) if x.startswith('_C_') ]:
    gl[nm] = getattr(_objc, nm)
del gl, nm, _objc, x


# Add usefull utility functions below


class _runtime:
    """
    Backward compatibility interface.

    This class provides (partial) support for the interface of 
    older versions of PyObjC.
    """
    def __getattr__(self, name):
        if name == '__objc_classes__':
            return getClassList()
        elif name == '__kind__':
            return 'python'

        return lookUpClass(name)

    def __eq__(self, other):
        return self is other

    def __repr__(self):
        return "objc.runtime"
runtime = _runtime()
del _runtime

#
# Interface builder support.
#
def IBOutlet(name):
    """
    Create an instance variable that can be used as an outlet in
    Interface Builder.
    """
    return ivar(name, isOutlet=1)

def IBAction(func):
    """
    Return an Objective-C method object that can be used as an action
    in Interface Builder.
    """
    return selector(func, signature="v@:@")

def accessor(func):
    """
    Return an Objective-C method object that is conformant with key-value coding
    and key-value observing.
    """
    if not isinstance(func, type(accessor)):
        raise ValueError, '%s is not a function'%(func,)

    argCount = func.func_code.co_argcount
    if argCount is 2:
        return selector(func, signature="v@:@")
    elif argCount is 1:
        return selector(func, signature="@@:")
    elif argCount is 0:
        raise ValueError, "Too few arguments to function '%s'.  Cannot create selector." % foo.func_name
    else:
        raise ValueError, "Too many arguments to function '%s'.  Cannot create selector." % foo.func_name

def Accessor(func):
    import warnings
    warnings.warn(
        "Use objc.accessor instead of objc.Accessor", DeprecationWarning)
    return accessor(func)

def pluginBundle(pluginName):
    """
    Return the main bundle for the named plugin. This should be used
    in combination with ``PyObjCTools.pluginbuilder``.
    """
    cls = 'PyObjC_Bundle_' + pluginName 
    return runtime.NSBundle.bundleForClass_(getattr(runtime, cls))

from _convenience import CONVENIENCE_METHODS, CLASS_METHODS

# Some special modules needed to correctly wrap all
# methods in the Foundation framework. Doing it here
# is ugly, but it is also something that would be very
# hard to avoid...

del sys

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

######
# Backward compatibility stuff
# (depricated functionality)

def recycle_autorelease_pool():
    """Depricated: Use recycleAutoreleasePool"""
    import warnings
    warnings.warn(
        "Use recycleAutoreleasePool instead of recycle_autorelease_pool",
        DeprecationWarning)
    recycleAutoreleasePool()

###
# This can be usefull to hunt down memory problems in the testsuite.
#import atexit
#atexit.register(recycleAutoreleasePool)
