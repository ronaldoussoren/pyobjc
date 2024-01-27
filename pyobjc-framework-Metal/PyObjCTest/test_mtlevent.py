import Metal
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

MTLSharedEventNotificationBlock = b"v@Q"


class TestMTLEventHelper(Metal.NSObject):
    def notifyListener_atValue_block_(self, a, b, c):
        pass

    def signaledValue(self):
        pass

    def waitUntilSignaledValue_timeoutMS_(self, a, b):
        return 1


class TestMTLEvent(TestCase):
    @min_os_level("10.14")
    def test_protocols(self):
        self.assertProtocolExists("MTLEvent")
        self.assertProtocolExists("MTLSharedEvent")

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

        self.assertResultIsBOOL(TestMTLEventHelper.waitUntilSignaledValue_timeoutMS_)
        self.assertArgHasType(
            TestMTLEventHelper.waitUntilSignaledValue_timeoutMS_, 0, objc._C_ULNGLNG
        )
        self.assertArgHasType(
            TestMTLEventHelper.waitUntilSignaledValue_timeoutMS_, 1, objc._C_ULNGLNG
        )
