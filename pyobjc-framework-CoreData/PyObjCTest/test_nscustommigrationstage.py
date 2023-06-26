import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSCustomMigrationStage(TestCase):
    @min_os_level("14.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            CoreData.NSCustomMigrationStage.willMigrateHandler, b"Z@@@"
        )
        self.assertArgIsBOOL(
            CoreData.NSCustomMigrationStage.setWillMigrateHandler_, 0, b"Z@@@"
        )

        self.assertResultIsBOOL(
            CoreData.NSCustomMigrationStage.didMigrateHandler, b"Z@@@"
        )
        self.assertArgIsBOOL(
            CoreData.NSCustomMigrationStage.setDidMigrateHandler_, 0, b"Z@@@"
        )
