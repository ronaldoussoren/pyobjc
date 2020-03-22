import Metal
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc

MTLDrawablePresentedHandler = b"v@"


class TestMTLDrawableHelper(Metal.NSObject):
    def presentAtTime_(self, a):
        pass

    def presentAfterMinimumDuration_(self, a):
        pass

    def addPresentedHandler_(self, a):
        pass

    def presentedTime(self):
        return 1

    def drawableID(self):
        return 1


class TestMTLDrawable(TestCase):
    @min_sdk_level("10.11")
    def test_protocols(self):
        objc.protocolNamed("MTLDrawable")

    def test_methods(self):
        self.assertArgHasType(TestMTLDrawableHelper.presentAtTime_, 0, objc._C_DBL)

        self.assertArgHasType(
            TestMTLDrawableHelper.presentAfterMinimumDuration_, 0, objc._C_DBL
        )
        self.assertArgIsBlock(TestMTLDrawableHelper.addPresentedHandler_, 0, b"v@")
        self.assertResultHasType(TestMTLDrawableHelper.presentedTime, objc._C_DBL)
        self.assertResultHasType(TestMTLDrawableHelper.drawableID, objc._C_NSUInteger)
