from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSBrowserCell (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSBrowserCell.isLeaf)
        self.failUnlessArgIsBOOL(NSBrowserCell.setLeaf_, 0)
        self.failUnlessResultIsBOOL(NSBrowserCell.isLoaded)
        self.failUnlessArgIsBOOL(NSBrowserCell.setLoaded_, 0)

if __name__ == "__main__":
    main()
