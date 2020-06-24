import DiskArbitration
from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
    os_release,
    expectedFailureIf,
)


class TestDADisk(TestCase):
    @min_os_level("10.10")
    def test_constants(self):
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionVolumeKindKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionVolumeMountableKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionVolumeNameKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionVolumeNetworkKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionVolumePathKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionVolumeUUIDKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaBlockSizeKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaBSDMajorKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaBSDMinorKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaBSDNameKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaBSDUnitKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaContentKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaEjectableKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaIconKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaKindKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaLeafKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaNameKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaPathKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaRemovableKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaSizeKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaTypeKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaUUIDKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaWholeKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaWritableKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionDeviceGUIDKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionDeviceInternalKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionDeviceModelKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionDevicePathKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionDeviceProtocolKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionDeviceRevisionKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionDeviceUnitKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionDeviceVendorKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionBusNameKey, str)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionBusPathKey, str)

    @min_os_level("10.14.14")
    def test_constants10_14_4(self):
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaEncryptedKey, str)
        self.assertIsInstance(
            DiskArbitration.kDADiskDescriptionMediaEncryptionDetailKey, str
        )
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionDeviceTDMLockedKey, str)

    @expectedFailureIf(os_release().rsplit(".", 1)[0] == "10.10")
    @min_os_level("10.10")
    def test_types(self):
        self.assertIsCFType(DiskArbitration.DADiskRef)

    @min_os_level("10.10")
    def test_functions(self):
        self.assertIsInstance(DiskArbitration.DADiskGetTypeID(), int)

        self.assertResultIsCFRetained(DiskArbitration.DADiskCreateFromBSDName)
        self.assertArgIsNullTerminated(DiskArbitration.DADiskCreateFromBSDName, 2)
        self.assertArgIsIn(DiskArbitration.DADiskCreateFromBSDName, 2)

        self.assertResultIsCFRetained(DiskArbitration.DADiskCreateFromIOMedia)
        self.assertResultIsCFRetained(DiskArbitration.DADiskCreateFromVolumePath)

        self.assertResultIsNullTerminated(DiskArbitration.DADiskGetBSDName)

        self.assertResultIsCFRetained(DiskArbitration.DADiskCopyDescription)
        self.assertResultIsCFRetained(DiskArbitration.DADiskCopyWholeDisk)

        DiskArbitration.DADiskCopyIOMedia
