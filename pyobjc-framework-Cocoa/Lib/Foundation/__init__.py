'''
Python mapping for the Foundation framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
#import ApplicationServices
from CoreFoundation import *

from Foundation._inlines import _inline_list_

__bundle__ = _objc.initFrameworkWrapper("Foundation",
    frameworkIdentifier="com.apple.Foundation",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/Foundation.framework"),
    globals=globals(),
    inlineTab=_inline_list_)

# Import the various manually maintained bits:
from Foundation._functiondefines import *
from Foundation._Foundation import *

import Foundation._nsobject
import Foundation._nsindexset

YES = objc.YES
NO = objc.NO

def MIN(a, b):
    if a < b:
        return a
    else:
        return b

def MAX(a, b):
    if a < b:
        return b
    else:
        return a

ABS = abs

import sys
NSMaximumStringLength = sys.maxint - 1
del sys

class _OC_DisabledSuddenTermination (object):
    """
    Helper class to implement NSDisabledSuddenTermination

    Usage::

        with NSDisabledSuddenTermination:
            pass

    Inside the with block sudden termination is disabled.

    This only has an effect on OSX 10.6 or later.
    """
    if hasattr(NSProcessInfo, 'disableSuddenTermination'):
        def __enter__(self):
            NSProcessInfo.processInfo().disableSuddenTermination()

        def __exit__(self, type, value, tb):
            NSProcessInfo.processInfo().enableSuddenTermination()

    else:
        def __enter__(self):
            pass

        def __exit__(self, type, value, tb):
            pass


NSDisabledSuddenTermination = _OC_DisabledSuddenTermination()
