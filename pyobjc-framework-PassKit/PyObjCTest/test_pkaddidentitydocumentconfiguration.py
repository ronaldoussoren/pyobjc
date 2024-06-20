from PyObjCTools.TestSupport import TestCase, min_os_level

import PassKit


class TestPKAddIdentityDocumentConfiguration(TestCase):
    @min_os_level("15.0")
    def test_methods(self):
        self.assertArgIsBlock(
            PassKit.PKAddIdentityDocumentConfiguration.configurationForMetadata_completion_,
            1,
            b"v@@",
        )
