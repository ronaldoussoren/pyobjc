from PyObjCTools.TestSupport import *
import AppKit


class TestNSSharingServicePickerToolbarItem(TestCase):
    @min_sdk_level("10.15")
    def test_protocols(self):
        objc.protocolNamed("NSSharingServicePickerToolbarItemDelegate")


if __name__ == "__main__":
    main()
