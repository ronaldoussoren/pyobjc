from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSScriptObjectSpecifiers (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSNoSpecifierError, 0)
        self.failUnlessEqual(NSNoTopLevelContainersSpecifierError, 1)
        self.failUnlessEqual(NSContainerSpecifierError, 2)
        self.failUnlessEqual(NSUnknownKeySpecifierError, 3)
        self.failUnlessEqual(NSInvalidIndexSpecifierError, 4)
        self.failUnlessEqual(NSInternalSpecifierError, 5)
        self.failUnlessEqual(NSOperationNotSupportedForKeySpecifierError, 6)

        self.failUnlessEqual(NSPositionAfter, 0)
        self.failUnlessEqual(NSPositionBefore, 1)
        self.failUnlessEqual(NSPositionBeginning, 2)
        self.failUnlessEqual(NSPositionEnd, 3)
        self.failUnlessEqual(NSPositionReplace, 4)

        self.failUnlessEqual(NSRelativeAfter, 0)
        self.failUnlessEqual(NSRelativeBefore, 1)

        self.failUnlessEqual(NSIndexSubelement, 0)
        self.failUnlessEqual(NSEverySubelement, 1)
        self.failUnlessEqual(NSMiddleSubelement, 2)
        self.failUnlessEqual(NSRandomSubelement, 3)
        self.failUnlessEqual(NSNoSubelement, 4)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSScriptObjectSpecifier.containerIsObjectBeingTested)
        self.failUnlessArgIsBOOL(NSScriptObjectSpecifier.setContainerIsObjectBeingTested_, 0)

        self.failUnlessResultIsBOOL(NSScriptObjectSpecifier.containerIsRangeContainerObject)
        self.failUnlessArgIsBOOL(NSScriptObjectSpecifier.setContainerIsRangeContainerObject_, 0)

        self.failUnlessArgIsOut(NSScriptObjectSpecifier.indicesOfObjectsByEvaluatingWithContainer_count_, 1)
        self.failUnlessResultSizeInArg(NSScriptObjectSpecifier.indicesOfObjectsByEvaluatingWithContainer_count_, 1)

if __name__ == "__main__":
    main()
