from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2**32:
    import ModelIO

    class TestMDLCamera (TestCase):
        def testConstants(self):
            self.assertEqual(ModelIO.MDLMaterialSemanticBaseColor, 0)
            self.assertEqual(ModelIO.MDLMaterialSemanticSubsurface, 1)
            self.assertEqual(ModelIO.MDLMaterialSemanticMetallic, 2)
            self.assertEqual(ModelIO.MDLMaterialSemanticSpecular, 3)
            self.assertEqual(ModelIO.MDLMaterialSemanticSpecularExponent, 4)
            self.assertEqual(ModelIO.MDLMaterialSemanticSpecularTint, 5)
            self.assertEqual(ModelIO.MDLMaterialSemanticRoughness, 6)
            self.assertEqual(ModelIO.MDLMaterialSemanticAnisotropic, 7)
            self.assertEqual(ModelIO.MDLMaterialSemanticAnisotropicRotation, 8)
            self.assertEqual(ModelIO.MDLMaterialSemanticSheen, 9)
            self.assertEqual(ModelIO.MDLMaterialSemanticSheenTint, 10)
            self.assertEqual(ModelIO.MDLMaterialSemanticClearcoat, 11)
            self.assertEqual(ModelIO.MDLMaterialSemanticClearcoatGloss, 12)
            self.assertEqual(ModelIO.MDLMaterialSemanticEmission, 13)
            self.assertEqual(ModelIO.MDLMaterialSemanticBump, 14)
            self.assertEqual(ModelIO.MDLMaterialSemanticOpacity, 15)
            self.assertEqual(ModelIO.MDLMaterialSemanticInterfaceIndexOfRefraction, 16)
            self.assertEqual(ModelIO.MDLMaterialSemanticMaterialIndexOfRefraction, 17)
            self.assertEqual(ModelIO.MDLMaterialSemanticObjectSpaceNormal, 18)
            self.assertEqual(ModelIO.MDLMaterialSemanticTangentSpaceNormal, 19)
            self.assertEqual(ModelIO.MDLMaterialSemanticDisplacement, 20)
            self.assertEqual(ModelIO.MDLMaterialSemanticDisplacementScale, 21)
            self.assertEqual(ModelIO.MDLMaterialSemanticAmbientOcclusion, 22)
            self.assertEqual(ModelIO.MDLMaterialSemanticAmbientOcclusionScale, 23)
            self.assertEqual(ModelIO.MDLMaterialSemanticNone, 0x8000)
            self.assertEqual(ModelIO.MDLMaterialSemanticUserDefined, 0x8001)

            self.assertEqual(ModelIO.MDLMaterialPropertyTypeNone, 0)
            self.assertEqual(ModelIO.MDLMaterialPropertyTypeString, 1)
            self.assertEqual(ModelIO.MDLMaterialPropertyTypeURL, 2)
            self.assertEqual(ModelIO.MDLMaterialPropertyTypeTexture, 3)
            self.assertEqual(ModelIO.MDLMaterialPropertyTypeColor, 4)
            self.assertEqual(ModelIO.MDLMaterialPropertyTypeFloat, 5)
            self.assertEqual(ModelIO.MDLMaterialPropertyTypeFloat2, 6)
            self.assertEqual(ModelIO.MDLMaterialPropertyTypeFloat3, 7)
            self.assertEqual(ModelIO.MDLMaterialPropertyTypeFloat4, 8)
            self.assertEqual(ModelIO.MDLMaterialPropertyTypeMatrix44, 9)

            self.assertEqual(ModelIO.MDLMaterialTextureWrapModeClamp, 0)
            self.assertEqual(ModelIO.MDLMaterialTextureWrapModeRepeat, 1)
            self.assertEqual(ModelIO.MDLMaterialTextureWrapModeMirror, 2)

            self.assertEqual(ModelIO.MDLMaterialTextureFilterModeNearest, 0)
            self.assertEqual(ModelIO.MDLMaterialTextureFilterModeLinear, 1)

            self.assertEqual(ModelIO.MDLMaterialMipMapFilterModeNearest, 0)
            self.assertEqual(ModelIO.MDLMaterialMipMapFilterModeLinear, 1)

            self.assertEqual(ModelIO.MDLMaterialFaceFront, 0)
            self.assertEqual(ModelIO.MDLMaterialFaceBack, 1)
            self.assertEqual(ModelIO.MDLMaterialFaceDoubleSided, 2)

        @min_os_level('10.12')
        def testMethods10_12(self):
            self.assertArgIsBlock(ModelIO.MDLMaterialPropertyNode.initWithInputs_outputs_evaluationFunction_, 2, b'v@')
            self.assertArgIsBlock(ModelIO.MDLMaterialPropertyNode.setEvaluationFunction_, 0, b'v@')
            self.assertResultIsBlock(ModelIO.MDLMaterialPropertyNode.evaluationFunction, b'v@')

if __name__ == "__main__":
    main()
