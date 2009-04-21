
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *
from Quartz import *

class TestCIPluginInterfaceHelper (NSObject):
    def load_(self, h): return 1

class TestCIPlugInInterface (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(TestCIPluginInterfaceHelper.load_)

    def no_testProtocol(self):
        p = objc.protocolNamed('CIPlugInRegistration')
        self.failUnlessIsInstancE(p, objc.formal_protocol)

if __name__ == "__main__":
    main()
