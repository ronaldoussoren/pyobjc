from PyObjCTools.TestSupport import TestCase, min_os_level

import ScreenTime


class TestSTWebHistory(TestCase):
    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertArgIsOut(ScreenTime.STWebHistory.initWithBundleIdentifier_error_, 1)
