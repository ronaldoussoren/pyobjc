from PyObjCTools.TestSupport import TestCase, min_os_level
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

    @min_os_level("26.0")
    def test_methods26_0(self):
        self.assertArgIsBlock(
            PHASE.PHASESoundEvent.startAtTime_completion_, 1, b"v" + objc._C_NSInteger
        )
        self.assertArgIsBlock(
            PHASE.PHASESoundEvent.seekToTime_resumeAtEngineTime_completion_,
            2,
            b"v" + objc._C_NSInteger,
        )
