"""
Wrappers for the OpenDirectory framework
"""
import objc as _objc
from CFOpenDirectory import *

__bundle__ = _objc.initFrameworkWrapper("OpenDirectory",
    frameworkIdentifier="com.apple.OpenDirectory",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/OpenDirectory.framework"),
    globals=globals())
