import IOSurface
from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure


class TestIOSurfaceObjC(TestCase):
    def testCFTypes(self):
        self.assertIsCFType(IOSurface.IOSurfaceRef)

    @min_os_level("10.12")
    def testConstants(self):
        self.assertIsInstance(IOSurface.IOSurfacePropertyAllocSizeKey, str)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyWidth, str)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyHeight, str)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyBytesPerRow, str)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyBytesPerElement, str)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyElementWidth, str)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyElementHeight, str)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyOffset, str)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyPlaneInfo, str)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyPlaneWidth, str)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyPlaneHeight, str)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyPlaneBytesPerRow, str)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyPlaneOffset, str)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyPlaneSize, str)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyPlaneBase, str)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyPlaneBytesPerElement, str)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyPlaneElementWidth, str)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyPlaneElementHeight, str)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyCacheMode, str)
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyPixelFormat, str)
        self.assertIsInstance(
            IOSurface.IOSurfacePropertyKeyPixelSizeCastingAllowed, str
        )

    @min_os_level("10.14")
    def testConstants10_14(self):
        self.assertIsInstance(IOSurface.IOSurfacePropertyKeyAllocSize, str)

    @min_os_level("10.12")
    def testMethods(self):
        self.assertArgIsOut(IOSurface.IOSurface.lockWithOptions_seed_, 1)
        self.assertArgIsOut(IOSurface.IOSurface.unlockWithOptions_seed_, 1)
        self.assertResultIsBOOL(IOSurface.IOSurface.isInUse)
        self.assertResultIsBOOL(IOSurface.IOSurface.allowsPixelSizeCasting)
        self.assertResultIsVariableSize(IOSurface.IOSurface.baseAddressOfPlaneAtIndex_)

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsOut(IOSurface.IOSurface.setPurgeable_oldState_, 1)

    @expectedFailure
    @min_os_level("10.12")
    def testMethods_unsupported(self):
        self.fail(IOSurface.IOSurface.baseAddressOfPlaneAtIndex_)  # Buffer
