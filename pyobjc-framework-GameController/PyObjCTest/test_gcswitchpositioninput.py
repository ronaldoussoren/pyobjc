from PyObjCTools.TestSupport import (
    TestCase,
    min_sdk_level,
)
import objc
import GameController


class TestGCSwitchPositionInputHelper(GameController.NSObject):
    def positionDidChangeHandler(self):
        return 1

    def setPositionDidChangeHandler_(self, a):
        pass

    def position(self):
        return 1

    def positionRange(self):
        return 1

    def isSequential(self):
        return 1

    def canWrap(self):
        return 1

    def lastPositionTimestamp(self):
        return 1

    def lastPositionLatency(self):
        return 1


class TestGCSwitchPositionInput(TestCase):
    @min_sdk_level("13.0")
    def test_protocols(self):
        self.assertProtocolExists("GCSwitchPositionInput")

    def test_protocol_methhods(self):
        self.assertResultIsBlock(
            GameController.TestGCSwitchPositionInputHelper.positionDidChangeHandler,
            b"v@@" + objc._C_NSInteger,
        )
        self.assertArgIsBlock(
            GameController.TestGCSwitchPositionInputHelper.setPositionDidChangeHandler_,
            0,
            b"v@@" + objc._C_NSInteger,
        )

        self.assertResultHasType(
            GameController.TestGCSwitchPositionInputHelper.position, objc._C_NSInteger
        )
        self.assertResultHasType(
            GameController.TestGCSwitchPositionInputHelper.positionRange,
            GameController.NSRange.__typestr__,
        )
        self.assertResultIsBOOL(
            GameController.TestGCSwitchPositionInputHelper.isSequential
        )
        self.assertResultIsBOOL(GameController.TestGCSwitchPositionInputHelper.canWrap)
        self.assertResultHasType(
            GameController.TestGCSwitchPositionInputHelper.lastPositionTimestamp, b"d"
        )
        self.assertResultHasType(
            GameController.TestGCSwitchPositionInputHelper.lastPositionLatency, b"d"
        )
