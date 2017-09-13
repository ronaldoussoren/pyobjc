from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:
    import GameplayKit

    class TestGKRuleSystem (TestCase):
        def testMethods(self):
            self.assertResultIsBOOL(GameplayKit.GKRule.evaluatePredicateWithSystem_)

            self.assertArgIsBlock(GameplayKit.GKRule.ruleWithBlockPredicate_action_, 0, b'Z@')
            self.assertArgIsBlock(GameplayKit.GKRule.ruleWithBlockPredicate_action_, 1, b'v@')

            self.assertResultIsBOOL(GameplayKit.GKNSPredicateRule.evaluatePredicateWithSystem_)

if __name__ == "__main__":
    main()
