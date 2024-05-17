from PyObjCTools.TestSupport import (
    TestCase,
    min_sdk_level,
    expectedFailure,
)
import GameController


class TestGCLinearInputHelper(GameController.NSObject):
    def valueDidChangeHandler(self):
        return 1

    def setValueDidChangeHandler_(self, a):
        pass

    def value(self):
        return 1

    def isAnalog(self):
        return 1

    def canWrap(self):
        return 1

    def lastValueTimestamp(self):
        return 1

    def lastValueLatency(self):
        return 1


class TestGCLinearInput(TestCase):
    @min_sdk_level("13.0")
    def test_protocols(self):
        self.assertProtocolExists("GCLinearInput")

    @expectedFailure  # value method requires explicit protocol definition
    def test_protocol_methods(self):
        self.assertResultIsBlock(TestGCLinearInputHelper.valueDidChangeHandler, b"v@@f")
        self.assertArgIsBlock(
            TestGCLinearInputHelper.setValueDidChangeHandler_, 0, b"v@@f"
        )

        self.assertResultHasType(TestGCLinearInputHelper.value, b"f")
        self.assertResultIsBOOL(TestGCLinearInputHelper.isAnalog)
        self.assertResultIsBOOL(TestGCLinearInputHelper.canWrap)
        self.assertResultHasType(TestGCLinearInputHelper.lastValueTimestamp, b"d")
        self.assertResultHasType(TestGCLinearInputHelper.lastValueLatency, b"d")
