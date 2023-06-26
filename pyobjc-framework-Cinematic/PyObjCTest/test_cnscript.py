from PyObjCTools.TestSupport import TestCase

import Cinematic


class TestCNScript(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            Cinematic.CNScript.loadFromAsset_changes_progress_completionHandler_,
            3,
            b"v@@",
        )
        self.assertResultIsBOOL(Cinematic.CNScript.addUserDecision_)
        self.assertResultIsBOOL(Cinematic.CNScript.removeUserDecision_)
        self.assertResultIsBOOL(Cinematic.CNScript.removeDetectionTrack_)
