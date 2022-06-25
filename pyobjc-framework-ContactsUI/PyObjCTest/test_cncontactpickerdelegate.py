from PyObjCTools.TestSupport import TestCase, min_os_level
import ContactsUI  # noqa: F401


class TestCNContactPickerDelegate(TestCase):
    @min_os_level("10.11")
    def testProtocols(self):
        self.assertProtocolExists("CNContactPickerDelegate")
