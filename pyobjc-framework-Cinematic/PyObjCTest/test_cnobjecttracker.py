from PyObjCTools.TestSupport import TestCase

import Cinematic


class TestCNObjectTracker(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(Cinematic.CNBoundsPrediction.isSupported)
        self.assertResultIsBOOL(
            Cinematic.CNBoundsPrediction.startTrackingAt_within_sourceImage_sourceDisparity_
        )
