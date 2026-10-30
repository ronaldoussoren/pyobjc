import AppKit
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestNSTouch(TestCase):
    def test_enums(self):
        self.assertIsEnumType(AppKit.NSTouchPhase)
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

        self.assertIsEnumType(AppKit.NSTouchType)
        self.assertEqual(AppKit.NSTouchTypeDirect, 0)
        self.assertEqual(AppKit.NSTouchTypeIndirect, 1)

        self.assertIsEnumType(AppKit.NSTouchTypeMask)
        self.assertEqual(AppKit.NSTouchTypeMaskDirect, 1 << 0)
        self.assertEqual(AppKit.NSTouchTypeMaskIndirect, 1 << 1)

    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSTouch.isResting)
        self.assertResultHasType(AppKit.NSTouch.deviceSize, AppKit.NSSize.__typestr__)

    @min_sdk_level("10.12")
    def test_functions10_12(self):
        self.assertEqual(
            AppKit.NSTouchTypeMaskFromType(AppKit.NSTouchTypeDirect),
            AppKit.NSTouchTypeMaskDirect,
        )
        self.assertEqual(
            AppKit.NSTouchTypeMaskFromType(AppKit.NSTouchTypeIndirect),
            AppKit.NSTouchTypeMaskIndirect,
        )
