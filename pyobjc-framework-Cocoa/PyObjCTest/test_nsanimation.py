import AppKit
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestNSAnimationHelper(AppKit.NSObject):
    def animationShouldStart_(self, animation):
        return 1

    def animation_valueForProgress_(self, a, b):
        return 1

    def animation_didReachProgressMark_(self, a, b):
        return 1


class TestNSAnimation(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSAnimationEaseInOut, 0)
        self.assertEqual(AppKit.NSAnimationEaseIn, 1)
        self.assertEqual(AppKit.NSAnimationEaseOut, 2)
        self.assertEqual(AppKit.NSAnimationLinear, 3)

        self.assertEqual(AppKit.NSAnimationBlocking, 0)
        self.assertEqual(AppKit.NSAnimationNonblocking, 1)
        self.assertEqual(AppKit.NSAnimationNonblockingThreaded, 2)

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

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSAnimation.isAnimating)

    @min_sdk_level("10.6")
    def testProtocol(self):
        objc.protocolNamed("NSAnimationDelegate")
        objc.protocolNamed("NSAnimatablePropertyContainer")

    def testProtocolMethods(self):
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
