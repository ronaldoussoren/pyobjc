import Metal
from PyObjCTools.TestSupport import TestCase


class TestMTLFunctionDescriptor(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Metal.MTLFunctionOptions)
        self.assertEqual(Metal.MTLFunctionOptionNone, 0)
        self.assertEqual(Metal.MTLFunctionOptionCompileToBinary, 1 << 0)
        self.assertEqual(
            Metal.MTLFunctionOptionStoreFunctionInMetalPipelinesScript, 1 << 1
        )
        self.assertEqual(Metal.MTLFunctionOptionStoreFunctionInMetalScript, 1 << 1)
        self.assertEqual(Metal.MTLFunctionOptionFailOnBinaryArchiveMiss, 1 << 2)
        self.assertEqual(Metal.MTLFunctionOptionPipelineIndependent, 1 << 3)
