from PyObjCTools.TestSupport import TestCase

import UniformTypeIdentifiers


class TestUTType(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(UniformTypeIdentifiers.UTType.isDynamic)
        self.assertResultIsBOOL(UniformTypeIdentifiers.UTType.isDeclared)
        self.assertResultIsBOOL(UniformTypeIdentifiers.UTType.isPublicType)

        self.assertResultIsBOOL(UniformTypeIdentifiers.UTType.conformsToType_)
        self.assertResultIsBOOL(UniformTypeIdentifiers.UTType.isSupertypeOfType_)
        self.assertResultIsBOOL(UniformTypeIdentifiers.UTType.isSubtypeOfType_)
