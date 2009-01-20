
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
        self.failUnlessIsInstance(IMAVManagerStateChangedNotification, unicode)
        self.failUnlessIsInstance(IMAVManagerURLToShareChangedNotification, unicode)

        self.failUnlessEqual(IMAVInactive, 0)
        self.failUnlessEqual(IMAVRequested, 1)
        self.failUnlessEqual(IMAVShuttingDown, 2)
        self.failUnlessEqual(IMAVStartingUp, 3)
        self.failUnlessEqual(IMAVPending, 4)
        self.failUnlessEqual(IMAVRunning, 5)

        self.failUnlessEqual(IMVideoOptimizationDefault, 0)
        self.failUnlessEqual(IMVideoOptimizationStills, 1 << 0)
        self.failUnlessEqual(IMVideoOptimizationReplacement, 1 << 1)

    def testInformalProtocol (self):
        self.assert_( hasattr(protocols, 'IMVideoDataSource') )
        self.assert_( isinstance(protocols.IMVideoDataSource, objc.informal_protocol) )

        self.failUnlessArgIsOut(TestIMAVManagerHelper.getPixelBufferPixelFormat_, 0)
        self.failUnlessArgHasType(TestIMAVManagerHelper.getPixelBufferPixelFormat_, 0, 'o^I')

        self.failUnlessResultIsBOOL(TestIMAVManagerHelper.renderIntoPixelBuffer_forTime_)
        self.failUnlessArgIsIn(TestIMAVManagerHelper.renderIntoPixelBuffer_forTime_, 1)


        self.failUnlessResultIsBOOL(TestIMAVManagerHelper.renderIntoOpenGLBuffer_onScreen_forTime_)


if __name__ == "__main__":
    main()
