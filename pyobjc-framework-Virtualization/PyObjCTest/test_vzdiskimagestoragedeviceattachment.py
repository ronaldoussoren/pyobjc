from PyObjCTools.TestSupport import TestCase, min_os_level

import Virtualization


class TestVZDiskImageStorageDeviceAttachment(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Virtualization.VZDiskImageCachingMode)
        self.assertIsEnumType(Virtualization.VZDiskImageSynchronizationMode)

    def test_constants(self):
        self.assertEqual(Virtualization.VZDiskImageSynchronizationModeFull, 1)
        self.assertEqual(Virtualization.VZDiskImageSynchronizationModeFsync, 2)
        self.assertEqual(Virtualization.VZDiskImageSynchronizationModeNone, 3)

        self.assertEqual(Virtualization.VZDiskImageCachingModeAutomatic, 0)
        self.assertEqual(Virtualization.VZDiskImageCachingModeUncached, 1)
        self.assertEqual(Virtualization.VZDiskImageCachingModeCached, 2)

    def test_methods(self):
        self.assertArgIsBOOL(
            Virtualization.VZDiskImageStorageDeviceAttachment.initWithURL_readOnly_error_,
            1,
        )
        self.assertArgIsOut(
            Virtualization.VZDiskImageStorageDeviceAttachment.initWithURL_readOnly_error_,
            2,
        )
        self.assertResultIsBOOL(
            Virtualization.VZDiskImageStorageDeviceAttachment.isReadOnly
        )

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertArgIsBOOL(
            Virtualization.VZDiskImageStorageDeviceAttachment.initWithURL_readOnly_cachingMode_synchronizationMode_error_,
            1,
        )
        self.assertArgIsOut(
            Virtualization.VZDiskImageStorageDeviceAttachment.initWithURL_readOnly_cachingMode_synchronizationMode_error_,
            4,
        )
