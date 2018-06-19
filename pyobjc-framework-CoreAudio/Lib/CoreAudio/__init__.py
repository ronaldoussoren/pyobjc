'''
Python mapping for the CoreAudio framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
'''

import objc
import sys
import Foundation

from CoreAudio import _metadata

sys.modules['CoreAudio'] = mod = objc.ObjCLazyModule(
    "CoreAudio",
    "com.apple.CoreAudio",
    objc.pathForFramework("/System/Library/Frameworks/CoreAudio.framework"),
    _metadata.__dict__, None, {
        '__doc__': __doc__,
        'objc': objc,
        '__path__': __path__,
        '__loader__': globals().get('__loader__', None),
    }, (Foundation,))

import sys
del sys.modules['CoreAudio._metadata']
