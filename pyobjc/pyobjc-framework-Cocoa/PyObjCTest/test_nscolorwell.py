from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSColorWell (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSColorWell.isActive)
        self.failUnlessArgIsBOOL(NSColorWell.activate_, 0)
        self.failUnlessResultIsBOOL(NSColorWell.isBordered)
        self.failUnlessArgIsBOOL(NSColorWell.setBordered_, 0)

if __name__ == "__main__":
    main()
