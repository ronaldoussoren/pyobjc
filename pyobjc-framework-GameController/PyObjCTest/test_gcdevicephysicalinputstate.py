from PyObjCTools.TestSupport import (
    TestCase,
    min_sdk_level,
)
import objc
import GameController


class TestGCDevicePhysicalInputStateHelper(GameController.NSObject):
    def lastEventTimestamp(self):
        return 1

    def lastEventLatency(self):
        return 1


class TestGCDevicePhysicalInputState(TestCase):
    @min_sdk_level("13.0")
    def test_protocols(self):
        self.assertProtocolExists("GCDevicePhysicalInputState")

    def test_protocol_methods(self):
        self.assertResultHasType(
            TestGCDevicePhysicalInputStateHelper.lastEventTimestamp, objc._C_DBL
        )
        self.assertResultHasType(
            TestGCDevicePhysicalInputStateHelper.lastEventLatency, objc._C_DBL
        )
