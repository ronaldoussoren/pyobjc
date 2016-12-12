from PyObjCTools.TestSupport import *
import objc
import sys

if os_level_key(os_release()) < os_level_key('10.12') or sys.maxsize >= 2**32:

    import SceneKit

    SCNSceneExportProgressHandler = b'vf@o^Z'

    class TestSCNScene (TestCase):
        def test_constants(self):
            self.assertIsInstance(SceneKit.SCNSceneStartTimeAttributeKey, unicode)
            self.assertIsInstance(SceneKit.SCNSceneEndTimeAttributeKey, unicode)
            self.assertIsInstance(SceneKit.SCNSceneFrameRateAttributeKey, unicode)

            self.assertIs(SceneKit.SCNSceneAttributeStartTime, SceneKit.SCNSceneStartTimeAttributeKey)
            self.assertIs(SceneKit.SCNSceneAttributeEndTime, SceneKit.SCNSceneEndTimeAttributeKey)
            self.assertIs(SceneKit.SCNSceneAttributeFrameRate, SceneKit.SCNSceneFrameRateAttributeKey)


        @min_os_level('10.9')
        def test_constants10_9(self):
            self.assertIsInstance(SceneKit.SCNSceneExportDestinationURL, unicode)

        @min_os_level('10.10')
        def test_constants10_10(self):
            self.assertIsInstance(SceneKit.SCNSceneUpAxisAttributeKey, unicode)

            self.assertIs(SceneKit.SCNSceneAttributeUpAxis, SceneKit.SCNSceneUpAxisAttributeKey)


        def testMethods(self):
            self.assertArgIsOut(SceneKit.SCNScene.sceneWithURL_options_error_, 2)

        @min_os_level('10.9')
        def testMethods10_9(self):
            self.assertResultIsBOOL(SceneKit.SCNScene.writeToURL_options_delegate_progressHandler_)
            self.assertArgIsBlock(SceneKit.SCNScene.writeToURL_options_delegate_progressHandler_, 3, SCNSceneExportProgressHandler)

        @min_os_level('10.10')
        def testMethods10_10(self):
            self.assertResultIsBOOL(SceneKit.SCNScene.isPaused)
            self.assertArgIsBOOL(SceneKit.SCNScene.setPaused_, 0)

        @min_sdk_level('10.10')
        def testProtocols(self):
            objc.protocolNamed('SCNSceneExportDelegate')


if __name__ == "__main__":
    main()
