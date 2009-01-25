
from PyObjCTools.TestSupport import *
from SearchKit import *
from Foundation import NSMutableData
import os

class TestSKIndex (TestCase):
    def testTypes(self):
        self.failUnlessIsInstance(SKIndexRef, objc.objc_class)
        self.failUnlessIsInstance(SKIndexDocumentIteratorRef, objc.objc_class)

    def testConstants(self):
        self.failUnlessEqual(kSKIndexUnknown, 0)
        self.failUnlessEqual(kSKIndexInverted, 1)
        self.failUnlessEqual(kSKIndexVector, 2)
        self.failUnlessEqual(kSKIndexInvertedVector, 3)

        self.failUnlessEqual(kSKDocumentStateNotIndexed, 0)
        self.failUnlessEqual(kSKDocumentStateIndexed, 1)
        self.failUnlessEqual(kSKDocumentStateAddPending, 2)
        self.failUnlessEqual(kSKDocumentStateDeletePending, 3)

    def testFunctions(self):

        self.failUnlessIsInstance(SKIndexGetTypeID(), (int, long))
        self.failUnlessIsInstance(SKIndexDocumentIteratorGetTypeID(), (int, long))

        self.failUnlessResultIsCFRetained(SKIndexCreateWithURL)
        try:
            url = CFURLCreateWithFileSystemPath(
                        None, u"/tmp/pyobjc.test.index",
                        kCFURLPOSIXPathStyle, False)
            self.failUnlessIsInstance(url, CFURLRef)
            ref = SKIndexCreateWithURL(
                    url,
                    "pyobjc.test",
                    kSKIndexInverted,
                    None)
            self.failUnlessIsInstance(ref, SKIndexRef)

            v = SKIndexFlush(ref)
            self.failUnlessIsInstance(v, bool)
            CFRetain(ref)
            SKIndexClose(ref)

            del ref

            ref = SKIndexOpenWithURL(url, "pyobjc.test", False)
            if ref is not None:
                # XXX: Don't understand why this doesn't work as planned...
                self.failUnlessIsInstance(ref, SKIndexRef)

        finally:
            os.unlink('/tmp/pyobjc.test.index')

        data = NSMutableData.data()

        self.failUnlessResultIsCFRetained(SKIndexCreateWithMutableData)
        ref = SKIndexCreateWithMutableData(
                data,
                "pyobjc.test", kSKIndexInverted, None)
        self.failUnlessIsInstance(ref, SKIndexRef)
        del ref

        ref = SKIndexOpenWithData(
                data,
                "pyobjc.test")
        self.failUnlessIsInstance(ref, SKIndexRef)
        del ref

        ref = SKIndexOpenWithMutableData(
                data,
                "pyobjc.test")
        if ref is not None:
            self.failUnlessIsInstance(ref, SKIndexRef)

        data = NSMutableData.data()
        self.failUnlessResultIsCFRetained(SKIndexCreateWithMutableData)
        ref = SKIndexCreateWithMutableData(
                data,
                "pyobjc.test", kSKIndexInverted, None)
        self.failUnlessIsInstance(ref, SKIndexRef)


        SKIndexSetMaximumBytesBeforeFlush(ref, 10000)

        v = SKIndexGetMaximumBytesBeforeFlush(ref)
        self.failUnlessIsInstance(v, (int, long))

        v = SKIndexCompact(ref)
        self.failUnlessIsInstance(v, bool)

        v = SKIndexGetIndexType(ref)
        self.failUnlessIsInstance(v, (int, long))

        v = SKIndexGetAnalysisProperties(ref)
        self.failUnless(v is None)

        v = SKIndexGetDocumentCount(ref)
        self.failUnlessIsInstance(v, (int, long))


        self.failUnlessResultIsBOOL(SKIndexAddDocumentWithText)
        self.failUnlessArgIsBOOL(SKIndexAddDocumentWithText, 3)


        doc = SKDocumentCreateWithURL(
                CFURLCreateWithFileSystemPath(
                    None, u"/Library/Documentation/Acknowledgements.rtf",
                    kCFURLPOSIXPathStyle, False))


        v = SKIndexAddDocumentWithText(ref, 
                doc, "hello world", True)
        self.failUnless(v)


        self.failUnlessResultIsBOOL(SKIndexAddDocument)
        self.failUnlessArgIsBOOL(SKIndexAddDocument, 3)
        v = SKIndexAddDocument(ref, doc, None, True)
        self.failUnless(v is True)

        SKIndexSetDocumentProperties(ref, doc, {"demo": "pyobjc"})

        v = SKIndexCopyDocumentProperties(ref, doc)
        self.failUnlessIsInstance(v, CFDictionaryRef)

        v = SKIndexGetDocumentState(ref, doc)
        self.failUnlessIsInstance(v, (int, long))

        v = docID = SKIndexGetDocumentID(ref, doc)
        self.failUnlessIsInstance(v, (int, long))

        self.failUnlessResultIsCFRetained(SKIndexCopyDocumentForDocumentID)
        v = SKIndexCopyDocumentForDocumentID(ref, v)
        self.failUnless(v is doc)

        v = SKIndexRenameDocument(ref, doc, "osx-acks.rtf")
        self.failUnless(v is True)

        v = SKIndexMoveDocument(ref, doc, None)
        self.failUnless(v is True)

        self.failUnlessResultIsCFRetained(SKIndexDocumentIteratorCreate)
        it = SKIndexDocumentIteratorCreate(ref, None)
        self.failUnlessIsInstance(it, SKIndexDocumentIteratorRef)

        self.failUnlessResultIsCFRetained(SKIndexDocumentIteratorCopyNext)
        v = SKIndexDocumentIteratorCopyNext(it)
        self.failUnlessIsInstance(v, SKDocumentRef)

        v = SKIndexDocumentIteratorCopyNext(it)
        self.failUnless(v is None)

        v = SKIndexGetMaximumDocumentID(ref)
        self.failUnlessIsInstance(v, (int, long))

        v = SKIndexGetDocumentTermCount(ref, docID)
        self.failUnlessIsInstance(v, (int, long))

        v = SKIndexCopyTermIDArrayForDocumentID(ref, docID)
        self.failUnlessIsInstance(v, CFArrayRef)
        tID = v[0]

        v = SKIndexGetDocumentTermFrequency(ref, docID, tID)
        self.failUnlessIsInstance(v, (int, long))

        v = SKIndexGetMaximumTermID(ref)
        self.failUnlessIsInstance(v, (int, long))

        v = SKIndexGetTermDocumentCount(ref, tID)
        self.failUnlessIsInstance(v, (int, long))

        v = SKIndexCopyDocumentIDArrayForTermID(ref, tID)
        self.failUnlessIsInstance(v, CFArrayRef)

        v = SKIndexCopyTermStringForTermID(ref, tID)
        self.failUnlessIsInstance(v, unicode)

        v = SKIndexGetTermIDForTermString(ref, v)
        self.failUnlessIsInstance(v, (int, long))

        SKLoadDefaultExtractorPlugIns()

        v = SKIndexRemoveDocument(ref, doc)
        self.failUnless(v)


if __name__ == "__main__":
    main()
