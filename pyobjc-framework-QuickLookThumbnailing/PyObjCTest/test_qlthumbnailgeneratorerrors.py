import sys
from PyObjCTest import *

if sys.maxsize > 2 ** 32:
    import QuickLookThumbnailing

    class TestQLThumbnailGeneratorErrors (TestCase):
        @min_os_level('10.15')
        def test_constants(self):
            self.assertIsInstance(QuickLookThumbnailing.QLThumbnailGeneratorErrorDomain, unicode)

            self.assertEqual(QuickLookThumbnailing.QLThumbnailGeneratorErrorGenerationFailed, 0)
            self.assertEqual(QuickLookThumbnailing.QLThumbnailGeneratorErrorSavingToURLFailed, 1)
            self.assertEqual(QuickLookThumbnailing.QLThumbnailGeneratorErrorNoCachedThumbnail, 2)
            self.assertEqual(QuickLookThumbnailing.QLThumbnailGeneratorErrorNoCloudThumbnail, 3)
            self.assertEqual(QuickLookThumbnailing.QLThumbnailGeneratorErrorRequestInvalid, 4)
            self.assertEqual(QuickLookThumbnailing.QLThumbnailGeneratorErrorRequestCancelled, 5)



