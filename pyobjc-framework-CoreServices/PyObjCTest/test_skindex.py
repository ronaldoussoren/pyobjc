
from PyObjCTools.TestSupport import *
import CoreServices
import os

class TestSKIndex (TestCase):
    def testTypes(self):
        self.assertIsCFType(CoreServices.SKIndexRef)
        self.assertIsCFType(CoreServices.SKIndexDocumentIteratorRef)

    def testConstants(self):
        self.assertEqual(CoreServices.kSKIndexUnknown, 0)
        self.assertEqual(CoreServices.kSKIndexInverted, 1)
        self.assertEqual(CoreServices.kSKIndexVector, 2)
        self.assertEqual(CoreServices.kSKIndexInvertedVector, 3)

        self.assertEqual(CoreServices.kSKDocumentStateNotIndexed, 0)
        self.assertEqual(CoreServices.kSKDocumentStateIndexed, 1)
        self.assertEqual(CoreServices.kSKDocumentStateAddPending, 2)
        self.assertEqual(CoreServices.kSKDocumentStateDeletePending, 3)

    def testFunctions(self):

        self.assertIsInstance(CoreServices.SKIndexGetTypeID(), (int, long))
        self.assertIsInstance(CoreServices.SKIndexDocumentIteratorGetTypeID(), (int, long))

        self.assertResultIsCFRetained(CoreServices.SKIndexCreateWithURL)
        try:
            url = CoreServices.CFURLCreateWithFileSystemPath(
                        None, b"/tmp/pyobjc.test.index".decode('latin1'),
                        CoreServices.kCFURLPOSIXPathStyle, False)
            self.assertIsInstance(url, CoreServices.CFURLRef)
            ref = CoreServices.SKIndexCreateWithURL(
                    url,
                    "pyobjc.test",
                    CoreServices.kSKIndexInverted,
                    None)
            self.assertIsInstance(ref, CoreServices.SKIndexRef)

            v = CoreServices.SKIndexFlush(ref)
            self.assertIsInstance(v, bool)
            CoreServices.CFRetain(ref)
            CoreServices.SKIndexClose(ref)

            del ref

            ref = CoreServices.SKIndexOpenWithURL(url, "pyobjc.test", False)
            if ref is not None:
                # XXX: Don't understand why this doesn't work as planned...
                self.assertIsInstance(ref, CoreServices.SKIndexRef)

        finally:
            os.unlink('/tmp/pyobjc.test.index')

        data = CoreServices.NSMutableData.data()

        self.assertResultIsCFRetained(CoreServices.SKIndexCreateWithMutableData)
        ref = CoreServices.SKIndexCreateWithMutableData(
                data,
                "pyobjc.test", CoreServices.kSKIndexInverted, None)
        self.assertIsInstance(ref, CoreServices.SKIndexRef)
        del ref

        ref = CoreServices.SKIndexOpenWithData(
                data,
                "pyobjc.test")
        self.assertIsInstance(ref, CoreServices.SKIndexRef)
        del ref

        ref = CoreServices.SKIndexOpenWithMutableData(
                data,
                "pyobjc.test")
        if ref is not None:
            self.assertIsInstance(ref, CoreServices.SKIndexRef)

        data = CoreServices.NSMutableData.data()
        self.assertResultIsCFRetained(CoreServices.SKIndexCreateWithMutableData)
        ref = CoreServices.SKIndexCreateWithMutableData(
                data,
                "pyobjc.test", CoreServices.kSKIndexInverted, None)
        self.assertIsInstance(ref, CoreServices.SKIndexRef)


        CoreServices.SKIndexSetMaximumBytesBeforeFlush(ref, 10000)

        v = CoreServices.SKIndexGetMaximumBytesBeforeFlush(ref)
        self.assertIsInstance(v, (int, long))

        v = CoreServices.SKIndexCompact(ref)
        self.assertIsInstance(v, bool)

        v = CoreServices.SKIndexGetIndexType(ref)
        self.assertIsInstance(v, (int, long))

        v = CoreServices.SKIndexGetAnalysisProperties(ref)
        self.failUnless(v is None)

        v = CoreServices.SKIndexGetDocumentCount(ref)
        self.assertIsInstance(v, (int, long))


        self.assertResultIsBOOL(CoreServices.SKIndexAddDocumentWithText)
        self.assertArgIsBOOL(CoreServices.SKIndexAddDocumentWithText, 3)


        fn = b"/Library/Documentation/Acknowledgements.rtf".decode('latin1')
        if not os.path.exists(fn):
            fn = b"/Library/Documentation/AirPort Acknowledgements.rtf".decode('latin1')

        doc = CoreServices.SKDocumentCreateWithURL(
                CoreServices.CFURLCreateWithFileSystemPath(
                    None, fn,
                    CoreServices.kCFURLPOSIXPathStyle, False))

        v = CoreServices.SKIndexAddDocumentWithText(ref,
                doc, "hello world", True)
        self.failUnless(v)

        self.assertResultIsBOOL(CoreServices.SKIndexAddDocument)
        self.assertArgIsBOOL(CoreServices.SKIndexAddDocument, 3)
        v = CoreServices.SKIndexAddDocument(ref, doc, None, True)
        self.failUnless(v is True)

        CoreServices.SKIndexSetDocumentProperties(ref, doc, {"demo": "pyobjc"})

        v = CoreServices.SKIndexCopyDocumentProperties(ref, doc)
        self.assertIsInstance(v, CoreServices.CFDictionaryRef)

        v = CoreServices.SKIndexGetDocumentState(ref, doc)
        self.assertIsInstance(v, (int, long))

        v = docID = CoreServices.SKIndexGetDocumentID(ref, doc)
        self.assertIsInstance(v, (int, long))

        self.assertResultIsCFRetained(CoreServices.SKIndexCopyDocumentForDocumentID)
        v = CoreServices.SKIndexCopyDocumentForDocumentID(ref, v)
        self.failUnless(v is doc)

        r = CoreServices.SKIndexFlush(ref)
        self.assertIs(r, True)

        self.assertResultIsCFRetained(CoreServices.SKIndexDocumentIteratorCreate)
        it = CoreServices.SKIndexDocumentIteratorCreate(ref, None)
        self.assertIsInstance(it, CoreServices.SKIndexDocumentIteratorRef)

        self.assertResultIsCFRetained(CoreServices.SKIndexDocumentIteratorCopyNext)
        v = CoreServices.SKIndexDocumentIteratorCopyNext(it)
        self.assertIsInstance(v, CoreServices.SKDocumentRef)

        v = CoreServices.SKIndexDocumentIteratorCopyNext(it)
        self.failUnless(v is None)

        v = CoreServices.SKIndexGetMaximumDocumentID(ref)
        self.assertIsInstance(v, (int, long))

        v = CoreServices.SKIndexGetDocumentTermCount(ref, docID)
        self.assertIsInstance(v, (int, long))


        v = CoreServices.SKIndexCopyTermIDArrayForDocumentID(ref, docID)
        self.assertIsInstance(v, CoreServices.CFArrayRef)

        tID =  CoreServices.SKIndexGetMaximumTermID(ref) - 1


        v = CoreServices.SKIndexGetDocumentTermFrequency(ref, docID, tID)
        self.assertIsInstance(v, (int, long))

        v = CoreServices.SKIndexGetMaximumTermID(ref)
        self.assertIsInstance(v, (int, long))

        v = CoreServices.SKIndexGetTermDocumentCount(ref, tID)
        self.assertIsInstance(v, (int, long))

        v = CoreServices.SKIndexCopyDocumentIDArrayForTermID(ref, tID)
        self.assertIsInstance(v, (CoreServices.CFArrayRef, type(None)))

        v = CoreServices.SKIndexCopyTermStringForTermID(ref, tID)
        self.assertIsInstance(v, (unicode, type(None)))

        v = CoreServices.SKIndexGetTermIDForTermString(ref, v)
        self.assertIsInstance(v, (int, long))

        CoreServices.SKLoadDefaultExtractorPlugIns()

        v = CoreServices.SKIndexRenameDocument(ref, doc, "osx-acks.rtf")
        self.failUnless(v is True)

        v = CoreServices.SKIndexMoveDocument(ref, doc, None)
        self.failUnless(v is True)

        v = CoreServices.SKIndexRemoveDocument(ref, doc)
        self.failUnless(v)


if __name__ == "__main__":
    main()
