from PyObjCTools.TestSupport import *

import AppKit

try:
    unicode
except NameError:
    unicode = str

class PopoverHelper (AppKit.NSObject):
    def popoverShouldClose_(self, a): return 1

class TestNSPopover (TestCase):
    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertEqual(AppKit.NSPopoverAppearanceMinimal, 0)
        self.assertEqual(AppKit.NSPopoverAppearanceHUD, 1)

        self.assertEqual(AppKit.NSPopoverBehaviorApplicationDefined, 0)
        self.assertEqual(AppKit.NSPopoverBehaviorTransient, 1)
        self.assertEqual(AppKit.NSPopoverBehaviorSemitransient, 2)

        self.assertIsInstance(AppKit.NSPopoverCloseReasonKey, unicode)
        self.assertIsInstance(AppKit.NSPopoverCloseReasonStandard, unicode)
        self.assertIsInstance(AppKit.NSPopoverCloseReasonDetachToWindow, unicode)
        self.assertIsInstance(AppKit.NSPopoverWillShowNotification, unicode)
        self.assertIsInstance(AppKit.NSPopoverDidShowNotification, unicode)
        self.assertIsInstance(AppKit.NSPopoverWillCloseNotification, unicode)
        self.assertIsInstance(AppKit.NSPopoverDidCloseNotification, unicode)

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertResultIsBOOL(AppKit.NSPopover.animates)
        self.assertArgIsBOOL(AppKit.NSPopover.setAnimates_, 0)

        self.assertResultIsBOOL(AppKit.NSPopover.isShown)
        self.assertArgIsBOOL(AppKit.NSPopover.setShown_, 0)

        self.assertArgHasType(AppKit.NSPopover.showRelativeToRect_ofView_preferredEdge_, 0, AppKit.NSRect.__typestr__)

    @min_os_level('10.7')
    def testProtocols10_7(self):
        self.assertResultIsBOOL(PopoverHelper.popoverShouldClose_)


if __name__ == "__main__":
    main()
