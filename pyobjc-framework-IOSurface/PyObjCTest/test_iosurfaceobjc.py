from PyObjCTools.TestSupport import *

import IOSurface

class TestIOSurfaceObjC (TestCase):
    def testCFTypes(self):
        self.assertIsCFType(IOSurface.IOSurfaceRef)

    @min_os_level('10.12')
    def testConstants(self):
        self.assertIsInstance(IOSurface.IOSurfacePropertyAllocSizeKey, unicode)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyWidth, unicode)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyHeight, unicode)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyBytesPerRow, unicode)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyBytesPerElement, unicode)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyElementWidth, unicode)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyElementHeight, unicode)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyOffset, unicode)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyPlaneInfo, unicode)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyPlaneWidth, unicode)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyPlaneHeight, unicode)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyPlaneBytesPerRow, unicode)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyPlaneOffset, unicode)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyPlaneSize, unicode)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyPlaneBase, unicode)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyPlaneBytesPerElement, unicode)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyPlaneElementWidth, unicode)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyPlaneElementHeight, unicode)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyCacheMode, unicode)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyPixelFormat, unicode)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyPixelSizeCastingAllowed, unicode)

    @min_os_level('10.12')
    def testMethods(self):
        self.assertArgIsOut(IOSurface.IOSurface.lockWithOptions_seed_, 1)
        self.assertArgIsOut(IOSurface.IOSurface.unlockWithOptions_seed_, 1)
        self.fail(IOSurface.IOSurface.baseAddressOfPlaneAtIndex) # Buffer
        self.assertResultIsBOOL(IOSurface.IOSurface.isInUse)
        self.assertResultIsBOOL(IOSurface.IOSurface.allowsPixelSizeCasting)

if __name__ == "__main__":
    main()
