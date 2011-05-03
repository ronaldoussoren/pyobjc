"""
Python <-> Objective-C bridge (PyObjC)

This module defines the core interfaces of the Python<->Objective-C bridge.
"""
import sys

# Aliases for some common Objective-C constants
nil = None
YES = True
NO = False

# Import the namespace from the _objc extension
def _update(g=globals()):

    # Dummy import of copy_reg, needed 
    # for py2app.
    if sys.version_info[0] == 2:
        import copy_reg

    import objc._objc as _objc
    for k,v in _objc.__dict__.iteritems():
        g.setdefault(k,v)
_update()
del _update

#import objc._setup

from objc._convenience import *
from objc._bridgesupport import *

from objc._dyld import *
from objc._protocols import *
from objc._descriptors import *
from objc._category import *
from objc._bridges import *
from objc._compat import *
from objc._pythonify import *
from objc._functions import *
from objc._locking import *
from objc._context import *
from objc._properties import *

import objc._pycoder as _pycoder

# Make sure our global autorelease pool is
# recycled when the interpreter shuts down.
# This avoids issue1402 in the python
# bugtracker
import atexit
atexit.register(recycleAutoreleasePool)
