'''
Python mapping for the PDFKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
from AppKit import *

__bundle__ = _objc.initFrameworkWrapper("PDFKit",
    frameworkIdentifier="com.apple.PDFKit",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/Quartz.framework/Frameworks/PDFKit.framework"),
    frameworkResourceName="Quartz.PDFKit",
    globals=globals())
