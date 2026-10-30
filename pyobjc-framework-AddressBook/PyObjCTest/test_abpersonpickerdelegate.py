import AddressBook  # noqa: F401
from PyObjCTools.TestSupport import TestCase


class TestABPersonPickerDelegate(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("ABPersonPickerDelegate", AddressBook)
