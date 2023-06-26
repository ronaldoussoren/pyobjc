import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSAttributeDescription(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CoreData.NSAttributeType)

    def testConstants(self):
        self.assertEqual(CoreData.NSUndefinedAttributeType, 0)
        self.assertEqual(CoreData.NSInteger16AttributeType, 100)
        self.assertEqual(CoreData.NSInteger32AttributeType, 200)
        self.assertEqual(CoreData.NSInteger64AttributeType, 300)
        self.assertEqual(CoreData.NSDecimalAttributeType, 400)
        self.assertEqual(CoreData.NSDoubleAttributeType, 500)
        self.assertEqual(CoreData.NSFloatAttributeType, 600)
        self.assertEqual(CoreData.NSStringAttributeType, 700)
        self.assertEqual(CoreData.NSBooleanAttributeType, 800)
        self.assertEqual(CoreData.NSDateAttributeType, 900)
        self.assertEqual(CoreData.NSBinaryDataAttributeType, 1000)
        self.assertEqual(CoreData.NSUUIDAttributeType, 1100)
        self.assertEqual(CoreData.NSURIAttributeType, 1200)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertEqual(CoreData.NSTransformableAttributeType, 1800)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(CoreData.NSObjectIDAttributeType, 2000)
        self.assertEqual(CoreData.NSCompositeAttributeType, 2100)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(
            CoreData.NSAttributeDescription.allowsExternalBinaryDataStorage
        )
        self.assertArgIsBOOL(
            CoreData.NSAttributeDescription.setAllowsExternalBinaryDataStorage_, 0
        )

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertResultIsBOOL(
            CoreData.NSAttributeDescription.preservesValueInHistoryOnDeletion
        )
        self.assertArgIsBOOL(
            CoreData.NSAttributeDescription.setPreservesValueInHistoryOnDeletion_, 0
        )

    @min_os_level("12.0")
    def testMethods12_0(self):
        self.assertResultIsBOOL(CoreData.NSAttributeDescription.allowsCloudEncryption)
        self.assertArgIsBOOL(
            CoreData.NSAttributeDescription.setAllowsCloudEncryption_, 0
        )
