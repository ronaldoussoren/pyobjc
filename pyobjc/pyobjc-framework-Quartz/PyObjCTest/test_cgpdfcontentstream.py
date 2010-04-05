
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGPDFContentStream (TestCase):
    def testTypes(self):
        self.assertIsOpaquePointer(CGPDFContentStreamRef)

    def testFunctions(self):
        doc = CGPDFDocumentCreateWithURL(
                CFURLCreateWithFileSystemPath(None,
                    "/Library/Documentation/Applications/iMovie/Acknowledgements.pdf",
                    kCFURLPOSIXPathStyle, False))
        self.assertIsInstance(doc, CGPDFDocumentRef)

        page = CGPDFDocumentGetPage(doc, 1)
        self.assertIsInstance(page, CGPDFPageRef)

        stream = CGPDFContentStreamCreateWithPage(page)
        self.assertIsInstance(stream, CGPDFContentStreamRef)


        v = CGPDFContentStreamRetain(stream)
        self.assertEqual(v.__pointer__, stream.__pointer__)

        CGPDFContentStreamRelease(v)

        v = CGPDFContentStreamGetResource(stream, b"ColorSpace", b"Cs1");
        self.assertIsInstance(v, CGPDFObject)


    def testIncomplete(self):
        self.fail("CGPDFContentStreamGetStreams") # Need manual wrapper




if __name__ == "__main__":
    main()
