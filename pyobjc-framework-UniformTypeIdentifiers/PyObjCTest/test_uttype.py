from PyObjCTools.TestSupport import TestCase, min_os_level

import UniformTypeIdentifiers


class TestUTType(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(UniformTypeIdentifiers.UTType.isDynamic)
        self.assertResultIsBOOL(UniformTypeIdentifiers.UTType.isDeclared)
        self.assertResultIsBOOL(UniformTypeIdentifiers.UTType.isPublicType)

        self.assertResultIsBOOL(UniformTypeIdentifiers.UTType.conformsToType_)
        self.assertResultIsBOOL(UniformTypeIdentifiers.UTType.isSupertypeOfType_)
        self.assertResultIsBOOL(UniformTypeIdentifiers.UTType.isSubtypeOfType_)

    @min_os_level("27.0")
    def test_methods27_0(self):
        self.assertArgIsBOOL(
            UniformTypeIdentifiers.UTType.typeWithIdentifier_allowUndeclared_, 1
        )
