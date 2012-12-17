
from PyObjCTools.TestSupport import *
from SearchKit import *
from Foundation import NSMutableData
import os

try:
    unicode
except NameError:
    unicode = str

try:
    long
except NameError:
    long = int

class TestSKIndex (TestCase):
    def testTypes(self):
        self.assertIsCFType(SKIndexRef)
        self.assertIsCFType(SKIndexDocumentIteratorRef)

    def testConstants(self):
        self.assertEqual(kSKIndexUnknown, 0)
        self.assertEqual(kSKIndexInverted, 1)
        self.assertEqual(kSKIndexVector, 2)
        self.assertEqual(kSKIndexInvertedVector, 3)

        self.assertEqual(kSKDocumentStateNotIndexed, 0)
        self.assertEqual(kSKDocumentStateIndexed, 1)
        self.assertEqual(kSKDocumentStateAddPending, 2)
        self.assertEqual(kSKDocumentStateDeletePending, 3)

    def testFunctions(self):

        self.assertIsInstance(SKIndexGetTypeID(), (int, long))
        self.assertIsInstance(SKIndexDocumentIteratorGetTypeID(), (int, long))

        self.assertResultIsCFRetained(SKIndexCreateWithURL)
        try:
            url = CFURLCreateWithFileSystemPath(
                        None, b"/tmp/pyobjc.test.index".decode('latin1'),
                        kCFURLPOSIXPathStyle, False)
            self.assertIsInstance(url, CFURLRef)
            ref = SKIndexCreateWithURL(
                    url,
                    "pyobjc.test",
                    kSKIndexInverted,
                    None)
            self.assertIsInstance(ref, SKIndexRef)

            v = SKIndexFlush(ref)
            self.assertIsInstance(v, bool)
            CFRetain(ref)
            SKIndexClose(ref)

            del ref

            ref = SKIndexOpenWithURL(url, "pyobjc.test", False)
            if ref is not None:
                # XXX: Don't understand why this doesn't work as planned...
                self.assertIsInstance(ref, SKIndexRef)

        finally:
            os.unlink('/tmp/pyobjc.test.index')

        data = NSMutableData.data()

        self.assertResultIsCFRetained(SKIndexCreateWithMutableData)
        ref = SKIndexCreateWithMutableData(
                data,
                "pyobjc.test", kSKIndexInverted, None)
        self.assertIsInstance(ref, SKIndexRef)
        del ref

        ref = SKIndexOpenWithData(
                data,
                "pyobjc.test")
        self.assertIsInstance(ref, SKIndexRef)
        del ref

        ref = SKIndexOpenWithMutableData(
                data,
                "pyobjc.test")
        if ref is not None:
            self.assertIsInstance(ref, SKIndexRef)

        data = NSMutableData.data()
        self.assertResultIsCFRetained(SKIndexCreateWithMutableData)
        ref = SKIndexCreateWithMutableData(
                data,
                "pyobjc.test", kSKIndexInverted, None)
        self.assertIsInstance(ref, SKIndexRef)


        SKIndexSetMaximumBytesBeforeFlush(ref, 10000)

        v = SKIndexGetMaximumBytesBeforeFlush(ref)
        self.assertIsInstance(v, (int, long))

        v = SKIndexCompact(ref)
        self.assertIsInstance(v, bool)

        v = SKIndexGetIndexType(ref)
        self.assertIsInstance(v, (int, long))

        v = SKIndexGetAnalysisProperties(ref)
        self.failUnless(v is None)

        v = SKIndexGetDocumentCount(ref)
        self.assertIsInstance(v, (int, long))


        self.assertResultIsBOOL(SKIndexAddDocumentWithText)
        self.assertArgIsBOOL(SKIndexAddDocumentWithText, 3)


        fn = b"/Library/Documentation/Acknowledgements.rtf".decode('latin1')
        if not os.path.exists(fn):
            fn = b"/Library/Documentation/AirPort Acknowledgements.rtf".decode('latin1')

        doc = SKDocumentCreateWithURL(
                CFURLCreateWithFileSystemPath(
                    None, fn,
                    kCFURLPOSIXPathStyle, False))

        v = SKIndexAddDocumentWithText(ref,
                doc, "hello world", True)
        self.failUnless(v)

        self.assertResultIsBOOL(SKIndexAddDocument)
        self.assertArgIsBOOL(SKIndexAddDocument, 3)
        v = SKIndexAddDocument(ref, doc, None, True)
        self.failUnless(v is True)

        SKIndexSetDocumentProperties(ref, doc, {"demo": "pyobjc"})

        v = SKIndexCopyDocumentProperties(ref, doc)
        self.assertIsInstance(v, CFDictionaryRef)

        v = SKIndexGetDocumentState(ref, doc)
        self.assertIsInstance(v, (int, long))

        v = docID = SKIndexGetDocumentID(ref, doc)
        self.assertIsInstance(v, (int, long))

        self.assertResultIsCFRetained(SKIndexCopyDocumentForDocumentID)
        v = SKIndexCopyDocumentForDocumentID(ref, v)
        self.failUnless(v is doc)

        r = SKIndexFlush(ref)
        self.assertIs(r, True)

        self.assertResultIsCFRetained(SKIndexDocumentIteratorCreate)
        it = SKIndexDocumentIteratorCreate(ref, None)
        self.assertIsInstance(it, SKIndexDocumentIteratorRef)

        self.assertResultIsCFRetained(SKIndexDocumentIteratorCopyNext)
        v = SKIndexDocumentIteratorCopyNext(it)
        self.assertIsInstance(v, SKDocumentRef)

        v = SKIndexDocumentIteratorCopyNext(it)
        self.failUnless(v is None)

        v = SKIndexGetMaximumDocumentID(ref)
        self.assertIsInstance(v, (int, long))

        v = SKIndexGetDocumentTermCount(ref, docID)
        self.assertIsInstance(v, (int, long))


        v = SKIndexCopyTermIDArrayForDocumentID(ref, docID)
        self.assertIsInstance(v, CFArrayRef)

        tID =  SKIndexGetMaximumTermID(ref) - 1


        v = SKIndexGetDocumentTermFrequency(ref, docID, tID)
        self.assertIsInstance(v, (int, long))

        v = SKIndexGetMaximumTermID(ref)
        self.assertIsInstance(v, (int, long))

        v = SKIndexGetTermDocumentCount(ref, tID)
        self.assertIsInstance(v, (int, long))

        v = SKIndexCopyDocumentIDArrayForTermID(ref, tID)
        self.assertIsInstance(v, (CFArrayRef, type(None)))

        v = SKIndexCopyTermStringForTermID(ref, tID)
        self.assertIsInstance(v, (unicode, type(None)))

        v = SKIndexGetTermIDForTermString(ref, v)
        self.assertIsInstance(v, (int, long))

        SKLoadDefaultExtractorPlugIns()

        v = SKIndexRenameDocument(ref, doc, "osx-acks.rtf")
        self.failUnless(v is True)

        v = SKIndexMoveDocument(ref, doc, None)
        self.failUnless(v is True)

        v = SKIndexRemoveDocument(ref, doc)
        self.failUnless(v)


if __name__ == "__main__":
    main()
