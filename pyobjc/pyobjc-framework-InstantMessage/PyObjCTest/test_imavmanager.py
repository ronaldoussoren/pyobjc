
from PyObjCTools.TestSupport import *
from InstantMessage import *

class TestIMAVManagerHelper (NSObject):
    def getPixelBufferPixelFormat_(self, _):
        return 10

    def renderIntoPixelBuffer_forTime_(self, buf, time):
        return False

    def getOpenGLBufferContext_pixelFormat_(self, ctx, fmt):
        pass

    def renderIntoOpenGLBuffer_onScreen_forTime_(self, buffer, screen, time):
        return False

class TestIMAVManager (TestCase):
    @min_os_level('10.5')
    def testConstants(self):
        self.assertIsInstance(IMAVManagerStateChangedNotification, unicode)
        self.assertIsInstance(IMAVManagerURLToShareChangedNotification, unicode)

        self.assertEqual(IMAVInactive, 0)
        self.assertEqual(IMAVRequested, 1)
        self.assertEqual(IMAVShuttingDown, 2)
        self.assertEqual(IMAVStartingUp, 3)
        self.assertEqual(IMAVPending, 4)
        self.assertEqual(IMAVRunning, 5)

        self.assertEqual(IMVideoOptimizationDefault, 0)
        self.assertEqual(IMVideoOptimizationStills, 1 << 0)
        self.assertEqual(IMVideoOptimizationReplacement, 1 << 1)

    def testInformalProtocol (self):
        self.assert_( hasattr(protocols, 'IMVideoDataSource') )
        self.assert_( isinstance(protocols.IMVideoDataSource, objc.informal_protocol) )

        self.assertArgIsOut(TestIMAVManagerHelper.getPixelBufferPixelFormat_, 0)
        self.assertArgHasType(TestIMAVManagerHelper.getPixelBufferPixelFormat_, 0, b'o^I')

        self.assertResultIsBOOL(TestIMAVManagerHelper.renderIntoPixelBuffer_forTime_)
        self.assertArgIsIn(TestIMAVManagerHelper.renderIntoPixelBuffer_forTime_, 1)


        self.assertResultIsBOOL(TestIMAVManagerHelper.renderIntoOpenGLBuffer_onScreen_forTime_)


if __name__ == "__main__":
    main()
