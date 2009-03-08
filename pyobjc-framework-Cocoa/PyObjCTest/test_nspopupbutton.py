
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSPopUpButton (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(NSPopUpButtonWillPopUpNotification, unicode)

if __name__ == "__main__":
    main()
