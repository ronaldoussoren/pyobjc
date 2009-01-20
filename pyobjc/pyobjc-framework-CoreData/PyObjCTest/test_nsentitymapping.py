
from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSEntityMapping (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSUndefinedEntityMappingType, 0x00)
        self.failUnlessEqual(NSCustomEntityMappingType, 0x01)
        self.failUnlessEqual(NSAddEntityMappingType, 0x02)
        self.failUnlessEqual(NSRemoveEntityMappingType, 0x03)
        self.failUnlessEqual(NSCopyEntityMappingType, 0x04)
        self.failUnlessEqual(NSTransformEntityMappingType, 0x05)

if __name__ == "__main__":
    main()
