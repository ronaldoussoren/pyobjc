from PyObjCTools.TestSupport import TestCase
import ShazamKit


class TestSHError(TestCase):
    def test_constants(self):
        self.assertIsInstance(ShazamKit.SHErrorDomain, str)

        self.assertEqual(ShazamKit.SHErrorCodeInvalidAudioFormat, 100)
        self.assertEqual(ShazamKit.SHErrorCodeAudioDiscontinuity, 101)
        self.assertEqual(ShazamKit.SHErrorCodeSignatureInvalid, 200)
        self.assertEqual(ShazamKit.SHErrorCodeSignatureDurationInvalid, 201)
        self.assertEqual(ShazamKit.SHErrorCodeMatchAttemptFailed, 202)
        self.assertEqual(ShazamKit.SHErrorCodeCustomCatalogInvalid, 300)
        self.assertEqual(ShazamKit.SHErrorCodeCustomCatalogInvalidURL, 301)
        self.assertEqual(ShazamKit.SHErrorCodeMediaLibrarySyncFailed, 400)
