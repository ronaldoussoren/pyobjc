import InterfaceBuilderKit
from PyObjCTools.TestSupport import TestCase


class TestIBObjectIntegrationHelper(InterfaceBuilderKit.NSObject):
    def ibIsChildViewUserMovable_(self, v):
        return False

    def ibIsChildViewUserSizable_(self, v):
        return False

    def ibRemoveChildren_(self, v):
        return True


class TestIBObjectIntegration(TestCase):
    def testContants(self):
        self.assertIsInstance(InterfaceBuilderKit.IBAttributeKeyPaths, str)
        self.assertIsInstance(InterfaceBuilderKit.IBToOneRelationshipKeyPaths, str)
        self.assertIsInstance(InterfaceBuilderKit.IBToManyRelationshipKeyPaths, str)
        self.assertIsInstance(InterfaceBuilderKit.IBLocalizableStringKeyPaths, str)
        self.assertIsInstance(InterfaceBuilderKit.IBLocalizableGeometryKeyPaths, str)
        self.assertIsInstance(InterfaceBuilderKit.IBAdditionalLocalizableKeyPaths, str)

    def testMethods(self):
        self.assertResultIsBOOL(TestIBObjectIntegrationHelper.ibIsChildViewUserMovable_)
        self.assertResultIsBOOL(TestIBObjectIntegrationHelper.ibIsChildViewUserSizable_)
        self.assertResultIsBOOL(TestIBObjectIntegrationHelper.ibRemoveChildren_)
