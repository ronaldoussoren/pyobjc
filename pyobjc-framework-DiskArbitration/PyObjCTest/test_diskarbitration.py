from PyObjCTools.TestSupport import *

import DiskArbitration

from Foundation import NSDictionary, NSArray

class TestDiskArbitration (TestCase):
    def test_constants(self):
        self.assertEqual(DiskArbitration.kDADiskMountOptionDefault, 0)
        self.assertEqual(DiskArbitration.kDADiskMountOptionWhole, 1)
        self.assertEqual(DiskArbitration.kDADiskRenameOptionDefault, 0)
        self.assertEqual(DiskArbitration.kDADiskUnmountOptionDefault, 0x00000000)
        self.assertEqual(DiskArbitration.kDADiskUnmountOptionForce, 0x00080000)
        self.assertEqual(DiskArbitration.kDADiskUnmountOptionWhole, 0x00000001)
        self.assertEqual(DiskArbitration.kDADiskEjectOptionDefault, 0)
        self.assertEqual(DiskArbitration.kDADiskClaimOptionDefault, 0)
        self.assertEqual(DiskArbitration.kDADiskOptionDefault, 0x00000000)
        self.assertEqual(DiskArbitration.kDADiskOptionEjectUponLogout, 0x00000001)
        self.assertEqual(DiskArbitration.kDADiskOptionMountAutomatic, 0x00000010)
        self.assertEqual(DiskArbitration.kDADiskOptionMountAutomaticNoDefer, 0x00000020)
        self.assertEqual(DiskArbitration.kDADiskOptionPrivate, 0x00000100)

        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMatchMediaUnformatted, NSDictionary)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMatchMediaWhole, NSDictionary)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMatchVolumeMountable, NSDictionary)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionMatchVolumeUnrecognized, NSDictionary)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionWatchVolumeName, NSArray)
        self.assertIsInstance(DiskArbitration.kDADiskDescriptionWatchVolumePath, NSArray)

    def test_functions(self):
        # Callbacks, need manual metadata (but from what I've seen so far no C code)
        # XXX: Tests cannot actually call most functions, some of them require admin privileges
        #      and can destroy information. Create separate test scripts that can be used to
        #      perform tests in a VM (with protection against running them accidently!)
        self.fail('DARegisterDiskAppearedCallback')
        self.fail('DARegisterDiskDescriptionChangedCallback')
        self.fail('...')

if __name__ == "__main__":
    main()
