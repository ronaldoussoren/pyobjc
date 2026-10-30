import Security
from PyObjCTools.TestSupport import TestCase


class TestSecCodeHost(TestCase):
    def test_constants(self):
        self.assertEqual(Security.kSecCSDedicatedHost, 1 << 0)
        self.assertEqual(Security.kSecCSGenerateGuestHash, 1 << 1)

    def test_functions(self):
        self.assertArgIsOut(Security.SecHostCreateGuest, 5)

        Security.SecHostRemoveGuest

        Security.SecHostSelectGuest

        self.assertArgIsOut(Security.SecHostSelectedGuest, 1)

        Security.SecHostSetGuestStatus

        Security.SecHostSetHostingPort
