from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSCursor (TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(NSCursor.setHiddenUntilMouseMoves_, 0)
        self.assertArgIsBOOL(NSCursor.setOnMouseExited_, 0)
        self.assertArgIsBOOL(NSCursor.setOnMouseEntered_, 0)
        self.assertResultIsBOOL(NSCursor.isSetOnMouseExited)
        self.assertResultIsBOOL(NSCursor.isSetOnMouseEntered)

    def testConstants(self):
        self.assertEqual(NSAppKitVersionNumberWithCursorSizeSupport, 682.0)


if __name__ == "__main__":
    main()
