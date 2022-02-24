import CoreData
from PyObjCTools.TestSupport import TestCase


class TestNSEntityMapping(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CoreData.NSEntityMappingType)

    def testConstants(self):
        self.assertEqual(CoreData.NSUndefinedEntityMappingType, 0x00)
        self.assertEqual(CoreData.NSCustomEntityMappingType, 0x01)
        self.assertEqual(CoreData.NSAddEntityMappingType, 0x02)
        self.assertEqual(CoreData.NSRemoveEntityMappingType, 0x03)
        self.assertEqual(CoreData.NSCopyEntityMappingType, 0x04)
        self.assertEqual(CoreData.NSTransformEntityMappingType, 0x05)
