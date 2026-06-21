import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level

AVAudioIONodeInputBlock = b"^{AudioBufferList=L[1{AudioBuffer=LL^v}]}I"
AVAudioIONodeInputBlockRealtimeSafe = b"^{AudioBufferList=L[1{AudioBuffer=LL^v}]}I"
AVAudioNodeTapBlock = b"v@@"


class TestAVAudioIONode(TestCase):
    def test_constants(self):
        self.assertIsEnumType(AVFoundation.AVAudioVoiceProcessingSpeechActivityEvent)
        self.assertEqual(AVFoundation.AVAudioVoiceProcessingSpeechActivityStarted, 0)
        self.assertEqual(AVFoundation.AVAudioVoiceProcessingSpeechActivityEnded, 1)

        self.assertIsEnumType(AVFoundation.AVAudioVoiceProcessingOtherAudioDuckingLevel)
        self.assertEqual(
            AVFoundation.AVAudioVoiceProcessingOtherAudioDuckingLevelDefault, 0
        )
        self.assertEqual(
            AVFoundation.AVAudioVoiceProcessingOtherAudioDuckingLevelMin, 10
        )
        self.assertEqual(
            AVFoundation.AVAudioVoiceProcessingOtherAudioDuckingLevelMid, 20
        )
        self.assertEqual(
            AVFoundation.AVAudioVoiceProcessingOtherAudioDuckingLevelMax, 30
        )

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(AVFoundation.AVCoreAnimationBeginTimeAtZero, float)
        self.assertIsInstance(AVFoundation.AVLayerVideoGravityResizeAspect, str)
        self.assertIsInstance(AVFoundation.AVLayerVideoGravityResizeAspectFill, str)
        self.assertIsInstance(AVFoundation.AVLayerVideoGravityResize, str)

    def test_structs(self):
        v = AVFoundation.AVAudioVoiceProcessingOtherAudioDuckingConfiguration()
        self.assertIsInstance(v.enableAdvancedDucking, bool)
        self.assertIsInstance(v.duckingLevel, int)

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertResultIsBOOL(
            AVFoundation.AVAudioInputNode.setManualRenderingInputPCMFormat_inputBlock_
        )
        self.assertArgIsBlock(
            AVFoundation.AVAudioInputNode.setManualRenderingInputPCMFormat_inputBlock_,
            1,
            AVAudioIONodeInputBlock,
        )

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertResultIsBOOL(AVFoundation.AVAudioIONode.isVoiceProcessingEnabled)

        self.assertResultIsBOOL(
            AVFoundation.AVAudioInputNode.setVoiceProcessingEnabled_error_
        )
        self.assertArgIsOut(
            AVFoundation.AVAudioInputNode.setVoiceProcessingEnabled_error_, 1
        )

        self.assertResultIsBOOL(AVFoundation.AVAudioInputNode.isVoiceProcessingBypassed)
        self.assertArgIsBOOL(
            AVFoundation.AVAudioInputNode.setVoiceProcessingBypassed_, 0
        )

    @min_os_level("27.0")
    def testMethods27_0(self):
        self.assertResultIsBOOL(
            AVFoundation.AVAudioInputNode.setRealtimeSafeManualRenderingInputPCMFormat_inputBlock_
        )
        self.assertArgIsBlock(
            AVFoundation.AVAudioInputNode.setRealtimeSafeManualRenderingInputPCMFormat_inputBlock_,
            1,
            AVAudioIONodeInputBlockRealtimeSafe,
        )

        self.assertResultIsBOOL(
            AVFoundation.AVAudioInputNode.installTapOnBus_bufferSize_format_error_block_
        )
        self.assertArgIsOut(
            AVFoundation.AVAudioInputNode.installTapOnBus_bufferSize_format_error_block_,
            3,
        )
        self.assertArgIsBlock(
            AVFoundation.AVAudioInputNode.installTapOnBus_bufferSize_format_error_block_,
            4,
            AVAudioNodeTapBlock,
        )
