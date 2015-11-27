from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2 ** 32:
    import GameCenter

    class TestGKSessionError (TestCase):
        @min_os_level('10.8')
        def testConstants10_8(self):
            self.assertIsInstance(GameCenter.GKSessionErrorDomain, unicode)

            self.assertEqual(GameCenter.GKSessionInvalidParameterError, 30500)
            self.assertEqual(GameCenter.GKSessionPeerNotFoundError, 30501)
            self.assertEqual(GameCenter.GKSessionDeclinedError, 30502)
            self.assertEqual(GameCenter.GKSessionTimedOutError, 30503)
            self.assertEqual(GameCenter.GKSessionCancelledError, 30504)
            self.assertEqual(GameCenter.GKSessionConnectionFailedError, 30505)
            self.assertEqual(GameCenter.GKSessionConnectionClosedError, 30506)
            self.assertEqual(GameCenter.GKSessionDataTooBigError, 30507)
            self.assertEqual(GameCenter.GKSessionNotConnectedError, 30508)
            self.assertEqual(GameCenter.GKSessionCannotEnableError, 30509)
            self.assertEqual(GameCenter.GKSessionInProgressError, 30510)
            self.assertEqual(GameCenter.GKSessionConnectivityError, 30201)
            self.assertEqual(GameCenter.GKSessionTransportError, 30202)
            self.assertEqual(GameCenter.GKSessionInternalError, 30203)
            self.assertEqual(GameCenter.GKSessionUnknownError, 30204)
            self.assertEqual(GameCenter.GKSessionSystemError, 30205)

if __name__ == "__main__":
    main()
