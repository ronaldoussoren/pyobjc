import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import LinkPresentation

    class TestLPMetadataProvider(TestCase):
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
