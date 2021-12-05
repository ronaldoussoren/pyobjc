import objc
from PyObjCTools.TestSupport import TestCase


class TestAllocateBuffer(TestCase):
    def testBadLengths(self):
        with self.assertRaisesRegex(ValueError, "Length must be greater than 0"):
            objc.allocateBuffer(0)
        with self.assertRaisesRegex(ValueError, "Length must be greater than 0"):
            objc.allocateBuffer(-1000)

    def testBuffer(self):
        b = objc.allocateBuffer(10000)
        self.assertEqual(len(b), 10000)

        self.assertIsInstance(b, bytearray)
