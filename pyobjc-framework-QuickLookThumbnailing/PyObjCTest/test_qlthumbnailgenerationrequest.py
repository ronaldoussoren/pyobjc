from PyObjCTools.TestSupport import TestCase, min_os_level

import QuickLookThumbnailing


class TestQLThumbnailGenerationRequest(TestCase):
    @min_os_level("10.15")
    def test_constants(self):
        self.assertEqual(
            QuickLookThumbnailing.QLThumbnailGenerationRequestRepresentationTypeIcon,
            1 << 0,
        )
        self.assertEqual(
            QuickLookThumbnailing.QLThumbnailGenerationRequestRepresentationTypeLowQualityThumbnail,  # noqa: B950
            1 << 1,
        )
        self.assertEqual(
            QuickLookThumbnailing.QLThumbnailGenerationRequestRepresentationTypeThumbnail,
            1 << 2,
        )
        self.assertEqual(
            QuickLookThumbnailing.QLThumbnailGenerationRequestRepresentationTypeAll,
            QuickLookThumbnailing.NSUIntegerMax,
        )

    @min_os_level("10.15")
    def test_methods(self):
        self.assertResultIsBOOL(
            QuickLookThumbnailing.QLThumbnailGenerationRequest.iconMode
        )
        self.assertArgIsBOOL(
            QuickLookThumbnailing.QLThumbnailGenerationRequest.setIconMode_, 0
        )
