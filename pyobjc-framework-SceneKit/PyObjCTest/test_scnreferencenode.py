from PyObjCTools.TestSupport import *
import objc
import sys

if os_level_key(os_release()) < os_level_key('10.12') or sys.maxsize >= 2**32:

    import SceneKit

    class TestSCNReferenceNode (TestCase):
        def test_constants(self):
            self.assertEqual(SceneKit.SCNReferenceLoadingPolicyImmediate, 0)
            self.assertEqual(SceneKit.SCNReferenceLoadingPolicyOnDemand, 1)

        @min_os_level('10.11')
        def testMethods(self):
            #self.assertArgIsBOOL(SceneKit.SCNReferenceNode.setLoaded_, 0)
            self.assertResultIsBOOL(SceneKit.SCNReferenceNode.isLoaded)


if __name__ == "__main__":
    main()
