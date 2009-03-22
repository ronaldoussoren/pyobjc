from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSUserDefaultsController (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSUserDefaultsController.appliesImmediately)
        self.failUnlessArgIsBOOL(NSUserDefaultsController.setAppliesImmediately_, 0)
        self.failUnlessResultIsBOOL(NSUserDefaultsController.hasUnappliedChanges)

if __name__ == "__main__":
    main()
