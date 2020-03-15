import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSURLCredentialStorage(TestCase):
    def testConstants(self):
        self.assertIsInstance(Foundation.NSURLCredentialStorageChangedNotification, str)
