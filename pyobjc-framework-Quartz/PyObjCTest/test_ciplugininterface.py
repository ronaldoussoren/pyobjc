from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCIPluginInterfaceHelper(Quartz.NSObject):
    def load_(self, h):
        return 1


class TestCIPlugInInterface(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("CIPlugInRegistration", Quartz)

    def test_protocol_methods(self):
        self.assertResultIsBOOL(TestCIPluginInterfaceHelper.load_)
