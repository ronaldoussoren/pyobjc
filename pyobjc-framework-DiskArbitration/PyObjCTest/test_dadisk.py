from PyObjCTools.TestSupport import *

import DiskArbitration

try:
    unicode
except NameError:
    unicode = str

try:
    long

except NameError:
    long = int

class TestDADisk (TestCase):
    def test_constants(self):
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionVolumeKindKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionVolumeMountableKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionVolumeNameKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionVolumeNetworkKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionVolumePathKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionVolumeUUIDKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaBlockSizeKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaBSDMajorKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaBSDMinorKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaBSDNameKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaBSDUnitKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaContentKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaEjectableKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaIconKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaKindKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaLeafKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaNameKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaPathKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaRemovableKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaSizeKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaTypeKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaUUIDKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaWholeKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMediaWritableKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionDeviceGUIDKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionDeviceInternalKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionDeviceModelKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionDevicePathKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionDeviceProtocolKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionDeviceRevisionKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionDeviceUnitKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionDeviceVendorKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionBusNameKey, unicode)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionBusPathKey, unicode)

    def test_types(self):
        self.assertIsCFType(DiskArbitration.DADiskRef)

    def test_functions(self):
        self.assertIsInstance(DiskArbitration.DADiskGetTypeID(), (int, long))

        self.assertResultIsCFRetained(DiskArbitration.DADiskCreateFromBSDName)
        self.assertArgIsNullTerminated(DiskArbitration.DADiskCreateFromBSDName, 2)
        self.assertArgIsIn(DiskArbitration.DADiskCreateFromBSDName, 2)

        self.assertResultIsCFRetained(DiskArbitration.DADiskCreateFromIOMedia)
        self.assertResultIsCFRetained(DiskArbitration.DADiskCreateFromVolumePath)

        self.assertResultIsNullTerminated(DiskArbitration.DADiskGetBSDName)

        self.assertResultIsCFRetained(DiskArbitration.DADiskCopyDescription)
        self.assertResultIsCFRetained(DiskArbitration.DADiskCopyWholeDisk)



if __name__ == "__main__":
    main()

