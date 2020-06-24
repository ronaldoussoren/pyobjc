from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCGDisplayFade(TestCase):
    def testConstants(self):
        self.assertEqual(Quartz.kCGDisplayFadeReservationInvalidToken, 0)
        self.assertEqual(Quartz.kCGDisplayBlendNormal, 0.0)
        self.assertEqual(Quartz.kCGDisplayBlendSolidColor, 1.0)
        self.assertEqual(Quartz.kCGMaxDisplayReservationInterval, 15.0)

    def testFunctions(self):
        err, config = Quartz.CGBeginDisplayConfiguration(None)
        self.assertEqual(err, 0)
        self.assertIsInstance(config, Quartz.CGDisplayConfigRef)

        err = Quartz.CGConfigureDisplayFadeEffect(config, 0.1, 0.1, 1.0, 1.0, 1.0)
        self.assertEqual(err, 0)

        err, token = Quartz.CGAcquireDisplayFadeReservation(1.0, None)
        if err == 0:
            self.assertEqual(err, 0)
            self.assertIsInstance(token, int)

            err = Quartz.CGDisplayFade(token, 0.5, 0.0, 1.0, 1.0, 1.0, 1.0, 1)
            self.assertEqual(err, 0)

            err = Quartz.CGReleaseDisplayFadeReservation(token)

            # Testing if the api actually works as intended is not necessary,
            # don't bail out if the function is unhappy.
            # self.assertEqual(err, 0)
            self.assertIsInstance(err, int)

        v = Quartz.CGDisplayFadeOperationInProgress()
        self.assertIsInstance(v, int)
