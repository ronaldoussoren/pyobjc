from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSFormCell (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSFormCell.isOpaque)

if __name__ == "__main__":
    main()
