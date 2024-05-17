from PyObjCTools.TestSupport import (
    TestCase,
    min_sdk_level,
    expectedFailure,
)
import GameController


class TestGCAxisInputHelper(GameController.NSObject):
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


class TestGCAxisInput(TestCase):
    @min_sdk_level("13.0")
    def test_protocols(self):
        self.assertProtocolExists("GCAxisInput")

    @expectedFailure  # 'value' method is requires explicit protocol definition.
    def test_protocol_methods(self):
        self.assertResultIsBlock(TestGCAxisInputHelper.valueDidChangeHandler, b"v@@f")

        self.assertArgIsBlock(
            TestGCAxisInputHelper.setValueDidChangeHandler_, 0, b"v@@f"
        )

        self.assertResultHasType(TestGCAxisInputHelper.value, b"f")

        self.assertResultIsBOOL(TestGCAxisInputHelper.isAnalog)
        self.assertResultIsBOOL(TestGCAxisInputHelper.canWrap)
        self.assertResultHasType(TestGCAxisInputHelper.lastValueTimestamp, b"d")
        self.assertResultHasType(TestGCAxisInputHelper.lastValueLatency, b"d")
