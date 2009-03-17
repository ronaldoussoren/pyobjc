from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSCursor (TestCase):
    def testMethods(self):
        self.failUnlessArgIsBOOL(NSCursor.setHiddenUntilMouseMoves_, 0)
        self.failUnlessArgIsBOOL(NSCursor.setOnMouseExited_, 0)
        self.failUnlessArgIsBOOL(NSCursor.setOnMouseEntered_, 0)
        self.failUnlessResultIsBOOL(NSCursor.isSetOnMouseExited)
        self.failUnlessResultIsBOOL(NSCursor.isSetOnMouseEntered)

if __name__ == "__main__":
    main()
