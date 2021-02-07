from PyObjCTools.TestSupport import TestCase
import Quartz
import objc


class TestCIPluginInterfaceHelper(Quartz.NSObject):
    def load_(self, h):
        return 1


class TestCIPlugInInterface(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(TestCIPluginInterfaceHelper.load_)

    def no_testProtocol(self):
        p = objc.protocolNamed("CIPlugInRegistration")
        self.assertIsInstancE(p, objc.formal_protocol)
