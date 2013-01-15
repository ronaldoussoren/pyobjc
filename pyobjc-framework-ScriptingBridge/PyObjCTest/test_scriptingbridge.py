from PyObjCTools.TestSupport import *
import objc
from ScriptingBridge import *

class TestSBApplicationHelper (NSObject):
    def eventDidFail_withError_(self, event, error):
        pass

class TestSBApplication (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(SBApplication.isRunning)

    def testProtocols(self):
        objc.protocolNamed('SBApplicationDelegate')


if __name__ == "__main__":
    main()
