import ServiceManagement
from PyObjCTools.TestSupport import TestCase


class TestSMLoginItem(TestCase):
    def test_functions(self):
        self.assertResultIsBOOL(ServiceManagement.SMLoginItemSetEnabled)
        self.assertArgIsBOOL(ServiceManagement.SMLoginItemSetEnabled, 1)
