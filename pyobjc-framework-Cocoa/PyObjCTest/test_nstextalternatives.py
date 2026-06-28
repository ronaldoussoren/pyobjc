import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSTextAlternatives(TestCase):
    def test_constants(self):
        self.assertIsInstance(
            AppKit.NSTextAlternativesSelectedAlternativeStringNotification, str
        )
