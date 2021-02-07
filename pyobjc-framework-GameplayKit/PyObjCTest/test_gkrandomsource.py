from PyObjCTools.TestSupport import TestCase
import objc

import GameplayKit


class TestGKRandomSourceHelper(GameplayKit.NSObject):
    def nextInt(self):
        return 1

    def nextIntWithUpperBound_(self, b):
        return 1

    def nextUniform(self):
        return 1

    def nextBool(self):
        return 1


class TestGKRandomSource(TestCase):
    def testProtocols(self):
        objc.protocolNamed("GKRandom")

    def testMethods(self):
        self.assertResultHasType(
            GameplayKit.TestGKRandomSourceHelper.nextInt, objc._C_NSInteger
        )

        self.assertResultHasType(
            GameplayKit.TestGKRandomSourceHelper.nextIntWithUpperBound_,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            GameplayKit.TestGKRandomSourceHelper.nextIntWithUpperBound_,
            0,
            objc._C_NSUInteger,
        )

        self.assertResultHasType(
            GameplayKit.TestGKRandomSourceHelper.nextUniform, objc._C_FLT
        )
