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

        obj = NSAppleScript.alloc().initWithSource_(
                'tell application "Terminal" to do script "ls -l"')
        m = obj.compileAndReturnError_.__metadata__()
        self.failUnless(m['arguments'][2]['type'].startswith('o^'))

        m = obj.executeAndReturnError_.__metadata__()
        self.failUnless(m['arguments'][2]['type'].startswith('o^'))

        m = obj.executeAppleEvent_error_.__metadata__()
        self.failUnless(m['arguments'][3]['type'].startswith('o^'))

        m = obj.initWithContentsOfURL_error_.__metadata__()
        self.failUnless(m['arguments'][3]['type'].startswith('o^'))


if __name__ == "__main__":
    main()
