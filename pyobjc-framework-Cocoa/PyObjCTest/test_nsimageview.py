from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSImage (TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(NSImageView.setEditable_, 0)
        self.assertResultIsBOOL(NSImageView.isEditable)
        self.assertArgIsBOOL(NSImageView.setAnimates_, 0)
        self.assertResultIsBOOL(NSImageView.animates)
        self.assertArgIsBOOL(NSImageView.setAllowsCutCopyPaste_, 0)
        self.assertResultIsBOOL(NSImageView.allowsCutCopyPaste)

if __name__ == "__main__":
    main()
