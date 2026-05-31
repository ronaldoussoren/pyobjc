from PyObjCTools.TestSupport import TestCase
import Quartz


class TestPDFSelection(TestCase):
    def test_enum(self):
        self.assertIsEnumType(Quartz.PDFSelectionGranularity)
        self.assertEqual(Quartz.PDFSelectionGranularityCharacter, 0)
        self.assertEqual(Quartz.PDFSelectionGranularityWord, 1)
        self.assertEqual(Quartz.PDFSelectionGranularityLine, 2)

    def testMethods(self):
        self.assertArgIsBOOL(Quartz.PDFSelection.drawForPage_withBox_active_, 2)
