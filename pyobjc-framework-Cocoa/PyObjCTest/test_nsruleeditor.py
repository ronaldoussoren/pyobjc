import AppKit
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestNSRuleEditorHelper(AppKit.NSObject):
    def ruleEditor_numberOfChildrenForCriterion_withRowType_(self, ed, cr, rt):
        return 1

    def ruleEditor_child_forCriterion_withRowType_(self, ed, ch, cr, rt):
        return 1

    def ruleEditor_displayValueForCriterion_inRow_(self, ed, cr, rw):
        return 1

    def ruleEditor_predicatePartsForCriterion_withDisplayValue_inRow_(
        self, ed, cr, dv, rw
    ):
        return 1


class TestNSRuleEditor(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSRuleEditorNestingModeSingle, 0)
        self.assertEqual(AppKit.NSRuleEditorNestingModeList, 1)
        self.assertEqual(AppKit.NSRuleEditorNestingModeCompound, 2)
        self.assertEqual(AppKit.NSRuleEditorNestingModeSimple, 3)

        self.assertEqual(AppKit.NSRuleEditorRowTypeSimple, 0)
        self.assertEqual(AppKit.NSRuleEditorRowTypeCompound, 1)

        self.assertIsInstance(AppKit.NSRuleEditorPredicateLeftExpression, str)
        self.assertIsInstance(AppKit.NSRuleEditorPredicateRightExpression, str)
        self.assertIsInstance(AppKit.NSRuleEditorPredicateComparisonModifier, str)
        self.assertIsInstance(AppKit.NSRuleEditorPredicateOptions, str)
        self.assertIsInstance(AppKit.NSRuleEditorPredicateOperatorType, str)
        self.assertIsInstance(AppKit.NSRuleEditorPredicateCustomSelector, str)

        self.assertIsInstance(AppKit.NSRuleEditorPredicateCompoundType, str)
        self.assertIsInstance(AppKit.NSRuleEditorRowsDidChangeNotification, str)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSRuleEditor.isEditable)
        self.assertArgIsBOOL(AppKit.NSRuleEditor.setEditable_, 0)
        self.assertResultIsBOOL(AppKit.NSRuleEditor.canRemoveAllRows)
        self.assertArgIsBOOL(AppKit.NSRuleEditor.setCanRemoveAllRows_, 0)
        self.assertArgIsBOOL(
            AppKit.NSRuleEditor.insertRowAtIndex_withType_asSubrowOfRow_animate_, 3
        )
        self.assertArgIsBOOL(AppKit.NSRuleEditor.removeRowsAtIndexes_includeSubrows_, 1)
        self.assertArgIsBOOL(
            AppKit.NSRuleEditor.selectRowIndexes_byExtendingSelection_, 1
        )

    @min_sdk_level("10.6")
    def testProtocolObjects(self):
        objc.protocolNamed("NSRuleEditorDelegate")

    def testProtocols(self):
        self.assertResultHasType(
            TestNSRuleEditorHelper.ruleEditor_numberOfChildrenForCriterion_withRowType_,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSRuleEditorHelper.ruleEditor_numberOfChildrenForCriterion_withRowType_,
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSRuleEditorHelper.ruleEditor_child_forCriterion_withRowType_,
            1,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSRuleEditorHelper.ruleEditor_child_forCriterion_withRowType_,
            3,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSRuleEditorHelper.ruleEditor_displayValueForCriterion_inRow_,
            2,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSRuleEditorHelper.ruleEditor_predicatePartsForCriterion_withDisplayValue_inRow_,  # noqa: B950
            3,
            objc._C_NSInteger,
        )
