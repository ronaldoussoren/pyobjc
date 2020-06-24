from PyObjCTools.TestSupport import TestCase

import LinkPresentation


class TestLPMetadataProvider(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            LinkPresentation.LPMetadataProvider.startFetchingMetadataForURL_completionHandler_,  # noqa: B950
            1,
            b"v@@",
        )

        self.assertResultIsBOOL(
            LinkPresentation.LPMetadataProvider.shouldFetchSubresources
        )
        self.assertArgIsBOOL(
            LinkPresentation.LPMetadataProvider.setShouldFetchSubresources_, 0
        )
