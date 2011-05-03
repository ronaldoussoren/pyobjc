'''
Python mapping for the CoreFoundation framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc

from CoreFoundation._inlines import _inline_list_


__bundle__ = _objc.initFrameworkWrapper("CoreFoundation",
    frameworkIdentifier="com.apple.CoreFoundation",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/CoreFoundation.framework"),
    globals=globals(),
    scan_classes=False,
    inlineTab=_inline_list_)

from CoreFoundation._CoreFoundation import *

#
# 'Emulation' for CFArray contructors
#
def _setup():
    NSArray = objc.lookUpClass('NSArray')
    NSMutableArray = objc.lookUpClass('NSMutableArray')

    def CFArrayCreate(allocator, values, numvalues, callbacks):
        assert callbacks is None
        return NSArray.alloc().initWithArray_(values[:numvalues])

    def CFArrayCreateMutable(allocator, capacity, callbacks):
        assert callbacks is None
        return NSMutableArray.alloc().init()

    return CFArrayCreate, CFArrayCreateMutable


CFArrayCreate, CFArrayCreateMutable = _setup()


# CFDictionary emulation functions

def _setup():
    NSDictionary = objc.lookUpClass('NSDictionary')
    NSMutableDictionary = objc.lookUpClass('NSMutableDictionary')
    def CFDictionaryCreate(allocator, keys, values, numValues, 
            keyCallbacks, valueCallbacks):
        assert keyCallbacks is None
        assert valueCallbacks is None

        keys = list(keys)[:numValues]
        values = list(values)[:numValues]

        return NSDictionary.dictionaryWithDictionary_(dict(zip(keys, values)))

    def CFDictionaryCreateMutable(allocator, capacity, keyCallbacks, valueCallbacks):
        assert keyCallbacks is None
        assert valueCallbacks is None

        return NSMutableDictionary.dictionary()

    return CFDictionaryCreate, CFDictionaryCreateMutable

CFDictionaryCreate, CFDictionaryCreateMutable = _setup()



# CFSet emulation functions

def _setup():
    NSSet = objc.lookUpClass('NSSet')
    NSMutableSet = objc.lookUpClass('NSMutableSet')

    def CFSetCreate(allocator, values, numvalues, callbacks):
        assert callbacks is None
        return NSSet.alloc().initWithArray_(values[:numvalues])

    def CFSetCreateMutable(allocator, capacity, callbacks):
        assert callbacks is None
        return NSMutableSet.alloc().init()

    return CFSetCreate, CFSetCreateMutable

CFSetCreate, CFSetCreateMutable = _setup()

kCFTypeArrayCallBacks = None
kCFTypeDictionaryKeyCallBacks  = None
kCFTypeDictionaryValueCallBacks = None
kCFTypeSetCallBacks = None


#
# Implementation of a number of macro's in the CFBundle API
#

def CFCopyLocalizedString(key, comment):
    return CFBundleCopyLocalizedString(CFBundleGetMainBundle(), (key), (key), None)

def CFCopyLocalizedStringFromTable(key, tbl, comment):
    return CFBundleCopyLocalizedString(CFBundleGetMainBundle(), (key), (key), (tbl))

def CFCopyLocalizedStringFromTableInBundle(key, tbl, bundle, comment):
    return CFBundleCopyLocalizedString((bundle), (key), (key), (tbl))

def CFCopyLocalizedStringWithDefaultValue(key, tbl, bundle, value, comment):
    return CFBundleCopyLocalizedString((bundle), (key), (value), (tbl))



def CFSTR(strval):
    return objc.lookUpClass('NSString').stringWithString_(strval)
