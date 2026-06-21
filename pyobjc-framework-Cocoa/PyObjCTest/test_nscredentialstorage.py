import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSURLCredentialStorage(TestCase):
    def test_constants(self):
        self.assertIsInstance(Foundation.NSURLCredentialStorageChangedNotification, str)
