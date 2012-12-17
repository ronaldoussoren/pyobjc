'''
Python mapping for the LaunchServices framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
'''
import objc, sys
import os
import Foundation

from LaunchServices import _metadata

if os.path.exists('/System/Library/Frameworks/ApplicationServices.framework/Frameworks/LaunchServices.framework'):
    framework = '/System/Library/Frameworks/ApplicationServices.framework/Frameworks/LaunchServices.framework'
else:
    framework = '/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework'

sys.modules['LaunchServices'] = mod = objc.ObjCLazyModule(
    "LaunchServices",
    "com.apple.LaunchServices",
    objc.pathForFramework(framework),
    _metadata.__dict__, None, {
    '__doc__': __doc__,
    'objc': objc,
    '__path__': __path__,
    }, (Foundation,))


# Load an undocumented, yet announced function. This function was announced
# in TN2029 (http://developer.apple.com/technotes/tn/tn2029.html)
#objc.loadBundleFunctions(
#        __bundle__, mod.__dict__,
#        [
#            ('_LSCopyAllApplicationURLs', b'v^@', '', { 'arguments': { 0: { 'already_retained': True, 'type_modifier': 'o',  } } } ),
#        ])
