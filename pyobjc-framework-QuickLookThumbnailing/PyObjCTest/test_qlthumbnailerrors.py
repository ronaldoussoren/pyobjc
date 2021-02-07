from PyObjCTools.TestSupport import TestCase

import QuickLookThumbnailing


class TestQLThumbnailErrors(TestCase):
    def test_constants(self):
        self.assertEqual(QuickLookThumbnailing.QLThumbnailErrorGenerationFailed, 0)
        self.assertEqual(QuickLookThumbnailing.QLThumbnailErrorSavingToURLFailed, 1)
        self.assertEqual(QuickLookThumbnailing.QLThumbnailErrorNoCachedThumbnail, 2)
        self.assertEqual(QuickLookThumbnailing.QLThumbnailErrorNoCloudThumbnail, 3)
        self.assertEqual(QuickLookThumbnailing.QLThumbnailErrorRequestInvalid, 4)
        self.assertEqual(QuickLookThumbnailing.QLThumbnailErrorRequestCancelled, 5)
