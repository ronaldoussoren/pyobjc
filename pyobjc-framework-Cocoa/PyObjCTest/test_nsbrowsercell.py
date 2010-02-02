from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSBrowserCell (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSBrowserCell.isLeaf)
        self.assertArgIsBOOL(NSBrowserCell.setLeaf_, 0)
        self.assertResultIsBOOL(NSBrowserCell.isLoaded)
        self.assertArgIsBOOL(NSBrowserCell.setLoaded_, 0)

if __name__ == "__main__":
    main()
