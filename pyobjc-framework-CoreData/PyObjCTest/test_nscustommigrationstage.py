import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSCustomMigrationStage(TestCase):
    @min_os_level("14.0")
    def test_methods(self):
        self.assertResultIsBlock(
            CoreData.NSCustomMigrationStage.willMigrateHandler, b"Z@@@"
        )
        self.assertArgIsBlock(
            CoreData.NSCustomMigrationStage.setWillMigrateHandler_, 0, b"Z@@@"
        )

        self.assertResultIsBlock(
            CoreData.NSCustomMigrationStage.didMigrateHandler, b"Z@@@"
        )
        self.assertArgIsBlock(
            CoreData.NSCustomMigrationStage.setDidMigrateHandler_, 0, b"Z@@@"
        )
