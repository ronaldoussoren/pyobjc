from PyObjCTools.TestSupport import *

from AppKit import *


class TestNSPasteboardItem (TestCase):
    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessResultIsBOOL(NSPasteboardItem.setDataProvider_forTypes_)
        self.failUnlessResultIsBOOL(NSPasteboardItem.setData_forType_)
        self.failUnlessResultIsBOOL(NSPasteboardItem.setString_forType_)
        self.failUnlessResultIsBOOL(NSPasteboardItem.setPropertyList_forType_)



if __name__ == "__main__":
    main()
