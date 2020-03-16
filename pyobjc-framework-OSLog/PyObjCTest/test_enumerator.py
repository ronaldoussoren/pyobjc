import OSLog
from PyObjCTools.TestSupport import TestCase


class TestEnumerator(TestCase):
    def test_constants(self):
        self.assertEqual(OSLog.OSLogEnumeratorReverse, 0x01)
