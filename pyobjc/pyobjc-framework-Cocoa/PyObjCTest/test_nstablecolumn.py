
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTableColumn (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSTableColumnNoResizing, 0)
        self.failUnlessEqual(NSTableColumnAutoresizingMask, ( 1 << 0 ))
        self.failUnlessEqual(NSTableColumnUserResizingMask, ( 1 << 1 ))

    def testMethods(self):
        self.failUnlessArgIsBOOL(NSTableColumn.setEditable_, 0)
        self.failUnlessResultIsBOOL(NSTableColumn.isEditable)
        self.failUnlessArgIsBOOL(NSTableColumn.setResizable_, 0)
        self.failUnlessResultIsBOOL(NSTableColumn.isResizable)

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.failUnlessArgIsBOOL(NSTableColumn.setHidden_, 0)
        self.failUnlessResultIsBOOL(NSTableColumn.isHidden)


if __name__ == "__main__":
    main()
