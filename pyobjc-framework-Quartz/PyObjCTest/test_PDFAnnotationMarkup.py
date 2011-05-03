
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFAnnotationMarkup (TestCase):
    def testConstants(self):
        self.assertEqual(kPDFMarkupTypeHighlight, 0)
        self.assertEqual(kPDFMarkupTypeStrikeOut, 1)
        self.assertEqual(kPDFMarkupTypeUnderline, 2)

if __name__ == "__main__":
    main()
