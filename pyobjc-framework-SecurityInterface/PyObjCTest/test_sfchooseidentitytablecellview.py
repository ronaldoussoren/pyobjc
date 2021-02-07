import SecurityInterface
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestSFChooseIdentityTableCellView(TestCase):
    @min_os_level("10.13")
    def test_classes(self):
        SecurityInterface.SFChooseIdentityTableCellView
