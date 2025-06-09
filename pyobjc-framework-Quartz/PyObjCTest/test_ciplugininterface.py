from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCIPluginInterfaceHelper(Quartz.NSObject):
    def load_(self, h):
        return 1


class TestCIPlugInInterface(TestCase):
    def no_testProtocol(self):
        self.assertProtocolExists("CIPlugInRegistration")
