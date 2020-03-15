import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSScriptCommand(TestCase):
    def testConstants(self):
        self.assertEqual(Foundation.NSNoScriptError, 0)
        self.assertEqual(Foundation.NSReceiverEvaluationScriptError, 1)
        self.assertEqual(Foundation.NSKeySpecifierEvaluationScriptError, 2)
        self.assertEqual(Foundation.NSArgumentEvaluationScriptError, 3)
        self.assertEqual(Foundation.NSReceiversCantHandleCommandScriptError, 4)
        self.assertEqual(Foundation.NSRequiredArgumentsMissingScriptError, 5)
        self.assertEqual(Foundation.NSArgumentsWrongScriptError, 6)
        self.assertEqual(Foundation.NSUnknownKeyScriptError, 7)
        self.assertEqual(Foundation.NSInternalScriptError, 8)
        self.assertEqual(Foundation.NSOperationNotSupportedForKeyScriptError, 9)
        self.assertEqual(Foundation.NSCannotCreateScriptCommandError, 10)

    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSScriptCommand.isWellFormed)
