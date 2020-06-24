import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestNSTouch(TestCase):
    @min_os_level("10.6")
    def testConstants(self):
        self.assertEqual(AppKit.NSTouchPhaseBegan, 1 << 0)
        self.assertEqual(AppKit.NSTouchPhaseMoved, 1 << 1)
        self.assertEqual(AppKit.NSTouchPhaseStationary, 1 << 2)
        self.assertEqual(AppKit.NSTouchPhaseEnded, 1 << 3)
        self.assertEqual(AppKit.NSTouchPhaseCancelled, 1 << 4)
        self.assertEqual(
            AppKit.NSTouchPhaseTouching,
            AppKit.NSTouchPhaseBegan
            | AppKit.NSTouchPhaseMoved
            | AppKit.NSTouchPhaseStationary,
        )
        self.assertEqual(AppKit.NSTouchPhaseAny, 0xFFFFFFFFFFFFFFFF)

        # 10.12
        self.assertEqual(AppKit.NSTouchTypeDirect, 0)
        self.assertEqual(AppKit.NSTouchTypeIndirect, 1)
        self.assertEqual(AppKit.NSTouchTypeMaskDirect, 1 << 0)
        self.assertEqual(AppKit.NSTouchTypeMaskIndirect, 1 << 1)

    @min_os_level("10.6")
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSTouch.isResting)
        self.assertResultHasType(AppKit.NSTouch.deviceSize, AppKit.NSSize.__typestr__)

    @min_sdk_level("10.12")
    def testFunctions10_12(self):
        self.assertEqual(
            AppKit.NSTouchTypeMaskFromType(AppKit.NSTouchTypeDirect),
            AppKit.NSTouchTypeMaskDirect,
        )
        self.assertEqual(
            AppKit.NSTouchTypeMaskFromType(AppKit.NSTouchTypeIndirect),
            AppKit.NSTouchTypeMaskIndirect,
        )
