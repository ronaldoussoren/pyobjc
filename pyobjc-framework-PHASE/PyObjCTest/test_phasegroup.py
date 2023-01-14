from PyObjCTools.TestSupport import TestCase

import PHASE


class TestPHASEGroup(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(PHASE.PHASEGroup.isMuted)
        self.assertResultIsBOOL(PHASE.PHASEGroup.isSoloed)
