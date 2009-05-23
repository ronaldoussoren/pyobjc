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
from Foundation._NSDecimal import *
from Foundation._nsinvocation import *
from Foundation._functioncallbacks import *
from Foundation._typecode import *
from Foundation._nscoder import *
from Foundation._data import *
from Foundation._netservice import *
from Foundation._string import *

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
