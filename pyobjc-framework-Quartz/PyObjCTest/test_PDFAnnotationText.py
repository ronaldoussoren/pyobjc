
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFAnnotationText (TestCase):
    def testConstants(self):
        self.assertEqual(kPDFTextAnnotationIconComment, 0)
        self.assertEqual(kPDFTextAnnotationIconKey, 1)
        self.assertEqual(kPDFTextAnnotationIconNote, 2)
        self.assertEqual(kPDFTextAnnotationIconHelp, 3)
        self.assertEqual(kPDFTextAnnotationIconNewParagraph, 4)
        self.assertEqual(kPDFTextAnnotationIconParagraph, 5)
        self.assertEqual(kPDFTextAnnotationIconInsert, 6)

        self.assertEqual(kPDFDocumentPermissionsNone, 0)
        self.assertEqual(kPDFDocumentPermissionsUser, 1)
        self.assertEqual(kPDFDocumentPermissionsOwner, 2)

if __name__ == "__main__":
    main()
