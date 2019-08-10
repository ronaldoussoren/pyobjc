import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import Logging

    class TestEntryLog(TestCase):
        def test_constants(self):
            self.assertEqual(Logging.OSLogEntryLogLevelUndefined, 0)
            self.assertEqual(Logging.OSLogEntryLogLevelDebug, 1)
            self.assertEqual(Logging.OSLogEntryLogLevelInfo, 2)
            self.assertEqual(Logging.OSLogEntryLogLevelNotice, 3)
            self.assertEqual(Logging.OSLogEntryLogLevelError, 4)
            self.assertEqual(Logging.OSLogEntryLogLevelFault, 5)
