from AppKit import *
from PyObjCTools.TestSupport import *


class TestNSNibLoading (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSBundle.loadNibFile_externalNameTable_withZone_)
        self.assertResultIsBOOL(NSBundle.loadNibNamed_owner_)
        self.assertResultIsBOOL(NSBundle.loadNibFile_externalNameTable_withZone_)

    @min_os_level('10.8')
    def testMethods10_8(self):
        self.assertResultIsBOOL(NSBundle.loadNibNamed_owner_topLevelObjects_)
        self.assertArgIsOut(NSBundle.loadNibNamed_owner_topLevelObjects_, 2)


if __name__ == "__main__":
    main()
