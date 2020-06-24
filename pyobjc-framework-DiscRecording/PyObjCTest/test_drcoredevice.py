import DiscRecording
from PyObjCTools.TestSupport import TestCase, expectedFailure


class TestDRCoreDevice(TestCase):
    @expectedFailure
    def testCFTypes(self):
        self.assertIsCFType(DiscRecording.DRDeviceRef)

    def testConstants(self):
        self.assertIsInstance(DiscRecording.kDRDeviceAppearedNotification, str)
        self.assertIsInstance(DiscRecording.kDRDeviceDisappearedNotification, str)
        self.assertIsInstance(DiscRecording.kDRDeviceStatusChangedNotification, str)
        self.assertIsInstance(DiscRecording.kDRDeviceSupportLevelKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceIORegistryEntryPathKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceVendorNameKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceProductNameKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceFirmwareRevisionKey, str)
        self.assertIsInstance(DiscRecording.kDRDevicePhysicalInterconnectKey, str)
        self.assertIsInstance(
            DiscRecording.kDRDevicePhysicalInterconnectLocationKey, str
        )
        self.assertIsInstance(DiscRecording.kDRDeviceWriteCapabilitiesKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceLoadingMechanismCanEjectKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceLoadingMechanismCanInjectKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceLoadingMechanismCanOpenKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceWriteBufferSizeKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceSupportLevelNone, str)
        self.assertIsInstance(DiscRecording.kDRDeviceSupportLevelUnsupported, str)
        self.assertIsInstance(DiscRecording.kDRDeviceSupportLevelVendorSupported, str)
        self.assertIsInstance(DiscRecording.kDRDeviceSupportLevelAppleSupported, str)
        self.assertIsInstance(DiscRecording.kDRDeviceSupportLevelAppleShipping, str)
        self.assertIsInstance(DiscRecording.kDRDevicePhysicalInterconnectATAPI, str)
        self.assertIsInstance(
            DiscRecording.kDRDevicePhysicalInterconnectFibreChannel, str
        )
        self.assertIsInstance(DiscRecording.kDRDevicePhysicalInterconnectFireWire, str)
        self.assertIsInstance(DiscRecording.kDRDevicePhysicalInterconnectUSB, str)
        self.assertIsInstance(DiscRecording.kDRDevicePhysicalInterconnectSCSI, str)
        self.assertIsInstance(
            DiscRecording.kDRDevicePhysicalInterconnectLocationInternal, str
        )
        self.assertIsInstance(
            DiscRecording.kDRDevicePhysicalInterconnectLocationExternal, str
        )
        self.assertIsInstance(
            DiscRecording.kDRDevicePhysicalInterconnectLocationUnknown, str
        )
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteCDKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteCDRKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteCDRWKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteDVDKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteDVDRKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteDVDRDualLayerKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteDVDRWKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteDVDRWDualLayerKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteDVDRAMKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteDVDPlusRKey, str)
        self.assertIsInstance(
            DiscRecording.kDRDeviceCanWriteDVDPlusRDoubleLayerKey, str
        )
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteDVDPlusRWKey, str)
        self.assertIsInstance(
            DiscRecording.kDRDeviceCanWriteDVDPlusRWDoubleLayerKey, str
        )
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteBDKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteBDRKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteBDREKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteHDDVDKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteHDDVDRKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteHDDVDRDualLayerKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteHDDVDRAMKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteHDDVDRWKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteHDDVDRWDualLayerKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteCDTextKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteIndexPointsKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteISRCKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteCDTAOKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteCDSAOKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteCDRawKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteDVDDAOKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceCanTestWriteCDKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceCanTestWriteDVDKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceCanUnderrunProtectCDKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceCanUnderrunProtectDVDKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceIsBusyKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceIsTrayOpenKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMaximumWriteSpeedKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceCurrentWriteSpeedKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaStateKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaInfoKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceBurnSpeedsKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceTrackRefsKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceTrackInfoKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaStateMediaPresent, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaStateInTransition, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaStateNone, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaBSDNameKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaIsBlankKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaIsAppendableKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaIsOverwritableKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaIsErasableKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaIsReservedKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaBlocksOverwritableKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaBlocksFreeKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaBlocksUsedKey, str)
        self.assertIsInstance(
            DiscRecording.kDRDeviceMediaDoubleLayerL0DataZoneBlocksKey, str
        )
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTrackCountKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaSessionCountKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaClassKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeKey, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaClassCD, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaClassDVD, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaClassBD, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaClassHDDVD, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaClassUnknown, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeCDROM, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeCDR, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeCDRW, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeDVDROM, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeDVDRAM, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeDVDR, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeDVDRDualLayer, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeDVDRW, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeDVDRWDualLayer, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeDVDPlusR, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeDVDPlusRDoubleLayer, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeDVDPlusRW, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeDVDPlusRWDoubleLayer, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeBDR, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeBDRE, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeBDROM, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeHDDVDROM, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeHDDVDR, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeHDDVDRDualLayer, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeHDDVDRAM, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeHDDVDRW, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeHDDVDRWDualLayer, str)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeUnknown, str)
        self.assertIsInstance(DiscRecording.kDRDeviceBurnSpeedCD1x, float)
        self.assertIsInstance(DiscRecording.kDRDeviceBurnSpeedDVD1x, float)
        self.assertIsInstance(DiscRecording.kDRDeviceBurnSpeedBD1x, float)
        self.assertIsInstance(DiscRecording.kDRDeviceBurnSpeedHDDVD1x, float)
        self.assertIsInstance(DiscRecording.kDRDeviceBurnSpeedMax, float)

    def testFunctions(self):
        self.assertIsInstance(DiscRecording.DRDeviceGetTypeID(), int)

        self.assertResultIsCFRetained(DiscRecording.DRCopyDeviceArray)

        self.assertResultIsCFRetained(DiscRecording.DRDeviceCopyDeviceForBSDName)

        self.assertResultIsCFRetained(
            DiscRecording.DRDeviceCopyDeviceForIORegistryEntryPath
        )

        self.assertResultIsBOOL(DiscRecording.DRDeviceIsValid)

        DiscRecording.DRDeviceOpenTray
        DiscRecording.DRDeviceCloseTray
        DiscRecording.DRDeviceEjectMedia
        DiscRecording.DRDeviceAcquireMediaReservation
        DiscRecording.DRDeviceReleaseMediaReservation
        DiscRecording.DRDeviceAcquireExclusiveAccess
        DiscRecording.DRDeviceReleaseExclusiveAccess

        self.assertResultIsCFRetained(DiscRecording.DRDeviceCopyInfo)

        self.assertResultIsCFRetained(DiscRecording.DRDeviceCopyStatus)

        DiscRecording.DRDeviceKPSForXFactor
        DiscRecording.DRDeviceXFactorForKPS

    def testMacros(self):
        import math

        self.assertEqual(
            DiscRecording.DRDeviceKPSForCDXFactor(2.5),
            2.5 * DiscRecording.kDRDeviceBurnSpeedCD1x,
        )
        self.assertEqual(
            DiscRecording.DRDeviceKPSForDVDXFactor(2.5),
            2.5 * DiscRecording.kDRDeviceBurnSpeedDVD1x,
        )
        self.assertEqual(
            DiscRecording.DRDeviceCDXFactorForKPS(2500),
            math.floor(2500 / DiscRecording.kDRDeviceBurnSpeedCD1x + 0.5),
        )
        self.assertEqual(
            DiscRecording.DRDeviceDVDXFactorForKPS(2500),
            math.floor(2500 / DiscRecording.kDRDeviceBurnSpeedDVD1x + 0.5),
        )
