from PyObjCTools.TestSupport import TestCase
import XgridFoundation


class TestXGAuthenticator(TestCase):
    def testConstants(self):
        self.assertEqual(XgridFoundation.XGAuthenticatorStateUnauthenticated, 0)
        self.assertEqual(XgridFoundation.XGAuthenticatorStateAuthenticating, 1)
        self.assertEqual(XgridFoundation.XGAuthenticatorStateAuthenticated, 2)
        self.assertEqual(XgridFoundation.XGAuthenticatorStateFailed, 3)
