from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCIPluginInterfaceHelper(Quartz.NSObject):
    def load_(self, h):
        return 1


class TestCIPlugInInterface(TestCase):
    def no_test_protocols(self):
        self.assertProtocolExists("CIPlugInRegistration", Quartz)
