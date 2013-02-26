'''
Python mapping for the AVFoundation framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
'''

import objc
import sys
import Foundation

from AVFoundation import _metadata

sys.modules['AVFoundation'] = mod = objc.ObjCLazyModule(
            "AVFoundation",
            "com.apple.avfoundation",
            objc.pathForFramework("/System/Library/Frameworks/AVFoundation.framework"),
            _metadata.__dict__, None, {
                '__doc__': __doc__,
                'objc': objc,
                '__path__': __path__,
            }, (Foundation,))
