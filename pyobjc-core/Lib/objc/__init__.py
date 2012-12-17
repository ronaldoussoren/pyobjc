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
    for k in _objc.__dict__:
        g.setdefault(k, getattr(_objc, k))
_update()
del _update

from objc._convenience import *
from objc._bridgesupport import *

from objc._dyld import *
from objc._protocols import *
from objc._descriptors import *
from objc._category import *
from objc._bridges import *
from objc._compat import *
from objc._pythonify import *
from objc._locking import *
from objc._context import *
from objc._properties import *
from objc._lazyimport import *

import objc._pycoder as _pycoder

# Make sure our global autorelease pool is
# recycled when the interpreter shuts down.
# This avoids issue1402 in the python
# bugtracker
import atexit
atexit.register(recycleAutoreleasePool)


# Helper function for new-style metadata modules
def _resolve_name(name):
    if '.' not in name:
        raise ValueError(name)

    module, name = name.rsplit('.', 1)
    m = __import__(module)
    for k in module.split('.')[1:]:
        m = getattr(m, k)

    return getattr(m, name)
