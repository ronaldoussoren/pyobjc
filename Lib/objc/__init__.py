"""
Python <-> Objective-C bridge (PyObjC)

This module defines the core interfaces of the Python<->Objective-C bridge.
"""

##
## Disable gc -- blows up w/Python 2.2
##
import sys
if sys.version_info[:3] == (2,2,0):
    import gc
    gc.disable()

# Aliases for some common Objective-C constants
import __builtin__
if hasattr(__builtin__, 'True'):
    YES=True
    NO=False
else:
    YES=1
    NO=0
nil=None

from _objc import *
from _objc import __version__

# Import values used to define signatures
import _objc
gl = globals()
for nm in [ x for x in dir(_objc) if x.startswith('_C_') ]:
    gl[nm] = getattr(_objc, nm)
del gl, nm, _objc, x


#
# Administration of methods that transfer ownership of objects to the
# caller. This list is used by the runtime to automaticly correct the
# refcount to the object.
#
# These must be set before any proxy classes are created.
#
# These 5 are documented in Apple's Objective-C book, in theory these
# are the only methods that transfer ownership.
#
def register_allocator_selector(selector):
    """
    register 'selector' as a method that transfers ownership of the 
    returned object to the caller. 
    
    This information is used by the proxy code to correctly maintain 
    reference counts. It is highly unlikely that this function should
    be called outside of the 'objc' module.
    """
    ALLOCATOR_METHODS[selector] = 1

register_allocator_selector('alloc')
register_allocator_selector('allocWithZone:')
register_allocator_selector('copy')
register_allocator_selector('copyWithZone:')
register_allocator_selector('mutableCopyWithZone:')



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
IBOutlet = ivar

def IBAction(func):
    """
    Return an Objective-C method object that can be used as an action
    in Interface Builder.
    """
    return selector(func, signature="v@:@")



from _convenience import CONVENIENCE_METHODS, CLASS_METHODS

# Some special modules needed to correctly wrap all
# methods in the Foundation framework. Doing it here
# is ugly, but it is also something that would be very
# hard to avoid...
try:
    import _FoundationSignatures
    del _FoundationSignatures
except ImportError:
    pass

try:
    import _FoundationMapping
    del _FoundationMapping
except ImportError:
    pass

# This is a hack, should probably patch python:
# - We want the resources directory to be on the python search-path
# - It must be at the start of the path
# - The CWD must not be on the path
if 1 :
    b = lookUpClass('NSBundle').mainBundle()
    if b:
        sys.path.insert(0, '%s/Contents/Resources'%str(b.bundlePath()))
    del b
del sys, __builtin__
