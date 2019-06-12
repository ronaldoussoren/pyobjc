import sys
from PyObjCTest import *

if sys.maxsize > 2 ** 32:
    import Logging

    class TestEnumerator (TestCase):
        def test_constants(self):
            self.assertEqual(Logging.OSLogEnumeratorReverse, 0x01)
