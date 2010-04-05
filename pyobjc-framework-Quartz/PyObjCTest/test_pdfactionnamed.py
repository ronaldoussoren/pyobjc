
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFActionNamed (TestCase):
    def testConstants(self):
        self.assertEqual(kPDFActionNamedNone, 0)
        self.assertEqual(kPDFActionNamedNextPage, 1)
        self.assertEqual(kPDFActionNamedPreviousPage, 2)
        self.assertEqual(kPDFActionNamedFirstPage, 3)
        self.assertEqual(kPDFActionNamedLastPage, 4)
        self.assertEqual(kPDFActionNamedGoBack, 5)
        self.assertEqual(kPDFActionNamedGoForward, 6)
        self.assertEqual(kPDFActionNamedGoToPage, 7)
        self.assertEqual(kPDFActionNamedFind, 8)
        self.assertEqual(kPDFActionNamedPrint, 9)
        self.assertEqual(kPDFActionNamedZoomIn, 10)
        self.assertEqual(kPDFActionNamedZoomOut, 11)

if __name__ == "__main__":
    main()
