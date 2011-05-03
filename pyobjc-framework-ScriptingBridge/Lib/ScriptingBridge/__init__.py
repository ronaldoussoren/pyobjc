'''
Python mapping for the ScriptingBridge framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
#from ApplicationServices import *
from Foundation import *

__bundle__ = _objc.initFrameworkWrapper("ScriptingBridge",
    frameworkIdentifier="com.apple.ScriptingBridge",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/ScriptingBridge.framework"),
    globals=globals())

# Override the default behaviour of the bridge to ensure that we
# make the minimal amount of AppleScript calls.
objc.addConvenienceForClass('SBElementArray', [
        ('__iter__', lambda self: iter(self.objectEnumerator())),
    ])
