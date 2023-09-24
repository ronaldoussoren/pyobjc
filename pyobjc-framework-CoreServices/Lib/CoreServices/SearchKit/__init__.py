"""
Python mapping for the SearchKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="SearchKit",
        frameworkIdentifier="com.apple.CoreServices",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/CoreServices.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(Foundation,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["CoreServices.SearchKit._metadata"]


globals().pop("_setup")()


# SKIndexGetTypeID is documented, but not actually exported by Leopard. Try to
# emulate the missing functionality.
#
# See also radar:6525606.
#
# UPDATE 20151123: The workaround is still necessary on OSX 10.11
def _workaround():
    from Foundation import NSMutableData, NSAutoreleasePool
    import CoreServices.SearchKit as mod
    import objc

    pool = NSAutoreleasePool.alloc().init()
    try:
        rI = mod.SKIndexCreateWithMutableData(
            NSMutableData.data(), None, mod.kSKIndexInverted, None
        )

        indexID = mod.CFGetTypeID(rI)

        r = mod.SKIndexDocumentIteratorCreate(rI, None)
        iterID = mod.CFGetTypeID(r)
        del r

        r = mod.SKSearchGroupCreate([rI])
        groupID = mod.CFGetTypeID(r)

        r = mod.SKSearchResultsCreateWithQuery(
            r, ".*", mod.kSKSearchRanked, 1, None, None
        )
        resultID = mod.CFGetTypeID(r)

        if mod.SKSearchGetTypeID() == 0:
            # Type doesn't get registered unless you try to use it.
            # That's no good for PyObjC, therefore forcefully create
            # a SKSearch object
            mod.SKSearchCreate(rI, "q", 0)
            searchref = objc.registerCFSignature(
                "SKSearchRef", b"^{__SKSearch=}", mod.SKSearchGetTypeID()
            )
        else:
            searchref = mod.SKSearchRef

        del r
        del rI

        r = mod.SKSummaryCreateWithString("foo")
        summaryID = mod.CFGetTypeID(r)
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

    indexType = objc.registerCFSignature("SKIndexRef", b"^{__SKIndex=}", indexID)
    iterType = objc.registerCFSignature(
        "SKIndexDocumentIteratorRef", b"^{__SKIndexDocumentIterator=}", iterID
    )
    groupType = objc.registerCFSignature(
        "SKSearchGroupRef", b"^{__SKSearchGroup=}", groupID
    )
    resultType = objc.registerCFSignature(
        "SKSearchResultsRef", b"^{__SKSearchResults=}", resultID
    )
    summaryType = objc.registerCFSignature(
        "SKSummaryRef", b"^{__SKSummary=}", summaryID
    )

    # For some reason SKDocumentGetTypeID doesn't return the right value
    # when the framework loader calls it the first time around,
    # by this time the framework is fully initialized and we get
    # the correct result.
    SKDocumentRef = objc.registerCFSignature(
        "SKDocumentRef", b"@", mod.SKDocumentGetTypeID()
    )

    globals()["SKIndexGetTypeID"] = SKIndexGetTypeID
    globals()["SKIndexRef"] = indexType
    globals()["SKIndexDocumentIteratorGetTypeID"] = SKIndexDocumentIteratorGetTypeID
    globals()["SKIndexDocumentRef"] = iterType
    globals()["SKSearchGroupGetTypeID"] = SKSearchGroupGetTypeID
    globals()["SKSearchGroupRef"] = groupType
    globals()["SKSearchResultsGetTypeID"] = SKSearchResultsGetTypeID
    globals()["SKSearchResultsRef"] = resultType
    globals()["SKSummaryGetTypeID"] = SKSummaryGetTypeID
    globals()["SKSummaryRef"] = summaryType
    globals()["SKIndexDocumentIteratorRef"] = iterType
    globals()["SKDocumentRef"] = SKDocumentRef
    globals()["SKSearchRef"] = searchref


globals().pop("_workaround")()
