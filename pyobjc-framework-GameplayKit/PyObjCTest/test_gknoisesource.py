from PyObjCTools.TestSupport import TestCase, min_os_level
import GameplayKit


class TestGKNoiseSource(TestCase):
    @min_os_level("10.12")
    def testMethods(self):
        self.assertResultIsBOOL(GameplayKit.GKVoronoiNoiseSource.isDistanceEnabled)
        self.assertArgIsBOOL(GameplayKit.GKVoronoiNoiseSource.setDistanceEnabled_, 0)
