from PyObjCTools.TestSupport import TestCase

import FSKit


class TestFSModuleIdentity(TestCase):
    def test_constants(self):
        self.assertIsTypedEnum(FSKit.FSModuleIdentityAttribute, str)
        self.assertIsInstance(FSKit.FSModuleIdentityAttributeSupportsServerURLs, str)
        self.assertIsInstance(
            FSKit.FSModuleIdentityAttributeSupportsBlockResources, str
        )
        self.assertIsInstance(FSKit.FSModuleIdentityAttributeSupportsKOIO, str)
        self.assertIsInstance(FSKit.FSModuleIdentityAttributeShortName, str)
        self.assertIsInstance(FSKit.FSModuleIdentityAttributeMediaTypes, str)
        self.assertIsInstance(FSKit.FSModuleIdentityAttributePersonalities, str)
        self.assertIsInstance(FSKit.FSModuleIdentityAttributeCheckOptionSyntax, str)
        self.assertIsInstance(FSKit.FSModuleIdentityAttributeFormatOptionSyntax, str)
        self.assertIsInstance(FSKit.FSModuleIdentityAttributeActivateOptionSyntax, str)

    def test_methods(self):
        self.assertResultIsBOOL(FSKit.FSModuleIdentity.isEnabled)
        self.assertResultIsBOOL(FSKit.FSModuleIdentity.isSystem)
