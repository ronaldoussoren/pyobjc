'''
Python mapping for the CoreFoundation framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc

import  CoreFoundation._inlines

__bundle__ = _objc.initFrameworkWrapper("CoreFoundation",
    frameworkIdentifier="com.apple.CoreFoundation",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/CoreFoundation.framework"),
    globals=globals(),
    scan_classes=False)

from CoreFoundation._CFCalendar import *
from CoreFoundation._CFTree import *
from CoreFoundation._CFArray import *
from CoreFoundation._CFFileDescriptor import *
from CoreFoundation._CFMachPort import *
from CoreFoundation._CFMessagePort import *
from CoreFoundation._CFNumber import *
from CoreFoundation._CFReadStream import *
from CoreFoundation._CFRunLoopObserver import *
from CoreFoundation._CFRunLoopTimer import *
from CoreFoundation._CFWriteStream import *
from CoreFoundation._CFRunLoopObserver import *
from CoreFoundation._CFRunLoopTimer import *

#
# 'Emulation' for CFArray contructors
#
def _setup():
    NSArray = objc.lookUpClass('NSArray')
    NSMutableArray = objc.lookUpClass('NSMutableArray')

    def CFArrayCreate(allocator, values, numvalues):
        return NSArray.alloc().initWithArray_(values[:numvalues])

    def CFArrayCreateMutable(allocator, capacity):
        return NSMutableArray.alloc().init()

    return CFArrayCreate, CFArrayCreateMutable

CFArrayCreate, CFArrayCreateMutable = _setup()

