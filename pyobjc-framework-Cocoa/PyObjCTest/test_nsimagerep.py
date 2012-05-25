
from PyObjCTools.TestSupport import *
from AppKit import *

try:
    unicode
except NameError:
    unicode = str

class TestNSImageRep (TestCase):
    def testConstants(self):
        self.assertEqual(NSImageRepMatchesDevice, 0)

        self.assertEqual(NSImageRepRegistryChangedNotification, NSImageRepRegistryDidChangeNotification)
        self.assertIsInstance(NSImageRepRegistryDidChangeNotification, unicode)


    def testMethods(self):
        self.assertResultIsBOOL(NSImageRep.draw)
        self.assertResultIsBOOL(NSImageRep.drawAtPoint_)
        self.assertResultIsBOOL(NSImageRep.drawInRect_)
        self.assertArgIsBOOL(NSImageRep.setAlpha_, 0)
        self.assertResultIsBOOL(NSImageRep.hasAlpha)
        self.assertArgIsBOOL(NSImageRep.setOpaque_, 0)
        self.assertResultIsBOOL(NSImageRep.isOpaque)
        self.assertResultIsBOOL(NSImageRep.canInitWithData_)
        self.assertResultIsBOOL(NSImageRep.canInitWithPasteboard_)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(NSImageRep.drawInRect_fromRect_operation_fraction_respectFlipped_hints_)
        self.assertArgHasType(NSImageRep.drawInRect_fromRect_operation_fraction_respectFlipped_hints_,
              0, NSRect.__typestr__)
        self.assertArgHasType(NSImageRep.drawInRect_fromRect_operation_fraction_respectFlipped_hints_,
              1, NSRect.__typestr__)
        self.assertArgIsBOOL(NSImageRep.drawInRect_fromRect_operation_fraction_respectFlipped_hints_, 4)

        self.assertArgHasType(NSImageRep.CGImageForProposedRect_context_hints_, 0,
                b'N^' + NSRect.__typestr__)

if __name__ == "__main__":
    main()
