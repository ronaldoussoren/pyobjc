'''
Python mapping for the SearchKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
from CoreFoundation import *

__bundle__ = _objc.initFrameworkWrapper("SearchKit",
    frameworkIdentifier="com.apple.SearchKit",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/CoreServices.framework/Frameworks/SearchKit.framework"),
    globals=globals())

try:
    SKIndexGetTypeID

except NameError:
    # SKIndexGetTypeID is documented, but not actually exported by Leopard. Try to
    # emulate the missing functionality. 
    #
    # See also radar:6525606.
    #
    def workaround():
        from Foundation import NSMutableData, NSAutoreleasePool

        pool = NSAutoreleasePool.alloc().init()
        try:
            r = SKIndexCreateWithMutableData(NSMutableData.data(),
                    None, kSKIndexInverted, None)

            indexID = CFGetTypeID(r)

            r = SKIndexDocumentIteratorCreate(r, None)
            iterID = CFGetTypeID(r)


        finally:
            del pool

        def SKIndexGetTypeID():
            return indexID

        def SKIndexDocumentIteratorGetTypeID():
            return iterID

        indexType = objc.registerCFSignature(
                "SKIndexRef", "^{__SKIndex=}", indexID)
        iterType = objc.registerCFSignature(
                "SKIndexDocumentIteratorRef", "^{__SKIndexDocumentIterator=}", indexID)

        return (SKIndexGetTypeID, indexType, SKIndexDocumentIteratorGetTypeID, iterType)

    (SKIndexGetTypeID, SKIndexRef, 
            SKIndexDocumentIteratorGetTypeID, SKIndexDocumentRef) = workaround()
