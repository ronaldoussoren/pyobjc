"""
Python <-> Objective-C bridge (PyObjC)

This module defines the core interfaces of the Python<->Objective-C bridge.
"""

##
## Disable gc -- blows up w/Python 2.2.0
##
## XXX Fix me: This is probably a bug in PyObjC, need to check why this
## fails on Python 2.2.0 and not on Python 2.2.2. Copying gcmodule.c from
## Python 2.2.2 to 2.2.0 causes the crash to go away...
import sys
if sys.version_info[:3] == (2,2,0):
    import gc
    gc.disable()

# Aliases for some common Objective-C constants
nil=None

from _objc import *
from _objc import __version__
import _FoundationSignatures

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
IBOutlet = lambda name: ivar(name, isOutlet=1)

def IBAction(func):
    """
    Return an Objective-C method object that can be used as an action
    in Interface Builder.
    """
    return selector(func, signature="v@:@")

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

try:
    import _FoundationMapping
    del _FoundationMapping
except ImportError:
    pass

del sys
