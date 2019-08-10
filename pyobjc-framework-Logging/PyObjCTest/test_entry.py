import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import Logging

    class TestEntryHelper(Logging.NSObject):
        def activityIdentifier(self):
            return 1

        def processIdentifier(self):
            return 1

        def threadIdentifier(self):
            return 1

    class TestEntry(TestCase):
        def test_constants(self):
            self.assertEqual(Logging.OSLogEntryStoreCategoryUndefined, 0)
            self.assertEqual(Logging.OSLogEntryStoreCategoryMetadata, 1)
            self.assertEqual(Logging.OSLogEntryStoreCategoryShortTerm, 2)
            self.assertEqual(Logging.OSLogEntryStoreCategoryLongTermAuto, 3)
            self.assertEqual(Logging.OSLogEntryStoreCategoryLongTerm1, 4)
            self.assertEqual(Logging.OSLogEntryStoreCategoryLongTerm3, 5)
            self.assertEqual(Logging.OSLogEntryStoreCategoryLongTerm7, 6)
            self.assertEqual(Logging.OSLogEntryStoreCategoryLongTerm14, 7)
            self.assertEqual(Logging.OSLogEntryStoreCategoryLongTerm30, 8)

        def test_protocols(self):
            objc.protocolNamed("OSLogEntryFromProcess")
            objc.protocolNamed("OSLogEntryWithPayload")

        def test_methods(self):
            self.assertResultHasType(TestEntryHelper.activityIdentifier, objc._C_ULNG_LNG)
            self.assertResultHasType(TestEntryHelper.processIdentifier, objc._C_INT)
            self.assertResultHasType(TestEntryHelper.threadIdentifier, objc._C_ULNG_LNG)
