from Quartz import *
from PyObjCTools.TestSupport import *


class TestCAEmitterLayer (TestCase):
    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessResultHasType(CAEmitterLayer.emitterPosition, CGPoint.__typestr__)
        self.failUnlessArgHasType(CAEmitterLayer.setEmitterPosition_, 0, CGPoint.__typestr__)
        self.failUnlessResultHasType(CAEmitterLayer.emitterSize, CGSize.__typestr__)
        self.failUnlessArgHasType(CAEmitterLayer.setEmitterSize_, 0, CGSize.__typestr__)

        self.failUnlessResultIsBOOL(CAEmitterLayer.preservesDepth)
        self.failUnlessArgIsBOOL(CAEmitterLayer.setPreservesDepth_, 0)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessIsInstance(kCAEmitterLayerPoint, unicode)
        self.failUnlessIsInstance(kCAEmitterLayerLine, unicode)
        self.failUnlessIsInstance(kCAEmitterLayerRectangle, unicode)
        self.failUnlessIsInstance(kCAEmitterLayerCuboid, unicode)
        self.failUnlessIsInstance(kCAEmitterLayerCircle, unicode)
        self.failUnlessIsInstance(kCAEmitterLayerSphere, unicode)
        self.failUnlessIsInstance(kCAEmitterLayerPoints, unicode)
        self.failUnlessIsInstance(kCAEmitterLayerOutline, unicode)
        self.failUnlessIsInstance(kCAEmitterLayerSurface, unicode)
        self.failUnlessIsInstance(kCAEmitterLayerVolume, unicode)
        self.failUnlessIsInstance(kCAEmitterLayerUnordered, unicode)
        self.failUnlessIsInstance(kCAEmitterLayerOldestFirst, unicode)
        self.failUnlessIsInstance(kCAEmitterLayerOldestLast, unicode)
        self.failUnlessIsInstance(kCAEmitterLayerBackToFront, unicode)
        self.failUnlessIsInstance(kCAEmitterLayerAdditive, unicode)

if __name__ == "__main__":
    main()
