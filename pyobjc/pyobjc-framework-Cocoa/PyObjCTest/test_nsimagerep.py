
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSImageRep (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSImageRepMatchesDevice, 0)

        self.failUnlessEqual(NSImageRepRegistryChangedNotification, NSImageRepRegistryDidChangeNotification)
        self.failUnlessIsInstance(NSImageRepRegistryDidChangeNotification, unicode)

if __name__ == "__main__":
    main()
