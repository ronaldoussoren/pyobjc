import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSColorPickerTouchBarItem(TestCase):
    @min_os_level("10.12")
    def test_methods10_12(self):
        self.assertResultIsBOOL(AppKit.NSColorPickerTouchBarItem.showsAlpha)
        self.assertArgIsBOOL(AppKit.NSColorPickerTouchBarItem.setShowsAlpha_, 0)

        self.assertResultIsBOOL(AppKit.NSColorPickerTouchBarItem.isEnabled)
        self.assertArgIsBOOL(AppKit.NSColorPickerTouchBarItem.setEnabled_, 0)
