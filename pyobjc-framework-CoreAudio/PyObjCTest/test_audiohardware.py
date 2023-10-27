import CoreAudio
from PyObjCTools.TestSupport import TestCase, min_os_level, fourcc

AudioObjectPropertyListenerProc = (
    b"iIIn^" + CoreAudio.AudioObjectPropertyAddress.__typestr__ + b"^v"
)
AudioObjectPropertyListenerBlock = (
    b"vIn^" + CoreAudio.AudioObjectPropertyAddress.__typestr__
)

AudioDeviceIOProc = (
    b"iIn^"
    + CoreAudio.AudioTimeStamp.__typestr__
    + b"^"
    + CoreAudio.AudioBufferList.__typestr__
    + b"n^"
    + CoreAudio.AudioTimeStamp.__typestr__
    + b"^"
    + CoreAudio.AudioBufferList.__typestr__
    + b"n^"
    + CoreAudio.AudioTimeStamp.__typestr__
    + b"^v"
)

AudioDeviceIOBlock = (
    b"vn^"
    + CoreAudio.AudioTimeStamp.__typestr__
    + b"^"
    + CoreAudio.AudioBufferList.__typestr__
    + b"n^"
    + CoreAudio.AudioTimeStamp.__typestr__
    + b"^"
    + CoreAudio.AudioBufferList.__typestr__
    + b"N^"
    + CoreAudio.AudioTimeStamp.__typestr__
)


class TestAudioHardware(TestCase):
    def testConstants(self):
        self.assertEqual(CoreAudio.kAudioObjectSystemObject, 1)

        self.assertEqual(CoreAudio.kAudioObjectPropertyCreator, fourcc(b"oplg"))
        self.assertEqual(CoreAudio.kAudioObjectPropertyListenerAdded, fourcc(b"lisa"))
        self.assertEqual(CoreAudio.kAudioObjectPropertyListenerRemoved, fourcc(b"lisr"))

        self.assertEqual(CoreAudio.kAudioSystemObjectClassID, fourcc(b"asys"))

        self.assertEqual(CoreAudio.kAudioHardwarePowerHintNone, 0)
        self.assertEqual(CoreAudio.kAudioHardwarePowerHintFavorSavingPower, 1)

        self.assertEqual(CoreAudio.kAudioHardwarePropertyDevices, fourcc(b"dev#"))
        self.assertEqual(
            CoreAudio.kAudioHardwarePropertyDefaultInputDevice, fourcc(b"dIn ")
        )
        self.assertEqual(
            CoreAudio.kAudioHardwarePropertyDefaultOutputDevice, fourcc(b"dOut")
        )
        self.assertEqual(
            CoreAudio.kAudioHardwarePropertyDefaultSystemOutputDevice, fourcc(b"sOut")
        )
        self.assertEqual(
            CoreAudio.kAudioHardwarePropertyTranslateUIDToDevice, fourcc(b"uidd")
        )
        self.assertEqual(
            CoreAudio.kAudioHardwarePropertyMixStereoToMono, fourcc(b"stmo")
        )
        self.assertEqual(CoreAudio.kAudioHardwarePropertyPlugInList, fourcc(b"plg#"))
        self.assertEqual(
            CoreAudio.kAudioHardwarePropertyTranslateBundleIDToPlugIn, fourcc(b"bidp")
        )
        self.assertEqual(
            CoreAudio.kAudioHardwarePropertyTransportManagerList, fourcc(b"tmg#")
        )
        self.assertEqual(
            CoreAudio.kAudioHardwarePropertyTranslateBundleIDToTransportManager,
            fourcc(b"tmbi"),
        )
        self.assertEqual(CoreAudio.kAudioHardwarePropertyBoxList, fourcc(b"box#"))
        self.assertEqual(
            CoreAudio.kAudioHardwarePropertyTranslateUIDToBox, fourcc(b"uidb")
        )
        self.assertEqual(
            CoreAudio.kAudioHardwarePropertyClockDeviceList, fourcc(b"clk#")
        )
        self.assertEqual(
            CoreAudio.kAudioHardwarePropertyTranslateUIDToClockDevice, fourcc(b"uidc")
        )
        self.assertEqual(
            CoreAudio.kAudioHardwarePropertyProcessIsMaster, fourcc(b"mast")
        )
        self.assertEqual(CoreAudio.kAudioHardwarePropertyProcessIsMain, fourcc(b"main"))
        self.assertEqual(
            CoreAudio.kAudioHardwarePropertyIsInitingOrExiting, fourcc(b"inot")
        )
        self.assertEqual(CoreAudio.kAudioHardwarePropertyUserIDChanged, fourcc(b"euid"))
        self.assertEqual(
            CoreAudio.kAudioHardwarePropertyProcessInputMute, fourcc(b"pmin")
        )
        self.assertEqual(
            CoreAudio.kAudioHardwarePropertyProcessIsAudible, fourcc(b"pmut")
        )
        self.assertEqual(
            CoreAudio.kAudioHardwarePropertySleepingIsAllowed, fourcc(b"slep")
        )
        self.assertEqual(
            CoreAudio.kAudioHardwarePropertyUnloadingIsAllowed, fourcc(b"unld")
        )
        self.assertEqual(
            CoreAudio.kAudioHardwarePropertyHogModeIsAllowed, fourcc(b"hogr")
        )
        self.assertEqual(
            CoreAudio.kAudioHardwarePropertyUserSessionIsActiveOrHeadless,
            fourcc(b"user"),
        )
        self.assertEqual(
            CoreAudio.kAudioHardwarePropertyServiceRestarted, fourcc(b"srst")
        )
        self.assertEqual(CoreAudio.kAudioHardwarePropertyPowerHint, fourcc(b"powh"))
        self.assertEqual(
            CoreAudio.kAudioHardwarePropertyProcessObjectList, fourcc(b"prs#")
        )
        self.assertEqual(
            CoreAudio.kAudioHardwarePropertyTranslatePIDToProcessObject, fourcc(b"id2p")
        )
        self.assertEqual(CoreAudio.kAudioHardwarePropertyTapList, fourcc(b"tps#"))
        self.assertEqual(
            CoreAudio.kAudioHardwarePropertyTranslateUIDToTap, fourcc(b"uidt")
        )

        self.assertEqual(CoreAudio.kAudioPlugInCreateAggregateDevice, fourcc(b"cagg"))
        self.assertEqual(CoreAudio.kAudioPlugInDestroyAggregateDevice, fourcc(b"dagg"))

        self.assertEqual(
            CoreAudio.kAudioTransportManagerCreateEndPointDevice, fourcc(b"cdev")
        )
        self.assertEqual(
            CoreAudio.kAudioTransportManagerDestroyEndPointDevice, fourcc(b"ddev")
        )

        self.assertEqual(CoreAudio.kAudioDeviceStartTimeIsInputFlag, 1 << 0)
        self.assertEqual(CoreAudio.kAudioDeviceStartTimeDontConsultDeviceFlag, 1 << 1)
        self.assertEqual(CoreAudio.kAudioDeviceStartTimeDontConsultHALFlag, 1 << 2)

        self.assertEqual(CoreAudio.kAudioDevicePropertyPlugIn, fourcc(b"plug"))
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyDeviceHasChanged, fourcc(b"diff")
        )
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyDeviceIsRunningSomewhere, fourcc(b"gone")
        )
        self.assertEqual(CoreAudio.kAudioDeviceProcessorOverload, fourcc(b"over"))
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyIOStoppedAbnormally, fourcc(b"stpd")
        )
        self.assertEqual(CoreAudio.kAudioDevicePropertyHogMode, fourcc(b"oink"))
        self.assertEqual(CoreAudio.kAudioDevicePropertyBufferFrameSize, fourcc(b"fsiz"))
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyBufferFrameSizeRange, fourcc(b"fsz#")
        )
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyUsesVariableBufferFrameSizes, fourcc(b"vfsz")
        )
        self.assertEqual(CoreAudio.kAudioDevicePropertyIOCycleUsage, fourcc(b"ncyc"))
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyStreamConfiguration, fourcc(b"slay")
        )
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyIOProcStreamUsage, fourcc(b"suse")
        )
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyActualSampleRate, fourcc(b"asrt")
        )
        self.assertEqual(CoreAudio.kAudioDevicePropertyClockDevice, fourcc(b"apcd"))
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyIOThreadOSWorkgroup, fourcc(b"oswg")
        )
        self.assertEqual(CoreAudio.kAudioDevicePropertyProcessMute, fourcc(b"appm"))

        self.assertEqual(CoreAudio.kAudioDevicePropertyJackIsConnected, fourcc(b"jack"))
        self.assertEqual(CoreAudio.kAudioDevicePropertyVolumeScalar, fourcc(b"volm"))
        self.assertEqual(CoreAudio.kAudioDevicePropertyVolumeDecibels, fourcc(b"vold"))
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyVolumeRangeDecibels, fourcc(b"vdb#")
        )
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyVolumeScalarToDecibels, fourcc(b"v2db")
        )
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyVolumeDecibelsToScalar, fourcc(b"db2v")
        )
        self.assertEqual(CoreAudio.kAudioDevicePropertyStereoPan, fourcc(b"span"))
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyStereoPanChannels, fourcc(b"spn#")
        )
        self.assertEqual(CoreAudio.kAudioDevicePropertyMute, fourcc(b"mute"))
        self.assertEqual(CoreAudio.kAudioDevicePropertySolo, fourcc(b"solo"))
        self.assertEqual(CoreAudio.kAudioDevicePropertyPhantomPower, fourcc(b"phan"))
        self.assertEqual(CoreAudio.kAudioDevicePropertyPhaseInvert, fourcc(b"phsi"))
        self.assertEqual(CoreAudio.kAudioDevicePropertyClipLight, fourcc(b"clip"))
        self.assertEqual(CoreAudio.kAudioDevicePropertyTalkback, fourcc(b"talb"))
        self.assertEqual(CoreAudio.kAudioDevicePropertyListenback, fourcc(b"lsnb"))
        self.assertEqual(CoreAudio.kAudioDevicePropertyDataSource, fourcc(b"ssrc"))
        self.assertEqual(CoreAudio.kAudioDevicePropertyDataSources, fourcc(b"ssc#"))
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyDataSourceNameForIDCFString, fourcc(b"lscn")
        )
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyDataSourceKindForID, fourcc(b"ssck")
        )
        self.assertEqual(CoreAudio.kAudioDevicePropertyClockSource, fourcc(b"csrc"))
        self.assertEqual(CoreAudio.kAudioDevicePropertyClockSources, fourcc(b"csc#"))
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyClockSourceNameForIDCFString, fourcc(b"lcsn")
        )
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyClockSourceKindForID, fourcc(b"csck")
        )
        self.assertEqual(CoreAudio.kAudioDevicePropertyPlayThru, fourcc(b"thru"))
        self.assertEqual(CoreAudio.kAudioDevicePropertyPlayThruSolo, fourcc(b"thrs"))
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyPlayThruVolumeScalar, fourcc(b"mvsc")
        )
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyPlayThruVolumeDecibels, fourcc(b"mvdb")
        )
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyPlayThruVolumeRangeDecibels, fourcc(b"mvd#")
        )
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyPlayThruVolumeScalarToDecibels,
            fourcc(b"mv2d"),
        )
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyPlayThruVolumeDecibelsToScalar,
            fourcc(b"mv2s"),
        )
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyPlayThruStereoPan, fourcc(b"mspn")
        )
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyPlayThruStereoPanChannels, fourcc(b"msp#")
        )
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyPlayThruDestination, fourcc(b"mdds")
        )
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyPlayThruDestinations, fourcc(b"mdd#")
        )
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyPlayThruDestinationNameForIDCFString,
            fourcc(b"mddc"),
        )
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyChannelNominalLineLevel, fourcc(b"nlvl")
        )
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyChannelNominalLineLevels, fourcc(b"nlv#")
        )
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyChannelNominalLineLevelNameForIDCFString,
            fourcc(b"lcnl"),
        )
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyHighPassFilterSetting, fourcc(b"hipf")
        )
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyHighPassFilterSettings, fourcc(b"hip#")
        )
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyHighPassFilterSettingNameForIDCFString,
            fourcc(b"hipl"),
        )
        self.assertEqual(CoreAudio.kAudioDevicePropertySubVolumeScalar, fourcc(b"svlm"))
        self.assertEqual(
            CoreAudio.kAudioDevicePropertySubVolumeDecibels, fourcc(b"svld")
        )
        self.assertEqual(
            CoreAudio.kAudioDevicePropertySubVolumeRangeDecibels, fourcc(b"svd#")
        )
        self.assertEqual(
            CoreAudio.kAudioDevicePropertySubVolumeScalarToDecibels, fourcc(b"sv2d")
        )
        self.assertEqual(
            CoreAudio.kAudioDevicePropertySubVolumeDecibelsToScalar, fourcc(b"sd2v")
        )
        self.assertEqual(CoreAudio.kAudioDevicePropertySubMute, fourcc(b"smut"))

        self.assertEqual(
            CoreAudio.kAudioDevicePropertyVoiceActivityDetectionEnable, fourcc(b"vAd+")
        )
        self.assertEqual(
            CoreAudio.kAudioDevicePropertyVoiceActivityDetectionState, fourcc(b"vAdS")
        )

        self.assertEqual(CoreAudio.kAudioAggregateDeviceClassID, fourcc(b"aagg"))

        self.assertEqual(CoreAudio.kAudioAggregateDeviceUIDKey, b"uid")
        self.assertEqual(CoreAudio.kAudioAggregateDeviceNameKey, b"name")
        self.assertEqual(CoreAudio.kAudioAggregateDeviceSubDeviceListKey, b"subdevices")
        self.assertEqual(CoreAudio.kAudioAggregateDeviceMasterSubDeviceKey, b"master")
        self.assertEqual(CoreAudio.kAudioAggregateDeviceMainSubDeviceKey, b"master")
        self.assertEqual(CoreAudio.kAudioAggregateDeviceClockDeviceKey, b"clock")
        self.assertEqual(CoreAudio.kAudioAggregateDeviceIsPrivateKey, b"private")
        self.assertEqual(CoreAudio.kAudioAggregateDeviceIsStackedKey, b"stacked")
        self.assertEqual(CoreAudio.kAudioAggregateDeviceTapListKey, b"taps")
        self.assertEqual(
            CoreAudio.kAudioAggregateDeviceTapAutoStartKey, b"tapautostart"
        )

        self.assertEqual(
            CoreAudio.kAudioAggregateDevicePropertyFullSubDeviceList, fourcc(b"grup")
        )
        self.assertEqual(
            CoreAudio.kAudioAggregateDevicePropertyActiveSubDeviceList, fourcc(b"agrp")
        )
        self.assertEqual(
            CoreAudio.kAudioAggregateDevicePropertyComposition, fourcc(b"acom")
        )
        self.assertEqual(
            CoreAudio.kAudioAggregateDevicePropertyMasterSubDevice, fourcc(b"amst")
        )
        self.assertEqual(
            CoreAudio.kAudioAggregateDevicePropertyMainSubDevice, fourcc(b"amst")
        )
        self.assertEqual(
            CoreAudio.kAudioAggregateDevicePropertyClockDevice, fourcc(b"apcd")
        )
        self.assertEqual(
            CoreAudio.kAudioAggregateDevicePropertyTapList, fourcc(b"tap#")
        )
        self.assertEqual(
            CoreAudio.kAudioAggregateDevicePropertySubTapList, fourcc(b"atap")
        )

        self.assertEqual(CoreAudio.kAudioSubDeviceClassID, fourcc(b"asub"))

        self.assertEqual(CoreAudio.kAudioSubTapClassID, fourcc(b"stap"))
        self.assertEqual(CoreAudio.kAudioSubTapUIDKey, b"uid")
        self.assertEqual(CoreAudio.kAudioSubTapExtraInputLatencyKey, b"latency-in")
        self.assertEqual(CoreAudio.kAudioSubTapExtraOutputLatencyKey, b"latency-out")
        self.assertEqual(CoreAudio.kAudioSubTapDriftCompensationKey, b"drift")
        self.assertEqual(
            CoreAudio.kAudioSubTapDriftCompensationQualityKey, b"drift quality"
        )

        self.assertEqual(CoreAudio.kAudioSubTapPropertyExtraLatency, fourcc(b"xltc"))
        self.assertEqual(
            CoreAudio.kAudioSubTapPropertyDriftCompensation, fourcc(b"drft")
        )
        self.assertEqual(
            CoreAudio.kAudioSubTapPropertyDriftCompensationQuality, fourcc(b"drfq")
        )

        self.assertEqual(CoreAudio.kAudioProcessClassID, fourcc(b"clnt"))

        self.assertEqual(CoreAudio.kAudioSubDeviceDriftCompensationMinQuality, 0)
        self.assertEqual(CoreAudio.kAudioSubDeviceDriftCompensationLowQuality, 0x20)
        self.assertEqual(CoreAudio.kAudioSubDeviceDriftCompensationMediumQuality, 0x40)
        self.assertEqual(CoreAudio.kAudioSubDeviceDriftCompensationHighQuality, 0x60)
        self.assertEqual(CoreAudio.kAudioSubDeviceDriftCompensationMaxQuality, 0x7F)

        self.assertEqual(CoreAudio.kAudioSubDeviceUIDKey, b"uid")
        self.assertEqual(CoreAudio.kAudioSubDeviceNameKey, b"name")
        self.assertEqual(CoreAudio.kAudioSubDeviceInputChannelsKey, b"channels-in")
        self.assertEqual(CoreAudio.kAudioSubDeviceOutputChannelsKey, b"channels-out")
        self.assertEqual(CoreAudio.kAudioSubDeviceExtraInputLatencyKey, b"latency-in")
        self.assertEqual(CoreAudio.kAudioSubDeviceExtraOutputLatencyKey, b"latency-out")
        self.assertEqual(CoreAudio.kAudioSubDeviceDriftCompensationKey, b"drift")
        self.assertEqual(
            CoreAudio.kAudioSubDeviceDriftCompensationQualityKey, b"drift quality"
        )

        self.assertEqual(CoreAudio.kAudioSubDevicePropertyExtraLatency, fourcc(b"xltc"))
        self.assertEqual(
            CoreAudio.kAudioSubDevicePropertyDriftCompensation, fourcc(b"drft")
        )
        self.assertEqual(
            CoreAudio.kAudioSubDevicePropertyDriftCompensationQuality, fourcc(b"drfq")
        )

        self.assertEqual(CoreAudio.kAudioProcessPropertyPID, fourcc(b"ppid"))
        self.assertEqual(CoreAudio.kAudioProcessPropertyBundleID, fourcc(b"pbid"))
        self.assertEqual(CoreAudio.kAudioProcessPropertyDevices, fourcc(b"pdv#"))
        self.assertEqual(CoreAudio.kAudioProcessPropertyIsRunning, fourcc(b"pir?"))
        self.assertEqual(CoreAudio.kAudioProcessPropertyIsRunningInput, fourcc(b"piri"))
        self.assertEqual(
            CoreAudio.kAudioProcessPropertyIsRunningOutput, fourcc(b"piro")
        )

        self.assertEqual(CoreAudio.kAudioTapClassID, fourcc(b"tcls"))

        self.assertEqual(CoreAudio.kAudioTapPropertyUID, fourcc(b"tuid"))
        self.assertEqual(CoreAudio.kAudioTapPropertyDescription, fourcc(b"tdsc"))
        self.assertEqual(CoreAudio.kAudioTapPropertyFormat, fourcc(b"tfmt"))

    def testFunctions(self):
        CoreAudio.AudioObjectShow

        self.assertArgIsIn(CoreAudio.AudioObjectHasProperty, 1)

        self.assertArgIsIn(CoreAudio.AudioObjectIsPropertySettable, 1)
        self.assertArgIsOut(CoreAudio.AudioObjectIsPropertySettable, 2)

        self.assertArgIsIn(CoreAudio.AudioObjectGetPropertyDataSize, 1)
        self.assertArgIsIn(CoreAudio.AudioObjectGetPropertyDataSize, 3)
        self.assertArgSizeInArg(CoreAudio.AudioObjectGetPropertyDataSize, 3, (2, 4))
        self.assertArgIsOut(CoreAudio.AudioObjectGetPropertyDataSize, 4)

        self.assertArgIsIn(CoreAudio.AudioObjectGetPropertyData, 1)
        self.assertArgIsIn(CoreAudio.AudioObjectGetPropertyData, 3)
        self.assertArgSizeInArg(CoreAudio.AudioObjectGetPropertyData, 3, 2)
        self.assertArgIsInOut(CoreAudio.AudioObjectGetPropertyData, 4)
        self.assertArgIsOut(CoreAudio.AudioObjectGetPropertyData, 5)
        self.assertArgSizeInArg(CoreAudio.AudioObjectGetPropertyData, 5, 4)

        self.assertArgIsIn(CoreAudio.AudioObjectSetPropertyData, 1)
        self.assertArgIsIn(CoreAudio.AudioObjectSetPropertyData, 3)
        self.assertArgSizeInArg(CoreAudio.AudioObjectSetPropertyData, 3, 2)
        self.assertArgIsIn(CoreAudio.AudioObjectSetPropertyData, 5)
        self.assertArgSizeInArg(CoreAudio.AudioObjectSetPropertyData, 5, 4)

        self.assertArgIsIn(CoreAudio.AudioObjectAddPropertyListener, 1)
        self.assertArgIsFunction(
            CoreAudio.AudioObjectAddPropertyListener,
            2,
            AudioObjectPropertyListenerProc,
            True,
        )

        self.assertArgIsIn(CoreAudio.AudioObjectRemovePropertyListener, 1)
        self.assertArgIsFunction(
            CoreAudio.AudioObjectRemovePropertyListener,
            2,
            AudioObjectPropertyListenerProc,
            True,
        )

        self.assertArgIsIn(CoreAudio.AudioObjectAddPropertyListenerBlock, 1)
        self.assertArgIsBlock(
            CoreAudio.AudioObjectAddPropertyListenerBlock,
            3,
            AudioObjectPropertyListenerBlock,
        )

        self.assertArgIsIn(CoreAudio.AudioObjectRemovePropertyListenerBlock, 1)
        self.assertArgIsBlock(
            CoreAudio.AudioObjectRemovePropertyListenerBlock,
            3,
            AudioObjectPropertyListenerBlock,
        )

        CoreAudio.AudioHardwareUnload

        self.assertArgIsFunction(
            CoreAudio.AudioDeviceCreateIOProcID, 1, AudioDeviceIOProc, True
        )
        self.assertArgIsOut(CoreAudio.AudioDeviceCreateIOProcID, 3)

        self.assertArgIsOut(CoreAudio.AudioDeviceCreateIOProcIDWithBlock, 0)
        self.assertArgIsBlock(
            CoreAudio.AudioDeviceCreateIOProcIDWithBlock, 3, AudioDeviceIOBlock
        )

        CoreAudio.AudioDeviceDestroyIOProcID
        CoreAudio.AudioDeviceStart
        CoreAudio.AudioDeviceStop

        self.assertArgIsOut(CoreAudio.AudioDeviceGetCurrentTime, 1)

        self.assertArgIsIn(CoreAudio.AudioDeviceTranslateTime, 1)
        self.assertArgIsOut(CoreAudio.AudioDeviceTranslateTime, 2)

        self.assertArgIsInOut(CoreAudio.AudioDeviceGetNearestStartTime, 1)

        self.assertEqual(CoreAudio.kAudioAggregateDriftCompensationMinQuality, 0)
        self.assertEqual(CoreAudio.kAudioAggregateDriftCompensationLowQuality, 0x20)
        self.assertEqual(CoreAudio.kAudioAggregateDriftCompensationMediumQuality, 0x40)
        self.assertEqual(CoreAudio.kAudioAggregateDriftCompensationHighQuality, 0x60)
        self.assertEqual(CoreAudio.kAudioAggregateDriftCompensationMaxQuality, 0x7F)

    @min_os_level("10.11")
    def test_functions10_11(self):
        self.assertArgIsOut(CoreAudio.AudioHardwareCreateAggregateDevice, 1)
        CoreAudio.AudioHardwareDestroyAggregateDevice

    def testStructs(self):
        # XXX: Requires manual support
        v = CoreAudio.AudioHardwareIOProcStreamUsage()
        self.assertEqual(v.mIOProc, None)
        self.assertEqual(v.mNumberStreams, 0)
        self.assertEqual(v.mStreamIsOn, None)
        self.assertPickleRoundTrips(v)
