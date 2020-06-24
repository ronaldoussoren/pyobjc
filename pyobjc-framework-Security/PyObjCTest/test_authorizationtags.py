import Security
from PyObjCTools.TestSupport import TestCase


class TestMDS(TestCase):
    def test_constants(self):
        self.assertEqual(Security.kAuthorizationEnvironmentUsername, b"username")
        self.assertEqual(Security.kAuthorizationEnvironmentPassword, b"password")
        self.assertEqual(Security.kAuthorizationEnvironmentShared, b"shared")
        self.assertEqual(Security.kAuthorizationRightExecute, b"system.privilege.admin")
        self.assertEqual(Security.kAuthorizationEnvironmentPrompt, b"prompt")
        self.assertEqual(Security.kAuthorizationEnvironmentIcon, b"icon")
        self.assertEqual(Security.kAuthorizationPamResult, b"pam_result")
