
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSSound (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(NSSoundPboardType, unicode)

if __name__ == "__main__":
    main()
