from PyObjCTools.TestSupport import TestCase, min_os_level

import PencilKit


class TestPKToolPickerInkingItem(TestCase):
    @min_os_level("26.0")
    def test_methods26_0(self):
        self.assertResultIsBOOL(PencilKit.PKToolPickerInkingItem.allowsColorSelection)
        self.assertArgIsBOOL(
            PencilKit.PKToolPickerInkingItem.setAllowsColorSelection_, 0
        )
