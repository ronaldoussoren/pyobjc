from PyObjCTools.TestSupport import TestCase
import ModelIO


class TestMDLCamera(TestCase):
    def testConstants(self):
        self.assertEqual(ModelIO.MDLLightTypeUnknown, 0)
        self.assertEqual(ModelIO.MDLLightTypeAmbient, 1)
        self.assertEqual(ModelIO.MDLLightTypeDirectional, 2)
        self.assertEqual(ModelIO.MDLLightTypeSpot, 3)
        self.assertEqual(ModelIO.MDLLightTypePoint, 4)
        self.assertEqual(ModelIO.MDLLightTypeLinear, 5)
        self.assertEqual(ModelIO.MDLLightTypeDiscArea, 6)
        self.assertEqual(ModelIO.MDLLightTypeRectangularArea, 7)
        self.assertEqual(ModelIO.MDLLightTypeSuperElliptical, 8)
        self.assertEqual(ModelIO.MDLLightTypePhotometric, 9)
        self.assertEqual(ModelIO.MDLLightTypeProbe, 10)
        self.assertEqual(ModelIO.MDLLightTypeEnvironment, 11)
