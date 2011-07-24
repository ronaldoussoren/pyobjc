'''
Python mapping for the CoreGraphics framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''
import sys
import objc
import CoreFoundation

from Quartz.CoreGraphics import _metadata
from Quartz.CoreGraphics._inlines import _inline_list_


sys.modules['Quartz.CoreGraphics'] = mod = objc.ObjCLazyModule('Quartz.CoreGraphics',
    "com.apple.CoreGraphics",
    objc.pathForFramework("/System/Library/Frameworks/ApplicationServices.framework/Frameworks/CoreGraphics.framework"),
    _metadata.__dict__, _inline_list_, {
       '__doc__': __doc__,
       '__path__': __path__,
       'objc': objc,
    }, ( CoreFoundation,))

import Quartz.CoreGraphics._callbacks
import Quartz.CoreGraphics._doubleindirect
import Quartz.CoreGraphics._sortandmap
import Quartz.CoreGraphics._coregraphics
import Quartz.CoreGraphics._contextmanager
