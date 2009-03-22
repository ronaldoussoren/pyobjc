from AppKit import *
from PyObjCTools.TestSupport import *


class TestNSNibLoading (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSBundle.loadNibFile_externalNameTable_withZone_)
        self.failUnlessResultIsBOOL(NSBundle.loadNibNamed_owner_)
        self.failUnlessResultIsBOOL(NSBundle.loadNibFile_externalNameTable_withZone_)

if __name__ == "__main__":
    main()
