
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTableColumn (TestCase):
    def testConstants(self):
        self.assertEqual(NSTableColumnNoResizing, 0)
        self.assertEqual(NSTableColumnAutoresizingMask, ( 1 << 0 ))
        self.assertEqual(NSTableColumnUserResizingMask, ( 1 << 1 ))

    def testMethods(self):
        self.assertArgIsBOOL(NSTableColumn.setEditable_, 0)
        self.assertResultIsBOOL(NSTableColumn.isEditable)
        self.assertArgIsBOOL(NSTableColumn.setResizable_, 0)
        self.assertResultIsBOOL(NSTableColumn.isResizable)

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.assertArgIsBOOL(NSTableColumn.setHidden_, 0)
        self.assertResultIsBOOL(NSTableColumn.isHidden)


if __name__ == "__main__":
    main()
