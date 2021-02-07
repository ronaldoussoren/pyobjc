from PyObjCTools.TestSupport import TestCase

import GameplayKit


class TestGKNoise(TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(
            GameplayKit.GKNoise.remapValuesToTerracesWithPeaks_terracesInverted_, 1
        )
