
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSRuleEditorHelper (NSObject):
    def ruleEditor_numberOfChildrenForCriterion_withRowType_(self, ed, cr, rt): return 1
    def ruleEditor_child_forCriterion_withRowType_(self, ed, ch, cr, rt): return 1
    def ruleEditor_displayValueForCriterion_inRow_(self, ed, cr, rw): return 1
    def ruleEditor_predicatePartsForCriterion_withDisplayValue_inRow_(self, ed, cr, dv, rw): return 1

class TestNSRuleEditor (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSRuleEditorNestingModeSingle, 0)
        self.failUnlessEqual(NSRuleEditorNestingModeList, 1)
        self.failUnlessEqual(NSRuleEditorNestingModeCompound, 2)
        self.failUnlessEqual(NSRuleEditorNestingModeSimple, 3)

        self.failUnlessEqual(NSRuleEditorRowTypeSimple, 0)
        self.failUnlessEqual(NSRuleEditorRowTypeCompound, 1)

        self.failUnlessIsInstance(NSRuleEditorPredicateLeftExpression, unicode)
        self.failUnlessIsInstance(NSRuleEditorPredicateRightExpression, unicode)
        self.failUnlessIsInstance(NSRuleEditorPredicateComparisonModifier, unicode)
        self.failUnlessIsInstance(NSRuleEditorPredicateOptions, unicode)
        self.failUnlessIsInstance(NSRuleEditorPredicateOperatorType, unicode)
        self.failUnlessIsInstance(NSRuleEditorPredicateCustomSelector, unicode)

        self.failUnlessIsInstance(NSRuleEditorPredicateCompoundType, unicode)
        self.failUnlessIsInstance(NSRuleEditorRowsDidChangeNotification, unicode)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSRuleEditor.isEditable)
        self.failUnlessArgIsBOOL(NSRuleEditor.setEditable_, 0)
        self.failUnlessResultIsBOOL(NSRuleEditor.canRemoveAllRows)
        self.failUnlessArgIsBOOL(NSRuleEditor.setCanRemoveAllRows_, 0)
        self.failUnlessArgIsBOOL(NSRuleEditor.insertRowAtIndex_withType_asSubrowOfRow_animate_, 3)
        self.failUnlessArgIsBOOL(NSRuleEditor.removeRowsAtIndexes_includeSubrows_, 1)
        self.failUnlessArgIsBOOL(NSRuleEditor.selectRowIndexes_byExtendingSelection_, 1)

    def testProtocols(self):
        self.failUnlessResultHasType(TestNSRuleEditorHelper.ruleEditor_numberOfChildrenForCriterion_withRowType_, objc._C_NSInteger)
        self.failUnlessArgHasType(TestNSRuleEditorHelper.ruleEditor_numberOfChildrenForCriterion_withRowType_, 2, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestNSRuleEditorHelper.ruleEditor_child_forCriterion_withRowType_, 1, objc._C_NSInteger)
        self.failUnlessArgHasType(TestNSRuleEditorHelper.ruleEditor_child_forCriterion_withRowType_, 3, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestNSRuleEditorHelper.ruleEditor_displayValueForCriterion_inRow_, 2, objc._C_NSInteger)
        self.failUnlessArgHasType(TestNSRuleEditorHelper.ruleEditor_predicatePartsForCriterion_withDisplayValue_inRow_, 3, objc._C_NSInteger)


if __name__ == "__main__":
    main()
