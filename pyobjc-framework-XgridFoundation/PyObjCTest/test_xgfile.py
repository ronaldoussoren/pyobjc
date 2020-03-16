from PyObjCTools.TestSupport import TestCase
import XgridFoundation


class TestXGFile(TestCase):
    def testConstants(self):
        self.assertEqual(XgridFoundation.XGFileTypeNone, 0)
        self.assertEqual(XgridFoundation.XGFileTypeRegular, 1)
        self.assertEqual(XgridFoundation.XGFileTypeStream, 2)
        self.assertIsInstance(XgridFoundation.XGFileStandardOutputPath, str)
        self.assertIsInstance(XgridFoundation.XGFileStandardErrorPath, str)
