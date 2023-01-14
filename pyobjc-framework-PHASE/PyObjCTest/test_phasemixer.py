from PyObjCTools.TestSupport import TestCase
from objc import simd

import PHASE


class TestPHASEMixer(TestCase):
    def test_methods(self):
        self.assertResultHasType(
            PHASE.PHASEAmbientMixerDefinition.orientation, simd.simd_quatf.__typestr__
        )
