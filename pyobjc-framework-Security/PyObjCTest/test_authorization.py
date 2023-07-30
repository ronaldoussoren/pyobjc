import Security
from PyObjCTools.TestSupport import TestCase
import objc


class TestAuthorization(TestCase):
    def test_types(self):
        self.assertIsOpaquePointer(Security.AuthorizationRef)

    def test_structs(self):
        v = Security.AuthorizationExternalForm()
        self.assertEqual(v.bytes, None)
        self.assertPickleRoundTrips(v)

        v.bytes = b"\x00" * 32
        self.assertPickleRoundTrips(v)

        w = objc.repythonify(v, Security.AuthorizationExternalForm.__typestr__)
        self.assertIsInstance(w, Security.AuthorizationExternalForm)
        self.assertEqual(w.bytes, (0,) * 32)
        self.assertPickleRoundTrips(w)

    def test_constants(self):
        self.assertEqual(Security.kAuthorizationExternalFormLength, 32)
        self.assertEqual(Security.kAuthorizationEmptyEnvironment, None)

        self.assertEqual(Security.errAuthorizationSuccess, 0)
        self.assertEqual(Security.errAuthorizationInvalidSet, -60001)
        self.assertEqual(Security.errAuthorizationInvalidRef, -60002)
        self.assertEqual(Security.errAuthorizationInvalidTag, -60003)
        self.assertEqual(Security.errAuthorizationInvalidPointer, -60004)
        self.assertEqual(Security.errAuthorizationDenied, -60005)
        self.assertEqual(Security.errAuthorizationCanceled, -60006)
        self.assertEqual(Security.errAuthorizationInteractionNotAllowed, -60007)
        self.assertEqual(Security.errAuthorizationInternal, -60008)
        self.assertEqual(Security.errAuthorizationExternalizeNotAllowed, -60009)
        self.assertEqual(Security.errAuthorizationInternalizeNotAllowed, -60010)
        self.assertEqual(Security.errAuthorizationInvalidFlags, -60011)
        self.assertEqual(Security.errAuthorizationToolExecuteFailure, -60031)
        self.assertEqual(Security.errAuthorizationToolEnvironmentError, -60032)
        self.assertEqual(Security.errAuthorizationBadAddress, -60033)

        self.assertEqual(Security.kAuthorizationFlagDefaults, 0)
        self.assertEqual(Security.kAuthorizationFlagInteractionAllowed, 1 << 0)
        self.assertEqual(Security.kAuthorizationFlagExtendRights, 1 << 1)
        self.assertEqual(Security.kAuthorizationFlagPartialRights, 1 << 2)
        self.assertEqual(Security.kAuthorizationFlagDestroyRights, 1 << 3)
        self.assertEqual(Security.kAuthorizationFlagPreAuthorize, 1 << 4)
        self.assertEqual(Security.kAuthorizationFlagSkipInternalAuth, 1 << 9)

        self.assertEqual(Security.kAuthorizationFlagNoData, 1 << 20)

        self.assertEqual(Security.kAuthorizationFlagCanNotPreAuthorize, 1 << 0)

    def test_functions(self):
        self.assertResultHasType(Security.AuthorizationFree, objc._C_INT)
        self.assertArgHasType(
            Security.AuthorizationFree, 0, Security.AuthorizationRef.__typestr__
        )
        self.assertArgHasType(Security.AuthorizationFree, 1, objc._C_UINT)

        self.assertResultHasType(Security.AuthorizationMakeExternalForm, objc._C_INT)
        self.assertArgHasType(
            Security.AuthorizationMakeExternalForm,
            0,
            Security.AuthorizationRef.__typestr__,
        )
        self.assertArgHasType(
            Security.AuthorizationMakeExternalForm,
            1,
            objc._C_OUT + objc._C_PTR + Security.AuthorizationExternalForm.__typestr__,
        )

        self.assertResultHasType(
            Security.AuthorizationCreateFromExternalForm, objc._C_INT
        )
        self.assertArgHasType(
            Security.AuthorizationCreateFromExternalForm,
            0,
            objc._C_IN + objc._C_PTR + Security.AuthorizationExternalForm.__typestr__,
        )
        self.assertArgHasType(
            Security.AuthorizationCreateFromExternalForm,
            1,
            objc._C_OUT + objc._C_PTR + Security.AuthorizationRef.__typestr__,
        )

        self.assertResultHasType(
            Security.AuthorizationCopyPrivilegedReference, objc._C_INT
        )
        self.assertArgHasType(
            Security.AuthorizationCopyPrivilegedReference,
            0,
            objc._C_OUT + objc._C_PTR + Security.AuthorizationRef.__typestr__,
        )

    def test_functions_manual(self):
        status, authref = Security.AuthorizationCreate(None, None, 0, None)
        self.assertEqual(status, 0)
        self.assertIsInstance(authref, Security.AuthorizationRef)

        status, info = Security.AuthorizationCopyInfo(authref, None, None)
        self.assertEqual(status, 0)
        self.assertEqual(info, ())

        status, info = Security.AuthorizationCopyInfo(authref, b"username", None)
        self.assertEqual(status, 0)
        self.assertEqual(info, ())

        Security.AuthorizationFree(authref, 0)

        rights = (
            Security.AuthorizationItem(
                name=b"system.services.systemconfiguration.network"
            ),
        )

        status, authref = Security.AuthorizationCreate(rights, None, 0, None)
        self.assertNotEqual(status, 0)
        self.assertIs(authref, None)

        self.assertFalse(hasattr(Security, "AuthorizationFreeItemSet"))

        # Not sure how to test this without increased privileges....
        self.assertFalse(isinstance(Security.AuthorizationCopyRights, objc.function))
        self.assertFalse(
            isinstance(Security.AuthorizationCopyRightsAsync, objc.function)
        )
        self.assertFalse(
            isinstance(Security.AuthorizationExecuteWithPrivileges, objc.function)
        )
