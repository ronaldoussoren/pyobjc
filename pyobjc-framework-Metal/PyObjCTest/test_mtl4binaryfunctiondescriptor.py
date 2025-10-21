import Metal
from PyObjCTools.TestSupport import TestCase


class TestMTL4BinaryFunctionDescriptor(TestCase):
    def test_enum(self):
        self.assertIsEnumType(Metal.MTL4BinaryFunctionOptions)
        self.assertEqual(Metal.MTL4BinaryFunctionOptionNone, 0)
        self.assertEqual(Metal.MTL4BinaryFunctionOptionPipelineIndependent, 1 << 1)
