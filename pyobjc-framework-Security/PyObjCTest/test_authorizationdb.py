import Security
from PyObjCTools.TestSupport import TestCase
import objc


class TestAuthorizationDB(TestCase):
    def test_constants(self):
        self.assertEqual(Security.kAuthorizationRightRule, b"rule")
        self.assertEqual(Security.kAuthorizationRuleIsAdmin, b"is-admin")
        self.assertEqual(
            Security.kAuthorizationRuleAuthenticateAsSessionUser,
            b"authenticate-session-owner",
        )
        self.assertEqual(
            Security.kAuthorizationRuleAuthenticateAsAdmin, b"authenticate-admin"
        )
        self.assertEqual(Security.kAuthorizationRuleClassAllow, b"allow")
        self.assertEqual(Security.kAuthorizationRuleClassDeny, b"deny")
        self.assertEqual(Security.kAuthorizationComment, b"comment")

    def test_functions(self):
        self.assertResultHasType(Security.AuthorizationRightGet, objc._C_INT)
        self.assertArgHasType(
            Security.AuthorizationRightGet,
            0,
            objc._C_IN + objc._C_PTR + objc._C_CHAR_AS_TEXT,
        )
        self.assertArgIsNullTerminated(Security.AuthorizationRightGet, 0)
        self.assertArgHasType(
            Security.AuthorizationRightGet, 1, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
        self.assertArgIsRetained(
            Security.AuthorizationRightGet, 1, objc._C_OUT + objc._C_PTR + objc._C_ID
        )

        self.assertResultHasType(Security.AuthorizationRightSet, objc._C_INT)
        self.assertArgHasType(
            Security.AuthorizationRightSet, 0, Security.AuthorizationRef.__typestr__
        )
        self.assertArgHasType(
            Security.AuthorizationRightSet,
            1,
            objc._C_IN + objc._C_PTR + objc._C_CHAR_AS_TEXT,
        )
        self.assertArgIsNullTerminated(Security.AuthorizationRightSet, 1)
        self.assertArgHasType(Security.AuthorizationRightSet, 2, objc._C_ID)
        self.assertArgHasType(Security.AuthorizationRightSet, 3, objc._C_ID)
        self.assertArgHasType(Security.AuthorizationRightSet, 4, objc._C_ID)
        self.assertArgHasType(Security.AuthorizationRightSet, 5, objc._C_ID)

        self.assertResultHasType(Security.AuthorizationRightRemove, objc._C_INT)
        self.assertArgHasType(
            Security.AuthorizationRightRemove, 0, Security.AuthorizationRef.__typestr__
        )
        self.assertArgHasType(
            Security.AuthorizationRightRemove,
            1,
            objc._C_IN + objc._C_PTR + objc._C_CHAR_AS_TEXT,
        )
        self.assertArgIsNullTerminated(Security.AuthorizationRightRemove, 1)
