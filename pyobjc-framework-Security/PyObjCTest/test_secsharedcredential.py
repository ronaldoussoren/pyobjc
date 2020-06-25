import Security
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestSecAccess(TestCase):
    @min_os_level("10.16")
    def test_constants10_16(self):
        self.assertIsInstance(Security.kSecSharedPassword, str)

    @min_os_level("10.16")
    def test_functions10_16(self):
        self.assertArgIsBlock(Security.SecAddSharedWebCredential, 3, b"v@")

        self.assertArgIsBlock(Security.SecRequestSharedWebCredential, 3, b"v@@")

        Security.SecCreateSharedWebCredentialPassword
