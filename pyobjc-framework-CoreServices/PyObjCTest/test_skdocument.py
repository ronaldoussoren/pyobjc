
from PyObjCTools.TestSupport import *
import CoreServices

class TestSKDocument (TestCase):
    def testTypes(self):
        self.assertIsCFType(CoreServices.SKDocumentRef)

    def testFunctions(self):
        self.assertIsInstance(CoreServices.SKDocumentGetTypeID(), (int,  long))

        self.assertResultIsCFRetained(CoreServices.SKDocumentCreateWithURL)
        ref = CoreServices.SKDocumentCreateWithURL(
                    CoreServices.CFURLCreateWithFileSystemPath(
                        None, b"/Library/Documentation/Acknowledgements.rtf".decode('latin1'),
                        CoreServices.kCFURLPOSIXPathStyle, False))
        self.assertIsInstance(ref, CoreServices.SKDocumentRef)

        self.assertResultIsCFRetained(CoreServices.SKDocumentCopyURL)
        v = CoreServices.SKDocumentCopyURL(ref)
        self.assertIsInstance(v, CoreServices.CFURLRef)

        self.assertResultIsCFRetained(CoreServices.SKDocumentCreate)
        ref2 = CoreServices.SKDocumentCreate(
                None, ref, "foobar")
        self.assertIsInstance(ref2, CoreServices.SKDocumentRef)

        v = CoreServices.SKDocumentGetSchemeName(ref)
        self.assertIsInstance(v, unicode)

        v = CoreServices.SKDocumentGetName(ref)
        self.assertIsInstance(v, unicode)

        v = CoreServices.SKDocumentGetParent(ref2)
        self.failUnless(v is ref)


if __name__ == "__main__":
    main()
