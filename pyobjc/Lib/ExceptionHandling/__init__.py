"""
Python mapping for the ExceptionHandling framework on MacOS X

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

# Load the ExceptionHandling bundle, and gather all classes defined there
import objc as _objc

from _ExceptionHandling import *
if _objc.platform == 'MACOSX':
    _objc.loadBundle(
        "ExceptionHandling",
        globals(),
        bundle_identifier=u'com.apple.ExceptionHandling',
    )
else:
    _objc.loadBundle(
        "ExceptionHandling",
        globals(),
        bundle_path=_objc.pathForFramework(
            u"/System/Library/Frameworks/ExceptionHandling.framework",
        ),
    )

import protocols  # no need to export these, just register with PyObjC

# these are #define'd convenience enumerators
NSLogAndHandleEveryExceptionMask = (NSLogUncaughtExceptionMask|NSLogUncaughtSystemExceptionMask|NSLogUncaughtRuntimeErrorMask|NSHandleUncaughtExceptionMask|NSHandleUncaughtSystemExceptionMask|NSHandleUncaughtRuntimeErrorMask|NSLogTopLevelExceptionMask|NSHandleTopLevelExceptionMask|NSLogOtherExceptionMask|NSHandleOtherExceptionMask)

NSHangOnEveryExceptionMask = (NSHangOnUncaughtExceptionMask|NSHangOnUncaughtSystemExceptionMask|NSHangOnUncaughtRuntimeErrorMask|NSHangOnTopLevelExceptionMask|NSHangOnOtherExceptionMask)

# Define useful utility methods here
