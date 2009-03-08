
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSControl (TestCase):
    def testMethods(self):
        self.fail("- (void)setAction:(SEL)aSelector;")

    def testConstants(self):
        self.failUnlessIsInstance(NSControlTextDidBeginEditingNotification, unicode)
        self.failUnlessIsInstance(NSControlTextDidEndEditingNotification, unicode)
        self.failUnlessIsInstance(NSControlTextDidChangeNotification, unicode)

if __name__ == "__main__":
    main()
