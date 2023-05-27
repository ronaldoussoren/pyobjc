from PyObjCTools.TestSupport import TestCase, min_os_level, arch_only

import Virtualization


class TestVZLinuxRosettaDirectoryShare(TestCase):
    def test_constants(self):
        self.assertIsEnumType(Virtualization.VZLinuxRosettaAvailability)
        self.assertEqual(Virtualization.VZLinuxRosettaAvailabilityNotSupported, 0)
        self.assertEqual(Virtualization.VZLinuxRosettaAvailabilityNotInstalled, 1)
        self.assertEqual(Virtualization.VZLinuxRosettaAvailabilityInstalled, 2)

    @min_os_level("13.0")
    @arch_only("arm64")
    def test_methods13_0(self):
        self.assertArgIsOut(
            Virtualization.VZLinuxRosettaDirectoryShare.initWithError_, 0
        )
        self.assertArgIsBlock(
            Virtualization.VZLinuxRosettaDirectoryShare.installRosettaWithCompletionHandler_,
            0,
            b"v@",
        )
