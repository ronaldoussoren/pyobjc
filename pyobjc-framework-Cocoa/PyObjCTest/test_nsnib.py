import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSNib(TestCase):
    def test_constants(self):
        self.assertIsInstance(AppKit.NSNibOwner, str)
        self.assertIsInstance(AppKit.NSNibTopLevelObjects, str)

    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSNib.instantiateNibWithOwner_topLevelObjects_)
        self.assertArgIsOut(AppKit.NSNib.instantiateNibWithOwner_topLevelObjects_, 1)

        self.assertResultIsBOOL(AppKit.NSNib.instantiateNibWithExternalNameTable_)

        self.assertResultIsBOOL(AppKit.NSNib.instantiateWithOwner_topLevelObjects_)
        self.assertArgIsOut(AppKit.NSNib.instantiateWithOwner_topLevelObjects_, 1)
