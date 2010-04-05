
from PyObjCTools.TestSupport import *
from InterfaceBuilderKit import *


class TestIBObjectIntegrationHelper (NSObject):
    def ibIsChildViewUserMovable_(self, v):
        return False
    def ibIsChildViewUserSizable_(self, v):
        return False
    def ibRemoveChildren_(self, v): return True

class TestIBObjectIntegration (TestCase):
    def testContants(self):
        self.assertIsInstance(IBAttributeKeyPaths, unicode)
        self.assertIsInstance(IBToOneRelationshipKeyPaths, unicode)
        self.assertIsInstance(IBToManyRelationshipKeyPaths, unicode)
        self.assertIsInstance(IBLocalizableStringKeyPaths, unicode)
        self.assertIsInstance(IBLocalizableGeometryKeyPaths, unicode)
        self.assertIsInstance(IBAdditionalLocalizableKeyPaths, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(TestIBObjectIntegrationHelper.ibIsChildViewUserMovable_)
        self.assertResultIsBOOL(TestIBObjectIntegrationHelper.ibIsChildViewUserSizable_)
        self.assertResultIsBOOL(TestIBObjectIntegrationHelper.ibRemoveChildren_)


if __name__ == "__main__":
    main()
