
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSColorSpace (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSUnknownColorSpaceModel, -1)
        self.failUnlessEqual(NSGrayColorSpaceModel, 0)
        self.failUnlessEqual(NSRGBColorSpaceModel, 1)
        self.failUnlessEqual(NSCMYKColorSpaceModel, 2)
        self.failUnlessEqual(NSLABColorSpaceModel, 3)
        self.failUnlessEqual(NSDeviceNColorSpaceModel, 4)
        self.failUnlessEqual(NSIndexedColorSpaceModel, 5)
        self.failUnlessEqual(NSPatternColorSpaceModel, 6)

    def testMethods(self):
        self.fail("- (id)initWithColorSyncProfile:(void * /* CMProfileRef */)prof;")
        self.fail("- (void * /* CMProfileRef */)colorSyncProfile;")


if __name__ == "__main__":
    main()
