from PyObjCTools.TestSupport import TestCase
import IntentsUI
import objc


class TestINUIHostedViewControllingHelper(IntentsUI.NSObject):
    def configureWithInteraction_context_completion_(self, a, b, c):
        pass

    def configureViewForParameters_ofInteraction_interactiveBehavior_context_completion_(
        self, a, b, c, d, e
    ):
        pass


class TestINUIHostedViewControlling(TestCase):
    def test_constants(self):
        self.assertEqual(IntentsUI.INUIInteractiveBehaviorNone, 0)
        self.assertEqual(IntentsUI.INUIInteractiveBehaviorNextView, 1)
        self.assertEqual(IntentsUI.INUIInteractiveBehaviorLaunch, 2)
        self.assertEqual(IntentsUI.INUIInteractiveBehaviorGenericAction, 3)

    def test_protocols(self):
        objc.protocolNamed("INUIHostedViewControlling")

    def test_methods(self):
        self.assertHasType(
            TestINUIHostedViewControllingHelper.configureWithInteraction_context_completion_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgIsBlock(
            TestINUIHostedViewControllingHelper.configureWithInteraction_context_completion_,
            2,
            b"v{CGSize=dd}",
        )

        self.assertArgHasType(
            TestINUIHostedViewControllingHelper.configureViewForParameters_ofInteraction_interactiveBehavior_context_completion_,
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestINUIHostedViewControllingHelper.configureViewForParameters_ofInteraction_interactiveBehavior_context_completion_,
            3,
            objc._C_NSUInteger,
        )
        self.assertArgIsBlock(
            TestINUIHostedViewControllingHelper.configureViewForParameters_ofInteraction_interactiveBehavior_context_completion_,
            4,
            b"vZ@{CGSize=dd}",
        )
