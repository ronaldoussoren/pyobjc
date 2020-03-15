import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSImageRep(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSImageRepMatchesDevice, 0)

        self.assertEqual(
            AppKit.NSImageRepRegistryChangedNotification,
            AppKit.NSImageRepRegistryDidChangeNotification,
        )
        self.assertIsInstance(AppKit.NSImageRepRegistryDidChangeNotification, str)

        self.assertEqual(AppKit.NSImageLayoutDirectionUnspecified, -1)
        self.assertEqual(AppKit.NSImageLayoutDirectionLeftToRight, 2)
        self.assertEqual(AppKit.NSImageLayoutDirectionRightToLeft, 3)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSImageRep.draw)
        self.assertResultIsBOOL(AppKit.NSImageRep.drawAtPoint_)
        self.assertResultIsBOOL(AppKit.NSImageRep.drawInRect_)
        self.assertArgIsBOOL(AppKit.NSImageRep.setAlpha_, 0)
        self.assertResultIsBOOL(AppKit.NSImageRep.hasAlpha)
        self.assertArgIsBOOL(AppKit.NSImageRep.setOpaque_, 0)
        self.assertResultIsBOOL(AppKit.NSImageRep.isOpaque)
        self.assertResultIsBOOL(AppKit.NSImageRep.canInitWithData_)
        self.assertResultIsBOOL(AppKit.NSImageRep.canInitWithPasteboard_)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(
            AppKit.NSImageRep.drawInRect_fromRect_operation_fraction_respectFlipped_hints_
        )
        self.assertArgHasType(
            AppKit.NSImageRep.drawInRect_fromRect_operation_fraction_respectFlipped_hints_,
            0,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            AppKit.NSImageRep.drawInRect_fromRect_operation_fraction_respectFlipped_hints_,
            1,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgIsBOOL(
            AppKit.NSImageRep.drawInRect_fromRect_operation_fraction_respectFlipped_hints_,
            4,
        )

        self.assertArgHasType(
            AppKit.NSImageRep.CGImageForProposedRect_context_hints_,
            0,
            b"N^" + AppKit.NSRect.__typestr__,
        )
