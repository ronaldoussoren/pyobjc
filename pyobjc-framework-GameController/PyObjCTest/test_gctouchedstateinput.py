from PyObjCTools.TestSupport import (
    TestCase,
    min_sdk_level,
)
import GameController


class TestGCTouchedStateInputHelper(GameController.NSObject):
    def touchedDidChangeHandler(self):
        return 1

    def setTouchedDidChangeHandler_(self, a):
        pass

    def isTouched(self):
        return 1

    def lastTouchedStateTimestamp(self):
        return 1

    def lastTouchedStateLatency(self):
        return 1


class TestGCTouchedStateInput(TestCase):
    @min_sdk_level("13.0")
    def test_protocols(self):
        self.assertProtocolExists("GCTouchedStateInput")

    def test_protocol_methods(self):
        self.assertResultIsBlock(
            TestGCTouchedStateInputHelper.touchedDidChangeHandler, b"v@@Z"
        )
        self.assertArgIsBlock(
            TestGCTouchedStateInputHelper.setTouchedDidChangeHandler_, 0, b"v@@Z"
        )
        self.assertResultIsBOOL(TestGCTouchedStateInputHelper.isTouched)
        self.assertResultHasType(
            TestGCTouchedStateInputHelper.lastTouchedStateTimestamp, b"d"
        )
        self.assertResultHasType(
            TestGCTouchedStateInputHelper.lastTouchedStateLatency, b"d"
        )
