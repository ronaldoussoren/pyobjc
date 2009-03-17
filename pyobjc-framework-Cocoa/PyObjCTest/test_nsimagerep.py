
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSImageRep (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSImageRepMatchesDevice, 0)

        self.failUnlessEqual(NSImageRepRegistryChangedNotification, NSImageRepRegistryDidChangeNotification)
        self.failUnlessIsInstance(NSImageRepRegistryDidChangeNotification, unicode)


    def testMethods(self):
        self.failUnlessResultIsBOOL(NSImageRep.draw)
        self.failUnlessResultIsBOOL(NSImageRep.drawAtPoint_)
        self.failUnlessResultIsBOOL(NSImageRep.drawInRect_)
        self.failUnlessArgIsBOOL(NSImageRep.setAlpha_, 0)
        self.failUnlessResultIsBOOL(NSImageRep.hasAlpha)
        self.failUnlessArgIsBOOL(NSImageRep.setOpaque_, 0)
        self.failUnlessResultIsBOOL(NSImageRep.isOpaque)
        self.failUnlessResultIsBOOL(NSImageRep.canInitWithData_)
        self.failUnlessResultIsBOOL(NSImageRep.canInitWithPasteboard_)

if __name__ == "__main__":
    main()
