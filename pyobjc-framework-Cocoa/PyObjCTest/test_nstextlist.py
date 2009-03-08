
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTextList (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSTextListPrependEnclosingMarker, 1)

if __name__ == "__main__":
    main()
