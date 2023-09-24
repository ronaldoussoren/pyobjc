from PyObjCTools.TestSupport import TestCase

import Virtualization


class TestVZError(TestCase):
    def test_constants(self):
        self.assertEqual(Virtualization.VZErrorInternal, 1)
        self.assertEqual(Virtualization.VZErrorInvalidVirtualMachineConfiguration, 2)
        self.assertEqual(Virtualization.VZErrorInvalidVirtualMachineState, 3)
        self.assertEqual(Virtualization.VZErrorInvalidVirtualMachineStateTransition, 4)
        self.assertEqual(Virtualization.VZErrorInvalidDiskImage, 5)
        self.assertEqual(Virtualization.VZErrorVirtualMachineLimitExceeded, 6)
        self.assertEqual(Virtualization.VZErrorNetworkError, 7)
        self.assertEqual(Virtualization.VZErrorOutOfDiskSpace, 8)
        self.assertEqual(Virtualization.VZErrorOperationCancelled, 9)
        self.assertEqual(Virtualization.VZErrorNotSupported, 10)
        self.assertEqual(Virtualization.VZErrorSave, 11)
        self.assertEqual(Virtualization.VZErrorRestore, 12)

        self.assertEqual(Virtualization.VZErrorRestoreImageCatalogLoadFailed, 10001)
        self.assertEqual(Virtualization.VZErrorInvalidRestoreImageCatalog, 10002)
        self.assertEqual(Virtualization.VZErrorNoSupportedRestoreImagesInCatalog, 10003)
        self.assertEqual(Virtualization.VZErrorRestoreImageLoadFailed, 10004)
        self.assertEqual(Virtualization.VZErrorInvalidRestoreImage, 10005)
        self.assertEqual(Virtualization.VZErrorInstallationRequiresUpdate, 10006)
        self.assertEqual(Virtualization.VZErrorInstallationFailed, 10007)
        self.assertEqual(
            Virtualization.VZErrorNetworkBlockDeviceNegotiationFailed, 20001
        )
        self.assertEqual(Virtualization.VZErrorNetworkBlockDeviceDisconnected, 20002)
