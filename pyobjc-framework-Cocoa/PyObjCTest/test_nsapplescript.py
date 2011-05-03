from Foundation import *
from PyObjCTools.TestSupport import *

class TestAE (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSAppleScriptErrorMessage, unicode)
        self.assertIsInstance(NSAppleScriptErrorNumber, unicode)
        self.assertIsInstance(NSAppleScriptErrorAppName, unicode)
        self.assertIsInstance(NSAppleScriptErrorBriefMessage, unicode)
        self.assertIsInstance(NSAppleScriptErrorRange, unicode)
    def testOutput(self):
        obj = NSAppleScript.alloc().initWithSource_(
                'tell application Terminal to do Xscript "ls -l"')
        ok, error = obj.compileAndReturnError_(None)
        self.assertIs(ok, False)
        self.assertIsInstance(error, NSDictionary)
    def testMethods(self):
        self.assertResultIsBOOL(NSAppleScript.isCompiled)
        self.assertResultIsBOOL(NSAppleScript.compileAndReturnError_)
        self.assertArgIsOut(NSAppleScript.compileAndReturnError_, 0)
        self.assertArgIsOut(NSAppleScript.executeAndReturnError_, 0)
        self.assertArgIsOut(NSAppleScript.executeAppleEvent_error_, 1)
        self.assertArgIsOut(NSAppleScript.initWithContentsOfURL_error_, 1)

if __name__ == "__main__":
    main()
