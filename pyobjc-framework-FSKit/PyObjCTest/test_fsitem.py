from PyObjCTools.TestSupport import TestCase

import FSKit


class TestFSItem(TestCase):
    def test_enum(self):
        self.assertIsEnumType(FSKit.FSItemAttribute)
        self.assertEqual(FSKit.FSItemAttributeUID, 1 << 0)
        self.assertEqual(FSKit.FSItemAttributeGID, 1 << 1)
        self.assertEqual(FSKit.FSItemAttributeMode, 1 << 2)
        self.assertEqual(FSKit.FSItemAttributeType, 1 << 3)
        self.assertEqual(FSKit.FSItemAttributeLinkCount, 1 << 4)
        self.assertEqual(FSKit.FSItemAttributeFlags, 1 << 5)
        self.assertEqual(FSKit.FSItemAttributeSize, 1 << 6)
        self.assertEqual(FSKit.FSItemAttributeAllocSize, 1 << 7)
        self.assertEqual(FSKit.FSItemAttributeFileID, 1 << 8)
        self.assertEqual(FSKit.FSItemAttributeParentID, 1 << 9)
        self.assertEqual(FSKit.FSItemAttributeSupportsLimitedXAttrs, 1 << 10)
        self.assertEqual(FSKit.FSItemAttributeInhibitKOIO, 1 << 11)
        self.assertEqual(FSKit.FSItemAttributeModifyTime, 1 << 12)
        self.assertEqual(FSKit.FSItemAttributeAddedTime, 1 << 13)
        self.assertEqual(FSKit.FSItemAttributeChangeTime, 1 << 14)
        self.assertEqual(FSKit.FSItemAttributeAccessTime, 1 << 15)
        self.assertEqual(FSKit.FSItemAttributeBirthTime, 1 << 16)
        self.assertEqual(FSKit.FSItemAttributeBackupTime, 1 << 17)

        self.assertIsEnumType(FSKit.FSItemType)
        self.assertEqual(FSKit.FSItemTypeUnknown, 0)
        self.assertEqual(FSKit.FSItemTypeFile, 1)
        self.assertEqual(FSKit.FSItemTypeDirectory, 2)
        self.assertEqual(FSKit.FSItemTypeSymlink, 3)
        self.assertEqual(FSKit.FSItemTypeFIFO, 4)
        self.assertEqual(FSKit.FSItemTypeCharDevice, 5)
        self.assertEqual(FSKit.FSItemTypeBlockDevice, 6)
        self.assertEqual(FSKit.FSItemTypeSocket, 7)

    def test_methods(self):
        self.assertResultIsBOOL(FSKit.FSItemAttributes.supportsLimitedXAttrs)
        self.assertArgIsBOOL(FSKit.FSItemAttributes.setSupportsLimitedXAttrs_, 0)

        self.assertResultIsBOOL(FSKit.FSItemAttributes.inhibitKOIO)
        self.assertArgIsBOOL(FSKit.FSItemAttributes.setInhibitKOIO_, 0)

        self.assertResultIsBOOL(FSKit.FSItemAttributes.isValid_)

        self.assertResultIsBOOL(FSKit.FSItemSetAttributesRequest.wasConsumed_)
        self.assertResultIsBOOL(FSKit.FSItemGetAttributesRequest.isWanted_)
