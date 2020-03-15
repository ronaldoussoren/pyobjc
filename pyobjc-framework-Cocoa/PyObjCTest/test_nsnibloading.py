import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSNibLoading(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSBundle.loadNibFile_externalNameTable_withZone_)
        self.assertResultIsBOOL(AppKit.NSBundle.loadNibNamed_owner_)
        self.assertResultIsBOOL(AppKit.NSBundle.loadNibFile_externalNameTable_withZone_)

    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertResultIsBOOL(AppKit.NSBundle.loadNibNamed_owner_topLevelObjects_)
        self.assertArgIsOut(AppKit.NSBundle.loadNibNamed_owner_topLevelObjects_, 2)
