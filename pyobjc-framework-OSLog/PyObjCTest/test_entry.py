import OSLog
import objc
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestEntryHelper(OSLog.NSObject):
    def activityIdentifier(self):
        return 1

    def processIdentifier(self):
        return 1

    def threadIdentifier(self):
        return 1


class TestEntry(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(OSLog.OSLogEntryStoreCategory)

    def test_constants(self):
        self.assertEqual(OSLog.OSLogEntryStoreCategoryUndefined, 0)
        self.assertEqual(OSLog.OSLogEntryStoreCategoryMetadata, 1)
        self.assertEqual(OSLog.OSLogEntryStoreCategoryShortTerm, 2)
        self.assertEqual(OSLog.OSLogEntryStoreCategoryLongTermAuto, 3)
        self.assertEqual(OSLog.OSLogEntryStoreCategoryLongTerm1, 4)
        self.assertEqual(OSLog.OSLogEntryStoreCategoryLongTerm3, 5)
        self.assertEqual(OSLog.OSLogEntryStoreCategoryLongTerm7, 6)
        self.assertEqual(OSLog.OSLogEntryStoreCategoryLongTerm14, 7)
        self.assertEqual(OSLog.OSLogEntryStoreCategoryLongTerm30, 8)

    def test_methods(self):
        self.assertResultHasType(TestEntryHelper.activityIdentifier, objc._C_NSUInteger)
        self.assertResultHasType(TestEntryHelper.processIdentifier, objc._C_INT)
        self.assertResultHasType(TestEntryHelper.threadIdentifier, objc._C_ULNGLNG)

    @min_sdk_level("10.15")
    def test_protocols(self):
        objc.protocolNamed("OSLogEntryFromProcess")
        objc.protocolNamed("OSLogEntryWithPayload")
