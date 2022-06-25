from PyObjCTools.TestSupport import (
    TestCase,
    min_sdk_level,
)
import GameController


class TestGCRelativeInputHelper(GameController.NSObject):
    def deltaDidChangeHandler(self):
        return 1

    def setDeltaDidChangeHandler_(self, a):
        pass

    def delta(self):
        return 1

    def isAnalog(self):
        return 1

    def lastDeltaTimestamp(self):
        return 1

    def lastDeltaLatency(self):
        return 1


class TestGCRelativeInput(TestCase):
    @min_sdk_level("13.0")
    def test_protocols(self):
        self.assertProtocolExists("GCRelativeInput")

    def test_protocol_methods(self):
        self.assertResultIsBlock(
            TestGCRelativeInputHelper.deltaDidChangeHandler, b"v@@f"
        )
        self.assertArgIsBlock(
            TestGCRelativeInputHelper.setDeltaDidChangeHandler_, 0, b"v@@f"
        )

        self.assertResultHasType(TestGCRelativeInputHelper.delta, b"f")
        self.assertResultIsBOOL(TestGCRelativeInputHelper.isAnalog)
        self.assertResultHasType(TestGCRelativeInputHelper.lastDeltaTimestamp, b"d")
        self.assertResultHasType(TestGCRelativeInputHelper.lastDeltaLatency, b"d")
