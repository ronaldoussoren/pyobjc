from PyObjCTools.TestSupport import *

import CoreAudio

AudioDeviceIOProc = b'iIn^' + CoreAudio.AudioTimeStamp.__typestr__ + b'^' \
    + CoreAudio.AudioBufferList.__typestr__ + b'n^' + CoreAudio.AudioTimeStamp.__typestr__ \
    + b'^' + CoreAudio.AudioBufferList.__typestr__ + b'n^' + CoreAudio.AudioTimeStamp.__typestr__ \
    + b'^v'
AudioHardwarePropertyListenerProc = b'iI^v'
AudioDevicePropertyListenerProc = b'iIIZI^v'
AudioStreamPropertyListenerProc = b'iIII^v'

class TestAudioHardwareDeprecated (TestCase):

    def testConstants(self):
        self.assertEqual(CoreAudio.kAudioDevicePropertyScopeInput, CoreAudio.kAudioObjectPropertyScopeInput)
        self.assertEqual(CoreAudio.kAudioDevicePropertyScopeOutput, CoreAudio.kAudioObjectPropertyScopeOutput)
        self.assertEqual(CoreAudio.kAudioDevicePropertyScopePlayThrough, CoreAudio.kAudioObjectPropertyScopePlayThrough)

        self.assertEqual(CoreAudio.kAudioPropertyWildcardPropertyID, CoreAudio.kAudioObjectPropertySelectorWildcard)

        self.assertEqual(CoreAudio.kAudioPropertyWildcardSection, 0xFF)

        self.assertEqual(CoreAudio.kAudioPropertyWildcardChannel, CoreAudio.kAudioObjectPropertyElementWildcard)

        self.assertEqual(CoreAudio.kAudioISubOwnerControlClassID, fourcc(b'atch'))

        self.assertEqual(CoreAudio.kAudioLevelControlPropertyDecibelsToScalarTransferFunction, fourcc(b'lctf'))

        self.assertEqual(CoreAudio.kAudioLevelControlTranferFunctionLinear, 0)
        self.assertEqual(CoreAudio.kAudioLevelControlTranferFunction1Over3, 1)
        self.assertEqual(CoreAudio.kAudioLevelControlTranferFunction1Over2, 2)
        self.assertEqual(CoreAudio.kAudioLevelControlTranferFunction3Over4, 3)
        self.assertEqual(CoreAudio.kAudioLevelControlTranferFunction3Over2, 4)
        self.assertEqual(CoreAudio.kAudioLevelControlTranferFunction2Over1, 5)
        self.assertEqual(CoreAudio.kAudioLevelControlTranferFunction3Over1, 6)
        self.assertEqual(CoreAudio.kAudioLevelControlTranferFunction4Over1, 7)
        self.assertEqual(CoreAudio.kAudioLevelControlTranferFunction5Over1, 8)
        self.assertEqual(CoreAudio.kAudioLevelControlTranferFunction6Over1, 9)
        self.assertEqual(CoreAudio.kAudioLevelControlTranferFunction7Over1, 10)
        self.assertEqual(CoreAudio.kAudioLevelControlTranferFunction8Over1, 11)
        self.assertEqual(CoreAudio.kAudioLevelControlTranferFunction9Over1, 12)
        self.assertEqual(CoreAudio.kAudioLevelControlTranferFunction10Over1, 13)
        self.assertEqual(CoreAudio.kAudioLevelControlTranferFunction11Over1, 14)
        self.assertEqual(CoreAudio.kAudioLevelControlTranferFunction12Over1, 15)

        self.assertEqual(CoreAudio.kAudioHardwareRunLoopMode, b"com.apple.audio.CoreAudio")

        self.assertEqual(CoreAudio.kAudioHardwarePropertyRunLoop, fourcc(b'rnlp'))
        self.assertEqual(CoreAudio.kAudioHardwarePropertyDeviceForUID, fourcc(b'duid'))
        self.assertEqual(CoreAudio.kAudioHardwarePropertyPlugInForBundleID, fourcc(b'pibi'))

        self.assertEqual(CoreAudio.kAudioHardwarePropertyBootChimeVolumeScalar, fourcc(b'bbvs'))
        self.assertEqual(CoreAudio.kAudioHardwarePropertyBootChimeVolumeDecibels, fourcc(b'bbvd'))
        self.assertEqual(CoreAudio.kAudioHardwarePropertyBootChimeVolumeRangeDecibels, fourcc(b'bbd#'))
        self.assertEqual(CoreAudio.kAudioHardwarePropertyBootChimeVolumeScalarToDecibels, fourcc(b'bv2d'))
        self.assertEqual(CoreAudio.kAudioHardwarePropertyBootChimeVolumeDecibelsToScalar, fourcc(b'bd2v'))
        self.assertEqual(CoreAudio.kAudioHardwarePropertyBootChimeVolumeDecibelsToScalarTransferFunction, fourcc(b'bvtf'))

        self.assertEqual(CoreAudio.kAudioDeviceUnknown, CoreAudio.kAudioObjectUnknown)

        self.assertEqual(CoreAudio.kAudioDeviceTransportTypeAutoAggregate, fourcc(b'fgrp'))

        self.assertEqual(CoreAudio.kAudioDevicePropertyVolumeDecibelsToScalarTransferFunction, fourcc(b'vctf'))
        self.assertEqual(CoreAudio.kAudioDevicePropertyPlayThruVolumeDecibelsToScalarTransferFunction, fourcc(b'mvtf'))
        self.assertEqual(CoreAudio.kAudioDevicePropertyDriverShouldOwniSub, fourcc(b'isub'))
        self.assertEqual(CoreAudio.kAudioDevicePropertySubVolumeDecibelsToScalarTransferFunction, fourcc(b'svtf'))

        self.assertEqual(CoreAudio.kAudioDevicePropertyDeviceName, fourcc(b'name'))
        self.assertEqual(CoreAudio.kAudioDevicePropertyDeviceNameCFString, CoreAudio.kAudioObjectPropertyName)
        self.assertEqual(CoreAudio.kAudioDevicePropertyDeviceManufacturer, fourcc(b'makr'))
        self.assertEqual(CoreAudio.kAudioDevicePropertyDeviceManufacturerCFString, CoreAudio.kAudioObjectPropertyManufacturer)
        self.assertEqual(CoreAudio.kAudioDevicePropertyRegisterBufferList, fourcc(b'rbuf'))
        self.assertEqual(CoreAudio.kAudioDevicePropertyBufferSize, fourcc(b'bsiz'))
        self.assertEqual(CoreAudio.kAudioDevicePropertyBufferSizeRange, fourcc(b'bsz#'))
        self.assertEqual(CoreAudio.kAudioDevicePropertyChannelName, fourcc(b'chnm'))
        self.assertEqual(CoreAudio.kAudioDevicePropertyChannelNameCFString, CoreAudio.kAudioObjectPropertyElementName)
        self.assertEqual(CoreAudio.kAudioDevicePropertyChannelCategoryName, fourcc(b'ccnm'))
        self.assertEqual(CoreAudio.kAudioDevicePropertyChannelCategoryNameCFString, CoreAudio.kAudioObjectPropertyElementCategoryName)
        self.assertEqual(CoreAudio.kAudioDevicePropertyChannelNumberName, fourcc(b'cnnm'))
        self.assertEqual(CoreAudio.kAudioDevicePropertyChannelNumberNameCFString, CoreAudio.kAudioObjectPropertyElementNumberName)
        self.assertEqual(CoreAudio.kAudioDevicePropertySupportsMixing, fourcc(b'mix?'))
        self.assertEqual(CoreAudio.kAudioDevicePropertyStreamFormat, fourcc(b'sfmt'))
        self.assertEqual(CoreAudio.kAudioDevicePropertyStreamFormats, fourcc(b'sfm#'))
        self.assertEqual(CoreAudio.kAudioDevicePropertyStreamFormatSupported, fourcc(b'sfm?'))
        self.assertEqual(CoreAudio.kAudioDevicePropertyStreamFormatMatch, fourcc(b'sfmm'))
        self.assertEqual(CoreAudio.kAudioDevicePropertyDataSourceNameForID, fourcc(b'sscn'))
        self.assertEqual(CoreAudio.kAudioDevicePropertyClockSourceNameForID, fourcc(b'cscn'))
        self.assertEqual(CoreAudio.kAudioDevicePropertyPlayThruDestinationNameForID, fourcc(b'mddn'))
        self.assertEqual(CoreAudio.kAudioDevicePropertyChannelNominalLineLevelNameForID, fourcc(b'cnlv'))
        self.assertEqual(CoreAudio.kAudioDevicePropertyHighPassFilterSettingNameForID, fourcc(b'chip'))

        self.assertEqual(CoreAudio.kAudioStreamUnknown, CoreAudio.kAudioObjectUnknown)

        self.assertEqual(CoreAudio.kAudioStreamPropertyOwningDevice, CoreAudio.kAudioObjectPropertyOwner)
        self.assertEqual(CoreAudio.kAudioStreamPropertyPhysicalFormats, fourcc(b'pft#'))
        self.assertEqual(CoreAudio.kAudioStreamPropertyPhysicalFormatSupported, fourcc(b'pft?'))
        self.assertEqual(CoreAudio.kAudioStreamPropertyPhysicalFormatMatch, fourcc(b'pftm'))

        self.assertEqual(CoreAudio.kAudioBootChimeVolumeControlClassID, fourcc(b'pram'))

        self.assertEqual(CoreAudio.kAudioControlPropertyVariant, fourcc(b'cvar'))

        self.assertEqual(CoreAudio.kAudioClockSourceControlPropertyItemKind, CoreAudio.kAudioSelectorControlPropertyItemKind)

    def testFunctions(self):
        CoreAudio.AudioHardwareAddRunLoopSource
        CoreAudio.AudioHardwareRemoveRunLoopSource

        self.assertArgIsOut(CoreAudio.AudioHardwareGetPropertyInfo, 1)
        self.assertArgIsOut(CoreAudio.AudioHardwareGetPropertyInfo, 2)

        self.assertArgIsInOut(CoreAudio.AudioHardwareGetProperty, 1)
        self.assertArgIsOut(CoreAudio.AudioHardwareGetProperty, 2)
        self.assertArgSizeInArg(CoreAudio.AudioHardwareGetProperty, 2, 1)

        self.assertArgIsIn(CoreAudio.AudioHardwareSetProperty, 2)
        self.assertArgSizeInArg(CoreAudio.AudioHardwareSetProperty, 2, 1)

        self.assertArgIsFunction(CoreAudio.AudioHardwareAddPropertyListener, 1, AudioHardwarePropertyListenerProc, True)

        self.assertArgIsFunction(CoreAudio.AudioHardwareRemovePropertyListener, 1, AudioHardwarePropertyListenerProc, True)

        self.assertArgIsFunction(CoreAudio.AudioDeviceAddIOProc, 1, AudioDeviceIOProc, True)
        self.assertArgIsFunction(CoreAudio.AudioDeviceRemoveIOProc, 1, AudioDeviceIOProc, True)

        self.assertArgIsIn(CoreAudio.AudioDeviceRead, 1)
        self.assertArgIsOut(CoreAudio.AudioDeviceRead, 2)

        self.assertArgIsBOOL(CoreAudio.AudioDeviceGetPropertyInfo, 2)
        self.assertArgIsOut(CoreAudio.AudioDeviceGetPropertyInfo, 4)
        self.assertArgIsOut(CoreAudio.AudioDeviceGetPropertyInfo, 5)

        self.assertArgIsInOut(CoreAudio.AudioDeviceGetProperty, 4)
        self.assertArgIsOut(CoreAudio.AudioDeviceGetProperty, 5)
        self.assertArgSizeInArg(CoreAudio.AudioDeviceGetProperty, 5, 4)

        self.assertArgIsIn(CoreAudio.AudioDeviceSetProperty, 1)
        self.assertArgIsIn(CoreAudio.AudioDeviceSetProperty, 6)
        self.assertArgSizeInArg(CoreAudio.AudioDeviceSetProperty, 6, 5)

        self.assertArgIsFunction(CoreAudio.AudioDeviceAddPropertyListener, 4, AudioDevicePropertyListenerProc, True)

        self.assertArgIsFunction(CoreAudio.AudioDeviceRemovePropertyListener, 4, AudioDevicePropertyListenerProc, True)

        self.assertArgIsOut(CoreAudio.AudioStreamGetPropertyInfo, 3)
        self.assertArgIsOut(CoreAudio.AudioStreamGetPropertyInfo, 4)

        self.assertArgIsInOut(CoreAudio.AudioStreamGetProperty, 3)
        self.assertArgIsOut(CoreAudio.AudioStreamGetProperty, 4)
        self.assertArgSizeInArg(CoreAudio.AudioStreamGetProperty, 4, 3)

        self.assertArgIsIn(CoreAudio.AudioDeviceSetProperty, 1)
        self.assertArgSizeInArg(CoreAudio.AudioDeviceSetProperty, 6, 5)

        self.assertArgIsFunction(CoreAudio.AudioStreamAddPropertyListener, 3, AudioStreamPropertyListenerProc, True)

        self.assertArgIsFunction(CoreAudio.AudioStreamRemovePropertyListener, 3, AudioStreamPropertyListenerProc, True)


if __name__ == "__main__":
    main()
