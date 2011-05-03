
from PyObjCTools.TestSupport import *
from ScriptingBridge import *

class TestSBApplication (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(SBApplication.isRunning)

    def testProtocols(self):
        self.assertIsInstance(protocols.SBApplicationDelegate, objc.informal_protocol)


if __name__ == "__main__":
    main()
