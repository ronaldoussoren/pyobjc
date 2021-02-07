import os

from PyObjCTools.TestSupport import TestCase, expectedFailure
import Quartz


class TestCGPDFContentStream(TestCase):
    def testTypes(self):
        self.assertIsOpaquePointer(Quartz.CGPDFContentStreamRef)

    def testFunctions(self):
        if os.path.exists(
            "/Library/Documentation//Applications/iWeb/Acknowledgements.pdf"
        ):
            pdf_path = "/Library/Documentation//Applications/iWeb/Acknowledgements.pdf"
        elif os.path.exists(
            "/Library/Documentation/Applications/iMovie/Acknowledgements.pdf"
        ):
            pdf_path = "/Library/Documentation/Applications/iMovie/Acknowledgements.pdf"
        elif os.path.exists("/Library/Documentation/WebObjects/Acknowlegdements.pdf"):
            pdf_path = "/Library/Documentation/WebObjects/Acknowlegdements.pdf"
        elif os.path.exists(
            "/Library/Documentation/License.lpdf/Contents/Resources/English.lproj/License.pdf"
        ):
            pdf_path = "/Library/Documentation/License.lpdf/Contents/Resources/English.lproj/License.pdf"
        elif os.path.exists(
            "/Library/Documentation//MacOSXServer/Server Acknowledgments.pdf"
        ):
            pdf_path = "/Library/Documentation//MacOSXServer/Server Acknowledgments.pdf"
        else:
            self.fail("No test PDF file found")

        doc = Quartz.CGPDFDocumentCreateWithURL(
            Quartz.CFURLCreateWithFileSystemPath(
                None, pdf_path, Quartz.kCFURLPOSIXPathStyle, False
            )
        )
        self.assertIsInstance(doc, Quartz.CGPDFDocumentRef)

        page = Quartz.CGPDFDocumentGetPage(doc, 1)
        self.assertIsInstance(page, Quartz.CGPDFPageRef)

        stream = Quartz.CGPDFContentStreamCreateWithPage(page)
        self.assertIsInstance(stream, Quartz.CGPDFContentStreamRef)

        v = Quartz.CGPDFContentStreamRetain(stream)
        self.assertEqual(v.__pointer__, stream.__pointer__)

        Quartz.CGPDFContentStreamRelease(v)

        v = Quartz.CGPDFContentStreamGetResource(stream, b"ColorSpace", b"Cs1")
        self.assertIsInstance(v, Quartz.CGPDFObject)

    @expectedFailure
    def testIncomplete(self):
        self.fail("CGPDFContentStreamGetStreams")  # Need manual wrapper
