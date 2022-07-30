from PyObjCTools.TestSupport import TestCase
import Quartz


class TestPDFAnnotationLine(TestCase):
    def testConstants(self):
        self.assertEqual(Quartz.kPDFLineStyleNone, 0)
        self.assertEqual(Quartz.kPDFLineStyleSquare, 1)
        self.assertEqual(Quartz.kPDFLineStyleCircle, 2)
        self.assertEqual(Quartz.kPDFLineStyleDiamond, 3)
        self.assertEqual(Quartz.kPDFLineStyleOpenArrow, 4)
        self.assertEqual(Quartz.kPDFLineStyleClosedArrow, 5)
