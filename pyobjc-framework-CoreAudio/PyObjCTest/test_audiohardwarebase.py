import CoreAudio
from PyObjCTools.TestSupport import TestCase, fourcc


class TestAudioHardwareBase(TestCase):
    def testStructs(self):
        v = CoreAudio.AudioObjectPropertyAddress()
        self.assertEqual(v.mSelector, 0)
        self.assertEqual(v.mScope, 0)
        self.assertEqual(v.mElement, 0)
        self.assertPickleRoundTrips(v)

        v = CoreAudio.AudioStreamRangedDescription()
        self.assertEqual(v.mFormat, CoreAudio.AudioStreamBasicDescription())
        self.assertEqual(v.mSampleRateRange, CoreAudio.AudioValueRange())
        self.assertPickleRoundTrips(v)

    def testConstants(self):
        self.assertEqual(CoreAudio.kAudioHardwareNoError, 0)
        self.assertEqual(CoreAudio.kAudioHardwareNotRunningError, fourcc(b"stop"))
        self.assertEqual(CoreAudio.kAudioHardwareUnspecifiedError, fourcc(b"what"))
        self.assertEqual(CoreAudio.kAudioHardwareUnknownPropertyError, fourcc(b"who?"))
        self.assertEqual(CoreAudio.kAudioHardwareBadPropertySizeError, fourcc(b"!siz"))
        self.assertEqual(CoreAudio.kAudioHardwareIllegalOperationError, fourcc(b"nope"))
        self.assertEqual(CoreAudio.kAudioHardwareBadObjectError, fourcc(b"!obj"))
        self.assertEqual(CoreAudio.kAudioHardwareBadDeviceError, fourcc(b"!dev"))
        self.assertEqual(CoreAudio.kAudioHardwareBadStreamError, fourcc(b"!str"))
        self.assertEqual(
            CoreAudio.kAudioHardwareUnsupportedOperationError, fourcc(b"unop")
        )
        self.assertEqual(CoreAudio.kAudioHardwareNotReadyError, fourcc(b"nrdy"))
        self.assertEqual(CoreAudio.kAudioDeviceUnsupportedFormatError, fourcc(b"!dat"))
        self.assertEqual(CoreAudio.kAudioDevicePermissionsError, fourcc(b"!hog"))

        self.assertEqual(CoreAudio.kAudioObjectPropertyScopeGlobal, fourcc(b"glob"))
        self.assertEqual(CoreAudio.kAudioObjectPropertyScopeInput, fourcc(b"inpt"))
        self.assertEqual(CoreAudio.kAudioObjectPropertyScopeOutput, fourcc(b"outp"))
        self.assertEqual(
            CoreAudio.kAudioObjectPropertyScopePlayThrough, fourcc(b"ptru")
        )
        self.assertEqual(CoreAudio.kAudioObjectPropertyElementMaster, 0)
        self.assertEqual(CoreAudio.kAudioObjectPropertyElementMain, 0)

        self.assertEqual(
            CoreAudio.kAudioObjectPropertySelectorWildcard, fourcc(b"****")
        )

        self.assertEqual(CoreAudio.kAudioObjectPropertyScopeWildcard, fourcc(b"****"))

        self.assertEqual(CoreAudio.kAudioObjectPropertyElementWildcard, 0xFFFFFFFF)

        self.assertEqual(CoreAudio.kAudioObjectClassIDWildcard, fourcc(b"****"))

        self.assertEqual(CoreAudio.kAudioObjectClassID, fourcc(b"aobj"))

        self.assertEqual(CoreAudio.kAudioObjectPropertyBaseClass, fourcc(b"bcls"))
        self.assertEqual(CoreAudio.kAudioObjectPropertyClass, fourcc(b"clas"))
        self.assertEqual(CoreAudio.kAudioObjectPropertyOwner, fourcc(b"stdv"))
        self.assertEqual(CoreAudio.kAudioObjectPropertyName, fourcc(b"lnam"))
        self.assertEqual(CoreAudio.kAudioObjectPropertyModelName, fourcc(b"lmod"))
        self.assertEqual(CoreAudio.kAudioObjectPropertyManufacturer, fourcc(b"lmak"))
        self.assertEqual(CoreAudio.kAudioObjectPropertyElementName, fourcc(b"lchn"))
        self.assertEqual(
            CoreAudio.kAudioObjectPropertyElementCategoryName, fourcc(b"lccn")
        )
        self.assertEqual(
            CoreAudio.kAudioObjectPropertyElementNumberName, fourcc(b"lcnn")
        )
        self.assertEqual(CoreAudio.kAudioObjectPropertyOwnedObjects, fourcc(b"ownd"))
        self.assertEqual(CoreAudio.kAudioObjectPropertyIdentify, fourcc(b"iden"))
        self.assertEqual(CoreAudio.kAudioObjectPropertySerialNumber, fourcc(b"snum"))
        self.assertEqual(CoreAudio.kAudioObjectPropertyFirmwareVersion, fourcc(b"fwvn"))

        self.assertEqual(CoreAudio.kAudioPlugInClassID, fourcc(b"aplg"))

        self.assertEqual(CoreAudio.kAudioPlugInPropertyBundleID, fourcc(b"piid"))
        self.assertEqual(CoreAudio.kAudioPlugInPropertyDeviceList, fourcc(b"dev#"))
        self.assertEqual(
            CoreAudio.kAudioPlugInPropertyTranslateUIDToDevice, fourcc(b"uidd")
        )
        self.assertEqual(CoreAudio.kAudioPlugInPropertyBoxList, fourcc(b"box#"))
        self.assertEqual(
            CoreAudio.kAudioPlugInPropertyTranslateUIDToBox, fourcc(b"uidb")
        )
        self.assertEqual(CoreAudio.kAudioPlugInPropertyClockDeviceList, fourcc(b"clk#"))
        self.assertEqual(
            CoreAudio.kAudioPlugInPropertyTranslateUIDToClockDevice, fourcc(b"uidc")
        )

        self.assertEqual(CoreAudio.kAudioTransportManagerClassID, fourcc(b"trpm"))

        self.assertEqual(
            CoreAudio.kAudioTransportManagerPropertyEndPointList, fourcc(b"end#")
        )
        self.assertEqual(
            CoreAudio.kAudioTransportManagerPropertyTranslateUIDToEndPoint,
            fourcc(b"uide"),
        )
        self.assertEqual(
            CoreAudio.kAudioTransportManagerPropertyTransportType, fourcc(b"tran")
        )

        self.assertEqual(CoreAudio.kAudioBoxClassID, fourcc(b"abox"))

        self.assertEqual(CoreAudio.kAudioBoxPropertyBoxUID, fourcc(b"buid"))
        self.assertEqual(CoreAudio.kAudioBoxPropertyTransportType, fourcc(b"tran"))
        self.assertEqual(CoreAudio.kAudioBoxPropertyHasAudio, fourcc(b"bhau"))
        self.assertEqual(CoreAudio.kAudioBoxPropertyHasVideo, fourcc(b"bhvi"))
        self.assertEqual(CoreAudio.kAudioBoxPropertyHasMIDI, fourcc(b"bhmi"))
        self.assertEqual(CoreAudio.kAudioBoxPropertyIsProtected, fourcc(b"bpro"))
        self.assertEqual(CoreAudio.kAudioBoxPropertyAcquired, fourcc(b"bxon"))
        self.assertEqual(CoreAudio.kAudioBoxPropertyAcquisitionFailed, fourcc(b"bxof"))
        self.assertEqual(CoreAudio.kAudioBoxPropertyDeviceList, fourcc(b"bdv#"))
        self.assertEqual(CoreAudio.kAudioBoxPropertyClockDeviceList, fourcc(b"bcl#"))

        self.assertEqual(CoreAudio.kAudioDeviceTransportTypeUnknown, 0)
        self.assertEqual(CoreAudio.kAudioDeviceTransportTypeBuiltIn, fourcc(b"bltn"))
        self.assertEqual(CoreAudio.kAudioDeviceTransportTypeAggregate, fourcc(b"grup"))
        self.assertEqual(CoreAudio.kAudioDeviceTransportTypeVirtual, fourcc(b"virt"))
        self.assertEqual(CoreAudio.kAudioDeviceTransportTypePCI, fourcc(b"pci "))
        self.assertEqual(CoreAudio.kAudioDeviceTransportTypeUSB, fourcc(b"usb "))
        self.assertEqual(CoreAudio.kAudioDeviceTransportTypeFireWire, fourcc(b"1394"))
        self.assertEqual(CoreAudio.kAudioDeviceTransportTypeBluetooth, fourcc(b"blue"))
        self.assertEqual(
            CoreAudio.kAudioDeviceTransportTypeBluetoothLE, fourcc(b"blea")
        )
        self.assertEqual(CoreAudio.kAudioDeviceTransportTypeHDMI, fourcc(b"hdmi"))
        self.assertEqual(
            CoreAudio.kAudioDeviceTransportTypeDisplayPort, fourcc(b"dprt")
        )
        self.assertEqual(CoreAudio.kAudioDeviceTransportTypeAirPlay, fourcc(b"airp"))
        self.assertEqual(CoreAudio.kAudioDeviceTransportTypeAVB, fourcc(b"eavb"))
        self.assertEqual(
            CoreAudio.kAudioDeviceTransportTypeThunderbolt, fourcc(b"thun")
        )

        self.assertEqual(
            CoreAudio.kAudioDevicePropertyConfigurationApplication, fourcc(b"capp")
        )
        self.assertEqual(CoreAudio.kAudioDevicePropertyDeviceUID, fourcc(b"uid "))
        self.assertEqual(CoreAudio.kAudioDevicePropertyModelUID, fourcc(b"muid"))
        self.assertEqual(CoreAudio.kAudioDevicePropertyTransportType, fourcc(b"tran"))
        self.assertEqual(CoreAudio.kAudioDevicePropertyRelatedDevices, fourcc(b"akin"))
        self.assertEqual(CoreAudio.kAudioDevicePropertyClockDomain, fourcc(b"clkd"))
        self.assertEqual(CoreAudio.kAudioDevicePropertyDeviceIsAlive, fourcc(b"livn"))
        self.assertEqual(CoreAudio.kAudioDevicePropertyDeviceIsRunning, fourcc(b"goin"))
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyDeviceCanBeDefaultDevice, fourcc(b"dflt")
        )
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyDeviceCanBeDefaultSystemDevice,
            fourcc(b"sflt"),
        )
        self.assertEqual(CoreAudio.kAudioDevicePropertyLatency, fourcc(b"ltnc"))
        self.assertEqual(CoreAudio.kAudioDevicePropertyStreams, fourcc(b"stm#"))
        self.assertEqual(CoreAudio.kAudioObjectPropertyControlList, fourcc(b"ctrl"))
        self.assertEqual(CoreAudio.kAudioDevicePropertySafetyOffset, fourcc(b"saft"))
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyNominalSampleRate, fourcc(b"nsrt")
        )
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyAvailableNominalSampleRates, fourcc(b"nsr#")
        )
        self.assertEqual(CoreAudio.kAudioDevicePropertyIcon, fourcc(b"icon"))
        self.assertEqual(CoreAudio.kAudioDevicePropertyIsHidden, fourcc(b"hidn"))
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyPreferredChannelsForStereo, fourcc(b"dch2")
        )
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyPreferredChannelLayout, fourcc(b"srnd")
        )

        self.assertEqual(CoreAudio.kAudioClockDeviceClassID, fourcc(b"aclk"))

        self.assertEqual(CoreAudio.kAudioClockDevicePropertyDeviceUID, fourcc(b"cuid"))
        self.assertEqual(
            CoreAudio.kAudioClockDevicePropertyTransportType, fourcc(b"tran")
        )
        self.assertEqual(
            CoreAudio.kAudioClockDevicePropertyClockDomain, fourcc(b"clkd")
        )
        self.assertEqual(
            CoreAudio.kAudioClockDevicePropertyDeviceIsAlive, fourcc(b"livn")
        )
        self.assertEqual(
            CoreAudio.kAudioClockDevicePropertyDeviceIsRunning, fourcc(b"goin")
        )
        self.assertEqual(CoreAudio.kAudioClockDevicePropertyLatency, fourcc(b"ltnc"))
        self.assertEqual(
            CoreAudio.kAudioClockDevicePropertyControlList, fourcc(b"ctrl")
        )
        self.assertEqual(
            CoreAudio.kAudioClockDevicePropertyNominalSampleRate, fourcc(b"nsrt")
        )
        self.assertEqual(
            CoreAudio.kAudioClockDevicePropertyAvailableNominalSampleRates,
            fourcc(b"nsr#"),
        )

        self.assertEqual(CoreAudio.kAudioEndPointDeviceClassID, fourcc(b"edev"))

        self.assertEqual(CoreAudio.kAudioEndPointDeviceUIDKey, b"uid")
        self.assertEqual(CoreAudio.kAudioEndPointDeviceNameKey, b"name")
        self.assertEqual(CoreAudio.kAudioEndPointDeviceEndPointListKey, b"endpoints")
        self.assertEqual(CoreAudio.kAudioEndPointDeviceMasterEndPointKey, b"master")
        self.assertEqual(CoreAudio.kAudioEndPointDeviceIsPrivateKey, b"private")

        self.assertEqual(
            CoreAudio.kAudioEndPointDevicePropertyComposition, fourcc(b"acom")
        )
        self.assertEqual(
            CoreAudio.kAudioEndPointDevicePropertyEndPointList, fourcc(b"agrp")
        )
        self.assertEqual(
            CoreAudio.kAudioEndPointDevicePropertyIsPrivate, fourcc(b"priv")
        )

        self.assertEqual(CoreAudio.kAudioEndPointClassID, fourcc(b"endp"))

        self.assertEqual(CoreAudio.kAudioEndPointUIDKey, b"uid")
        self.assertEqual(CoreAudio.kAudioEndPointNameKey, b"name")
        self.assertEqual(CoreAudio.kAudioEndPointInputChannelsKey, b"channels-in")
        self.assertEqual(CoreAudio.kAudioEndPointOutputChannelsKey, b"channels-out")

        self.assertEqual(CoreAudio.kAudioStreamClassID, fourcc(b"astr"))

        self.assertEqual(CoreAudio.kAudioStreamTerminalTypeUnknown, 0)
        self.assertEqual(CoreAudio.kAudioStreamTerminalTypeLine, fourcc(b"line"))
        self.assertEqual(
            CoreAudio.kAudioStreamTerminalTypeDigitalAudioInterface, fourcc(b"spdf")
        )
        self.assertEqual(CoreAudio.kAudioStreamTerminalTypeSpeaker, fourcc(b"spkr"))
        self.assertEqual(CoreAudio.kAudioStreamTerminalTypeHeadphones, fourcc(b"hdph"))
        self.assertEqual(CoreAudio.kAudioStreamTerminalTypeLFESpeaker, fourcc(b"lfes"))
        self.assertEqual(
            CoreAudio.kAudioStreamTerminalTypeReceiverSpeaker, fourcc(b"rspk")
        )
        self.assertEqual(CoreAudio.kAudioStreamTerminalTypeMicrophone, fourcc(b"micr"))
        self.assertEqual(
            CoreAudio.kAudioStreamTerminalTypeHeadsetMicrophone, fourcc(b"hmic")
        )
        self.assertEqual(
            CoreAudio.kAudioStreamTerminalTypeReceiverMicrophone, fourcc(b"rmic")
        )
        self.assertEqual(CoreAudio.kAudioStreamTerminalTypeTTY, fourcc(b"tty_"))
        self.assertEqual(CoreAudio.kAudioStreamTerminalTypeHDMI, fourcc(b"hdmi"))
        self.assertEqual(CoreAudio.kAudioStreamTerminalTypeDisplayPort, fourcc(b"dprt"))

        self.assertEqual(CoreAudio.kAudioStreamPropertyIsActive, fourcc(b"sact"))
        self.assertEqual(CoreAudio.kAudioStreamPropertyDirection, fourcc(b"sdir"))
        self.assertEqual(CoreAudio.kAudioStreamPropertyTerminalType, fourcc(b"term"))
        self.assertEqual(CoreAudio.kAudioStreamPropertyStartingChannel, fourcc(b"schn"))
        self.assertEqual(
            CoreAudio.kAudioStreamPropertyLatency, CoreAudio.kAudioDevicePropertyLatency
        )
        self.assertEqual(CoreAudio.kAudioStreamPropertyVirtualFormat, fourcc(b"sfmt"))
        self.assertEqual(
            CoreAudio.kAudioStreamPropertyAvailableVirtualFormats, fourcc(b"sfma")
        )
        self.assertEqual(CoreAudio.kAudioStreamPropertyPhysicalFormat, fourcc(b"pft "))
        self.assertEqual(
            CoreAudio.kAudioStreamPropertyAvailablePhysicalFormats, fourcc(b"pfta")
        )

        self.assertEqual(CoreAudio.kAudioControlClassID, fourcc(b"actl"))

        self.assertEqual(CoreAudio.kAudioControlPropertyScope, fourcc(b"cscp"))
        self.assertEqual(CoreAudio.kAudioControlPropertyElement, fourcc(b"celm"))

        self.assertEqual(CoreAudio.kAudioSliderControlClassID, fourcc(b"sldr"))

        self.assertEqual(CoreAudio.kAudioSliderControlPropertyValue, fourcc(b"sdrv"))
        self.assertEqual(CoreAudio.kAudioSliderControlPropertyRange, fourcc(b"sdrr"))

        self.assertEqual(CoreAudio.kAudioLevelControlClassID, fourcc(b"levl"))
        self.assertEqual(CoreAudio.kAudioVolumeControlClassID, fourcc(b"vlme"))
        self.assertEqual(CoreAudio.kAudioLFEVolumeControlClassID, fourcc(b"subv"))

        self.assertEqual(
            CoreAudio.kAudioLevelControlPropertyScalarValue, fourcc(b"lcsv")
        )
        self.assertEqual(
            CoreAudio.kAudioLevelControlPropertyDecibelValue, fourcc(b"lcdv")
        )
        self.assertEqual(
            CoreAudio.kAudioLevelControlPropertyDecibelRange, fourcc(b"lcdr")
        )
        self.assertEqual(
            CoreAudio.kAudioLevelControlPropertyConvertScalarToDecibels, fourcc(b"lcsd")
        )
        self.assertEqual(
            CoreAudio.kAudioLevelControlPropertyConvertDecibelsToScalar, fourcc(b"lcds")
        )

        self.assertEqual(CoreAudio.kAudioBooleanControlClassID, fourcc(b"togl"))
        self.assertEqual(CoreAudio.kAudioMuteControlClassID, fourcc(b"mute"))
        self.assertEqual(CoreAudio.kAudioSoloControlClassID, fourcc(b"solo"))
        self.assertEqual(CoreAudio.kAudioJackControlClassID, fourcc(b"jack"))
        self.assertEqual(CoreAudio.kAudioLFEMuteControlClassID, fourcc(b"subm"))
        self.assertEqual(CoreAudio.kAudioPhantomPowerControlClassID, fourcc(b"phan"))
        self.assertEqual(CoreAudio.kAudioPhaseInvertControlClassID, fourcc(b"phsi"))
        self.assertEqual(CoreAudio.kAudioClipLightControlClassID, fourcc(b"clip"))
        self.assertEqual(CoreAudio.kAudioTalkbackControlClassID, fourcc(b"talb"))
        self.assertEqual(CoreAudio.kAudioListenbackControlClassID, fourcc(b"lsnb"))

        self.assertEqual(CoreAudio.kAudioBooleanControlPropertyValue, fourcc(b"bcvl"))

        self.assertEqual(CoreAudio.kAudioSelectorControlClassID, fourcc(b"slct"))
        self.assertEqual(CoreAudio.kAudioDataSourceControlClassID, fourcc(b"dsrc"))
        self.assertEqual(CoreAudio.kAudioDataDestinationControlClassID, fourcc(b"dest"))
        self.assertEqual(CoreAudio.kAudioClockSourceControlClassID, fourcc(b"clck"))
        self.assertEqual(CoreAudio.kAudioLineLevelControlClassID, fourcc(b"nlvl"))
        self.assertEqual(CoreAudio.kAudioHighPassFilterControlClassID, fourcc(b"hipf"))

        self.assertEqual(
            CoreAudio.kAudioSelectorControlPropertyCurrentItem, fourcc(b"scci")
        )
        self.assertEqual(
            CoreAudio.kAudioSelectorControlPropertyAvailableItems, fourcc(b"scai")
        )
        self.assertEqual(
            CoreAudio.kAudioSelectorControlPropertyItemName, fourcc(b"scin")
        )
        self.assertEqual(
            CoreAudio.kAudioSelectorControlPropertyItemKind, fourcc(b"clkk")
        )

        self.assertEqual(CoreAudio.kAudioSelectorControlItemKindSpacer, fourcc(b"spcr"))

        self.assertEqual(CoreAudio.kAudioClockSourceItemKindInternal, fourcc(b"int "))

        self.assertEqual(CoreAudio.kAudioStereoPanControlClassID, fourcc(b"span"))

        self.assertEqual(CoreAudio.kAudioStereoPanControlPropertyValue, fourcc(b"spcv"))
        self.assertEqual(
            CoreAudio.kAudioStereoPanControlPropertyPanningChannels, fourcc(b"spcc")
        )
