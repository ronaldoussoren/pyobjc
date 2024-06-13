from PyObjCTools.TestSupport import TestCase

import FSKit


class TestFSItem(TestCase):
    def test_enum(self):
        self.assertIsEnumType(FSKit.FSItemType)
        self.assertEqual(FSKit.FSItemTypeUnknown, 0)
        self.assertEqual(FSKit.FSItemTypeFile, 1)
        self.assertEqual(FSKit.FSItemTypeDir, 2)
        self.assertEqual(FSKit.FSItemTypeSymlink, 3)
        self.assertEqual(FSKit.FSItemTypeFIFO, 4)
        self.assertEqual(FSKit.FSItemTypeCharDev, 5)
        self.assertEqual(FSKit.FSItemTypeBlockDev, 6)
        self.assertEqual(FSKit.FSItemTypeSocket, 7)

    def test_methods(self):
        self.assertArgIsOut(FSKit.FSItemAttributes.modifyTime_, 0)
        self.assertArgIsOut(FSKit.FSItemAttributes.addedTime_, 0)
        self.assertArgIsOut(FSKit.FSItemAttributes.changeTime_, 0)
        self.assertArgIsOut(FSKit.FSItemAttributes.accessTime_, 0)
        self.assertArgIsOut(FSKit.FSItemAttributes.birthTime_, 0)
        self.assertArgIsOut(FSKit.FSItemAttributes.backupTime_, 0)

        self.assertArgIsIn(FSKit.FSItemAttributes.setModifyTime_, 0)
        self.assertArgIsIn(FSKit.FSItemAttributes.setAddedTime_, 0)
        self.assertArgIsIn(FSKit.FSItemAttributes.setChangeTime_, 0)
        self.assertArgIsIn(FSKit.FSItemAttributes.setAccessTime_, 0)
        self.assertArgIsIn(FSKit.FSItemAttributes.setBirthTime_, 0)
        self.assertArgIsIn(FSKit.FSItemAttributes.setBackupTime_, 0)
