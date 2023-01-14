from PyObjCTools.TestSupport import TestCase
import objc

import PHASE


class TestPHASESoundEvent(TestCase):
    def test_methods(self):
        self.assertArgIsOut(
            PHASE.PHASESoundEvent.initWithEngine_assetIdentifier_mixerParameters_error_,
            3,
        )
        self.assertArgIsOut(
            PHASE.PHASESoundEvent.initWithEngine_assetIdentifier_error_, 2
        )
        self.assertArgIsBlock(
            PHASE.PHASESoundEvent.prepareWithCompletion_, 0, b"v" + objc._C_NSInteger
        )
        self.assertArgIsBlock(
            PHASE.PHASESoundEvent.startWithCompletion_, 0, b"v" + objc._C_NSInteger
        )
        self.assertArgIsBlock(
            PHASE.PHASESoundEvent.seekToTime_completion_, 1, b"v" + objc._C_NSInteger
        )
        self.assertResultIsBOOL(PHASE.PHASESoundEvent.isIndefinite)
