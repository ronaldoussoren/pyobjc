from PyObjCTools.TestSupport import TestCase, expectedFailure

import SceneKit


class TestSceneKit_simd(TestCase):
    def test_no_vector_functions(self):
        self.assertFalse(hasattr(SceneKit, "SCNVector3ToFloat3"))
        self.assertFalse(hasattr(SceneKit, "SCNVector3FromFloat3"))

    @expectedFailure
    def test_functions(self):
        self.fail("inline functions with vector_floatX types need manual wrappers")
