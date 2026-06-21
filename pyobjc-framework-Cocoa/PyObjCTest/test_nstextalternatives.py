import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSTextAlternatives(TestCase):
    @min_os_level("10.8")
    def test_constants10_8(self):
        self.assertIsInstance(
            AppKit.NSTextAlternativesSelectedAlternativeStringNotification, str
        )
