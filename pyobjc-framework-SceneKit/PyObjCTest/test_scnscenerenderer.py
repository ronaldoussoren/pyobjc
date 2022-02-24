import objc
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level

import SceneKit

SCNSceneExportProgressHandler = b"vf@o^Z"


class TestSCNSceneRendererHelper(SceneKit.NSObject):
    def presentScene_withTransition_incomingPointOfView_completionHandler_(
        self, s, t, v, h
    ):
        pass

    def sceneTime(self):
        return 1

    def setSceneTime_(self, t):
        pass

    def hitTest_options_(self, p, o):
        return 1

    def isNodeInsideFrustum_withPointOfView_(self, n, v):
        return 1

    def projectPoint_(self, p):
        return p

    def unprojectPoint_(self, p):
        return p

    def isPlaying(self):
        return 1

    def setPlaying_(self, v):
        pass

    def loops(self):
        return 1

    def setLoops_(self, v):
        pass

    def autoenablesDefaultLighting(self):
        return 1

    def setAutoenablesDefaultLighting_(self, v):
        pass

    def isJitteringEnabled(self):
        return 1

    def setJitteringEnabled_(self, v):
        pass

    def prepareObject_shouldAbortBlock_(self, o, b):
        return 1

    def prepareObjects_withCompletionHandler_(self, o, h):
        pass

    def showsStatistics(self):
        return 1

    def setShowsStatistics_(self, v):
        pass

    def debugOptions(self):
        return 1

    def setDebugOptions_(self, v):
        pass

    def renderingAPI(self):
        return 1

    def context(self):
        return 1

    def colorPixelFormat(self):
        return 1

    def depthPixelFormat(self):
        return 1

    def stencilPixelFormat(self):
        return 1

    def currentTime(self):
        return 1

    def setCurrentTime_(self, v):
        pass

    def renderer_updateAtTime_(self, r, t):
        pass

    def renderer_didApplyAnimationsAtTime_(self, r, t):
        pass

    def renderer_didSimulatePhysicsAtTime_(self, r, t):
        pass

    def renderer_didRenderScene_atTime_(self, r, s, t):
        pass

    def renderer_didApplyConstraintsAtTime_atTime_(self, r, s, t):
        pass

    def renderer_willRenderScene_atTime_(self, r, s, t):
        pass

    def isTemporalAntialiasingEnabled(self):
        return 1

    def setTemporalAntialiasingEnabled_(self, v):
        pass

    def currentViewport(self):
        return 1


class TestSCNSceneRenderer(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(SceneKit.SCNAntialiasingMode)
        self.assertIsEnumType(SceneKit.SCNDebugOptions)
        self.assertIsEnumType(SceneKit.SCNRenderingAPI)

    def test_constants(self):
        self.assertIsInstance(SceneKit.SCNHitTestFirstFoundOnlyKey, str)
        self.assertIsInstance(SceneKit.SCNHitTestSortResultsKey, str)
        self.assertIsInstance(SceneKit.SCNHitTestClipToZRangeKey, str)
        self.assertIsInstance(SceneKit.SCNHitTestBackFaceCullingKey, str)
        self.assertIsInstance(SceneKit.SCNHitTestBoundingBoxOnlyKey, str)
        self.assertIsInstance(SceneKit.SCNHitTestIgnoreChildNodesKey, str)
        self.assertIsInstance(SceneKit.SCNHitTestRootNodeKey, str)

        self.assertEqual(SceneKit.SCNRenderingAPIMetal, 0)
        self.assertEqual(SceneKit.SCNRenderingAPIOpenGLLegacy, 1)
        self.assertEqual(SceneKit.SCNRenderingAPIOpenGLCore32, 2)
        self.assertEqual(SceneKit.SCNRenderingAPIOpenGLCore41, 3)

        self.assertEqual(SceneKit.SCNDebugOptionNone, 0)
        self.assertEqual(SceneKit.SCNDebugOptionShowPhysicsShapes, 1 << 0)
        self.assertEqual(SceneKit.SCNDebugOptionShowBoundingBoxes, 1 << 1)
        self.assertEqual(SceneKit.SCNDebugOptionShowLightInfluences, 1 << 2)
        self.assertEqual(SceneKit.SCNDebugOptionShowLightExtents, 1 << 3)
        self.assertEqual(SceneKit.SCNDebugOptionShowPhysicsFields, 1 << 4)
        self.assertEqual(SceneKit.SCNDebugOptionShowWireframe, 1 << 5)
        self.assertEqual(SceneKit.SCNDebugOptionRenderAsWireframe, 1 << 6)
        self.assertEqual(SceneKit.SCNDebugOptionShowSkeletons, 1 << 7)
        self.assertEqual(SceneKit.SCNDebugOptionShowCreases, 1 << 8)
        self.assertEqual(SceneKit.SCNDebugOptionShowConstraints, 1 << 9)
        self.assertEqual(SceneKit.SCNDebugOptionShowCameras, 1 << 10)

        self.assertIs(
            SceneKit.SCNHitTestOptionFirstFoundOnly,
            SceneKit.SCNHitTestFirstFoundOnlyKey,
        )
        self.assertIs(
            SceneKit.SCNHitTestOptionSortResults, SceneKit.SCNHitTestSortResultsKey
        )
        self.assertIs(
            SceneKit.SCNHitTestOptionClipToZRange, SceneKit.SCNHitTestClipToZRangeKey
        )
        self.assertIs(
            SceneKit.SCNHitTestOptionBackFaceCulling,
            SceneKit.SCNHitTestBackFaceCullingKey,
        )
        self.assertIs(
            SceneKit.SCNHitTestOptionBoundingBoxOnly,
            SceneKit.SCNHitTestBoundingBoxOnlyKey,
        )
        self.assertIs(
            SceneKit.SCNHitTestOptionIgnoreChildNodes,
            SceneKit.SCNHitTestIgnoreChildNodesKey,
        )
        self.assertIs(SceneKit.SCNHitTestOptionRootNode, SceneKit.SCNHitTestRootNodeKey)

    @min_os_level("10.9")
    def test_constants10_9(self):
        self.assertIsInstance(SceneKit.SCNHitTestIgnoreHiddenNodesKey, str)
        self.assertIs(
            SceneKit.SCNHitTestOptionIgnoreHiddenNodes,
            SceneKit.SCNHitTestIgnoreHiddenNodesKey,
        )

    @min_os_level("10.12")
    def test_constants10_12(self):
        self.assertIsInstance(SceneKit.SCNHitTestOptionCategoryBitMask, str)

    def testProtocolObjects(self):
        objc.protocolNamed("SCNSceneRenderer")

    @min_sdk_level("10.10")
    def testProtocolObjects10_10(self):
        objc.protocolNamed("SCNSceneRendererDelegate")

    def testMethods(self):
        self.assertArgIsBlock(
            TestSCNSceneRendererHelper.presentScene_withTransition_incomingPointOfView_completionHandler_,
            3,
            b"v",
        )
        self.assertResultHasType(TestSCNSceneRendererHelper.sceneTime, objc._C_DBL)
        self.assertArgHasType(TestSCNSceneRendererHelper.setSceneTime_, 0, objc._C_DBL)
        self.assertResultIsBOOL(
            TestSCNSceneRendererHelper.isNodeInsideFrustum_withPointOfView_
        )
        self.assertResultHasType(
            TestSCNSceneRendererHelper.projectPoint_, SceneKit.SCNVector3.__typestr__
        )
        self.assertArgHasType(
            TestSCNSceneRendererHelper.projectPoint_, 0, SceneKit.SCNVector3.__typestr__
        )
        self.assertResultHasType(
            TestSCNSceneRendererHelper.unprojectPoint_, SceneKit.SCNVector3.__typestr__
        )
        self.assertArgHasType(
            TestSCNSceneRendererHelper.unprojectPoint_,
            0,
            SceneKit.SCNVector3.__typestr__,
        )
        self.assertResultIsBOOL(TestSCNSceneRendererHelper.isPlaying)
        self.assertArgIsBOOL(TestSCNSceneRendererHelper.setPlaying_, 0)
        self.assertResultIsBOOL(TestSCNSceneRendererHelper.loops)
        self.assertArgIsBOOL(TestSCNSceneRendererHelper.setLoops_, 0)
        self.assertResultIsBOOL(TestSCNSceneRendererHelper.autoenablesDefaultLighting)
        self.assertArgIsBOOL(
            TestSCNSceneRendererHelper.setAutoenablesDefaultLighting_, 0
        )
        self.assertResultIsBOOL(TestSCNSceneRendererHelper.isJitteringEnabled)
        self.assertArgIsBOOL(TestSCNSceneRendererHelper.setJitteringEnabled_, 0)
        self.assertResultIsBOOL(
            TestSCNSceneRendererHelper.prepareObject_shouldAbortBlock_
        )
        self.assertArgIsBlock(
            TestSCNSceneRendererHelper.prepareObject_shouldAbortBlock_, 1, b"Z"
        )
        self.assertArgIsBlock(
            TestSCNSceneRendererHelper.prepareObjects_withCompletionHandler_, 1, b"vZ"
        )
        self.assertResultIsBOOL(TestSCNSceneRendererHelper.showsStatistics)
        self.assertArgIsBOOL(TestSCNSceneRendererHelper.setShowsStatistics_, 0)
        self.assertResultHasType(
            TestSCNSceneRendererHelper.debugOptions, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestSCNSceneRendererHelper.setDebugOptions_, 0, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestSCNSceneRendererHelper.renderingAPI, objc._C_NSUInteger
        )
        # self.assertArgHasType(TestSCNSceneRendererHelper.setRenderingAPI_, 0, objc._C_NSUInteger)
        self.assertResultHasType(TestSCNSceneRendererHelper.context, b"^v")
        # self.assertArgHasType(TestSCNSceneRendererHelper.setContext_, 0, b'^v')
        self.assertResultHasType(
            TestSCNSceneRendererHelper.colorPixelFormat, objc._C_NSUInteger
        )
        # self.assertArgHasType(TestSCNSceneRendererHelper.setColorPixelFormat_, 0, objc._C_NSUInteger)
        self.assertResultHasType(
            TestSCNSceneRendererHelper.depthPixelFormat, objc._C_NSUInteger
        )
        # self.assertArgHasType(TestSCNSceneRendererHelper.setDepthPixelFormat_, 0, objc._C_NSUInteger)
        self.assertResultHasType(
            TestSCNSceneRendererHelper.stencilPixelFormat, objc._C_NSUInteger
        )
        # self.assertArgHasType(TestSCNSceneRendererHelper.setStencilPixelFormat_, 0, objc._C_NSUInteger)
        self.assertResultHasType(TestSCNSceneRendererHelper.currentTime, objc._C_DBL)
        self.assertArgHasType(
            TestSCNSceneRendererHelper.setCurrentTime_, 0, objc._C_DBL
        )
        self.assertArgHasType(
            TestSCNSceneRendererHelper.renderer_updateAtTime_, 1, objc._C_DBL
        )
        self.assertArgHasType(
            TestSCNSceneRendererHelper.renderer_didApplyAnimationsAtTime_,
            1,
            objc._C_DBL,
        )
        self.assertArgHasType(
            TestSCNSceneRendererHelper.renderer_didSimulatePhysicsAtTime_,
            1,
            objc._C_DBL,
        )

        self.assertArgHasType(
            TestSCNSceneRendererHelper.renderer_didApplyConstraintsAtTime_atTime_,
            2,
            objc._C_DBL,
        )
        self.assertArgHasType(
            TestSCNSceneRendererHelper.renderer_willRenderScene_atTime_, 2, objc._C_DBL
        )
        self.assertArgHasType(
            TestSCNSceneRendererHelper.renderer_didRenderScene_atTime_, 2, objc._C_DBL
        )

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertResultIsBOOL(
            TestSCNSceneRendererHelper.isTemporalAntialiasingEnabled
        )
        self.assertArgIsBOOL(
            TestSCNSceneRendererHelper.setTemporalAntialiasingEnabled_, 0
        )

        self.assertResultHasType(
            TestSCNSceneRendererHelper.currentViewport, SceneKit.CGRect.__typestr__
        )
