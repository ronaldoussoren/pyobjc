from PyObjCTools.TestSupport import *
import objc
import sys

if os_level_key(os_release()) < os_level_key('10.12') or sys.maxsize >= 2**32:

    import SceneKit

    class TestSCNViewHelper (SceneKit.NSObject):
        def autoSwitchToFreeCamera(self): return 1
        def allowsTranslation(self): return 1
        def flyModeVelocity(self): return 1
        def panSensitivity(self): return 1
        def truckSensitivity(self): return 1
        def rotationSensitivity(self): return 1

        def setAutoSwitchToFreeCamera_(self, v): pass
        def setAllowsTranslation_(self, v): pass
        def setFlyModeVelocity_(self, v): pass
        def setPanSensitivity_(self, v): pass
        def setTruckSensitivity_(self, v): pass
        def setRotationSensitivity_(self, v): pass

    class TestSCNView (TestCase):
        def testConstants(self):
            self.assertEqual(SceneKit.SCNAntialiasingModeNone, 0)
            self.assertEqual(SceneKit.SCNAntialiasingModeMultisampling2X, 1)
            self.assertEqual(SceneKit.SCNAntialiasingModeMultisampling4X, 2)
            self.assertEqual(SceneKit.SCNAntialiasingModeMultisampling8X, 3)
            self.assertEqual(SceneKit.SCNAntialiasingModeMultisampling16X, 4)

        @min_os_level('10.11')
        def testConstants10_11(self):
            self.assertIsInstance(SceneKit.SCNPreferredRenderingAPIKey, unicode)
            self.assertIsInstance(SceneKit.SCNPreferredDeviceKey, unicode)
            self.assertIsInstance(SceneKit.SCNPreferLowPowerDeviceKey, unicode)

            self.assertIs(SceneKit.SCNViewOptionPreferredRenderingAPI, SceneKit.SCNPreferredRenderingAPIKey)
            self.assertIs(SceneKit.SCNViewOptionPreferredDevice, SceneKit.SCNPreferredDeviceKey)
            self.assertIs(SceneKit.SCNViewOptionPreferLowPowerDevice, SceneKit.SCNPreferLowPowerDeviceKey)

        def testMethods(self):
            self.assertResultIsBOOL(TestSCNViewHelper.autoSwitchToFreeCamera)
            self.assertResultIsBOOL(TestSCNViewHelper.allowsTranslation)
            self.assertResultHasType(TestSCNViewHelper.flyModeVelocity, objc._C_CGFloat)
            self.assertResultHasType(TestSCNViewHelper.panSensitivity, objc._C_CGFloat)
            self.assertResultHasType(TestSCNViewHelper.truckSensitivity, objc._C_CGFloat)
            self.assertResultHasType(TestSCNViewHelper.rotationSensitivity, objc._C_CGFloat)

            self.assertArgIsBOOL(TestSCNViewHelper.setAutoSwitchToFreeCamera_, 0)
            self.assertArgIsBOOL(TestSCNViewHelper.setAllowsTranslation_, 0)
            self.assertArgHasType(TestSCNViewHelper.setFlyModeVelocity_, 0, objc._C_CGFloat)
            self.assertArgHasType(TestSCNViewHelper.setPanSensitivity_, 0, objc._C_CGFloat)
            self.assertArgHasType(TestSCNViewHelper.setTruckSensitivity_, 0, objc._C_CGFloat)
            self.assertArgHasType(TestSCNViewHelper.setRotationSensitivity_, 0, objc._C_CGFloat)


        @min_os_level('10.8')
        def testMethods10_8(self):
            self.assertArgIsBOOL(SceneKit.SCNView.setAllowsCameraControl_, 0)
            self.assertResultIsBOOL(SceneKit.SCNView.allowsCameraControl)

        @min_os_level('10.13')
        def testMethods10_13(self):
            self.assertArgIsBOOL(SceneKit.SCNView.setRendersContinuously_, 0)
            self.assertResultIsBOOL(SceneKit.SCNView.rendersContinuously)
            self.assertArgIsBOOL(SceneKit.SCNView.setAllowsCameraControl_, 0)
            self.assertResultIsBOOL(SceneKit.SCNView.allowsCameraControl)

        @min_sdk_level('10.13')
        def testProtocols(self):
            objc.protocolNamed('SCNCameraControlConfiguration')

if __name__ == "__main__":
    main()
