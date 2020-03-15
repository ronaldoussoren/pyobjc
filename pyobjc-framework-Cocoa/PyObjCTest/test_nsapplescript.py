import Foundation
from PyObjCTools.TestSupport import TestCase


class TestAE(TestCase):
    def testConstants(self):
        self.assertIsInstance(Foundation.NSAppleScriptErrorMessage, str)
        self.assertIsInstance(Foundation.NSAppleScriptErrorNumber, str)
        self.assertIsInstance(Foundation.NSAppleScriptErrorAppName, str)
        self.assertIsInstance(Foundation.NSAppleScriptErrorBriefMessage, str)
        self.assertIsInstance(Foundation.NSAppleScriptErrorRange, str)

    def testOutput(self):
        obj = Foundation.NSAppleScript.alloc().initWithSource_(
            'tell application Terminal to do Xscript "ls -l"'
        )
        ok, error = obj.compileAndReturnError_(None)
        self.assertIs(ok, False)
        self.assertIsInstance(error, Foundation.NSDictionary)

    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSAppleScript.isCompiled)
        self.assertResultIsBOOL(Foundation.NSAppleScript.compileAndReturnError_)
        self.assertArgIsOut(Foundation.NSAppleScript.compileAndReturnError_, 0)
        self.assertArgIsOut(Foundation.NSAppleScript.executeAndReturnError_, 0)
        self.assertArgIsOut(Foundation.NSAppleScript.executeAppleEvent_error_, 1)
        self.assertArgIsOut(Foundation.NSAppleScript.initWithContentsOfURL_error_, 1)
