from AppKit import *
from PyObjCTools.TestSupport import *


class TestNSNibLoading (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSBundle.loadNibFile_externalNameTable_withZone_)
        self.assertResultIsBOOL(NSBundle.loadNibNamed_owner_)
        self.assertResultIsBOOL(NSBundle.loadNibFile_externalNameTable_withZone_)

if __name__ == "__main__":
    main()
