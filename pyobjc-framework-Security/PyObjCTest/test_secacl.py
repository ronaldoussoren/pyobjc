import Security
from PyObjCTools.TestSupport import TestCase
import objc


class TestSecACL(TestCase):
    def test_types(self):
        self.assertIsCFType(Security.SecACLRef)

    def test_constants(self):

        self.assertEqual(Security.kSecKeychainPromptRequirePassphase, 0x0001)
        self.assertEqual(Security.kSecKeychainPromptUnsigned, 0x0010)
        self.assertEqual(Security.kSecKeychainPromptUnsignedAct, 0x0020)
        self.assertEqual(Security.kSecKeychainPromptInvalid, 0x0040)
        self.assertEqual(Security.kSecKeychainPromptInvalidAct, 0x0080)

    def test_functions(self):
        self.assertIsInstance(Security.SecACLGetTypeID(), int)

        self.assertFalse(hasattr(Security, "SecACLCreateFromSimpleContents"))

        self.assertResultHasType(Security.SecACLCreateWithSimpleContents, objc._C_INT)
        self.assertArgHasType(Security.SecACLCreateWithSimpleContents, 0, objc._C_ID)
        self.assertArgHasType(Security.SecACLCreateWithSimpleContents, 1, objc._C_ID)
        self.assertArgHasType(Security.SecACLCreateWithSimpleContents, 2, objc._C_ID)
        self.assertArgHasType(Security.SecACLCreateWithSimpleContents, 3, objc._C_USHT)
        self.assertArgHasType(
            Security.SecACLCreateWithSimpleContents,
            4,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )
        self.assertArgIsCFRetained(Security.SecACLCreateWithSimpleContents, 4)

        self.assertResultHasType(Security.SecACLRemove, objc._C_INT)
        self.assertArgHasType(Security.SecACLRemove, 0, objc._C_ID)

        self.assertFalse(hasattr(Security, "SecACLCopySimpleContents"))

        self.assertResultHasType(Security.SecACLCopyContents, objc._C_INT)
        self.assertArgHasType(Security.SecACLCopyContents, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecACLCopyContents, 1, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
        self.assertArgIsCFRetained(Security.SecACLCopyContents, 1)
        self.assertArgHasType(
            Security.SecACLCopyContents, 2, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
        self.assertArgIsCFRetained(Security.SecACLCopyContents, 2)
        self.assertArgHasType(
            Security.SecACLCopyContents, 3, objc._C_OUT + objc._C_PTR + objc._C_USHT
        )

        self.assertFalse(hasattr(Security, "SecACLSetSimpleContents"))

        self.assertResultHasType(Security.SecACLSetContents, objc._C_INT)
        self.assertArgHasType(Security.SecACLSetContents, 0, objc._C_ID)
        self.assertArgHasType(Security.SecACLSetContents, 1, objc._C_ID)
        self.assertArgHasType(Security.SecACLSetContents, 2, objc._C_ID)
        self.assertArgHasType(Security.SecACLSetContents, 3, objc._C_USHT)

        self.assertFalse(hasattr(Security, "SecACLGetAuthorizations"))

        self.assertResultHasType(Security.SecACLCopyAuthorizations, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecACLCopyAuthorizations)
        self.assertArgHasType(Security.SecACLCopyAuthorizations, 0, objc._C_ID)

        self.assertFalse(hasattr(Security, "SecACLSetAuthorizations"))

        self.assertResultHasType(Security.SecACLUpdateAuthorizations, objc._C_INT)
        self.assertArgHasType(Security.SecACLUpdateAuthorizations, 0, objc._C_ID)
        self.assertArgHasType(Security.SecACLUpdateAuthorizations, 1, objc._C_ID)
