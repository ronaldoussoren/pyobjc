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

    # Dummy import of copy_reg, needed 
    # for py2app.
    import copy_reg

    import _objc
    for k,v in _objc.__dict__.iteritems():
        g.setdefault(k,v)
_update()
del _update

from _convenience import *
from _bridgesupport import *

from _dyld import *
from _protocols import *
from _descriptors import *
from _category import *
from _bridges import *
from _compat import *
from _pythonify import *
from _functions import *
from _locking import *
from _context import *

import _pycoder

# Make sure our global autorelease pool is
# recycled when the interpreter shuts down.
# This avoids issue1402 in the python
# bugtracker
import atexit
atexit.register(recycleAutoreleasePool)
