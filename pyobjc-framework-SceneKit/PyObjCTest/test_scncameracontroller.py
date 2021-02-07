import objc
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level

import SceneKit


class TestSCNCameraController(TestCase):
    def testConstants(self):
        self.assertEqual(SceneKit.SCNInteractionModeFly, 0)
        self.assertEqual(SceneKit.SCNInteractionModeOrbitTurntable, 1)
        self.assertEqual(SceneKit.SCNInteractionModeOrbitAngleMapping, 2)
        self.assertEqual(SceneKit.SCNInteractionModeOrbitCenteredArcball, 3)
        self.assertEqual(SceneKit.SCNInteractionModeOrbitArcball, 4)
        self.assertEqual(SceneKit.SCNInteractionModePan, 5)
        self.assertEqual(SceneKit.SCNInteractionModeTruck, 6)

    @min_sdk_level("10.13")
    def testProtocols(self):
        objc.protocolNamed("SCNCameraControllerDelegate")

    @min_os_level("10.13")
    def testMethods(self):
        self.assertResultIsBOOL(SceneKit.SCNCameraController.automaticTarget)
        self.assertArgIsBOOL(SceneKit.SCNCameraController.setAutomaticTarget_, 0)
        self.assertResultIsBOOL(SceneKit.SCNCameraController.inertiaEnabled)
        self.assertArgIsBOOL(SceneKit.SCNCameraController.setInertiaEnabled_, 0)
        self.assertResultIsBOOL(SceneKit.SCNCameraController.isInertiaRunning)
