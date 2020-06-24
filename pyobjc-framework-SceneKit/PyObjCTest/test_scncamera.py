from PyObjCTools.TestSupport import TestCase, min_os_level

import SceneKit


class TestSCNCamera(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(SceneKit.SCNCamera.usesOrthographicProjection)
        self.assertArgIsBOOL(SceneKit.SCNCamera.setUsesOrthographicProjection_, 0)

    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertResultIsBOOL(SceneKit.SCNCamera.automaticallyAdjustsZRange)
        self.assertArgIsBOOL(SceneKit.SCNCamera.setAutomaticallyAdjustsZRange_, 0)

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertResultIsBOOL(SceneKit.SCNCamera.wantsHDR)
        self.assertArgIsBOOL(SceneKit.SCNCamera.setWantsHDR_, 0)

        self.assertResultIsBOOL(SceneKit.SCNCamera.wantsExposureAdaptation)
        self.assertArgIsBOOL(SceneKit.SCNCamera.setWantsExposureAdaptation_, 0)

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertResultIsBOOL(SceneKit.SCNCamera.wantsDepthOfField)
        self.assertArgIsBOOL(SceneKit.SCNCamera.setWantsDepthOfField_, 0)

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertResultIsBOOL(SceneKit.SCNCamera.grainIsColored)
        self.assertArgIsBOOL(SceneKit.SCNCamera.setGrainIsColored_, 0)

    def testConstants(self):
        self.assertEqual(SceneKit.SCNCameraProjectionDirectionVertical, 0)
        self.assertEqual(SceneKit.SCNCameraProjectionDirectionHorizontal, 1)
