import OSLog
from PyObjCTools.TestSupport import TestCase


class TestEntryLog(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(OSLog.OSLogEntryLogLevel)

    def test_constants(self):
        self.assertEqual(OSLog.OSLogEntryLogLevelUndefined, 0)
        self.assertEqual(OSLog.OSLogEntryLogLevelDebug, 1)
        self.assertEqual(OSLog.OSLogEntryLogLevelInfo, 2)
        self.assertEqual(OSLog.OSLogEntryLogLevelNotice, 3)
        self.assertEqual(OSLog.OSLogEntryLogLevelError, 4)
        self.assertEqual(OSLog.OSLogEntryLogLevelFault, 5)
