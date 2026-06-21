import ServiceManagement
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestSMLoginItem(TestCase):
    @min_os_level("10.6")
    def test_functions(self):
        self.assertResultIsBOOL(ServiceManagement.SMLoginItemSetEnabled)
        self.assertArgIsBOOL(ServiceManagement.SMLoginItemSetEnabled, 1)
