from PyObjCTools.TestSupport import TestCase
import SyncServices
import objc


class TestISyncRecordSnapshot(TestCase):
    def test_methods(self):
        self.assertArgHasType(
            SyncServices.ISyncRecordSnapshot.recordIdentifierForReference_isModified_,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_NSBOOL,
        )
