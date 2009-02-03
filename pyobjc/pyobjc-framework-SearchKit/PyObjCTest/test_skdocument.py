
from PyObjCTools.TestSupport import *
from SearchKit import *

class TestSKDocument (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(SKDocumentRef)

    def testFunctions(self):
        self.failUnlessIsInstance(SKDocumentGetTypeID(), (int,  long))

        self.failUnlessResultIsCFRetained(SKDocumentCreateWithURL)
        ref = SKDocumentCreateWithURL(
                    CFURLCreateWithFileSystemPath(
                        None, u"/Library/Documentation/Acknowledgements.rtf",
                        kCFURLPOSIXPathStyle, False))
        self.failUnlessIsInstance(ref, SKDocumentRef)

        self.failUnlessResultIsCFRetained(SKDocumentCopyURL)
        v = SKDocumentCopyURL(ref)
        self.failUnlessIsInstance(v, CFURLRef)

        self.failUnlessResultIsCFRetained(SKDocumentCreate)
        ref2 = SKDocumentCreate(
                None, ref, "foobar")
        self.failUnlessIsInstance(ref2, SKDocumentRef)

        v = SKDocumentGetSchemeName(ref)
        self.failUnlessIsInstance(v, unicode)

        v = SKDocumentGetName(ref)
        self.failUnlessIsInstance(v, unicode)

        v = SKDocumentGetParent(ref2)
        self.failUnless(v is ref)


if __name__ == "__main__":
    main()
