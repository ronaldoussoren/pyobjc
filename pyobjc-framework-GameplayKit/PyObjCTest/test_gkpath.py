from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

import GameplayKit


class TestGKPath(TestCase):
    def testProtocols(self):
        objc.protocolNamed("GKAgentDelegate")

    def testMethods(self):
        self.assertResultIsBOOL(GameplayKit.GKPath.isCyclical)
        self.assertArgIsBOOL(GameplayKit.GKPath.setCyclical_, 0)

        # SIMD
        # self.assertArgIsIn(GameplayKit.GKPath.pathWithPoints_count_radius_cyclical_, 0)
        # self.assertArgSizeInArg(GameplayKit.GKPath.pathWithPoints_count_radius_cyclical_, 0, 1)
        # self.assertArgIsBOOL(GameplayKit.GKPath.pathWithPoints_count_radius_cyclical_, 3)

        # self.assertArgIsIn(GameplayKit.GKPath.initWithPoints_count_radius_cyclical_, 0)
        # self.assertArgSizeInArg(GameplayKit.GKPath.initWithPoints_count_radius_cyclical_, 0, 1)
        # self.assertArgIsBOOL(GameplayKit.GKPath.initWithPoints_count_radius_cyclical_, 3)

    @min_os_level("10.12")
    def testMethods10_12(self):
        # self.assertArgIsIn(GameplayKit.GKPath.pathWithFloat3Points_count_radius_cyclical_, 0)
        # self.assertArgSizeInArg(GameplayKit.GKPath.pathWithFloat3Points_count_radius_cyclical_, 0, 1)
        # self.assertArgIsBOOL(GameplayKit.GKPath.pathWithFloat3Points_count_radius_cyclical_, 3)

        # self.assertArgIsIn(GameplayKit.GKPath.initWithFloat3Points_count_radius_cyclical_, 0)
        # self.assertArgSizeInArg(GameplayKit.GKPath.initWithFloat3Points_count_radius_cyclical_, 0, 1)
        # self.assertArgIsBOOL(GameplayKit.GKPath.initWithFloat3Points_count_radius_cyclical_, 3)
        pass
