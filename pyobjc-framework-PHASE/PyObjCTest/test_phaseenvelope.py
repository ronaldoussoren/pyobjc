from PyObjCTools.TestSupport import TestCase
from objc import simd

import PHASE


class TestPHASEEnvelope(TestCase):
    def test_methods(self):
        self.assertResultHasType(
            PHASE.PHASEEnvelope.startPoint, simd.simd_double2.__typestr__
        )
