
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSParagraphStyle (TestCase):
    def testConstants(self):
        self.assertEqual(NSLeftTabStopType, 0)
        self.assertEqual(NSRightTabStopType, 1)
        self.assertEqual(NSCenterTabStopType, 2)
        self.assertEqual(NSDecimalTabStopType, 3)

        self.assertEqual(NSLineBreakByWordWrapping,  0)
        self.assertEqual(NSLineBreakByCharWrapping, 1)
        self.assertEqual(NSLineBreakByClipping, 2)
        self.assertEqual(NSLineBreakByTruncatingHead, 3)
        self.assertEqual(NSLineBreakByTruncatingTail, 4)
        self.assertEqual(NSLineBreakByTruncatingMiddle, 5)

        self.assertIsInstance(NSTabColumnTerminatorsAttributeName, unicode)

if __name__ == "__main__":
    main()
