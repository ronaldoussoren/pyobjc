
from PyObjCTools.TestSupport import *
from SearchKit import *

class TestSKDocument (TestCase):
    def testTypes(self):
        self.assertIsCFType(SKDocumentRef)

    def testFunctions(self):
        self.assertIsInstance(SKDocumentGetTypeID(), (int,  long))

        self.assertResultIsCFRetained(SKDocumentCreateWithURL)
        ref = SKDocumentCreateWithURL(
                    CFURLCreateWithFileSystemPath(
                        None, u"/Library/Documentation/Acknowledgements.rtf",
                        kCFURLPOSIXPathStyle, False))
        self.assertIsInstance(ref, SKDocumentRef)

        self.assertResultIsCFRetained(SKDocumentCopyURL)
        v = SKDocumentCopyURL(ref)
        self.assertIsInstance(v, CFURLRef)

        self.assertResultIsCFRetained(SKDocumentCreate)
        ref2 = SKDocumentCreate(
                None, ref, "foobar")
        self.assertIsInstance(ref2, SKDocumentRef)

        v = SKDocumentGetSchemeName(ref)
        self.assertIsInstance(v, unicode)

        v = SKDocumentGetName(ref)
        self.assertIsInstance(v, unicode)

        v = SKDocumentGetParent(ref2)
        self.failUnless(v is ref)


if __name__ == "__main__":
    main()
