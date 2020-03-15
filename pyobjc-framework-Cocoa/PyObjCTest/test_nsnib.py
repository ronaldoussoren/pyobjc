import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSNib(TestCase):
    def testConstants(self):
        self.assertIsInstance(AppKit.NSNibOwner, str)
        self.assertIsInstance(AppKit.NSNibTopLevelObjects, str)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSNib.instantiateNibWithOwner_topLevelObjects_)
        self.assertArgIsOut(AppKit.NSNib.instantiateNibWithOwner_topLevelObjects_, 1)

        self.assertResultIsBOOL(AppKit.NSNib.instantiateNibWithExternalNameTable_)

    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertResultIsBOOL(AppKit.NSNib.instantiateWithOwner_topLevelObjects_)
        self.assertArgIsOut(AppKit.NSNib.instantiateWithOwner_topLevelObjects_, 1)
