from PyObjCTools.TestSupport import TestCase, min_os_level

import Virtualization


class TestVZGenericPlatformConfiguration(TestCase):
    @min_os_level("15.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            Virtualization.VZGenericPlatformConfiguration.isNestedVirtualizationSupported
        )

        self.assertResultIsBOOL(
            Virtualization.VZGenericPlatformConfiguration.isNestedVirtualizationEnabled
        )
        self.assertArgIsBOOL(
            Virtualization.VZGenericPlatformConfiguration.setNestedVirtualizationEnabled_,
            0,
        )
