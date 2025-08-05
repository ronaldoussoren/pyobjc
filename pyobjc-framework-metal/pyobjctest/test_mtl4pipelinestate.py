import Metal
from PyObjCTools.TestSupport import TestCase


class TestMTL4PipelineState(TestCase):
    def test_enum(self):
        self.assertIsEnumType(Metal.MTL4ShaderReflection)
        self.assertEqual(Metal.MTL4ShaderReflectionNone, 0)
        self.assertEqual(Metal.MTL4ShaderReflectionBindingInfo, 1 << 0)
        self.assertEqual(Metal.MTL4ShaderReflectionBufferTypeInfo, 1 << 1)

        self.assertIsEnumType(Metal.MTL4AlphaToOneState)
        self.assertEqual(Metal.MTL4AlphaToOneStateDisabled, 0)
        self.assertEqual(Metal.MTL4AlphaToOneStateEnabled, 1)

        self.assertIsEnumType(Metal.MTL4BlendState)
        self.assertEqual(Metal.MTL4BlendStateDisabled, 0)
        self.assertEqual(Metal.MTL4BlendStateEnabled, 1)
        self.assertEqual(Metal.MTL4BlendStateUnspecialized, 2)

        self.assertIsEnumType(Metal.MTL4IndirectCommandBufferSupportState)
        self.assertEqual(Metal.MTL4IndirectCommandBufferSupportStateDisabled, 0)
        self.assertEqual(Metal.MTL4IndirectCommandBufferSupportStateEnabled, 1)
