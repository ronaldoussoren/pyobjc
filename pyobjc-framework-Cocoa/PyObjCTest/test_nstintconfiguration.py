import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSTintConfiguration(TestCase):
    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertResultIsBOOL(AppKit.NSTintConfiguration.adaptsToUserAccentColor)
