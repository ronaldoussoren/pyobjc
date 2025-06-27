import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestNSWritingToolsCoordinatorHelper(AppKit.NSObject):
    def writingToolsCoordinator_requestsContextsForScope_completion_(self, a, b, c):
        pass

    def writingToolsCoordinator_replaceRange_inContext_proposedText_reason_animationParameters_completion_(
        self, a, b, c, d, e, f, g
    ):
        pass

    def writingToolsCoordinator_selectRanges_inContext_completion_(self, a, b, c, d):
        pass

    def writingToolsCoordinator_requestsRangeInContextWithIdentifierForPoint_completion_(
        self, a, b, c
    ):
        pass

    def writingToolsCoordinator_requestsBoundingBezierPathsForRange_inContext_completion_(
        self, a, b, c, d
    ):
        pass

    def writingToolsCoordinator_requestsUnderlinePathsForRange_inContext_completion_(
        self, a, b, c, d
    ):
        pass

    def writingToolsCoordinator_prepareForTextAnimation_forRange_inContext_completion_(
        self, a, b, c, d, e
    ):
        pass

    def writingToolsCoordinator_requestsPreviewForTextAnimation_ofRange_inContext_completion_(
        self, a, b, c, d, e
    ):
        pass

    def writingToolsCoordinator_requestsPreviewForRect_inContext_completion_(
        self, a, b, c, d
    ):
        pass

    def writingToolsCoordinator_finishTextAnimation_forRange_inContext_completion_(
        self, a, b, c, d, e
    ):
        pass

    def writingToolsCoordinator_requestsSingleContainerSubrangesOfRange_inContext_completion_(
        self, a, b, c, d
    ):
        pass

    def writingToolsCoordinator_requestsDecorationContainerViewForRange_inContext_completion_(
        self, a, b, c, d
    ):
        pass

    def writingToolsCoordinator_willChangeToState_completion_(self, a, b, c):
        pass


class TestNSWritingToolsCoordinator(TestCase):
    def test_enum(self):
        self.assertIsEnumType(AppKit.NSWritingToolsCoordinatorTextUpdateReason)
        self.assertEqual(AppKit.NSWritingToolsCoordinatorTextUpdateReasonTyping, 0)
        self.assertEqual(AppKit.NSWritingToolsCoordinatorTextUpdateReasonUndoRedo, 1)

        self.assertIsEnumType(AppKit.NSWritingToolsCoordinatorState)
        self.assertEqual(AppKit.NSWritingToolsCoordinatorStateInactive, 0)
        self.assertEqual(AppKit.NSWritingToolsCoordinatorStateNoninteractive, 1)
        self.assertEqual(AppKit.NSWritingToolsCoordinatorStateInteractiveResting, 2)
        self.assertEqual(AppKit.NSWritingToolsCoordinatorStateInteractiveStreaming, 3)

        self.assertIsEnumType(AppKit.NSWritingToolsCoordinatorTextReplacementReason)
        self.assertEqual(
            AppKit.NSWritingToolsCoordinatorTextReplacementReasonInteractive, 0
        )
        self.assertEqual(
            AppKit.NSWritingToolsCoordinatorTextReplacementReasonNoninteractive, 1
        )

        self.assertIsEnumType(AppKit.NSWritingToolsCoordinatorContextScope)
        self.assertEqual(AppKit.NSWritingToolsCoordinatorContextScopeUserSelection, 0)
        self.assertEqual(AppKit.NSWritingToolsCoordinatorContextScopeFullDocument, 1)
        self.assertEqual(AppKit.NSWritingToolsCoordinatorContextScopeVisibleArea, 2)

        self.assertIsEnumType(AppKit.NSWritingToolsCoordinatorTextAnimation)
        self.assertEqual(AppKit.NSWritingToolsCoordinatorTextAnimationAnticipate, 0)
        self.assertEqual(AppKit.NSWritingToolsCoordinatorTextAnimationRemove, 1)
        self.assertEqual(AppKit.NSWritingToolsCoordinatorTextAnimationInsert, 2)
        self.assertEqual(
            AppKit.NSWritingToolsCoordinatorTextAnimationAnticipateInactive, 8
        )
        self.assertEqual(AppKit.NSWritingToolsCoordinatorTextAnimationTranslate, 9)

    @min_sdk_level("15.2")
    def test_protocols(self):
        self.assertProtocolExists("NSWritingToolsCoordinatorDelegate")

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestNSWritingToolsCoordinatorHelper.writingToolsCoordinator_requestsContextsForScope_completion_,
            1,
            b"q",
        )
        self.assertArgIsBlock(
            TestNSWritingToolsCoordinatorHelper.writingToolsCoordinator_requestsContextsForScope_completion_,
            2,
            b"v@",
        )

        self.assertArgHasType(
            TestNSWritingToolsCoordinatorHelper.writingToolsCoordinator_replaceRange_inContext_proposedText_reason_animationParameters_completion_,
            1,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSWritingToolsCoordinatorHelper.writingToolsCoordinator_replaceRange_inContext_proposedText_reason_animationParameters_completion_,
            4,
            b"q",
        )
        self.assertArgIsBlock(
            TestNSWritingToolsCoordinatorHelper.writingToolsCoordinator_replaceRange_inContext_proposedText_reason_animationParameters_completion_,
            6,
            b"v@",
        )

        self.assertArgIsBlock(
            TestNSWritingToolsCoordinatorHelper.writingToolsCoordinator_selectRanges_inContext_completion_,
            3,
            b"v",
        )

        self.assertArgHasType(
            TestNSWritingToolsCoordinatorHelper.writingToolsCoordinator_requestsRangeInContextWithIdentifierForPoint_completion_,
            1,
            AppKit.NSPoint.__typestr__,
        )
        self.assertArgIsBlock(
            TestNSWritingToolsCoordinatorHelper.writingToolsCoordinator_requestsRangeInContextWithIdentifierForPoint_completion_,
            2,
            b"v" + AppKit.NSRange.__typestr__ + b"@",
        )

        self.assertArgHasType(
            TestNSWritingToolsCoordinatorHelper.writingToolsCoordinator_requestsBoundingBezierPathsForRange_inContext_completion_,
            1,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgIsBlock(
            TestNSWritingToolsCoordinatorHelper.writingToolsCoordinator_requestsBoundingBezierPathsForRange_inContext_completion_,
            3,
            b"v@",
        )

        self.assertArgHasType(
            TestNSWritingToolsCoordinatorHelper.writingToolsCoordinator_requestsUnderlinePathsForRange_inContext_completion_,
            1,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgIsBlock(
            TestNSWritingToolsCoordinatorHelper.writingToolsCoordinator_requestsUnderlinePathsForRange_inContext_completion_,
            3,
            b"v@",
        )

        self.assertArgHasType(
            TestNSWritingToolsCoordinatorHelper.writingToolsCoordinator_prepareForTextAnimation_forRange_inContext_completion_,
            1,
            b"q",
        )
        self.assertArgHasType(
            TestNSWritingToolsCoordinatorHelper.writingToolsCoordinator_prepareForTextAnimation_forRange_inContext_completion_,
            2,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgIsBlock(
            TestNSWritingToolsCoordinatorHelper.writingToolsCoordinator_prepareForTextAnimation_forRange_inContext_completion_,
            4,
            b"v",
        )

        self.assertArgHasType(
            TestNSWritingToolsCoordinatorHelper.writingToolsCoordinator_requestsPreviewForTextAnimation_ofRange_inContext_completion_,
            1,
            b"q",
        )
        self.assertArgHasType(
            TestNSWritingToolsCoordinatorHelper.writingToolsCoordinator_requestsPreviewForTextAnimation_ofRange_inContext_completion_,
            2,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgIsBlock(
            TestNSWritingToolsCoordinatorHelper.writingToolsCoordinator_requestsPreviewForTextAnimation_ofRange_inContext_completion_,
            4,
            b"v@",
        )

        self.assertArgHasType(
            TestNSWritingToolsCoordinatorHelper.writingToolsCoordinator_requestsPreviewForRect_inContext_completion_,
            1,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgIsBlock(
            TestNSWritingToolsCoordinatorHelper.writingToolsCoordinator_requestsPreviewForRect_inContext_completion_,
            3,
            b"v@",
        )

        self.assertArgHasType(
            TestNSWritingToolsCoordinatorHelper.writingToolsCoordinator_finishTextAnimation_forRange_inContext_completion_,
            1,
            b"q",
        )
        self.assertArgHasType(
            TestNSWritingToolsCoordinatorHelper.writingToolsCoordinator_finishTextAnimation_forRange_inContext_completion_,
            2,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgIsBlock(
            TestNSWritingToolsCoordinatorHelper.writingToolsCoordinator_finishTextAnimation_forRange_inContext_completion_,
            4,
            b"v",
        )

        self.assertArgHasType(
            TestNSWritingToolsCoordinatorHelper.writingToolsCoordinator_requestsSingleContainerSubrangesOfRange_inContext_completion_,
            1,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgIsBlock(
            TestNSWritingToolsCoordinatorHelper.writingToolsCoordinator_requestsSingleContainerSubrangesOfRange_inContext_completion_,
            3,
            b"v@",
        )

        self.assertArgHasType(
            TestNSWritingToolsCoordinatorHelper.writingToolsCoordinator_requestsDecorationContainerViewForRange_inContext_completion_,
            1,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgIsBlock(
            TestNSWritingToolsCoordinatorHelper.writingToolsCoordinator_requestsDecorationContainerViewForRange_inContext_completion_,
            3,
            b"v@",
        )

        self.assertArgHasType(
            TestNSWritingToolsCoordinatorHelper.writingToolsCoordinator_willChangeToState_completion_,
            1,
            b"q",
        )
        self.assertArgIsBlock(
            TestNSWritingToolsCoordinatorHelper.writingToolsCoordinator_willChangeToState_completion_,
            2,
            b"v",
        )

    @min_os_level("15.2")
    def test_methods(self):
        self.assertResultIsBOOL(
            AppKit.NSWritingToolsCoordinator.isWritingToolsAvailable
        )
