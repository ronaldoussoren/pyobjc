'''
Python mapping for the CoreText framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
#import ATS
from CoreFoundation import *
import Foundation
from Quartz import *

__bundle__ = _objc.initFrameworkWrapper("CoreText",
    frameworkIdentifier="com.apple.CoreText",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/ApplicationServices.framework/Frameworks/CoreText.framework"),
    globals=globals())

from CoreText._manual import *
