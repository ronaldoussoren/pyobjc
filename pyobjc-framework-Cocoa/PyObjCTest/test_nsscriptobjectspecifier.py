from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSScriptObjectSpecifiers (TestCase):
    def testConstants(self):
        self.assertEqual(NSNoSpecifierError, 0)
        self.assertEqual(NSNoTopLevelContainersSpecifierError, 1)
        self.assertEqual(NSContainerSpecifierError, 2)
        self.assertEqual(NSUnknownKeySpecifierError, 3)
        self.assertEqual(NSInvalidIndexSpecifierError, 4)
        self.assertEqual(NSInternalSpecifierError, 5)
        self.assertEqual(NSOperationNotSupportedForKeySpecifierError, 6)

        self.assertEqual(NSPositionAfter, 0)
        self.assertEqual(NSPositionBefore, 1)
        self.assertEqual(NSPositionBeginning, 2)
        self.assertEqual(NSPositionEnd, 3)
        self.assertEqual(NSPositionReplace, 4)

        self.assertEqual(NSRelativeAfter, 0)
        self.assertEqual(NSRelativeBefore, 1)

        self.assertEqual(NSIndexSubelement, 0)
        self.assertEqual(NSEverySubelement, 1)
        self.assertEqual(NSMiddleSubelement, 2)
        self.assertEqual(NSRandomSubelement, 3)
        self.assertEqual(NSNoSubelement, 4)

    def testMethods(self):
        self.assertResultIsBOOL(NSScriptObjectSpecifier.containerIsObjectBeingTested)
        self.assertArgIsBOOL(NSScriptObjectSpecifier.setContainerIsObjectBeingTested_, 0)

        self.assertResultIsBOOL(NSScriptObjectSpecifier.containerIsRangeContainerObject)
        self.assertArgIsBOOL(NSScriptObjectSpecifier.setContainerIsRangeContainerObject_, 0)

        self.assertArgIsOut(NSScriptObjectSpecifier.indicesOfObjectsByEvaluatingWithContainer_count_, 1)
        self.assertResultSizeInArg(NSScriptObjectSpecifier.indicesOfObjectsByEvaluatingWithContainer_count_, 1)

        self.assertResultIsBOOL(NSPositionalSpecifier.insertionReplaces)

if __name__ == "__main__":
    main()
