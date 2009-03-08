
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSSplitView (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSSplitViewDividerStyleThick, 1)
        self.failUnlessEqual(NSSplitViewDividerStyleThin, 2)

        self.failUnlessIsInstance(NSSplitViewWillResizeSubviewsNotification, unicode)
        self.failUnlessIsInstance(NSSplitViewDidResizeSubviewsNotification, unicode)


if __name__ == "__main__":
    main()
