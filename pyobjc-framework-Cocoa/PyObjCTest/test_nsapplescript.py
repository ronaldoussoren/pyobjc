from Foundation import *
from PyObjCTools.TestSupport import *

class TestAE (TestCase):
    def testConstants(self):
        self.failUnless(isinstance(NSAppleScriptErrorMessage, unicode))
        self.failUnless(isinstance(NSAppleScriptErrorNumber, unicode))
        self.failUnless(isinstance(NSAppleScriptErrorAppName, unicode))
        self.failUnless(isinstance(NSAppleScriptErrorBriefMessage, unicode))
        self.failUnless(isinstance(NSAppleScriptErrorRange, unicode))

    def testOutput(self):
        obj = NSAppleScript.alloc().initWithSource_(
                'tell application Terminal to do Xscript "ls -l"')
        ok, error = obj.compileAndReturnError_(None)
        self.failUnless(ok is False)
        self.failUnless(isinstance(error, NSDictionary))


    def testMethods(self):
        self.failUnlessResultIsBOOL(NSAppleScript.isCompiled)
        self.failUnlessResultIsBOOL(NSAppleScript.compileAndReturnError_)
        self.failUnlessArgIsOut(NSAppleScript.compileAndReturnError_, 0)
        self.failUnlessArgIsOut(NSAppleScript.executeAndReturnError_, 0)
        self.failUnlessArgIsOut(NSAppleScript.executeAppleEvent_error_, 1)
        self.failUnlessArgIsOut(NSAppleScript.initWithContentsOfURL_error_, 1)

if __name__ == "__main__":
    main()
