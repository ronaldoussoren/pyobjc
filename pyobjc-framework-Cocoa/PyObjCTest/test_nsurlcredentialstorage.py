import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSURLCredentialStorage(TestCase):
    def testConstants(self):
        self.assertIsInstance(Foundation.NSURLCredentialStorageChangedNotification, str)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(
            Foundation.NSURLCredentialStorageRemoveSynchronizableCredentials, str
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsBlock(
            Foundation.NSURLCredentialStorage.getCredentialsForProtectionSpace_task_completionHandler_,  # noqa: B950
            2,
            b"v@",
        )
        self.assertArgIsBlock(
            Foundation.NSURLCredentialStorage.getDefaultCredentialForProtectionSpace_task_completionHandler_,  # noqa: B950
            2,
            b"v@",
        )
