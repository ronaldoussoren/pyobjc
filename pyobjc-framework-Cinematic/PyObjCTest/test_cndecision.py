from PyObjCTools.TestSupport import TestCase

import Cinematic


class TestCNDecision(TestCase):
    def test_methods(self):
        self.assertArgIsBOOL(Cinematic.CNDecision.initWithTime_detectionID_strong_, 2)
        self.assertArgIsBOOL(
            Cinematic.CNDecision.initWithTime_detectionGroupID_strong_, 2
        )

        self.assertResultIsBOOL(Cinematic.CNDecision.isUserDecision)
        self.assertResultIsBOOL(Cinematic.CNDecision.isGroupDecision)
        self.assertResultIsBOOL(Cinematic.CNDecision.isStrongDecision)
