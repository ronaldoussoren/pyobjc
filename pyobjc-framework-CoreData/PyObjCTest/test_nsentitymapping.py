
from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSEntityMapping (TestCase):
    def testConstants(self):
        self.assertEqual(NSUndefinedEntityMappingType, 0x00)
        self.assertEqual(NSCustomEntityMappingType, 0x01)
        self.assertEqual(NSAddEntityMappingType, 0x02)
        self.assertEqual(NSRemoveEntityMappingType, 0x03)
        self.assertEqual(NSCopyEntityMappingType, 0x04)
        self.assertEqual(NSTransformEntityMappingType, 0x05)

if __name__ == "__main__":
    main()
