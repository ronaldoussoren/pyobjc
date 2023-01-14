from PyObjCTools.TestSupport import TestCase

import PHASE


class TestPHASEEngine(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(PHASE.PHASEEngine.startAndReturnError_)
        self.assertArgIsOut(PHASE.PHASEEngine.startAndReturnError_, 0)
