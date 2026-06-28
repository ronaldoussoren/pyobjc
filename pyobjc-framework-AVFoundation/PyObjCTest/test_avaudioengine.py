import AVFoundation
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level

AVAudioEngineManualRenderingBlock = (
    objc._C_NSInteger + b"Io^{AudioBufferList=L[1{AudioBuffer=LL^v}]}o^i"
)
AUMIDIOutputEventBlock = b"iqC" + objc._C_NSInteger + b"n^v"

# XXX: This won't work automaticly
AUMIDIEventListBlock = (
    b"iQ" + objc._C_CHAR_AS_INT + b"^{MIDIEventList=iI[1{MIDIEventPacket=II[64I]}]}"
)


class TestAVAudioEngine(TestCase):
    def test_enums(self):
        self.assertIsEnumType(AVFoundation.AVAudioEngineManualRenderingError)
        self.assertEqual(
            AVFoundation.AVAudioEngineManualRenderingErrorInvalidMode, -80800
        )
        self.assertEqual(
            AVFoundation.AVAudioEngineManualRenderingErrorInitialized, -80801
        )
        self.assertEqual(
            AVFoundation.AVAudioEngineManualRenderingErrorNotRunning, -80802
        )

        self.assertIsEnumType(AVFoundation.AVAudioEngineManualRenderingStatus)
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

        self.assertIsEnumType(AVFoundation.AVAudioEngineManualRenderingMode)
        self.assertEqual(
            AVFoundation.AVAudioEngineManualRenderingModeOffline, 0
        )  # noqa: B950
        self.assertEqual(
            AVFoundation.AVAudioEngineManualRenderingModeRealtime, 1
        )  # noqa: B950

    @min_os_level("10.10")
    def test_constants10_10(self):
        self.assertIsInstance(
            AVFoundation.AVAudioEngineConfigurationChangeNotification, str
        )

    @min_os_level("10.10")
    def test_methods(self):
        self.assertArgIsOut(AVFoundation.AVAudioEngine.startAndReturnError_, 0)
        self.assertResultIsBOOL(AVFoundation.AVAudioEngine.isRunning)

    @min_os_level("10.13")
    def test_methods10_13(self):
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
    def test_methods10_14(self):
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

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertArgIsBlock(
            AVFoundation.AVAudioEngine.connectMIDI_to_format_eventListBlock_,
            3,
            AUMIDIEventListBlock,
        )
        self.assertArgIsBlock(
            AVFoundation.AVAudioEngine.connectMIDI_toNodes_format_eventListBlock_,
            3,
            AUMIDIEventListBlock,
        )

    @min_os_level("27.0")
    def test_methods27_0(self):
        self.assertArgIsOut(
            AVFoundation.AVAudioEngine.connect_to_fromBus_toBus_format_error_, 5
        )
        self.assertArgIsOut(AVFoundation.AVAudioEngine.connect_to_format_error_, 3)
        self.assertArgIsOut(
            AVFoundation.AVAudioEngine.connect_toConnectionPoints_fromBus_format_error_,
            4,
        )
        self.assertArgIsBlock(
            AVFoundation.AVAudioEngine.connectMIDI_to_format_eventListProvider_,
            3,
            AUMIDIEventListBlock,
        )
        self.assertArgIsBlock(
            AVFoundation.AVAudioEngine.connectMIDI_toNodes_format_eventListProvider_,
            3,
            AUMIDIEventListBlock,
        )
