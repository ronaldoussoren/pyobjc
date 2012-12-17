'''
Python mapping for the Foundation framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
'''
import sys
import objc
import CoreFoundation

from Foundation import _metadata
from Foundation._inlines import _inline_list_

sys.modules['Foundation'] = mod = objc.ObjCLazyModule('Foundation',
        'com.apple.Foundation',
        objc.pathForFramework("/System/Library/Frameworks/Foundation.framework"),
        _metadata.__dict__, _inline_list_, {
            '__doc__': __doc__,
            'objc': objc,
            'YES': objc.YES,
            'NO': objc.NO,
            'NSMaximumStringLength': sys.maxsize - 1,
            '__path__': __path__,
        }, (CoreFoundation,))

import Foundation._Foundation
for nm in dir(Foundation._Foundation):
    if nm.startswith('_'): continue
    setattr(mod, nm, getattr(Foundation._Foundation, nm))

import Foundation._nsobject
import Foundation._nsindexset


import Foundation._functiondefines
for nm in dir(Foundation._functiondefines):
    setattr(mod, nm, getattr(Foundation._functiondefines, nm))


# XXX: This is suboptimal, could calculate this in the metadata
# generator.
import sys
mod.NSIntegerMax = sys.maxsize
mod.NSIntegerMin = - sys.maxsize - 1
mod.NSUIntegerMax = (sys.maxsize * 2) + 1

import Foundation._context
for nm in dir(Foundation._context):
    setattr(mod, nm, getattr(Foundation._context, nm))
