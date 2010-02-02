from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSScriptCommand (TestCase):
    def testConstants(self):
        self.assertEqual(NSNoScriptError, 0)
        self.assertEqual(NSReceiverEvaluationScriptError, 1)
        self.assertEqual(NSKeySpecifierEvaluationScriptError, 2)
        self.assertEqual(NSArgumentEvaluationScriptError, 3)
        self.assertEqual(NSReceiversCantHandleCommandScriptError,  4)
        self.assertEqual(NSRequiredArgumentsMissingScriptError, 5)
        self.assertEqual(NSArgumentsWrongScriptError,  6)
        self.assertEqual(NSUnknownKeyScriptError,  7)
        self.assertEqual(NSInternalScriptError,  8)
        self.assertEqual(NSOperationNotSupportedForKeyScriptError, 9)
        self.assertEqual(NSCannotCreateScriptCommandError, 10)

    def testMethods(self):
        self.assertResultIsBOOL(NSScriptCommand.isWellFormed)


if __name__ == "__main__":
    main()

