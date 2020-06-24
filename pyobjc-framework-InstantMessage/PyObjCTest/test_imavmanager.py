import InstantMessage
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestIMAVManagerHelper(InstantMessage.NSObject):
    def getPixelBufferPixelFormat_(self, _):
        return 10

    def renderIntoPixelBuffer_forTime_(self, buf, time):
        return False

    def getOpenGLBufferContext_pixelFormat_(self, ctx, fmt):
        pass

    def renderIntoOpenGLBuffer_onScreen_forTime_(self, buffer, screen, time):
        return False


class TestIMAVManager(TestCase):
    @min_os_level("10.5")
    def testConstants(self):
        self.assertIsInstance(InstantMessage.IMAVManagerStateChangedNotification, str)
        self.assertIsInstance(
            InstantMessage.IMAVManagerURLToShareChangedNotification, str
        )

        self.assertEqual(InstantMessage.IMAVInactive, 0)
        self.assertEqual(InstantMessage.IMAVRequested, 1)
        self.assertEqual(InstantMessage.IMAVShuttingDown, 2)
        self.assertEqual(InstantMessage.IMAVStartingUp, 3)
        self.assertEqual(InstantMessage.IMAVPending, 4)
        self.assertEqual(InstantMessage.IMAVRunning, 5)

        self.assertEqual(InstantMessage.IMVideoOptimizationDefault, 0)
        self.assertEqual(InstantMessage.IMVideoOptimizationStills, 1 << 0)
        self.assertEqual(InstantMessage.IMVideoOptimizationReplacement, 1 << 1)

    def testInformalProtocol(self):
        # self.assert_( hasattr(protocols, 'IMVideoDataSource') )
        # self.assert_( isinstance(protocols.IMVideoDataSource, objc.informal_protocol) )

        self.assertArgIsOut(TestIMAVManagerHelper.getPixelBufferPixelFormat_, 0)
        self.assertArgHasType(
            TestIMAVManagerHelper.getPixelBufferPixelFormat_, 0, b"o^" + objc._C_UINT
        )

        self.assertResultIsBOOL(TestIMAVManagerHelper.renderIntoPixelBuffer_forTime_)
        self.assertArgIsIn(TestIMAVManagerHelper.renderIntoPixelBuffer_forTime_, 1)

        self.assertResultIsBOOL(
            TestIMAVManagerHelper.renderIntoOpenGLBuffer_onScreen_forTime_
        )
