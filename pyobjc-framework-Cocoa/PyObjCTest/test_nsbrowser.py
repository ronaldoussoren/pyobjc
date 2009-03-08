
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSBrowser (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSBrowserNoColumnResizing, 0)
        self.failUnlessEqual(NSBrowserAutoColumnResizing, 1)
        self.failUnlessEqual(NSBrowserUserColumnResizing, 2)

        self.failUnlessEqual(NSBrowserDropOn, 0)
        self.failUnlessEqual(NSBrowserDropAbove, 1)

        self.failUnlessIsInstance(NSBrowserColumnConfigurationDidChangeNotification, unicode)
        

    def testMethods(self):
        self.fail("- (void)setDoubleAction:(SEL)aSelector;")


if __name__ == "__main__":
    main()
