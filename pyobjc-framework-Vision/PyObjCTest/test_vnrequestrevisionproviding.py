import objc

from PyObjCTools.TestSupport import TestCase, min_sdk_level
import Vision


class TestVNRequestRevisionProviderHelper(Vision.NSObject):
    def requestRevision(self):
        return 1


class TestVNRequestRevisionProvider(TestCase):
    def test_methods(self):
        self.assertResultHasType(
            TestVNRequestRevisionProviderHelper.requestRevision, objc._C_NSUInteger
        )

    @min_sdk_level("10.14")
    def test_protocols(self):
        objc.protocolNamed("VNRequestRevisionProviding")
