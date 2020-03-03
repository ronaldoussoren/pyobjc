import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAudioUnitComponent(TestCase):
    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(AVFoundation.AVAudioUnitTypeOutput, str)
        self.assertIsInstance(AVFoundation.AVAudioUnitTypeMusicDevice, str)
        self.assertIsInstance(AVFoundation.AVAudioUnitTypeMusicEffect, str)
        self.assertIsInstance(AVFoundation.AVAudioUnitTypeFormatConverter, str)
        self.assertIsInstance(AVFoundation.AVAudioUnitTypeEffect, str)
        self.assertIsInstance(AVFoundation.AVAudioUnitTypeMixer, str)
        self.assertIsInstance(AVFoundation.AVAudioUnitTypePanner, str)
        self.assertIsInstance(AVFoundation.AVAudioUnitTypeGenerator, str)
        self.assertIsInstance(AVFoundation.AVAudioUnitTypeOfflineEffect, str)
        self.assertIsInstance(AVFoundation.AVAudioUnitTypeMIDIProcessor, str)
        self.assertIsInstance(
            AVFoundation.AVAudioUnitManufacturerNameApple, str
        )  # noqa: B950

        self.assertIsInstance(
            AVFoundation.AVAudioUnitComponentTagsDidChangeNotification, str
        )

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(
            AVFoundation.AVAudioUnitComponentManagerRegistrationsChangedNotification,  # noqa: B950
            str,
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(AVFoundation.AVAudioUnitComponent.isSandboxSafe)
        self.assertResultIsBOOL(AVFoundation.AVAudioUnitComponent.hasMIDIInput)
        self.assertResultIsBOOL(AVFoundation.AVAudioUnitComponent.hasMIDIOutput)
        self.assertResultIsBOOL(AVFoundation.AVAudioUnitComponent.passesAUVal)
        self.assertResultIsBOOL(AVFoundation.AVAudioUnitComponent.hasCustomView)
        self.assertResultIsBOOL(
            AVFoundation.AVAudioUnitComponent.supportsNumberInputChannels_outputChannels_  # noqa: B950
        )

        self.assertArgIsBlock(
            AVFoundation.AVAudioUnitComponentManager.componentsPassingTest_, 0, b"Z@o^Z"
        )
