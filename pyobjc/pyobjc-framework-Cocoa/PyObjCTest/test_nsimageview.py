from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSImage (TestCase):
    def testMethods(self):
        self.failUnlessArgIsBOOL(NSImageView.setEditable_, 0)
        self.failUnlessResultIsBOOL(NSImageView.isEditable)
        self.failUnlessArgIsBOOL(NSImageView.setAnimates_, 0)
        self.failUnlessResultIsBOOL(NSImageView.animates)
        self.failUnlessArgIsBOOL(NSImageView.setAllowsCutCopyPaste_, 0)
        self.failUnlessResultIsBOOL(NSImageView.allowsCutCopyPaste)

if __name__ == "__main__":
    main()
