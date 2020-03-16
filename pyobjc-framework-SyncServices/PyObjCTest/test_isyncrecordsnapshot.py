from PyObjCTools.TestSupport import TestCase, min_os_level
import SyncServices
import objc


class TestISyncRecordSnapshot(TestCase):
    @min_os_level("10.5")
    def testMethods(self):
        self.assertArgHasType(
            SyncServices.ISyncRecordSnapshot.recordIdentifierForReference_isModified_,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_NSBOOL,
        )
