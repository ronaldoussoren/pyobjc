from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSDockTile (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSDockTile.showsApplicationBadge)
        self.failUnlessArgIsBOOL(NSDockTile.setShowsApplicationBadge_, 0)

    def testConstants(self):
        self.failUnlessEqual(NSAppKitVersionNumberWithDockTilePlugInSupport, 1001.0)

if __name__ == "__main__":
    main()
