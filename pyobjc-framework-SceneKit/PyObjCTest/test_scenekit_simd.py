from PyObjCTools.TestSupport import *
import objc

import SceneKit

class TestSceneKit_simd (TestCase):
    @expectedFailure
    def test_functions(self):
        self.fail("inline functions with vector_floatX types need manual wrappers")

if __name__ == "__main__":
    main()
