from PyObjCTools.TestSupport import TestCase, min_os_level

import Virtualization


class TestVZLinuxRosettaAbstractSocketCachingOptions(TestCase):
    @min_os_level("14.0")
    def test_methods(self):
        self.assertArgIsOut(
            Virtualization.VZLinuxRosettaAbstractSocketCachingOptions.initWithName_error_,
            1,
        )
