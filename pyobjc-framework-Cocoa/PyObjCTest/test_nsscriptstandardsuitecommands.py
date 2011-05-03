from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSScriptStandardSuiteCommands (TestCase):
    def testCommands(self):
        self.assertEqual(NSSaveOptionsYes, 0)
        self.assertEqual(NSSaveOptionsNo, 1)
        self.assertEqual(NSSaveOptionsAsk, 2)

if __name__ == "__main__":
    main()
