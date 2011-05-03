from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSColorWell (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSColorWell.isActive)
        self.assertArgIsBOOL(NSColorWell.activate_, 0)
        self.assertResultIsBOOL(NSColorWell.isBordered)
        self.assertArgIsBOOL(NSColorWell.setBordered_, 0)

if __name__ == "__main__":
    main()
