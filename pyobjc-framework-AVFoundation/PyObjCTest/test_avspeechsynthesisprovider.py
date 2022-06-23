import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level

AVSpeechSynthesisProviderOutputBlock = b"v@@"


class TestAVSpeechSynthesisProvider(TestCase):
    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertResultIsBlock(
            AVFoundation.AVSpeechSynthesisProviderAudioUnit.speechSynthesisOutputMetadataBlock,
            AVSpeechSynthesisProviderOutputBlock,
        )
        self.assertArgIsBlock(
            AVFoundation.AVSpeechSynthesisProviderAudioUnit.setSpeechSynthesisOutputMetadataBlock_,
            0,
            AVSpeechSynthesisProviderOutputBlock,
        )
