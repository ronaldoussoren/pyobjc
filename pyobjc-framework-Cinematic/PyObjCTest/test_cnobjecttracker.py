from PyObjCTools.TestSupport import TestCase

import Cinematic


class TestCNObjectTracker(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(Cinematic.CNObjectTracker.isSupported)
        self.assertResultIsBOOL(
            Cinematic.CNObjectTracker.startTrackingAt_within_sourceImage_sourceDisparity_
        )
