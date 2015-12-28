from PyObjCTools.TestSupport import *
from Foundation import *

class TestNSURLCredentialStorage (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSURLCredentialStorageChangedNotification, unicode)

    @min_os_level('10.9')
    def testConstants10_9(self):
        self.assertIsInstance(NSURLCredentialStorageRemoveSynchronizableCredentials, unicode)

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertArgIsBlock(NSURLCredentialStorage.getCredentialsForProtectionSpace_task_completionHandler_, 2, b'v@')
        self.assertArgIsBlock(NSURLCredentialStorage.getDefaultCredentialForProtectionSpace_task_completionHandler_, 2, b'v@')


if __name__ == "__main__":
    main()
