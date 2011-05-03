from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSUserDefaultsController (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSUserDefaultsController.appliesImmediately)
        self.assertArgIsBOOL(NSUserDefaultsController.setAppliesImmediately_, 0)
        self.assertResultIsBOOL(NSUserDefaultsController.hasUnappliedChanges)

if __name__ == "__main__":
    main()
