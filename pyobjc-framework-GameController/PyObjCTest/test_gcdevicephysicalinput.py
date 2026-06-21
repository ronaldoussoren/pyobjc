from PyObjCTools.TestSupport import (
    TestCase,
    min_sdk_level,
)
import GameController


class TestGCDevicePhysicalInputHelper(GameController.NSObject):
    def elementValueDidChangeHandler(self):
        return 1

    def setElementValueDidChangeHandler_(self, a):
        pass

    def inputStateAvailableHandler(self):
        return 1

    def setInputStateAvailableHandler_(self, a):
        pass

    def inputStateQueueDepth(self):
        return 1

    def setInputStateQueueDepth_(self, a):
        pass

    def inputStateForSpatialAccessoryAnchorTimestamp_(self, a):
        return 1


class TestGCDevicePhysicalInput(TestCase):
    @min_sdk_level("13.0")
    def test_protocols(self):
        self.assertProtocolExists("GCDevicePhysicalInput", GameController)

    def test_protocol_methods(self):
        self.assertResultIsBlock(
            TestGCDevicePhysicalInputHelper.elementValueDidChangeHandler, b"v@@"
        )
        self.assertArgIsBlock(
            TestGCDevicePhysicalInputHelper.setElementValueDidChangeHandler_, 0, b"v@@"
        )

        self.assertResultIsBlock(
            TestGCDevicePhysicalInputHelper.inputStateAvailableHandler, b"v@"
        )
        self.assertArgIsBlock(
            TestGCDevicePhysicalInputHelper.setInputStateAvailableHandler_, 0, b"v@"
        )

        self.assertArgHasType(
            TestGCDevicePhysicalInputHelper.inputStateForSpatialAccessoryAnchorTimestamp_,
            0,
            b"d",
        )
