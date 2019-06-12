import sys
from PyObjCTest import *

if sys.maxsize > 2 ** 32:
    import Logging

    class TestEntrySignpost (TestCase):
        def test_constants(self):
            self.assertEqual(Logging.OSLogEntrySignpostTypeUndefined, 0)
            self.assertEqual(Logging.OSLogEntrySignpostTypeIntervalBegin, 1)
            self.assertEqual(Logging.OSLogEntrySignpostTypeIntervalEnd, 2)
            self.assertEqual(Logging.OSLogEntrySignpostTypeEvent, 3)
