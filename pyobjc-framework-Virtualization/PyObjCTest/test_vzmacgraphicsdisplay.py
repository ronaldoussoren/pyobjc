from PyObjCTools.TestSupport import TestCase, min_os_level

import Virtualization


class TestVZMacGraphicsDisplay(TestCase):
    @min_os_level("27.3")
    def test_methods(self):
        self.assertResultIsBOOL(Virtualization.VZMacGraphicsDisplay.isHDREnabled)
