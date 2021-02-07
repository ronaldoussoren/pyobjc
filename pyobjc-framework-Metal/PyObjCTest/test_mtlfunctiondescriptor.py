import Metal
from PyObjCTools.TestSupport import TestCase


class TestMTLFunctionDescriptor(TestCase):
    def test_constants(self):
        self.assertEqual(Metal.MTLFunctionOptionNone, 0)
        self.assertEqual(Metal.MTLFunctionOptionCompileToBinary, 1 << 0)
