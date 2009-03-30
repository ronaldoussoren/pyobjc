from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSScriptCommand (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSNoScriptError, 0)
        self.failUnlessEqual(NSReceiverEvaluationScriptError, 1)
        self.failUnlessEqual(NSKeySpecifierEvaluationScriptError, 2)
        self.failUnlessEqual(NSArgumentEvaluationScriptError, 3)
        self.failUnlessEqual(NSReceiversCantHandleCommandScriptError,  4)
        self.failUnlessEqual(NSRequiredArgumentsMissingScriptError, 5)
        self.failUnlessEqual(NSArgumentsWrongScriptError,  6)
        self.failUnlessEqual(NSUnknownKeyScriptError,  7)
        self.failUnlessEqual(NSInternalScriptError,  8)
        self.failUnlessEqual(NSOperationNotSupportedForKeyScriptError, 9)
        self.failUnlessEqual(NSCannotCreateScriptCommandError, 10)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSScriptCommand.isWellFormed)


if __name__ == "__main__":
    main()

