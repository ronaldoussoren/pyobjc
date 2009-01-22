
from PyObjCTools.TestSupport import *
from ScriptingBridge import *

class TestSBApplication (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(SBApplication.isRunning)

    def testProtocols(self):
        self.failUnlessIsInstance(protocols.SBApplicationDelegate, objc.informal_protocol)


if __name__ == "__main__":
    main()
