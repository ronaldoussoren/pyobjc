"""
Python mapping for the Cocoa AppKit.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import AppKit as _AppKit
import objc as _objc

# We first register special methods signatures with the runtime. The module
# is not used for anything else.

from _WebKit import *

# Load the Cocoa bundle, and gather all classes defined there

if _objc.platform == 'MACOSX':
    _objc.loadBundle(
        "WebKit",
        globals(),
        bundle_identifier=u'com.apple.WebKit',
    )
else:
    _objc.loadBundle(
        "WebKit",
        globals(),
        bundle_path=_objc.pathForFramework(
            u"/System/Library/Frameworks/WebKit.framework",
        ),
    )

import protocols  # no need to export these, just register with PyObjC

_objc.setSignatureForSelector('NSJavaVirtualMachine', 'versionRangeFromString:lower:upper:', 'v@:r*o^Io^I')
