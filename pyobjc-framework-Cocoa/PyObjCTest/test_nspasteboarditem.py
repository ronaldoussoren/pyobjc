from PyObjCTools.TestSupport import *

from AppKit import *


class TestNSPasteboardItem (TestCase):
    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(NSPasteboardItem.setDataProvider_forTypes_)
        self.assertResultIsBOOL(NSPasteboardItem.setData_forType_)
        self.assertResultIsBOOL(NSPasteboardItem.setString_forType_)
        self.assertResultIsBOOL(NSPasteboardItem.setPropertyList_forType_)



if __name__ == "__main__":
    main()
