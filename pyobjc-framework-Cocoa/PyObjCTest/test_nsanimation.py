import AppKit
from PyObjCTools.TestSupport import TestCase
import objc


class TestNSAnimationHelper(AppKit.NSObject):
    def animationShouldStart_(self, animation):
        return 1

    def animation_valueForProgress_(self, a, b):
        return 1

    def animation_didReachProgressMark_(self, a, b):
        return 1


class TestNSAnimation(TestCase):
    def test_enums(self):
        self.assertIsEnumType(AppKit.NSAnimationCurve)
        self.assertEqual(AppKit.NSAnimationEaseInOut, 0)
        self.assertEqual(AppKit.NSAnimationEaseIn, 1)
        self.assertEqual(AppKit.NSAnimationEaseOut, 2)
        self.assertEqual(AppKit.NSAnimationLinear, 3)

        self.assertIsEnumType(AppKit.NSAnimationBlockingMode)
        self.assertEqual(AppKit.NSAnimationBlocking, 0)
        self.assertEqual(AppKit.NSAnimationNonblocking, 1)
        self.assertEqual(AppKit.NSAnimationNonblockingThreaded, 2)

    def test_typed_enums(self):
        self.assertIsTypedEnum(AppKit.NSViewAnimationEffectName, str)
        self.assertIsTypedEnum(AppKit.NSViewAnimationKey, str)

    def test_constants(self):
        self.assertIsInstance(AppKit.NSAnimationProgressMarkNotification, str)
        self.assertIsInstance(AppKit.NSAnimationProgressMark, str)

        self.assertIsInstance(AppKit.NSViewAnimationTargetKey, str)
        self.assertIsInstance(AppKit.NSViewAnimationStartFrameKey, str)
        self.assertIsInstance(AppKit.NSViewAnimationEndFrameKey, str)
        self.assertIsInstance(AppKit.NSViewAnimationEffectKey, str)
        self.assertIsInstance(AppKit.NSViewAnimationFadeInEffect, str)
        self.assertIsInstance(AppKit.NSViewAnimationFadeOutEffect, str)

        self.assertIsInstance(AppKit.NSAnimationTriggerOrderIn, str)
        self.assertIsInstance(AppKit.NSAnimationTriggerOrderOut, str)

    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSAnimation.isAnimating)

    def test_protocols(self):
        self.assertProtocolExists("NSAnimationDelegate", AppKit)
        self.assertProtocolExists("NSAnimatablePropertyContainer", AppKit)

    def test_protocol_methods(self):
        self.assertResultIsBOOL(TestNSAnimationHelper.animationShouldStart_)

        self.assertResultHasType(
            TestNSAnimationHelper.animation_valueForProgress_, objc._C_FLT
        )
        self.assertArgHasType(
            TestNSAnimationHelper.animation_valueForProgress_, 1, objc._C_FLT
        )
        self.assertArgHasType(
            TestNSAnimationHelper.animation_didReachProgressMark_, 1, objc._C_FLT
        )
