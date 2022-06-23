from PyObjCTools.TestSupport import (
    TestCase,
    min_sdk_level,
)
import objc
import GameController


class TestGCPressedStateInputHelper(GameController.NSObject):
    def pressedDidChangeHandler(self):
        return 1

    def setPressedDidChangeHandler_(self, a):
        pass

    def isPressed(self):
        return 1

    def lastPressedStateTimestamp(self):
        return 1

    def lastPressedStateLatency(self):
        return 1


class TestGCPressedStateInput(TestCase):
    @min_sdk_level("13.0")
    def test_protocols(self):
        objc.protocolNamed("GCPressedStateInput")

    def test_protocol_methods(self):
        self.assertResultIsBlock(
            TestGCPressedStateInputHelper.pressedDidChangeHandler, b"v@Z"
        )
        self.assertArgIsBlock(
            TestGCPressedStateInputHelper.setPressedDidChangeHandler_, 0, b"v@Z"
        )

        self.assertResultIsBOOL(TestGCPressedStateInputHelper.isPressed)
        self.assertResultIsHasType(
            TestGCPressedStateInputHelper.lastPressedStateTimestamp, b"d"
        )
        self.assertResultIsHasType(
            TestGCPressedStateInputHelper.setLastPressedStateTimestamp_, 0, b"d"
        )
