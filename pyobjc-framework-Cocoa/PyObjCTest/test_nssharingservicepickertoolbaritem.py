import AppKit  # noqa: F401
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestNSSharingServicePickerToolbarItem(TestCase):
    @min_sdk_level("10.15")
    def test_protocols(self):
        self.assertProtocolExists("NSSharingServicePickerToolbarItemDelegate")
