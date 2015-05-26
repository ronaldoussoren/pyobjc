'''
Python mapping for the SpriteKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
'''

import objc
import sys
import Quartz
import Cocoa

from SpriteKit import _metadata
from SpriteKit import _SpriteKit

sys.modules['SpriteKit'] = mod = objc.ObjCLazyModule(
    "SpriteKit",
    "com.apple.SpriteKit",
    objc.pathForFramework("/System/Library/Frameworks/SpriteKit.framework"),
    _metadata.__dict__, None, {
        '__doc__': __doc__,
        'objc': objc,
        '__path__': __path__,
        '__loader__': globals().get('__loader__', None),
    }, (Cocoa, Quartz))


import sys, objc

# A number of metadata updates that cannot yet be done through metadata
# (that's primarily because "vector_float3" doesn't @encode() at all)
mod = sys.modules['SpriteKit']
mod.SK3DNode.projectPoint_.signature = objc._C_VECTOR_FLOAT3 + b'@:' + objc._C_VECTOR_FLOAT3
mod.SK3DNode.unprojectPoint_.signature = objc._C_VECTOR_FLOAT3 + b'@:' + objc._C_VECTOR_FLOAT3
del sys.modules['SpriteKit._metadata']
