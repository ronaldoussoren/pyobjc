
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTextFieldCell (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSTextFieldSquareBezel, 0)
        self.failUnlessEqual(NSTextFieldRoundedBezel, 1)


if __name__ == "__main__":
    main()
