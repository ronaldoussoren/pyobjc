import AddressBook  # noqa: F401
import objc
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestABPersonPickerDelegate(TestCase):
    @min_sdk_level("10.9")
    def test_protocols(self):
        objc.protocolNamed("ABPersonPickerDelegate")
