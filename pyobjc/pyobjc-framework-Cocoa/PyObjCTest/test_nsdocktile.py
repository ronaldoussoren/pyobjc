from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSDockTile (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSDockTile.showsApplicationBadge)
        self.failUnlessArgIsBOOL(NSDockTile.setShowsApplicationBadge_, 0)

if __name__ == "__main__":
    main()
