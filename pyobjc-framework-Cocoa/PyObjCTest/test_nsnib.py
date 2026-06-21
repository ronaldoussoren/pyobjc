import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSNib(TestCase):
    def test_constants(self):
        self.assertIsInstance(AppKit.NSNibOwner, str)
        self.assertIsInstance(AppKit.NSNibTopLevelObjects, str)

    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSNib.instantiateNibWithOwner_topLevelObjects_)
        self.assertArgIsOut(AppKit.NSNib.instantiateNibWithOwner_topLevelObjects_, 1)

        self.assertResultIsBOOL(AppKit.NSNib.instantiateNibWithExternalNameTable_)

    @min_os_level("10.8")
    def test_methods10_8(self):
        self.assertResultIsBOOL(AppKit.NSNib.instantiateWithOwner_topLevelObjects_)
        self.assertArgIsOut(AppKit.NSNib.instantiateWithOwner_topLevelObjects_, 1)
