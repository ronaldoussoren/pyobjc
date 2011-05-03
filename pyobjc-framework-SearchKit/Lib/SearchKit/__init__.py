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
    SKDocumentRef

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
            rI = SKIndexCreateWithMutableData(NSMutableData.data(),
                    None, kSKIndexInverted, None)

            indexID = CFGetTypeID(rI)

            r = SKIndexDocumentIteratorCreate(rI, None)
            iterID = CFGetTypeID(r)
            del r

            r = SKSearchGroupCreate([rI])
            groupID = CFGetTypeID(r)

            r = SKSearchResultsCreateWithQuery(r, ".*", kSKSearchRanked, 1, None, None)
            resultID = CFGetTypeID(r)

            if SKSearchGetTypeID() == 0:
                # Type doesn't get registered unless you try to use it.
                # That's no good for PyObjC, therefore forcefully create
                # a SKSearch object
                SKSearchCreate(rI, "q", 0)
                searchref = objc.registerCFSignature(
                        "SKSearchRef", b"^{__SKSearch=}", SKSearchGetTypeID())
            else:
                searchref = SKSearchRef

            del r
            del rI

            r = SKSummaryCreateWithString("foo")
            summaryID = CFGetTypeID(r)
            del r

        finally:
            del pool

        def SKIndexGetTypeID():
            return indexID

        def SKIndexDocumentIteratorGetTypeID():
            return iterID

        def SKSearchGroupGetTypeID():
            return groupID

        def SKSearchResultsGetTypeID():
            return resultID

        def SKSummaryGetTypeID():
            return summaryID

        indexType = objc.registerCFSignature(
                "SKIndexRef", b"^{__SKIndex=}", indexID)
        iterType = objc.registerCFSignature(
                "SKIndexDocumentIteratorRef", b"^{__SKIndexDocumentIterator=}", iterID)
        groupType = objc.registerCFSignature(
                "SKSearchGroupRef", b"^{__SKSearchGroup=}", groupID)
        resultType = objc.registerCFSignature(
                "SKSearchResultsRef", b"^{__SKSearchResults=}", resultID)
        summaryType = objc.registerCFSignature(
                "SKSummaryRef", b"^{__SKSummary=}", summaryID)


        # For some reason SKDocumentGetTypeID doesn't return the right value
        # when the framework loader calls it the first time around,
        # by this time the framework is fully initialized and we get
        # the correct result.
        SKDocumentRef = objc.registerCFSignature(
                "SKDocumentRef", b"@", SKDocumentGetTypeID())


        return (SKIndexGetTypeID, indexType, SKIndexDocumentIteratorGetTypeID, iterType, 
                SKSearchGroupGetTypeID, groupType, SKSearchResultsGetTypeID, resultType,
                SKSummaryGetTypeID, summaryType, iterType,
                SKDocumentRef, searchref)

    (SKIndexGetTypeID, SKIndexRef, 
        SKIndexDocumentIteratorGetTypeID, SKIndexDocumentRef, 
        SKSearchGroupGetTypeID, SKSearchGroupRef,
        SKSearchResultsGetTypeID, SKSearchResultsRef,
        SKSummaryGetTypeID, SKSummaryRef,
        SKIndexDocumentIteratorRef,
        SKDocumentRef, SKSearchRef,
    ) = workaround()

    del workaround
