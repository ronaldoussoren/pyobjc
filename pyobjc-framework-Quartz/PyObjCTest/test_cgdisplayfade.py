
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGDisplayFade (TestCase):
    def testConstants(self):
        self.failUnlessEqual(kCGDisplayFadeReservationInvalidToken, 0)
        self.failUnlessEqual(kCGDisplayBlendNormal, 0.0)
        self.failUnlessEqual(kCGDisplayBlendSolidColor, 1.0)
        self.failUnlessEqual(kCGMaxDisplayReservationInterval, 15.0)

    def testFunctions(self):
        err, config = CGBeginDisplayConfiguration(None)
        self.failUnlessEqual(err, 0)
        self.failUnlessIsInstance(config, CGDisplayConfigRef)

        err = CGConfigureDisplayFadeEffect(config,
                0.1, 0.1, 1.0, 1.0, 1.0)
        self.failUnlessEqual(err, 0)

        err, token = CGAcquireDisplayFadeReservation(1.0, None)
        self.failUnlessEqual(err, 0)
        self.failUnlessIsInstance(token, (int, long))

        err = CGDisplayFade(token,
                0.5, 0.0, 1.0, 1.0, 1.0, 1.0, 1)
        self.failUnlessEqual(err, 0)

        err = CGReleaseDisplayFadeReservation(token)
        self.failUnlessEqual(err, 0)

        v = CGDisplayFadeOperationInProgress()
        self.failUnlessIsInstance(v, (int, long))


if __name__ == "__main__":
    main()
