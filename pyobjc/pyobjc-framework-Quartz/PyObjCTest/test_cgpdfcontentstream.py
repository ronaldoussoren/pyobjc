
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGPDFContentStream (TestCase):
    def testTypes(self):
        self.failUnlessIsOpaquePointer(CGPDFContentStreamRef)

    def testFunctions(self):
        doc = CGPDFDocumentCreateWithURL(
                CFURLCreateWithFileSystemPath(None,
                    "/Library/Documentation/Applications/iMovie/Acknowledgements.pdf",
                    kCFURLPOSIXPathStyle, False))
        self.failUnlessIsInstance(doc, CGPDFDocumentRef)

        page = CGPDFDocumentGetPage(doc, 1)
        self.failUnlessIsInstance(page, CGPDFPageRef)

        stream = CGPDFContentStreamCreateWithPage(page)
        self.failUnlessIsInstance(stream, CGPDFContentStreamRef)


        v = CGPDFContentStreamRetain(stream)
        self.failUnlessEqual(v.__pointer__, stream.__pointer__)


    def testIncomplete(self):
        self.fail("CGPDFContentStreamRelease")
        self.fail("CGPDFContentStreamGetResource")
        self.fail("CGPDFContentStreamGetStreams") # Need manual wrapper




if __name__ == "__main__":
    main()
