from PyObjCTools.TestSupport import *

import Metal

MTLDrawablePresentedHandler = b"v@"


class TestMTLDrawableHelper(Metal.NSObject):
    def presentAtTime_(self, a):
        pass


class TestMTLDrawable(TestCase):
    @min_sdk_level("10.11")
    def test_protocols(self):
        objc.protocolNamed("MTLDrawable")

    def test_methods(self):
        self.assertArgHasType(TestMTLDrawableHelper.presentAtTime_, 0, objc._C_DBL)
