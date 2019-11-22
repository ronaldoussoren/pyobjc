from PyObjCTools.TestSupport import *

import OSLog


class TestEnumerator(TestCase):
    def test_constants(self):
        self.assertEqual(OSLog.OSLogEnumeratorReverse, 0x01)
