import AppKit  # noqa: F401
from PyObjCTools.TestSupport import TestCase


class TestNSSpellProtocol(TestCase):
    def testProtocols(self):
        self.assertProtocolExists("NSChangeSpelling")
        self.assertProtocolExists("NSIgnoreMisspelledWords")
