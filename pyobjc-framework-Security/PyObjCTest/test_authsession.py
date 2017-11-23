from PyObjCTools.TestSupport import *

import Security

class TestAuthSession (TestCase):

    def test_constants(self):
        self.assertEqual(Security.noSecuritySession, 0)
        self.assertEqual(Security.callerSecuritySession, -1)

        self.assertEqual(Security.sessionIsRoot, 0x0001)
        self.assertEqual(Security.sessionHasGraphicAccess, 0x0010)
        self.assertEqual(Security.sessionHasTTY, 0x0020)
        self.assertEqual(Security.sessionIsRemote, 0x1000)

        self.assertEqual(Security.sessionKeepCurrentBootstrap, 0x8000)

        self.assertEqual(Security.errSessionSuccess, 0)
        self.assertEqual(Security.errSessionInvalidId, -60500)
        self.assertEqual(Security.errSessionInvalidAttributes, -60501)
        self.assertEqual(Security.errSessionAuthorizationDenied, -60502)
        self.assertEqual(Security.errSessionValueNotSet, -60503)
        self.assertEqual(Security.errSessionInternal, Security.errAuthorizationInternal)
        self.assertEqual(Security.errSessionInvalidFlags, Security.errAuthorizationInvalidFlags)

    def test_functions(self):
        self.assertResultHasType(Security.SessionGetInfo, objc._C_INT)
        self.assertArgHasType(Security.SessionGetInfo, 0, objc._C_UINT)
        self.assertArgHasType(Security.SessionGetInfo, 1, objc._C_OUT + objc._C_PTR + objc._C_UINT)
        self.assertArgHasType(Security.SessionGetInfo, 2, objc._C_OUT + objc._C_PTR + objc._C_UINT)

        self.assertResultHasType(Security.SessionCreate, objc._C_INT)
        self.assertArgHasType(Security.SessionCreate, 0, objc._C_UINT)
        self.assertArgHasType(Security.SessionCreate, 1, objc._C_UINT)


if __name__ == "__main__":
    main()
