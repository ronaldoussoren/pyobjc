import objc as _objc
import sys

from _Foundation import *


NSClassFromString = _objc.lookUpClass

# Do something smart to collect Foundation classes...

NSBundle = _objc.lookUpClass('NSBundle')

_objc.loadBundle("Foundation", globals(), bundle_path="/System/Library/Frameworks/Foundation.framework")

import os
import sys
if 'PYOBJCFRAMEWORKS' in os.environ:
    paths = os.environ['PYOBJCFRAMEWORKS'].split(":")
    count = 0
    for path in paths:
        bundle = NSBundle.bundleWithPath_(path)
        bundle.principalClass()
        sys.path.insert(count, str(bundle.resourcePath()))
        count = count + 1

        initPath = bundle.pathForResource_ofType_( "Init", "py")
        if initPath:
            execfile(initPath, globals(), locals())

# Install an observer callback in the current CFRunLoop that will
# automatically release and acquire the Global Interpreter Lock
# when needed. This is needed so other Python threads get a chance
# to run while we're inside the event loop.
#
# The autoGIL module is only present when using Python 2.2 on MacOS X
import sys
if sys.version_info[:2] == (2, 2):
    try:
        import autoGIL
    except ImportError:
        pass
    else:
        autoGIL.installAutoGIL()

import protocols  # no need to export these, just register with PyObjC

#
# (informal) protocols eported for b/w compatibility
#
from protocols import NSConnectionDelegateMethods, NSDistantObjectRequestMethods, \
                      NSCopyLinkMoveHandler, NSKeyedArchiverDelegate, \
                      NSKeyedUnarchiverDelegate, NSNetServiceDelegateMethods, \
                      NSNetServiceBrowserDelegateMethods, NSPortDelegateMethods

