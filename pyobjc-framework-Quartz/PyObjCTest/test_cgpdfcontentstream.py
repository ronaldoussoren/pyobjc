
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *
import os

class TestCGPDFContentStream (TestCase):
    def testTypes(self):
        self.assertIsOpaquePointer(CGPDFContentStreamRef)

    def testFunctions(self):
        if os.path.exists("/Library/Documentation//Applications/iWeb/Acknowledgements.pdf"):
            pdf_path = "/Library/Documentation//Applications/iWeb/Acknowledgements.pdf"
        elif os.path.exists("/Library/Documentation/Applications/iMovie/Acknowledgements.pdf"):
            pdf_path = "/Library/Documentation/Applications/iMovie/Acknowledgements.pdf"
        elif os.path.exists("/Library/Documentation/WebObjects/Acknowlegdements.pdf"):
            pdf_path = "/Library/Documentation/WebObjects/Acknowlegdements.pdf"
        else:
            self.fail("No test PDF file found")

        doc = CGPDFDocumentCreateWithURL(
                CFURLCreateWithFileSystemPath(None,
                    pdf_path,
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


    @expectedFailure
    def testIncomplete(self):
        self.fail("CGPDFContentStreamGetStreams") # Need manual wrapper




if __name__ == "__main__":
    main()
