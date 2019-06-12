import sys
from PyObjCTest import *

if sys.maxsize > 2 ** 32:
    import Logging

    class TestEntry (TestCase):
        def test_methods(self):
            self.assertArgIsOut(Logging.OSLogStore.localStoreAndReturnError_, 0)
            self.assertArgIsOut(Logging.OSLogStore.storeWithURL_error_, 1)
            self.assertArgIsOut(Logging.OSLogStore.entriesEnumeratorWithOptions_position_predicate_error_, 3)
            self.assertArgIsOut(Logging.OSLogStore.entriesEnumeratorAndReturnError_, 0)
