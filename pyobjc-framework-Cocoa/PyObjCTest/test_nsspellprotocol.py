import AppKit  # noqa: F401
import objc
from PyObjCTools.TestSupport import TestCase


class TestNSSpellProtocol(TestCase):
    def testProtocols(self):
        objc.protocolNamed("NSChangeSpelling")
        objc.protocolNamed("NSIgnoreMisspelledWords")
