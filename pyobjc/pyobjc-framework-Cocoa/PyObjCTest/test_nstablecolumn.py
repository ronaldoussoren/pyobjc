
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTableColumn (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSTableColumnNoResizing, 0)
        self.failUnlessEqual(NSTableColumnAutoresizingMask, ( 1 << 0 ))
        self.failUnlessEqual(NSTableColumnUserResizingMask, ( 1 << 1 ))

if __name__ == "__main__":
    main()
