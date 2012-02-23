
from PyObjCTools.TestSupport import *
from ScriptingBridge import *

class TestSBApplicationHelper (NSObject):
    def eventDidFail_withError_(self, event, error):
        pass

class TestSBApplication (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(SBApplication.isRunning)


if __name__ == "__main__":
    main()
