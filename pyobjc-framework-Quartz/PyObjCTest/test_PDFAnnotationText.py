from PyObjCTools.TestSupport import TestCase
import Quartz


class TestPDFAnnotationText(TestCase):
    def testConstants(self):
        self.assertEqual(Quartz.kPDFTextAnnotationIconComment, 0)
        self.assertEqual(Quartz.kPDFTextAnnotationIconKey, 1)
        self.assertEqual(Quartz.kPDFTextAnnotationIconNote, 2)
        self.assertEqual(Quartz.kPDFTextAnnotationIconHelp, 3)
        self.assertEqual(Quartz.kPDFTextAnnotationIconNewParagraph, 4)
        self.assertEqual(Quartz.kPDFTextAnnotationIconParagraph, 5)
        self.assertEqual(Quartz.kPDFTextAnnotationIconInsert, 6)

        self.assertEqual(Quartz.kPDFDocumentPermissionsNone, 0)
        self.assertEqual(Quartz.kPDFDocumentPermissionsUser, 1)
        self.assertEqual(Quartz.kPDFDocumentPermissionsOwner, 2)
