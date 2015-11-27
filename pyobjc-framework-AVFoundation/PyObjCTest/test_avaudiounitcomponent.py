from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVAudioUnitComponent (TestCase):
    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertIsInstance(AVFoundation.AVAudioUnitTypeOutput, unicode)
        self.assertIsInstance(AVFoundation.AVAudioUnitTypeMusicDevice, unicode)
        self.assertIsInstance(AVFoundation.AVAudioUnitTypeMusicEffect, unicode)
        self.assertIsInstance(AVFoundation.AVAudioUnitTypeFormatConverter, unicode)
        self.assertIsInstance(AVFoundation.AVAudioUnitTypeEffect, unicode)
        self.assertIsInstance(AVFoundation.AVAudioUnitTypeMixer, unicode)
        self.assertIsInstance(AVFoundation.AVAudioUnitTypePanner, unicode)
        self.assertIsInstance(AVFoundation.AVAudioUnitTypeGenerator, unicode)
        self.assertIsInstance(AVFoundation.AVAudioUnitTypeOfflineEffect, unicode)
        self.assertIsInstance(AVFoundation.AVAudioUnitTypeMIDIProcessor, unicode)
        self.assertIsInstance(AVFoundation.AVAudioUnitManufacturerNameApple, unicode)

        self.assertIsInstance(AVFoundation.AVAudioUnitComponentTagsDidChangeNotification, unicode)

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(AVFoundation.AVAudioUnitComponent.isSandboxSafe)
        self.assertResultIsBOOL(AVFoundation.AVAudioUnitComponent.hasMIDIInput)
        self.assertResultIsBOOL(AVFoundation.AVAudioUnitComponent.hasMIDIOutput)
        self.assertResultIsBOOL(AVFoundation.AVAudioUnitComponent.passesAUVal)
        self.assertResultIsBOOL(AVFoundation.AVAudioUnitComponent.hasCustomView)
        self.assertResultIsBOOL(AVFoundation.AVAudioUnitComponent.supportsNumberInputChannels_outputChannels_)

        self.assertArgIsBlock(AVFoundation.AVAudioUnitComponentManager.componentsPassingTest_, 0, b'Z@o^Z')

if __name__ == "__main__":
    main()
