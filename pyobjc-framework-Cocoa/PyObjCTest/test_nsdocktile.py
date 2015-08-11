from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSDockTile (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSDockTile.showsApplicationBadge)
        self.assertArgIsBOOL(NSDockTile.setShowsApplicationBadge_, 0)

    def testConstants(self):
        self.assertEqual(NSAppKitVersionNumberWithDockTilePlugInSupport, 1001.0)

    @min_sdk_level('10.10')
    def testProtocol(self):
        objc.protocolNamed('NSDockTilePlugIn')

if __name__ == "__main__":
    main()
