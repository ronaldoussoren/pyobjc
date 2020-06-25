import CoreServices
from PyObjCTools.TestSupport import TestCase


class TestSKDocument(TestCase):
    def testTypes(self):
        self.assertIsCFType(CoreServices.SKDocumentRef)

    def testFunctions(self):
        self.assertIsInstance(CoreServices.SKDocumentGetTypeID(), int)

        self.assertResultIsCFRetained(CoreServices.SKDocumentCreateWithURL)
        ref = CoreServices.SKDocumentCreateWithURL(
            CoreServices.CFURLCreateWithFileSystemPath(
                None,
                "/Library/Documentation/Acknowledgements.rtf",
                CoreServices.kCFURLPOSIXPathStyle,
                False,
            )
        )
        self.assertIsInstance(ref, CoreServices.SKDocumentRef)

        self.assertResultIsCFRetained(CoreServices.SKDocumentCopyURL)
        v = CoreServices.SKDocumentCopyURL(ref)
        self.assertIsInstance(v, CoreServices.CFURLRef)

        self.assertResultIsCFRetained(CoreServices.SKDocumentCreate)
        ref2 = CoreServices.SKDocumentCreate(None, ref, "foobar")
        self.assertIsInstance(ref2, CoreServices.SKDocumentRef)

        v = CoreServices.SKDocumentGetSchemeName(ref)
        self.assertIsInstance(v, str)

        v = CoreServices.SKDocumentGetName(ref)
        self.assertIsInstance(v, str)

        v = CoreServices.SKDocumentGetParent(ref2)
        self.assertTrue(v is ref)
