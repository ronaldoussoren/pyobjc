
from PyObjCTools.TestSupport import *
from XgridFoundation import *

class TestXGFile (TestCase):
    def testConstants(self):
        self.assertEqual(XGFileTypeNone, 0)
        self.assertEqual(XGFileTypeRegular, 1)
        self.assertEqual(XGFileTypeStream, 2)
        self.assertIsInstance(XGFileStandardOutputPath, unicode)
        self.assertIsInstance(XGFileStandardErrorPath, unicode)

if __name__ == "__main__":
    main()
