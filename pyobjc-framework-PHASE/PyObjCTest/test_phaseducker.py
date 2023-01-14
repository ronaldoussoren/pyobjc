from PyObjCTools.TestSupport import TestCase

import PHASE


class TestPHASEDucker(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(PHASE.PHASEDucker.isActive)
