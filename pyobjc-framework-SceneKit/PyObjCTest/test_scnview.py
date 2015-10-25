from PyObjCTools.TestSupport import *
import objc

import SceneKit

try:
    unicode
except NameError:
    unicode = str

class TestSCNView (TestCase):
    def testConstants(self):
        self.assertEqual(SceneKit.SCNAntialiasingModeNone, 0)
        self.assertEqual(SceneKit.SCNAntialiasingModeMultisampling2X, 1)
        self.assertEqual(SceneKit.SCNAntialiasingModeMultisampling4X, 2)
        self.assertEqual(SceneKit.SCNAntialiasingModeMultisampling8X, 3)
        self.assertEqual(SceneKit.SCNAntialiasingModeMultisampling16X, 4)

    @min_os_level('10.11')
    def testConstants10_11(self):
        self.assertEqual(SceneKit.SCNPreferredRenderingAPIKey, unicode)
        self.assertEqual(SceneKit.SCNPreferredDeviceKey, unicode)
        self.assertEqual(SceneKit.SCNPreferLowPowerDeviceKey, unicode)

    @min_os_level('10.8')
    def testMethods10_8(self):
        self.assertArgIsBOOL(SceneKit.SCNView.setAllowsCameraControl_, 0)
        self.assertResultIsBOOL(SceneKit.SCNView.allowsCameraControl)


if __name__ == "__main__":
    main()
