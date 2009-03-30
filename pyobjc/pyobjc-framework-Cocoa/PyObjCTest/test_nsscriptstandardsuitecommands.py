from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSScriptStandardSuiteCommands (TestCase):
    def testCommands(self):
        self.failUnlessEqual(NSSaveOptionsYes, 0)
        self.failUnlessEqual(NSSaveOptionsNo, 1)
        self.failUnlessEqual(NSSaveOptionsAsk, 2)

if __name__ == "__main__":
    main()
