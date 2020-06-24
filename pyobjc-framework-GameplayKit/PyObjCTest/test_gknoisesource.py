from PyObjCTools.TestSupport import TestCase
import GameplayKit


class TestGKNoiseSource(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(GameplayKit.GKVoronoiNoiseSource.isDistanceEnabled)
        self.assertArgIsBOOL(GameplayKit.GKVoronoiNoiseSource.setDistanceEnabled_, 0)
