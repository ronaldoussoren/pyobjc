import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSTintConfiguration(TestCase):
    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertResultIsBOOL(AppKit.NSTintConfiguration.adaptsToUserAccentColor)
