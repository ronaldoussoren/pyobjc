import objc
from PyObjCTools.TestSupport import TestCase


class TestAllocateBuffer(TestCase):
    def testBadLengths(self):
        self.assertRaises(ValueError, objc.allocateBuffer, 0)
        self.assertRaises(ValueError, objc.allocateBuffer, -1000)

    def testBuffer(self):
        b = objc.allocateBuffer(10000)
        self.assertEqual(len(b), 10000)

        self.assertIsInstance(b, bytearray)
