
from PyObjCTools.TestSupport import *
from AppKit import *

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


if __name__ == "__main__":
    main()
