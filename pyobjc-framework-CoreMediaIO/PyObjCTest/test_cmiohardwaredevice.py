import CoreMediaIO
from PyObjCTools.TestSupport import TestCase, min_os_level, fourcc
import objc

CMIODeviceGetSMPTETimeProc = b"d^v^Q^Z^I"


class TestCMIOHardwareDevice(TestCase):
    def testStructs(self):
        v = CoreMediaIO.CMIODeviceStreamConfiguration()
        self.assertEqual(v.mNumberStreams, 0)
        self.assertEqual(v.mNumberChannels, None)
        self.assertPickleRoundTrips(v)

        v = CoreMediaIO.CMIODeviceAVCCommand()
        self.assertEqual(v.mCommand, None)
        self.assertEqual(v.mCommandLength, 0)
        self.assertEqual(v.mResponse, None)
        self.assertEqual(v.mResponseLength, 0)
        self.assertEqual(v.mResponseUsed, 0)
        self.assertPickleRoundTrips(v)

        v = CoreMediaIO.CMIODeviceRS422Command()
        self.assertEqual(v.mCommand, None)
        self.assertEqual(v.mCommandLength, 0)
        self.assertEqual(v.mResponse, None)
        self.assertEqual(v.mResponseLength, 0)
        self.assertEqual(v.mResponseUsed, 0)
        self.assertPickleRoundTrips(v)

        v = CoreMediaIO.CMIODeviceSMPTETimeCallback()
        self.assertEqual(v.mGetSMPTETimeProc, None)
        self.assertEqual(v.mRefCon, None)
        self.assertPickleRoundTrips(v)

    def testConstants(self):
        self.assertEqual(CoreMediaIO.kCMIODevicePropertyScopeInput, fourcc(b"inpt"))
        self.assertEqual(CoreMediaIO.kCMIODevicePropertyScopeOutput, fourcc(b"outp"))
        self.assertEqual(
            CoreMediaIO.kCMIODevicePropertyScopePlayThrough, fourcc(b"ptru")
        )
        self.assertEqual(CoreMediaIO.kCMIODeviceClassID, fourcc(b"adev"))
        self.assertEqual(CoreMediaIO.kCMIODeviceUnknown, CoreMediaIO.kCMIOObjectUnknown)

        self.assertEqual(CoreMediaIO.kCMIOAVCDeviceType_Unknown, fourcc(b"unkn"))
        self.assertEqual(CoreMediaIO.kCMIOAVCDeviceType_DV_NTSC, fourcc(b"dvc "))
        self.assertEqual(CoreMediaIO.kCMIOAVCDeviceType_DV_PAL, fourcc(b"dvcp"))
        self.assertEqual(CoreMediaIO.kCMIOAVCDeviceType_DVCPro_NTSC, fourcc(b"dvpn"))
        self.assertEqual(CoreMediaIO.kCMIOAVCDeviceType_DVCPro_PAL, fourcc(b"dvpp"))
        self.assertEqual(CoreMediaIO.kCMIOAVCDeviceType_DVCPro50_NTSC, fourcc(b"dv5n"))
        self.assertEqual(CoreMediaIO.kCMIOAVCDeviceType_DVCPro50_PAL, fourcc(b"dv5p"))
        self.assertEqual(CoreMediaIO.kCMIOAVCDeviceType_DVCPro100_NTSC, fourcc(b"dv1n"))
        self.assertEqual(CoreMediaIO.kCMIOAVCDeviceType_DVCPro100_PAL, fourcc(b"dv1p"))
        self.assertEqual(CoreMediaIO.kCMIOAVCDeviceType_DVCPro100_720p, fourcc(b"dvhp"))
        self.assertEqual(
            CoreMediaIO.kCMIOAVCDeviceType_DVCProHD_1080i50, fourcc(b"dvh5")
        )
        self.assertEqual(
            CoreMediaIO.kCMIOAVCDeviceType_DVCProHD_1080i60, fourcc(b"dvh6")
        )
        self.assertEqual(CoreMediaIO.kCMIOAVCDeviceType_MPEG2, fourcc(b"mpg2"))

        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeSD525_60, 0x00)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeSDL525_60, 0x04)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeHD1125_60, 0x08)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeSD625_50, 0x80)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeSDL625_50, 0x84)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeHD1250_50, 0x88)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeMPEG25Mbps_60, 0x10)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeHDV1_60, 0x10)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeMPEG12Mbps_60, 0x14)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeMPEG6Mbps_60, 0x18)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeMPEG25Mbps_50, 0x90)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeHDV1_50, 0x90)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeMPEG12Mbps_50, 0x94)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeMPEG6Mbps_50, 0x98)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeDVHS, 0x01)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeVHSNTSC, 0x05)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeVHSMPAL, 0x25)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeVHSPAL, 0xA5)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeVHSNPAL, 0xB5)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeVHSSECAM, 0xC5)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeVHSMESECAM, 0xD5)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeSVHS525_60, 0x0D)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeSVHS625_50, 0xED)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalMode8mmNTSC, 0x06)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalMode8mmPAL, 0x86)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeHi8NTSC, 0x0E)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeHi8PAL, 0x8E)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeMicroMV12Mbps_60, 0x24)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeMicroMV6Mbps_60, 0x28)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeMicroMV12Mbps_50, 0xA4)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeMicroMV6Mbps_50, 0xA8)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeAudio, 0x20)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeHDV2_60, 0x1A)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeHDV2_50, 0x9A)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeDVCPro25_625_50, 0xF8)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeDVCPro25_525_60, 0x78)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeDVCPro50_625_50, 0xF4)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeDVCPro50_525_60, 0x74)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeDVCPro100_50, 0xF0)
        self.assertEqual(CoreMediaIO.kCMIODeviceAVCSignalModeDVCPro100_60, 0x70)

        self.assertEqual(CoreMediaIO.kCMIODevicePropertyPlugIn, fourcc(b"plug"))
        self.assertEqual(CoreMediaIO.kCMIODevicePropertyDeviceUID, fourcc(b"uid "))
        self.assertEqual(CoreMediaIO.kCMIODevicePropertyModelUID, fourcc(b"muid"))
        self.assertEqual(CoreMediaIO.kCMIODevicePropertyTransportType, fourcc(b"tran"))
        self.assertEqual(CoreMediaIO.kCMIODevicePropertyDeviceIsAlive, fourcc(b"livn"))
        self.assertEqual(
            CoreMediaIO.kCMIODevicePropertyDeviceHasChanged, fourcc(b"diff")
        )
        self.assertEqual(
            CoreMediaIO.kCMIODevicePropertyDeviceIsRunning, fourcc(b"goin")
        )
        self.assertEqual(
            CoreMediaIO.kCMIODevicePropertyDeviceIsRunningSomewhere, fourcc(b"gone")
        )
        self.assertEqual(
            CoreMediaIO.kCMIODevicePropertyDeviceCanBeDefaultDevice, fourcc(b"dflt")
        )
        self.assertEqual(CoreMediaIO.kCMIODevicePropertyHogMode, fourcc(b"oink"))
        self.assertEqual(CoreMediaIO.kCMIODevicePropertyLatency, fourcc(b"ltnc"))
        self.assertEqual(CoreMediaIO.kCMIODevicePropertyStreams, fourcc(b"stm#"))
        self.assertEqual(
            CoreMediaIO.kCMIODevicePropertyStreamConfiguration, fourcc(b"slay")
        )
        self.assertEqual(CoreMediaIO.kCMIODevicePropertyDeviceMaster, fourcc(b"pmnh"))
        self.assertEqual(CoreMediaIO.kCMIODevicePropertyDeviceControl, fourcc(b"pmnh"))
        self.assertEqual(
            CoreMediaIO.kCMIODevicePropertyExcludeNonDALAccess, fourcc(b"ixna")
        )
        self.assertEqual(
            CoreMediaIO.kCMIODevicePropertyClientSyncDiscontinuity, fourcc(b"pmcs")
        )
        self.assertEqual(
            CoreMediaIO.kCMIODevicePropertySMPTETimeCallback, fourcc(b"pmsc")
        )
        self.assertEqual(
            CoreMediaIO.kCMIODevicePropertyCanProcessAVCCommand, fourcc(b"pmac")
        )
        self.assertEqual(CoreMediaIO.kCMIODevicePropertyAVCDeviceType, fourcc(b"pmat"))
        self.assertEqual(
            CoreMediaIO.kCMIODevicePropertyAVCDeviceSignalMode, fourcc(b"pmsm")
        )
        self.assertEqual(
            CoreMediaIO.kCMIODevicePropertyCanProcessRS422Command, fourcc(b"r422")
        )
        self.assertEqual(
            CoreMediaIO.kCMIODevicePropertyLinkedCoreAudioDeviceUID, fourcc(b"plud")
        )
        self.assertEqual(
            CoreMediaIO.kCMIODevicePropertyVideoDigitizerComponents, fourcc(b"vdig")
        )
        self.assertEqual(
            CoreMediaIO.kCMIODevicePropertySuspendedByUser, fourcc(b"sbyu")
        )
        self.assertEqual(
            CoreMediaIO.kCMIODevicePropertyLinkedAndSyncedCoreAudioDeviceUID,
            fourcc(b"plsd"),
        )
        self.assertEqual(
            CoreMediaIO.kCMIODevicePropertyIIDCInitialUnitSpace, fourcc(b"iuns")
        )
        self.assertEqual(CoreMediaIO.kCMIODevicePropertyIIDCCSRData, fourcc(b"csrd"))
        self.assertEqual(
            CoreMediaIO.kCMIODevicePropertyCanSwitchFrameRatesWithoutFrameDrops,
            fourcc(b"frnd"),
        )
        self.assertEqual(CoreMediaIO.kCMIODevicePropertyLocation, fourcc(b"dloc"))
        self.assertEqual(
            CoreMediaIO.kCMIODevicePropertyDeviceHasStreamingError, fourcc(b"serr")
        )

        self.assertEqual(CoreMediaIO.kCMIODevicePropertyLocationUnknown, 0)
        self.assertEqual(CoreMediaIO.kCMIODevicePropertyLocationBuiltInDisplay, 1)
        self.assertEqual(CoreMediaIO.kCMIODevicePropertyLocationExternalDisplay, 2)
        self.assertEqual(CoreMediaIO.kCMIODevicePropertyLocationExternalDevice, 3)
        self.assertEqual(
            CoreMediaIO.kCMIODevicePropertyLocationExternalWirelessDevice, 4
        )

    @min_os_level("10.7")
    def testFunctions(self):
        CoreMediaIO.CMIODeviceStartStream
        CoreMediaIO.CMIODeviceStopStream

        self.assertNotIsInstance(CoreMediaIO.CMIODeviceProcessAVCCommand, objc.function)
        self.assertNotIsInstance(
            CoreMediaIO.CMIODeviceProcessRS422Command, objc.function
        )
