from PyObjCTools.TestSupport import TestCase

import Cinematic


class TestCNDetectionTrack(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(Cinematic.CNDetectionTrack.isUserCreated)
        self.assertResultIsBOOL(Cinematic.CNDetectionTrack.isDiscrete)

        self.assertArgIsBOOL(
            Cinematic.CNCustomDetectionTrack.initWithDetections_smooth_, 1
        )
