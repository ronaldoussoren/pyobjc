import objc
import warnings
from PyObjCTools.TestSupport import TestCase


class TestAllocateBuffer(TestCase):
    def test_deprecated(self):
        with warnings.catch_warnings():
            warnings.filterwarnings("error", category=DeprecationWarning)

            with self.assertRaisesRegex(DeprecationWarning, "Use bytearray instead"):
                objc.allocateBuffer(10)

    def testBadLengths(self):
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)

            with self.assertRaisesRegex(TypeError, "length must be a positive integer"):
                objc.allocateBuffer(0)
            with self.assertRaisesRegex(TypeError, "length must be a positive integer"):
                objc.allocateBuffer(-1000)
            with self.assertRaisesRegex(TypeError, "length must be a positive integer"):
                objc.allocateBuffer("42")

    def testBuffer(self):
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)

            b = objc.allocateBuffer(10000)
            self.assertEqual(len(b), 10000)

            self.assertIsInstance(b, bytearray)
