import OSLog
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestStore(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(OSLog.OSLogStoreScope)

    def test_constants(self):
        self.assertEqual(OSLog.OSLogStoreSystem, 0)
        self.assertEqual(OSLog.OSLogStoreCurrentProcessIdentifier, 1)

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsOut(OSLog.OSLogStore.localStoreAndReturnError_, 0)
        self.assertArgIsOut(OSLog.OSLogStore.storeWithURL_error_, 1)
        self.assertArgIsOut(
            OSLog.OSLogStore.entriesEnumeratorWithOptions_position_predicate_error_, 3
        )
        self.assertArgIsOut(OSLog.OSLogStore.entriesEnumeratorAndReturnError_, 0)

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertArgIsOut(OSLog.OSLogStore.storeWithScope_error_, 1)
