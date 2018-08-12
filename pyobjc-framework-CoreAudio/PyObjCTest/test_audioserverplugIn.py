from PyObjCTools.TestSupport import *

import CoreAudio

class TestAudioServerPlugIn (TestCase):
    def testConstants(self):
        self.assertFalse(hasattr(CoreAudio, 'kAudioServerPlugInTypeUUID'))

        self.assertFalse(hasattr(CoreAudio, 'kAudioObjectPlugInObject'))
        self.assertFalse(hasattr(CoreAudio, 'kAudioServerPlugInHostClientID'))

        self.assertFalse(hasattr(CoreAudio, 'kAudioServerPlugInCustomPropertyDataTypeNone'))
        self.assertFalse(hasattr(CoreAudio, 'kAudioServerPlugInCustomPropertyDataTypeCFString'))
        self.assertFalse(hasattr(CoreAudio, 'kAudioServerPlugInCustomPropertyDataTypeCFPropertyList'))

        self.assertFalse(hasattr(CoreAudio, 'kAudioServerPlugInIOOperationThread'))
        self.assertFalse(hasattr(CoreAudio, 'kAudioServerPlugInIOOperationCycle'))
        self.assertFalse(hasattr(CoreAudio, 'kAudioServerPlugInIOOperationReadInput'))
        self.assertFalse(hasattr(CoreAudio, 'kAudioServerPlugInIOOperationConvertInput'))
        self.assertFalse(hasattr(CoreAudio, 'kAudioServerPlugInIOOperationProcessInput'))
        self.assertFalse(hasattr(CoreAudio, 'kAudioServerPlugInIOOperationProcessOutput'))
        self.assertFalse(hasattr(CoreAudio, 'kAudioServerPlugInIOOperationMixOutput'))
        self.assertFalse(hasattr(CoreAudio, 'kAudioServerPlugInIOOperationProcessMix'))
        self.assertFalse(hasattr(CoreAudio, 'kAudioServerPlugInIOOperationConvertMix'))
        self.assertFalse(hasattr(CoreAudio, 'kAudioServerPlugInIOOperationWriteMix'))

        self.assertFalse(hasattr(CoreAudio, 'kAudioObjectPropertyCustomPropertyInfoList'))

        self.assertFalse(hasattr(CoreAudio, 'kAudioPlugInPropertyResourceBundle'))

        self.assertFalse(hasattr(CoreAudio, 'kAudioDeviceClockAlgorithmRaw'))
        self.assertFalse(hasattr(CoreAudio, 'kAudioDeviceClockAlgorithmSimpleIIR'))
        self.assertFalse(hasattr(CoreAudio, 'kAudioDeviceClockAlgorithm12PtMovingWindowAverage'))

        self.assertFalse(hasattr(CoreAudio, 'kAudioDevicePropertyZeroTimeStampPeriod'))
        self.assertFalse(hasattr(CoreAudio, 'kAudioDevicePropertyClockAlgorithm'))
        self.assertFalse(hasattr(CoreAudio, 'kAudioDevicePropertyClockIsStable'))

        self.assertFalse(hasattr(CoreAudio, 'kAudioServerPlugInDriverInterfaceUUID'))

    def testStructs(self):
        self.assertFalse(hasattr(CoreAudio, 'AudioServerPlugInCustomPropertyInfo'))
        self.assertFalse(hasattr(CoreAudio, 'AudioServerPlugInClientInfo'))
        self.assertFalse(hasattr(CoreAudio, 'AudioServerPlugInIOCycleInfo'))
        self.assertFalse(hasattr(CoreAudio, 'AudioServerPlugInHostInterface'))
        self.assertFalse(hasattr(CoreAudio, 'AudioServerPlugInDriverInterface'))


if __name__ == "__main__":
    main()
