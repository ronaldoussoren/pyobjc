"""
Python mapping for the Cocoa SenTestingKit.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import SenTestingKit as _AppKit
import objc as _objc

# We first register special methods signatures with the runtime. The module
# is not used for anything else.

from _SenTestingKit import *

# Load the Cocoa bundle, and gather all classes defined there

if _objc.platform == 'MACOSX':
    _objc.loadBundle(
        "SenTestingKit",
        globals(),
        bundle_identifier=u'ch.sente.SenTestingKit',
    )
else:
    _objc.loadBundle(
        "SenTestingKit",
        globals(),
        bundle_path=_objc.pathForFramework(
            u"/System/Library/Frameworks/SenTestingKit.framework",
        ),
    )

import protocols  # no need to export these, just register with PyObjC
