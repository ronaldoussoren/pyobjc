import Security
from PyObjCTools.TestSupport import TestCase


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

        self.assertArgIsOut(
            Security.SecACLCreateWithSimpleContents,
            4,
        )
        self.assertArgIsCFRetained(Security.SecACLCreateWithSimpleContents, 4)

        Security.SecACLRemove

        self.assertFalse(hasattr(Security, "SecACLCopySimpleContents"))

        self.assertArgIsOut(Security.SecACLCopyContents, 1)
        self.assertArgIsCFRetained(Security.SecACLCopyContents, 1)
        self.assertArgIsOut(Security.SecACLCopyContents, 2)
        self.assertArgIsCFRetained(Security.SecACLCopyContents, 2)
        self.assertArgIsOut(Security.SecACLCopyContents, 3)

        self.assertFalse(hasattr(Security, "SecACLSetSimpleContents"))

        Security.SecACLSetContents

        self.assertFalse(hasattr(Security, "SecACLGetAuthorizations"))

        Security.SecACLCopyAuthorizations

        self.assertFalse(hasattr(Security, "SecACLSetAuthorizations"))

        Security.SecACLUpdateAuthorizations
