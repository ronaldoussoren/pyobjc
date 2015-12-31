'''
Python mapping for the SceneKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
'''

import objc
import sys
import Quartz
import Cocoa

from SceneKit import _metadata
from SceneKit import _SceneKit
from SceneKit._inlines import _inline_list_


sys.modules['SceneKit'] = mod = objc.ObjCLazyModule(
    "SceneKit",
    "com.apple.SceneKit",
    objc.pathForFramework("/System/Library/Frameworks/SceneKit.framework"),
    _metadata.__dict__, _inline_list_, {
        '__doc__': __doc__,
        'objc': objc,
        '__path__': __path__,
        '__loader__': globals().get('__loader__', None),
    }, (Cocoa, Quartz))


import sys
del sys.modules['SceneKit._metadata']
