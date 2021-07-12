import CoreServices
from PyObjCTools.TestSupport import TestCase


class TestPLStringFuncs(TestCase):
    def assert_not_wrapped(self, name):
        self.assertTrue(
            not hasattr(CoreServices, name), f"{name!r} exposed in bindings"
        )

    def test_not_wrapped(self):
        self.assert_not_wrapped("PLstrcmp")
        self.assert_not_wrapped("PLstrncmp")
        self.assert_not_wrapped("PLstrcpy")
        self.assert_not_wrapped("PLstrncpy")
        self.assert_not_wrapped("PLstrcat")
        self.assert_not_wrapped("PLstrncat")
        self.assert_not_wrapped("PLstrchr")
        self.assert_not_wrapped("PLstrrchr")
        self.assert_not_wrapped("PLstrpbrk")
        self.assert_not_wrapped("PLstrspn")
        self.assert_not_wrapped("PLstrstr")
        self.assert_not_wrapped("PLstrlen")
        self.assert_not_wrapped("PLpos")
