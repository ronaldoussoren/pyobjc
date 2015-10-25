from PyObjCTools.TestSupport import *
import objc

import SceneKit

class TestSCNCamera (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(SceneKit.SCNCamera.usesOrthographicProjection)
        self.assertArgIsBOOL(SceneKit.SCNCamera.setUsesOrthographicProjection_, 0)

    @min_os_level('10.9')
    def testMethods10_9(self):
        self.assertResultIsBOOL(SceneKit.SCNCamera.automaticallyAdjustsZRange)
        self.assertArgIsBOOL(SceneKit.SCNCamera.setAutomaticallyAdjustsZRange_, 0)


if __name__ == "__main__":
    main()
