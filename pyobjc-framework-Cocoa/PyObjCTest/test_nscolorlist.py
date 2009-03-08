
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSColorList (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(NSColorListDidChangeNotification, unicode)

if __name__ == "__main__":
    main()
