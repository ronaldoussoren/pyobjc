'''
Python mapping for the ImageIO framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
'''
import sys
import objc
import Quartz.CoreGraphics

from Quartz.ImageIO import _metadata

sys.modules['Quartz.ImageIO'] = mod = objc.ObjCLazyModule('Quartz.ImageIO',
    "com.apple.ImageIO.framework",
    objc.pathForFramework("/System/Library/Frameworks/ApplicationServices.framework/Frameworks/ImageIO.framework"),
    _metadata.__dict__, None, {
       '__doc__': __doc__,
       '__path__': __path__,
       'objc': objc,
    }, ( Quartz.CoreGraphics,))
