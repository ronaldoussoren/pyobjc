from PyObjCTools.TestSupport import *

import DiscRecording

class TestDRCoreDevice (TestCase):
    @expectedFailure
    def testCFTypes(self):
        self.assertIsCFType(DiscRecording.DRDeviceRef)

    def testConstants(self):
        self.assertIsInstance(DiscRecording.kDRDeviceAppearedNotification, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceDisappearedNotification, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceStatusChangedNotification, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceSupportLevelKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceIORegistryEntryPathKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceVendorNameKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceProductNameKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceFirmwareRevisionKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDevicePhysicalInterconnectKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDevicePhysicalInterconnectLocationKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceWriteCapabilitiesKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceLoadingMechanismCanEjectKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceLoadingMechanismCanInjectKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceLoadingMechanismCanOpenKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceWriteBufferSizeKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceSupportLevelNone, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceSupportLevelUnsupported, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceSupportLevelVendorSupported, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceSupportLevelAppleSupported, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceSupportLevelAppleShipping, unicode)
        self.assertIsInstance(DiscRecording.kDRDevicePhysicalInterconnectATAPI, unicode)
        self.assertIsInstance(DiscRecording.kDRDevicePhysicalInterconnectFibreChannel, unicode)
        self.assertIsInstance(DiscRecording.kDRDevicePhysicalInterconnectFireWire, unicode)
        self.assertIsInstance(DiscRecording.kDRDevicePhysicalInterconnectUSB, unicode)
        self.assertIsInstance(DiscRecording.kDRDevicePhysicalInterconnectSCSI, unicode)
        self.assertIsInstance(DiscRecording.kDRDevicePhysicalInterconnectLocationInternal, unicode)
        self.assertIsInstance(DiscRecording.kDRDevicePhysicalInterconnectLocationExternal, unicode)
        self.assertIsInstance(DiscRecording.kDRDevicePhysicalInterconnectLocationUnknown, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteCDKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteCDRKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteCDRWKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteDVDKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteDVDRKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteDVDRDualLayerKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteDVDRWKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteDVDRWDualLayerKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteDVDRAMKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteDVDPlusRKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteDVDPlusRDoubleLayerKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteDVDPlusRWKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteDVDPlusRWDoubleLayerKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteBDKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteBDRKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteBDREKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteHDDVDKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteHDDVDRKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteHDDVDRDualLayerKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteHDDVDRAMKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteHDDVDRWKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteHDDVDRWDualLayerKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteCDTextKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteIndexPointsKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteISRCKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteCDTAOKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteCDSAOKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteCDRawKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanWriteDVDDAOKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanTestWriteCDKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanTestWriteDVDKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanUnderrunProtectCDKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCanUnderrunProtectDVDKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceIsBusyKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceIsTrayOpenKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMaximumWriteSpeedKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceCurrentWriteSpeedKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaStateKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaInfoKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceBurnSpeedsKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceTrackRefsKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceTrackInfoKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaStateMediaPresent, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaStateInTransition, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaStateNone, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaBSDNameKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaIsBlankKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaIsAppendableKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaIsOverwritableKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaIsErasableKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaIsReservedKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaBlocksOverwritableKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaBlocksFreeKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaBlocksUsedKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaDoubleLayerL0DataZoneBlocksKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTrackCountKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaSessionCountKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaClassKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeKey, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaClassCD, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaClassDVD, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaClassBD, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaClassHDDVD, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaClassUnknown, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeCDROM, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeCDR, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeCDRW, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeDVDROM, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeDVDRAM, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeDVDR, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeDVDRDualLayer, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeDVDRW, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeDVDRWDualLayer, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeDVDPlusR, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeDVDPlusRDoubleLayer, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeDVDPlusRW, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeDVDPlusRWDoubleLayer, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeBDR, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeBDRE, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeBDROM, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeHDDVDROM, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeHDDVDR, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeHDDVDRDualLayer, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeHDDVDRAM, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeHDDVDRW, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeHDDVDRWDualLayer, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceMediaTypeUnknown, unicode)
        self.assertIsInstance(DiscRecording.kDRDeviceBurnSpeedCD1x, float)
        self.assertIsInstance(DiscRecording.kDRDeviceBurnSpeedDVD1x, float)
        self.assertIsInstance(DiscRecording.kDRDeviceBurnSpeedBD1x, float)
        self.assertIsInstance(DiscRecording.kDRDeviceBurnSpeedHDDVD1x, float)
        self.assertIsInstance(DiscRecording.kDRDeviceBurnSpeedMax, float)

    def testFunctions(self):
        self.assertIsInstance(DiscRecording.DRDeviceGetTypeID(), (int, long))

        self.assertResultIsCFRetained(DiscRecording.DRCopyDeviceArray)

        self.assertResultIsCFRetained(DiscRecording.DRDeviceCopyDeviceForBSDName)

        self.assertResultIsCFRetained(DiscRecording.DRDeviceCopyDeviceForIORegistryEntryPath)

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

        self.assertEqual(DiscRecording.DRDeviceKPSForCDXFactor(2.5), 2.5 * DiscRecording.kDRDeviceBurnSpeedCD1x)
        self.assertEqual(DiscRecording.DRDeviceKPSForDVDXFactor(2.5), 2.5 * DiscRecording.kDRDeviceBurnSpeedDVD1x)
        self.assertEqual(DiscRecording.DRDeviceCDXFactorForKPS(2500), math.floor(2500/DiscRecording.kDRDeviceBurnSpeedCD1x + 0.5))
        self.assertEqual(DiscRecording.DRDeviceDVDXFactorForKPS(2500), math.floor(2500/DiscRecording.kDRDeviceBurnSpeedDVD1x + 0.5))

if __name__ == "__main__":
    main()
