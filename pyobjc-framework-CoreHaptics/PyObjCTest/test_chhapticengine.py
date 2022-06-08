import CoreHaptics
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc

CHHapticCompletionHandler = b"v@"
CHHapticEngineFinishedHandler = objc._C_NSInteger + b"@"
CHHapticEngineStoppedHandler = b"v" + objc._C_NSInteger
CHHapticEngineResetHandler = b"v"


class TestCHHapticEngine(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CoreHaptics.CHHapticEngineFinishedAction)
        self.assertIsEnumType(CoreHaptics.CHHapticEngineStoppedReason)

    def test_constants(self):
        self.assertEqual(CoreHaptics.CHHapticTimeImmediate, 0.0)

        self.assertEqual(CoreHaptics.CHHapticEngineFinishedActionStopEngine, 1)
        self.assertEqual(CoreHaptics.CHHapticEngineFinishedActionLeaveEngineRunning, 2)

        self.assertEqual(
            CoreHaptics.CHHapticEngineStoppedReasonAudioSessionInterrupt, 1
        )
        self.assertEqual(CoreHaptics.CHHapticEngineStoppedReasonApplicationSuspended, 2)
        self.assertEqual(CoreHaptics.CHHapticEngineStoppedReasonIdleTimeout, 3)
        self.assertEqual(CoreHaptics.CHHapticEngineStoppedReasonNotifyWhenFinished, 4)
        self.assertEqual(CoreHaptics.CHHapticEngineStoppedReasonEngineDestroyed, 5)
        self.assertEqual(
            CoreHaptics.CHHapticEngineStoppedReasonGameControllerDisconnect, 6
        )

        self.assertEqual(CoreHaptics.CHHapticEngineStoppedReasonSystemError, -1)

    @min_sdk_level("12.0")
    def test_constants12_0(self):
        self.assertIsInstance(
            CoreHaptics.CHHapticAudioResourceKeyUseVolumeEnvelope, str
        )

    @min_sdk_level("13.0")
    def test_constants13_0(self):
        self.assertIsInstance(CoreHaptics.CHHapticAudioResourceKeyLoopEnabled, str)

    @min_sdk_level("10.15")
    def test_methods10_15(self):
        self.assertResultIsBlock(
            CoreHaptics.CHHapticEngine.stoppedHandler, CHHapticEngineStoppedHandler
        )
        self.assertResultIsBlock(
            CoreHaptics.CHHapticEngine.resetHandler, CHHapticEngineResetHandler
        )

        self.assertArgIsBlock(
            CoreHaptics.CHHapticEngine.setStoppedHandler_,
            0,
            CHHapticEngineStoppedHandler,
        )
        self.assertArgIsBlock(
            CoreHaptics.CHHapticEngine.setResetHandler_, 0, CHHapticEngineResetHandler
        )

        self.assertResultIsBOOL(CoreHaptics.CHHapticEngine.playsHapticsOnly)
        self.assertResultIsBOOL(CoreHaptics.CHHapticEngine.isMutedForAudio)
        self.assertResultIsBOOL(CoreHaptics.CHHapticEngine.isMutedForHaptics)
        self.assertResultIsBOOL(CoreHaptics.CHHapticEngine.isAutoShutdownEnabled)

        self.assertArgIsBOOL(CoreHaptics.CHHapticEngine.setPlaysHapticsOnly_, 0)
        self.assertArgIsBOOL(CoreHaptics.CHHapticEngine.setIsMutedForAudio_, 0)
        self.assertArgIsBOOL(CoreHaptics.CHHapticEngine.setIsMutedForHaptics_, 0)
        self.assertArgIsBOOL(CoreHaptics.CHHapticEngine.setAutoShutdownEnabled_, 0)

        self.assertArgIsOut(CoreHaptics.CHHapticEngine.initAndReturnError_, 0)
        self.assertArgIsOut(CoreHaptics.CHHapticEngine.initWithAudioSession_error_, 1)

        self.assertArgIsBlock(
            CoreHaptics.CHHapticEngine.startWithCompletionHandler_,
            0,
            CHHapticCompletionHandler,
        )

        self.assertResultIsBOOL(CoreHaptics.CHHapticEngine.startAndReturnError_)
        self.assertArgIsOut(CoreHaptics.CHHapticEngine.startAndReturnError_, 0)

        self.assertArgIsBlock(
            CoreHaptics.CHHapticEngine.stopWithCompletionHandler_,
            0,
            CHHapticCompletionHandler,
        )

        self.assertArgIsBlock(
            CoreHaptics.CHHapticEngine.notifyWhenPlayersFinished_,
            0,
            CHHapticEngineFinishedHandler,
        )

        self.assertArgIsOut(
            CoreHaptics.CHHapticEngine.createPlayerWithPattern_error_, 1
        )
        self.assertArgIsOut(
            CoreHaptics.CHHapticEngine.createAdvancedPlayerWithPattern_error_, 1
        )
        self.assertArgIsOut(
            CoreHaptics.CHHapticEngine.registerAudioResource_options_error_, 2
        )

        self.assertResultIsBOOL(
            CoreHaptics.CHHapticEngine.unregisterAudioResource_error_, 1
        )
        self.assertArgIsOut(
            CoreHaptics.CHHapticEngine.unregisterAudioResource_error_, 1
        )

        self.assertResultIsBOOL(CoreHaptics.CHHapticEngine.playPatternFromURL_error_, 1)
        self.assertArgIsOut(CoreHaptics.CHHapticEngine.playPatternFromURL_error_, 1)

        self.assertResultIsBOOL(
            CoreHaptics.CHHapticEngine.playPatternFromData_error_, 1
        )
        self.assertArgIsOut(CoreHaptics.CHHapticEngine.playPatternFromData_error_, 1)

    @min_sdk_level("13.0")
    def test_methods13_0(self):
        self.assertResultIsBOOL(CoreHaptics.CHHapticEngine.playsAudioOnly)
        self.assertArgIsBOOL(CoreHaptics.CHHapticEngine.setPlaysAudioOnly_, 0)
