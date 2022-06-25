from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level

import SceneKit

SCNSceneExportProgressHandler = b"vf@o^Z"


class TestSCNScene(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(SceneKit.SCNSceneAttribute, str)

    def test_constants(self):
        self.assertIsInstance(SceneKit.SCNSceneStartTimeAttributeKey, str)
        self.assertIsInstance(SceneKit.SCNSceneEndTimeAttributeKey, str)
        self.assertIsInstance(SceneKit.SCNSceneFrameRateAttributeKey, str)

        self.assertIs(
            SceneKit.SCNSceneAttributeStartTime, SceneKit.SCNSceneStartTimeAttributeKey
        )
        self.assertIs(
            SceneKit.SCNSceneAttributeEndTime, SceneKit.SCNSceneEndTimeAttributeKey
        )
        self.assertIs(
            SceneKit.SCNSceneAttributeFrameRate, SceneKit.SCNSceneFrameRateAttributeKey
        )

    @min_os_level("10.9")
    def test_constants10_9(self):
        self.assertIsInstance(SceneKit.SCNSceneExportDestinationURL, str)

    @min_os_level("10.10")
    def test_constants10_10(self):
        self.assertIsInstance(SceneKit.SCNSceneUpAxisAttributeKey, str)

        self.assertIs(
            SceneKit.SCNSceneAttributeUpAxis, SceneKit.SCNSceneUpAxisAttributeKey
        )

    def testMethods(self):
        self.assertArgIsOut(SceneKit.SCNScene.sceneWithURL_options_error_, 2)

    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertResultIsBOOL(
            SceneKit.SCNScene.writeToURL_options_delegate_progressHandler_
        )
        self.assertArgIsBlock(
            SceneKit.SCNScene.writeToURL_options_delegate_progressHandler_,
            3,
            SCNSceneExportProgressHandler,
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(SceneKit.SCNScene.isPaused)
        self.assertArgIsBOOL(SceneKit.SCNScene.setPaused_, 0)

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertResultIsBOOL(SceneKit.SCNScene.wantsScreenSpaceReflection)
        self.assertArgIsBOOL(SceneKit.SCNScene.setWantsScreenSpaceReflection_, 0)

    @min_sdk_level("10.10")
    def testProtocols(self):
        self.assertProtocolExists("SCNSceneExportDelegate")
