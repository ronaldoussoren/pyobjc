from PyObjCTools.TestSupport import TestCase, min_os_level

import QuickLookThumbnailing


class TestQLThumbnailRepresentation(TestCase):
    @min_os_level("10.15")
    def test_constants(self):
        self.assertEqual(QuickLookThumbnailing.QLThumbnailRepresentationTypeIcon, 0)
        self.assertEqual(
            QuickLookThumbnailing.QLThumbnailRepresentationTypeLowQualityThumbnail, 1
        )
        self.assertEqual(
            QuickLookThumbnailing.QLThumbnailRepresentationTypeThumbnail, 2
        )
