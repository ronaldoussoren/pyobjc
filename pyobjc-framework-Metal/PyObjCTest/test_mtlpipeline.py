import Metal
from PyObjCTools.TestSupport import TestCase


class TestMTLPipeline(TestCase):
    def test_constants(self):
        self.assertIsEnumType(Metal.MTLMutability)
        self.assertEqual(Metal.MTLMutabilityDefault, 0)
        self.assertEqual(Metal.MTLMutabilityMutable, 1)
        self.assertEqual(Metal.MTLMutabilityImmutable, 2)

        self.assertIsEnumType(Metal.MTLShaderValidation)
        self.assertEqual(Metal.MTLShaderValidationDefault, 0)
        self.assertEqual(Metal.MTLShaderValidationEnabled, 1)
        self.assertEqual(Metal.MTLShaderValidationDisabled, 2)
