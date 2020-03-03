import AVFoundation
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level

AVAudioEngineManualRenderingBlock = (
    objc._C_NSInteger + b"Io^{AudioBufferList=L[1{AudioBuffer=LL^v}]}o^i"
)
AUMIDIOutputEventBlock = b"iqC" + objc._C_NSInteger + b"n^v"


class TestAVAudioEngine(TestCase):
    @min_os_level("10.10")
    def testMethods(self):
        self.assertArgIsOut(AVFoundation.AVAudioEngine.startAndReturnError_, 0)
        self.assertResultIsBOOL(AVFoundation.AVAudioEngine.isRunning)

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertResultIsBOOL(
            AVFoundation.AVAudioEngine.isAutoShutdownEnabled
        )  # noqa: B950
        self.assertArgIsBOOL(
            AVFoundation.AVAudioEngine.setAutoShutdownEnabled_, 0
        )  # noqa: B950

        self.assertResultIsBOOL(
            AVFoundation.AVAudioEngine.enableManualRenderingMode_format_maximumFrameCount_error_  # noqa: B950
        )
        self.assertArgIsOut(
            AVFoundation.AVAudioEngine.enableManualRenderingMode_format_maximumFrameCount_error_,  # noqa: B950
            3,
        )

        self.assertArgIsOut(
            AVFoundation.AVAudioEngine.renderOffline_toBuffer_error_, 2
        )  # noqa: B950

        self.assertResultIsBOOL(
            AVFoundation.AVAudioEngine.isInManualRenderingMode
        )  # noqa: B950

        # NOTE: This almost certainly requires a manual wrapper to use correctly
        self.assertResultIsBlock(
            AVFoundation.AVAudioEngine.manualRenderingBlock,
            AVAudioEngineManualRenderingBlock,
        )

    @min_os_level("10.14")
    def testMethods10_14(self):
        self.assertArgIsBlock(
            AVFoundation.AVAudioEngine.connectMIDI_to_format_block_,
            3,
            AUMIDIOutputEventBlock,
        )
        self.assertArgIsBlock(
            AVFoundation.AVAudioEngine.connectMIDI_toNodes_format_block_,
            3,
            AUMIDIOutputEventBlock,
        )

    def testConstants(self):
        self.assertEqual(
            AVFoundation.AVAudioEngineManualRenderingErrorInvalidMode, -80800
        )
        self.assertEqual(
            AVFoundation.AVAudioEngineManualRenderingErrorInitialized, -80801
        )
        self.assertEqual(
            AVFoundation.AVAudioEngineManualRenderingErrorNotRunning, -80802
        )

        self.assertEqual(
            AVFoundation.AVAudioEngineManualRenderingStatusError, -1
        )  # noqa: B950
        self.assertEqual(
            AVFoundation.AVAudioEngineManualRenderingStatusSuccess, 0
        )  # noqa: B950
        self.assertEqual(
            AVFoundation.AVAudioEngineManualRenderingStatusInsufficientDataFromInputNode,  # noqa: B950
            1,
        )
        self.assertEqual(
            AVFoundation.AVAudioEngineManualRenderingStatusCannotDoInCurrentContext,
            2,  # noqa: B950
        )

        self.assertEqual(
            AVFoundation.AVAudioEngineManualRenderingModeOffline, 0
        )  # noqa: B950
        self.assertEqual(
            AVFoundation.AVAudioEngineManualRenderingModeRealtime, 1
        )  # noqa: B950

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(
            AVFoundation.AVAudioEngineConfigurationChangeNotification, str
        )
