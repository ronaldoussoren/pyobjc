from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCAEmitterLayer(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(Quartz.CAEmitterLayerEmitterMode, str)
        self.assertIsTypedEnum(Quartz.CAEmitterLayerEmitterShape, str)
        self.assertIsTypedEnum(Quartz.CAEmitterLayerRenderMode, str)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(Quartz.kCAEmitterLayerPoint, str)
        self.assertIsInstance(Quartz.kCAEmitterLayerLine, str)
        self.assertIsInstance(Quartz.kCAEmitterLayerRectangle, str)
        self.assertIsInstance(Quartz.kCAEmitterLayerCuboid, str)
        self.assertIsInstance(Quartz.kCAEmitterLayerCircle, str)
        self.assertIsInstance(Quartz.kCAEmitterLayerSphere, str)
        self.assertIsInstance(Quartz.kCAEmitterLayerPoints, str)
        self.assertIsInstance(Quartz.kCAEmitterLayerOutline, str)
        self.assertIsInstance(Quartz.kCAEmitterLayerSurface, str)
        self.assertIsInstance(Quartz.kCAEmitterLayerVolume, str)
        self.assertIsInstance(Quartz.kCAEmitterLayerUnordered, str)
        self.assertIsInstance(Quartz.kCAEmitterLayerOldestFirst, str)
        self.assertIsInstance(Quartz.kCAEmitterLayerOldestLast, str)
        self.assertIsInstance(Quartz.kCAEmitterLayerBackToFront, str)
        self.assertIsInstance(Quartz.kCAEmitterLayerAdditive, str)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultHasType(
            Quartz.CAEmitterLayer.emitterPosition, Quartz.CGPoint.__typestr__
        )
        self.assertArgHasType(
            Quartz.CAEmitterLayer.setEmitterPosition_, 0, Quartz.CGPoint.__typestr__
        )
        self.assertResultHasType(
            Quartz.CAEmitterLayer.emitterSize, Quartz.CGSize.__typestr__
        )
        self.assertArgHasType(
            Quartz.CAEmitterLayer.setEmitterSize_, 0, Quartz.CGSize.__typestr__
        )

        self.assertResultIsBOOL(Quartz.CAEmitterLayer.preservesDepth)
        self.assertArgIsBOOL(Quartz.CAEmitterLayer.setPreservesDepth_, 0)
