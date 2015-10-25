from PyObjCTools.TestSupport import *
import objc

import SceneKit

SCNSceneExportProgressHandler = b'vf@o^Z'

class TestSCNSceneRendererHelper (SceneKit.NSObject):
    def presentScene_withTransition_incomingPointOfView_completionHandler_(self, s, t, v, h): pass
    def sceneTime(self): return 1
    def setSceneTime_(self, t): pass
    def hitTest_options_(self, p, o): return 1
    def isNodeInsideFrustum_withPointOfView_(self, n, v): return 1
    def projectPoint_(self, p): return p
    def unprojectPoint_(self, p): return p
    def isPlaying(self): return 1
    def setPlaying_(self, v): pass
    def loops(self): return 1
    def setLoops_(self, v): pass
    def autoenablesDefaultLighting(self): return 1
    def setAutoenablesDefaultLighting_(self, v): pass
    def isJitteringEnabled(self): return 1
    def setJitteringEnabled_(self, v): pass
    def prepareObject_shouldAbortBlock_(self, o, b): return 1
    def prepareObjects_withCompletionHandler_(self, o, h): pass
    def showsStatistics(self): return 1
    def setShowsStatistics_(self, v): pass
    def debugOptions(self): return 1
    def setDebugOptions_(self, v): pass
    def renderingAPI(self): return 1
    def context(self): return 1
    def colorPixelFormat(self): return 1
    def depthPixelFormat(self): return 1
    def stencilPixelFormat(self): return 1
    def currentTime(self): return 1
    def setCurrentTime_(self, v): pass

    def renderer_updateAtTime_(self, r, t): pass
    def renderer_didApplyAnimationsAtTime_(self, r, t): pass
    def renderer_didSimulatePhysicsAtTime_(self, r, t): pass
    def renderer_didRenderScene_atTime_(self, r, s, t): pass




class TestSCNSceneRenderer (TestCase):
    def test_constants(self):
        self.assertIsInstance(SceneKit.SCNHitTestFirstFoundOnlyKey, unicode)
        self.assertIsInstance(SceneKit.SCNHitTestSortResultsKey, unicode)
        self.assertIsInstance(SceneKit.SCNHitTestClipToZRangeKey, unicode)
        self.assertIsInstance(SceneKit.SCNHitTestBackFaceCullingKey, unicode)
        self.assertIsInstance(SceneKit.SCNHitTestBoundingBoxOnlyKey, unicode)
        self.assertIsInstance(SceneKit.SCNHitTestIgnoreChildNodesKey, unicode)
        self.assertIsInstance(SceneKit.SCNHitTestRootNodeKey, unicode)

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


    @min_os_level('10.9')
    def test_constants10_9(self):
        self.assertIsInstance(SceneKit.SCNHitTestIgnoreHiddenNodesKey, unicode)

    def testProtocols(self):
        objc.protocolNamed('SCNSceneRenderer')
        objc.protocolNamed('SCNSceneRendererDelegate')


    def testMethods(self):
        self.fail('TestSCNSceneRendererHelper')


if __name__ == "__main__":
    main()
