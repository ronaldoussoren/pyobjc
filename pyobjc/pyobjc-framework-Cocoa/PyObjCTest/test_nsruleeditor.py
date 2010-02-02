
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSRuleEditorHelper (NSObject):
    def ruleEditor_numberOfChildrenForCriterion_withRowType_(self, ed, cr, rt): return 1
    def ruleEditor_child_forCriterion_withRowType_(self, ed, ch, cr, rt): return 1
    def ruleEditor_displayValueForCriterion_inRow_(self, ed, cr, rw): return 1
    def ruleEditor_predicatePartsForCriterion_withDisplayValue_inRow_(self, ed, cr, dv, rw): return 1

class TestNSRuleEditor (TestCase):
    def testConstants(self):
        self.assertEqual(NSRuleEditorNestingModeSingle, 0)
        self.assertEqual(NSRuleEditorNestingModeList, 1)
        self.assertEqual(NSRuleEditorNestingModeCompound, 2)
        self.assertEqual(NSRuleEditorNestingModeSimple, 3)

        self.assertEqual(NSRuleEditorRowTypeSimple, 0)
        self.assertEqual(NSRuleEditorRowTypeCompound, 1)

        self.assertIsInstance(NSRuleEditorPredicateLeftExpression, unicode)
        self.assertIsInstance(NSRuleEditorPredicateRightExpression, unicode)
        self.assertIsInstance(NSRuleEditorPredicateComparisonModifier, unicode)
        self.assertIsInstance(NSRuleEditorPredicateOptions, unicode)
        self.assertIsInstance(NSRuleEditorPredicateOperatorType, unicode)
        self.assertIsInstance(NSRuleEditorPredicateCustomSelector, unicode)

        self.assertIsInstance(NSRuleEditorPredicateCompoundType, unicode)
        self.assertIsInstance(NSRuleEditorRowsDidChangeNotification, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(NSRuleEditor.isEditable)
        self.assertArgIsBOOL(NSRuleEditor.setEditable_, 0)
        self.assertResultIsBOOL(NSRuleEditor.canRemoveAllRows)
        self.assertArgIsBOOL(NSRuleEditor.setCanRemoveAllRows_, 0)
        self.assertArgIsBOOL(NSRuleEditor.insertRowAtIndex_withType_asSubrowOfRow_animate_, 3)
        self.assertArgIsBOOL(NSRuleEditor.removeRowsAtIndexes_includeSubrows_, 1)
        self.assertArgIsBOOL(NSRuleEditor.selectRowIndexes_byExtendingSelection_, 1)

    def testProtocols(self):
        self.assertResultHasType(TestNSRuleEditorHelper.ruleEditor_numberOfChildrenForCriterion_withRowType_, objc._C_NSInteger)
        self.assertArgHasType(TestNSRuleEditorHelper.ruleEditor_numberOfChildrenForCriterion_withRowType_, 2, objc._C_NSUInteger)
        self.assertArgHasType(TestNSRuleEditorHelper.ruleEditor_child_forCriterion_withRowType_, 1, objc._C_NSInteger)
        self.assertArgHasType(TestNSRuleEditorHelper.ruleEditor_child_forCriterion_withRowType_, 3, objc._C_NSUInteger)
        self.assertArgHasType(TestNSRuleEditorHelper.ruleEditor_displayValueForCriterion_inRow_, 2, objc._C_NSInteger)
        self.assertArgHasType(TestNSRuleEditorHelper.ruleEditor_predicatePartsForCriterion_withDisplayValue_inRow_, 3, objc._C_NSInteger)


if __name__ == "__main__":
    main()
