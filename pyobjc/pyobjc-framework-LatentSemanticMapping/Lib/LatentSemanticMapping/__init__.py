'''
Python mapping for the LatentSemanticMapping framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
from Foundation import *
#import CoreServices

__bundle__ = _objc.initFrameworkWrapper("LatentSemanticMapping",
    frameworkIdentifier="com.apple.speech.LatentSemanticMappingFramework",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/LatentSemanticMapping.framework"),
    globals=globals())
