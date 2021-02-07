import DiskArbitration
from Foundation import NSArray, NSDictionary
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestDiskArbitration(TestCase):
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

    @min_os_level("10.10")
    def test_constants10_10(self):
        self.assertIsInstance(
            DiskArbitration.kDADiskDescriptionMatchMediaUnformatted, NSDictionary
        )
        self.assertIsInstance(
            DiskArbitration.kDADiskDescriptionMatchMediaWhole, NSDictionary
        )
        self.assertIsInstance(
            DiskArbitration.kDADiskDescriptionMatchVolumeMountable, NSDictionary
        )
        self.assertIsInstance(
            DiskArbitration.kDADiskDescriptionMatchVolumeUnrecognized, NSDictionary
        )
        self.assertIsInstance(
            DiskArbitration.kDADiskDescriptionWatchVolumeName, NSArray
        )
        self.assertIsInstance(
            DiskArbitration.kDADiskDescriptionWatchVolumePath, NSArray
        )

    def test_functions(self):
        # Callbacks, need manual metadata (but from what I've seen so far no C code)
        # XXX: Tests cannot actually call most functions, some of them require admin privileges
        #      and can destroy information. Create separate test scripts that can be used to
        #      perform tests in a VM (with protection against running them accidently!)
        DADiskRef = b"^{__DADisk=}"
        DADissenterRef = b"^{__DADissenter=}"

        self.assertArgIsFunction(
            DiskArbitration.DARegisterDiskAppearedCallback,
            2,
            b"v" + DADiskRef + b"^v",
            True,
        )
        self.assertArgIsFunction(
            DiskArbitration.DARegisterDiskDescriptionChangedCallback,
            3,
            b"v" + DADiskRef + b"^{__CFArray=}^v",
            True,
        )
        self.assertArgIsFunction(
            DiskArbitration.DARegisterDiskDisappearedCallback,
            2,
            b"v" + DADiskRef + b"^v",
            True,
        )
        self.assertArgIsFunction(
            DiskArbitration.DADiskMount,
            3,
            b"v" + DADiskRef + DADissenterRef + b"^v",
            True,
        )

        self.assertArgIsFunction(
            DiskArbitration.DADiskMountWithArguments,
            3,
            b"v" + DADiskRef + DADissenterRef + b"^v",
            True,
        )
        self.assertArgIsIn(DiskArbitration.DADiskMountWithArguments, 4)
        self.assertArgIsNullTerminated(DiskArbitration.DADiskMountWithArguments, 4)

        self.assertArgIsFunction(
            DiskArbitration.DARegisterDiskMountApprovalCallback,
            2,
            DADissenterRef + DADiskRef + b"^v",
            True,
        )
        self.assertArgIsFunction(
            DiskArbitration.DADiskRename,
            3,
            b"v" + DADiskRef + DADissenterRef + b"^v",
            True,
        )
        self.assertArgIsFunction(
            DiskArbitration.DADiskUnmount,
            2,
            b"v" + DADiskRef + DADissenterRef + b"^v",
            True,
        )
        self.assertArgIsFunction(
            DiskArbitration.DARegisterDiskUnmountApprovalCallback,
            2,
            DADissenterRef + DADiskRef + b"^v",
            True,
        )
        self.assertArgIsFunction(
            DiskArbitration.DADiskEject,
            2,
            b"v" + DADiskRef + DADissenterRef + b"^v",
            True,
        )
        self.assertArgIsFunction(
            DiskArbitration.DARegisterDiskEjectApprovalCallback,
            2,
            DADissenterRef + DADiskRef + b"^v",
            True,
        )

        self.assertArgIsFunction(
            DiskArbitration.DADiskClaim, 2, DADissenterRef + DADiskRef + b"^v", True
        )
        self.assertArgIsFunction(
            DiskArbitration.DADiskClaim,
            4,
            b"v" + DADiskRef + DADissenterRef + b"^v",
            True,
        )

        self.assertResultIsBOOL(DiskArbitration.DADiskIsClaimed)
        DiskArbitration.DADiskUnclaim

        self.assertArgIsFunction(
            DiskArbitration.DARegisterDiskPeekCallback,
            3,
            b"v" + DADiskRef + b"^v",
            True,
        )

        DiskArbitration.DADiskGetOptions
        self.assertArgIsBOOL(DiskArbitration.DADiskSetOptions, 2)

        DiskArbitration.DAUnregisterCallback
        DiskArbitration.DAUnregisterApprovalCallback
