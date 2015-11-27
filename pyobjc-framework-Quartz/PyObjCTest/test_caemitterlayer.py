from Quartz import *
from PyObjCTools.TestSupport import *


class TestCAEmitterLayer (TestCase):
    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultHasType(CAEmitterLayer.emitterPosition, CGPoint.__typestr__)
        self.assertArgHasType(CAEmitterLayer.setEmitterPosition_, 0, CGPoint.__typestr__)
        self.assertResultHasType(CAEmitterLayer.emitterSize, CGSize.__typestr__)
        self.assertArgHasType(CAEmitterLayer.setEmitterSize_, 0, CGSize.__typestr__)

        self.assertResultIsBOOL(CAEmitterLayer.preservesDepth)
        self.assertArgIsBOOL(CAEmitterLayer.setPreservesDepth_, 0)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(kCAEmitterLayerPoint, unicode)
        self.assertIsInstance(kCAEmitterLayerLine, unicode)
        self.assertIsInstance(kCAEmitterLayerRectangle, unicode)
        self.assertIsInstance(kCAEmitterLayerCuboid, unicode)
        self.assertIsInstance(kCAEmitterLayerCircle, unicode)
        self.assertIsInstance(kCAEmitterLayerSphere, unicode)
        self.assertIsInstance(kCAEmitterLayerPoints, unicode)
        self.assertIsInstance(kCAEmitterLayerOutline, unicode)
        self.assertIsInstance(kCAEmitterLayerSurface, unicode)
        self.assertIsInstance(kCAEmitterLayerVolume, unicode)
        self.assertIsInstance(kCAEmitterLayerUnordered, unicode)
        self.assertIsInstance(kCAEmitterLayerOldestFirst, unicode)
        self.assertIsInstance(kCAEmitterLayerOldestLast, unicode)
        self.assertIsInstance(kCAEmitterLayerBackToFront, unicode)
        self.assertIsInstance(kCAEmitterLayerAdditive, unicode)

if __name__ == "__main__":
    main()
