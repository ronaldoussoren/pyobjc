
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

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessResultIsBOOL(NSImageRep.drawInRect_fromRect_operation_fraction_respectFlipped_hints_)
        self.failUnlessArgHasType(NSImageRep.drawInRect_fromRect_operation_fraction_respectFlipped_hints_,
              0, NSRect.__typestr__)
        self.failUnlessArgHasType(NSImageRep.drawInRect_fromRect_operation_fraction_respectFlipped_hints_,
              1, NSRect.__typestr__)
        self.failUnlessArgIsBOOL(NSImageRep.drawInRect_fromRect_operation_fraction_respectFlipped_hints_, 4)

        self.failUnlessArgHasType(NSImageRep.CGImageForProposedRect_context_hints_, 0,
                'N^' + NSRect.__typestr__)

if __name__ == "__main__":
    main()
