import Metal
from PyObjCTools.TestSupport import TestCase


class TestMTLFunctionDescriptor(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Metal.MTLFunctionOptions)

    def test_constants(self):
        self.assertEqual(Metal.MTLFunctionOptionNone, 0)
        self.assertEqual(Metal.MTLFunctionOptionCompileToBinary, 1 << 0)
        self.assertEqual(Metal.MTLFunctionOptionStoreFunctionInMetalScript, 1 << 1)
