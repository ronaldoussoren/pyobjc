import OSLog
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestStore(TestCase):
    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsOut(OSLog.OSLogStore.localStoreAndReturnError_, 0)
        self.assertArgIsOut(OSLog.OSLogStore.storeWithURL_error_, 1)
        self.assertArgIsOut(
            OSLog.OSLogStore.entriesEnumeratorWithOptions_position_predicate_error_, 3
        )
        self.assertArgIsOut(OSLog.OSLogStore.entriesEnumeratorAndReturnError_, 0)
