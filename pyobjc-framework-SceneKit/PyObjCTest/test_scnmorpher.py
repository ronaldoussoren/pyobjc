
from PyObjCTools.TestSupport import *
import objc
import sys

if os_level_key(os_release()) < os_level_key('10.12') or sys.maxsize >= 2**32:

    import SceneKit

    class TestSCNMorpher (TestCase):
        def testConstants(self):
            self.assertEqual(SceneKit.SCNMorpherCalculationModeNormalized, 0)
            self.assertEqual(SceneKit.SCNMorpherCalculationModeAdditive, 1)

if __name__ == "__main__":
    main()
