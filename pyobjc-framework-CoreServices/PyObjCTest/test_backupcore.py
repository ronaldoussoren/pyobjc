import CoreServices
from PyObjCTools.TestSupport import TestCase


class TestBackupCore(TestCase):
    def test_functions(self):
        self.assertArgIsBOOL(CoreServices.CSBackupSetItemExcluded, 1)
        self.assertArgIsBOOL(CoreServices.CSBackupSetItemExcluded, 2)

        self.assertResultIsBOOL(CoreServices.CSBackupIsItemExcluded)
        self.assertArgHasType(CoreServices.CSBackupIsItemExcluded, 1, b"o^Z")
