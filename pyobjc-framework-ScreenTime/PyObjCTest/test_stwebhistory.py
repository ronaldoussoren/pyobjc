from PyObjCTools.TestSupport import TestCase, min_os_level

import ScreenTime


class TestSTWebHistory(TestCase):
    @min_os_level("10.16")
    def test_methods(self):
        self.assertArgIsOut(ScreenTime.STWebHistory.initWithBundleIdentifier_error_, 1)
