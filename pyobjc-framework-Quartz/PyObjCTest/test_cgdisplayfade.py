
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGDisplayFade (TestCase):
    def testConstants(self):
        self.assertEqual(kCGDisplayFadeReservationInvalidToken, 0)
        self.assertEqual(kCGDisplayBlendNormal, 0.0)
        self.assertEqual(kCGDisplayBlendSolidColor, 1.0)
        self.assertEqual(kCGMaxDisplayReservationInterval, 15.0)

    def testFunctions(self):
        err, config = CGBeginDisplayConfiguration(None)
        self.assertEqual(err, 0)
        self.assertIsInstance(config, CGDisplayConfigRef)

        err = CGConfigureDisplayFadeEffect(config,
                0.1, 0.1, 1.0, 1.0, 1.0)
        self.assertEqual(err, 0)

        err, token = CGAcquireDisplayFadeReservation(1.0, None)
        self.assertEqual(err, 0)
        self.assertIsInstance(token, (int, long))

        err = CGDisplayFade(token,
                0.5, 0.0, 1.0, 1.0, 1.0, 1.0, 1)
        self.assertEqual(err, 0)

        err = CGReleaseDisplayFadeReservation(token)
        self.assertEqual(err, 0)

        v = CGDisplayFadeOperationInProgress()
        self.assertIsInstance(v, (int, long))


if __name__ == "__main__":
    main()
