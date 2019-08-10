from PyObjCTools.TestSupport import *

import FileProvider


class TestNSFileProviderRequest(TestCase):
    def test_constants(self):
        self.assertEqual(FileProvider.NSFileProviderPresenceAuthorizationNotDetermined, 0)
        self.assertEqual(FileProvider.NSFileProviderPresenceAuthorizationRestricted, 1)
        self.assertEqual(FileProvider.NSFileProviderPresenceAuthorizationDenied, 2)
        self.assertEqual(FileProvider.NSFileProviderPresenceAuthorizationAllowed, 3)
