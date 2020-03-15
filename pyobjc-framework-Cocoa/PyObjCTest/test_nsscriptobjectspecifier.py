import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSScriptObjectSpecifiers(TestCase):
    def testConstants(self):
        self.assertEqual(Foundation.NSNoSpecifierError, 0)
        self.assertEqual(Foundation.NSNoTopLevelContainersSpecifierError, 1)
        self.assertEqual(Foundation.NSContainerSpecifierError, 2)
        self.assertEqual(Foundation.NSUnknownKeySpecifierError, 3)
        self.assertEqual(Foundation.NSInvalidIndexSpecifierError, 4)
        self.assertEqual(Foundation.NSInternalSpecifierError, 5)
        self.assertEqual(Foundation.NSOperationNotSupportedForKeySpecifierError, 6)

        self.assertEqual(Foundation.NSPositionAfter, 0)
        self.assertEqual(Foundation.NSPositionBefore, 1)
        self.assertEqual(Foundation.NSPositionBeginning, 2)
        self.assertEqual(Foundation.NSPositionEnd, 3)
        self.assertEqual(Foundation.NSPositionReplace, 4)

        self.assertEqual(Foundation.NSRelativeAfter, 0)
        self.assertEqual(Foundation.NSRelativeBefore, 1)

        self.assertEqual(Foundation.NSIndexSubelement, 0)
        self.assertEqual(Foundation.NSEverySubelement, 1)
        self.assertEqual(Foundation.NSMiddleSubelement, 2)
        self.assertEqual(Foundation.NSRandomSubelement, 3)
        self.assertEqual(Foundation.NSNoSubelement, 4)

    def testMethods(self):
        self.assertResultIsBOOL(
            Foundation.NSScriptObjectSpecifier.containerIsObjectBeingTested
        )
        self.assertArgIsBOOL(
            Foundation.NSScriptObjectSpecifier.setContainerIsObjectBeingTested_, 0
        )

        self.assertResultIsBOOL(
            Foundation.NSScriptObjectSpecifier.containerIsRangeContainerObject
        )
        self.assertArgIsBOOL(
            Foundation.NSScriptObjectSpecifier.setContainerIsRangeContainerObject_, 0
        )

        self.assertArgIsOut(
            Foundation.NSScriptObjectSpecifier.indicesOfObjectsByEvaluatingWithContainer_count_,
            1,
        )
        self.assertResultSizeInArg(
            Foundation.NSScriptObjectSpecifier.indicesOfObjectsByEvaluatingWithContainer_count_,
            1,
        )

        self.assertResultIsBOOL(Foundation.NSPositionalSpecifier.insertionReplaces)
