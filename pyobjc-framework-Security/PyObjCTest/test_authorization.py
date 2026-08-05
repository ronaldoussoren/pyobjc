import Security
from PyObjCTools.TestSupport import TestCase, NoObjCClass
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
        with self.assertRaisesRegex(TypeError, "expected 4 arguments, got 0"):
            Security.AuthorizationCreate()

        with self.assertRaisesRegex(TypeError, "'int' object is not iterable"):
            Security.AuthorizationCreate(42, None, 0, None)

        with self.assertRaisesRegex(TypeError, "'int' object is not iterable"):
            Security.AuthorizationCreate(None, 42, 0, None)

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned int', got 'str'"
        ):
            Security.AuthorizationCreate(None, None, "0", None)

        with self.assertRaisesRegex(ValueError, "authorization must be None"):
            Security.AuthorizationCreate(None, None, 0, 42)

        status, authref = Security.AuthorizationCreate(None, None, 0, None)
        self.assertEqual(status, 0)
        self.assertIsInstance(authref, Security.AuthorizationRef)

        with self.assertRaisesRegex(TypeError, "expected 3 arguments, got 0"):
            Security.AuthorizationCopyInfo()

        with self.assertRaisesRegex(
            TypeError,
            "Need instance of objc.AuthorizationRef, got instance of NoObjCClass",
        ):
            Security.AuthorizationCopyInfo(NoObjCClass(), None, None)

        with self.assertRaisesRegex(ValueError, "tag must be byte string or None"):
            Security.AuthorizationCopyInfo(None, "hello", None)

        with self.assertRaisesRegex(ValueError, "info must be None"):
            Security.AuthorizationCopyInfo(None, None, "hello")

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

        # XXX: Create a valid authref

        # Not sure how to test this without increased privileges....

        # SYNC
        with self.assertRaisesRegex(TypeError, "expected 5 arguments, got 0"):
            Security.AuthorizationCopyRights()

        with self.assertRaisesRegex(
            TypeError,
            "Need instance of objc.AuthorizationRef, got instance of NoObjCClass",
        ):
            Security.AuthorizationCopyRights(NoObjCClass(), [], [], 0, None)

        with self.assertRaisesRegex(TypeError, "'int' object is not iterable"):
            Security.AuthorizationCopyRights(authref, 42, [], 0, None)

        with self.assertRaisesRegex(TypeError, "'int' object is not iterable"):
            Security.AuthorizationCopyRights(authref, [], 42, 0, None)

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned int', got 'str'"
        ):
            Security.AuthorizationCopyRights(authref, [], [], "0", None)

        with self.assertRaisesRegex(
            ValueError, "authorizedRights must be None or objc.NULL"
        ):
            Security.AuthorizationCopyRights(authref, [], [], 0, 42)

        # status, item  = Security.AuthorizationCopyRights(authref, [], [], 0, None)
        # self.assertEqual(status, 0)
        # self.assertIsNot(item, None)

        # ASYNC

        # Not sure how to test this without increased privileges....
        items = []

        def callback(status, rights):
            items.append((status, rights))

        with self.assertRaisesRegex(TypeError, "expected 5 arguments, got 0"):
            Security.AuthorizationCopyRightsAsync()

        with self.assertRaisesRegex(
            TypeError,
            "Need instance of objc.AuthorizationRef, got instance of NoObjCClass",
        ):
            Security.AuthorizationCopyRightsAsync(NoObjCClass(), [], [], 0, callback)

        with self.assertRaisesRegex(TypeError, "'int' object is not iterable"):
            Security.AuthorizationCopyRightsAsync(authref, 42, [], 0, callback)

        with self.assertRaisesRegex(TypeError, "'int' object is not iterable"):
            Security.AuthorizationCopyRightsAsync(authref, [], 42, 0, callback)

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned int', got 'str'"
        ):
            Security.AuthorizationCopyRightsAsync(authref, [], [], "0", callback)

        with self.assertRaisesRegex(ValueError, "callback must be callable"):
            Security.AuthorizationCopyRightsAsync(authref, [], [], 0, 42)

        # status, item  = Security.AuthorizationCopyRightsAsync(authref, [], [], 0, callback)
        # self.assertEqual(status, 0)
        # self.assertIsNot(item, None)

        # Execute

        # XXX: Create authref

        with self.assertRaisesRegex(TypeError, "expected 5 arguments, got 0"):
            Security.AuthorizationExecuteWithPrivileges()

        with self.assertRaisesRegex(
            TypeError,
            "Need instance of objc.AuthorizationRef, got instance of NoObjCClass",
        ):
            Security.AuthorizationExecuteWithPrivileges(
                NoObjCClass(), b"/usr/bin/id", 0, [b"id", b"-u"], None
            )

        with self.assertRaisesRegex(ValueError, "pathToTool must be a bytes string"):
            Security.AuthorizationExecuteWithPrivileges(
                authref, "/usr/bin/id", 0, [b"id", b"-u"], None
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned int', got 'str'"
        ):
            Security.AuthorizationExecuteWithPrivileges(
                authref, b"/usr/bin/id", "0", [b"id", b"-u"], None
            )

        with self.assertRaisesRegex(TypeError, "'int' object is not iterable"):
            Security.AuthorizationExecuteWithPrivileges(
                authref, b"/usr/bin/id", 0, 42, None
            )

        with self.assertRaisesRegex(
            ValueError, "arguments must be a sequence of byte strings"
        ):
            Security.AuthorizationExecuteWithPrivileges(
                authref, b"/usr/bin/id", 0, [b"id", "-g"], None
            )

        with self.assertRaisesRegex(
            ValueError, "communicationsPipe must be None or objc.NULL"
        ):
            Security.AuthorizationExecuteWithPrivileges(
                authref, b"/usr/bin/id", 0, [b"id", b"-g"], 42
            )

        # status, pipe = Security.AuthorizationExecuteWithPrivileges(authref, b"/usr/bin/id", 0, [b"id", b"-u"], None)
        # self.assertEqual(status, 0)
        # self.assertIsNot(pipe, None)

        self.fail("incomplete tests")
