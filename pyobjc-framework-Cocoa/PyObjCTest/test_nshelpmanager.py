
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSHelpManager (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(NSContextHelpModeDidActivateNotification, unicode)
        self.failUnlessIsInstance(NSContextHelpModeDidDeactivateNotification, unicode)


if __name__ == "__main__":
    main()
