import OSLog
from PyObjCTools.TestSupport import TestCase


class TestEnumerator(TestCase):
    def test_enums(self):
        self.assertIsEnumType(OSLog.OSLogEnumeratorOptions)
        self.assertEqual(OSLog.OSLogEnumeratorReverse, 0x01)
