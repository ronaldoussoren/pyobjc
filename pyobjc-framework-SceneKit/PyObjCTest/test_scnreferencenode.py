from PyObjCTools.TestSupport import TestCase, min_os_level

import SceneKit


class TestSCNReferenceNode(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(SceneKit.SCNReferenceLoadingPolicy)

    def test_constants(self):
        self.assertEqual(SceneKit.SCNReferenceLoadingPolicyImmediate, 0)
        self.assertEqual(SceneKit.SCNReferenceLoadingPolicyOnDemand, 1)

    @min_os_level("10.11")
    def testMethods(self):
        # self.assertArgIsBOOL(SceneKit.SCNReferenceNode.setLoaded_, 0)
        self.assertResultIsBOOL(SceneKit.SCNReferenceNode.isLoaded)
