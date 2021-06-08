from PyObjCTools.TestSupport import TestCase, min_os_level

import LinkPresentation


class TestLPMetadataProvider(TestCase):
    @min_os_level("10.15")
    def test_methods(self):
        self.assertArgIsBlock(
            LinkPresentation.LPMetadataProvider.startFetchingMetadataForURL_completionHandler_,
            1,
            b"v@@",
        )

        self.assertResultIsBOOL(
            LinkPresentation.LPMetadataProvider.shouldFetchSubresources
        )
        self.assertArgIsBOOL(
            LinkPresentation.LPMetadataProvider.setShouldFetchSubresources_, 0
        )

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertArgIsBlock(
            LinkPresentation.LPMetadataProvider.startFetchingMetadataForRequest_completionHandler_,
            1,
            b"v@@",
        )
