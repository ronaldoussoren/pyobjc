
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSColorList (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSColorListDidChangeNotification, unicode)

if __name__ == "__main__":
    main()
