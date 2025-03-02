from PyObjCTools.TestSupport import TestCase, min_os_level

import ScreenTime


class TestSTWebHistory(TestCase):
    def test_constants(self):
        self.assertIsTypedEnum(ScreenTime.STWebHistoryProfileIdentifier, str)

    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertArgIsOut(ScreenTime.STWebHistory.initWithBundleIdentifier_error_, 1)

    @min_os_level("15.4")
    def test_methods15_4(self):
        self.assertArgIsOut(
            ScreenTime.STWebHistory.initWithBundleIdentifier_profileIdentifier_error_, 2
        )
