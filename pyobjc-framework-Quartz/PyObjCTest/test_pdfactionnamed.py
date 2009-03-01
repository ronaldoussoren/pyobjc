
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFActionNamed (TestCase):
    def testConstants(self):
        self.failUnlessEqual(kPDFActionNamedNone, 0)
        self.failUnlessEqual(kPDFActionNamedNextPage, 1)
        self.failUnlessEqual(kPDFActionNamedPreviousPage, 2)
        self.failUnlessEqual(kPDFActionNamedFirstPage, 3)
        self.failUnlessEqual(kPDFActionNamedLastPage, 4)
        self.failUnlessEqual(kPDFActionNamedGoBack, 5)
        self.failUnlessEqual(kPDFActionNamedGoForward, 6)
        self.failUnlessEqual(kPDFActionNamedGoToPage, 7)
        self.failUnlessEqual(kPDFActionNamedFind, 8)
        self.failUnlessEqual(kPDFActionNamedPrint, 9)
        self.failUnlessEqual(kPDFActionNamedZoomIn, 10)
        self.failUnlessEqual(kPDFActionNamedZoomOut, 11)

if __name__ == "__main__":
    main()
