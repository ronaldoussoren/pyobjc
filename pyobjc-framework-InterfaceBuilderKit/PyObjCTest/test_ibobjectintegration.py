
from PyObjCTools.TestSupport import *
from InterfaceBuilderKit import *


class TestIBObjectIntegrationHelper (NSObject):
    def ibIsChildViewUserMovable_(self, v):
        return False
    def ibIsChildViewUserSizable_(self, v):
        return False

class TestIBObjectIntegration (TestCase):
    def testContants(self):
        self.failUnlessIsInstance(IBAttributeKeyPaths, unicode)
        self.failUnlessIsInstance(IBToOneRelationshipKeyPaths, unicode)
        self.failUnlessIsInstance(IBToManyRelationshipKeyPaths, unicode)
        self.failUnlessIsInstance(IBLocalizableStringKeyPaths, unicode)
        self.failUnlessIsInstance(IBLocalizableGeometryKeyPaths, unicode)
        self.failUnlessIsInstance(IBAdditionalLocalizableKeyPaths, unicode)

    def testMethods(self):
        self.failUnlessResultIsBOOL(TestIBObjectIntegrationHelper.ibIsChildViewUserMovable_)
        self.failUnlessResultIsBOOL(TestIBObjectIntegrationHelper.ibIsChildViewUserSizable_)


if __name__ == "__main__":
    main()
