import Metal
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

MTLSharedEventNotificationBlock = b"v@Q"


class TestMTLEventHelper(Metal.NSObject):
    def notifyListener_atValue_block_(self, a, b, c):
        pass

    def signaledValue(self):
        pass


class TestMTLEvent(TestCase):
    @min_os_level("10.14")
    def test_protocols(self):
        objc.protocolNamed("MTLEvent")
        objc.protocolNamed("MTLSharedEvent")

    def test_methods(self):
        self.assertArgHasType(
            TestMTLEventHelper.notifyListener_atValue_block_, 1, objc._C_ULNGLNG
        )
        self.assertArgIsBlock(
            TestMTLEventHelper.notifyListener_atValue_block_,
            2,
            MTLSharedEventNotificationBlock,
        )
        self.assertResultHasType(TestMTLEventHelper.signaledValue, objc._C_ULNGLNG)
