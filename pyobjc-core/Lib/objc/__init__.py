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

from _convenience import *
from _bridgesupport import *

# Add useful utility functions below
if platform == 'MACOSX':
    from _dyld import *
else:
    from _gnustep import *

from _protocols import *
from _descriptors import *
from _category import *
from _bridges import *
from _compat import *
from _pythonify import *
from _functions import *

###
# This can be usefull to hunt down memory problems in the testsuite.
#import atexit
#atexit.register(recycleAutoreleasePool)
