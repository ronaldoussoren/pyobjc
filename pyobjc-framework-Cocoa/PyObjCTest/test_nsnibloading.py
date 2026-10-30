import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSNibLoading(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSBundle.loadNibFile_externalNameTable_withZone_)
        self.assertResultIsBOOL(AppKit.NSBundle.loadNibNamed_owner_)
        self.assertResultIsBOOL(AppKit.NSBundle.loadNibFile_externalNameTable_withZone_)

        self.assertResultIsBOOL(AppKit.NSBundle.loadNibNamed_owner_topLevelObjects_)
        self.assertArgIsOut(AppKit.NSBundle.loadNibNamed_owner_topLevelObjects_, 2)
