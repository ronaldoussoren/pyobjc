from PyObjCTools.TestSupport import TestCase

import AuthenticationServices


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(AuthenticationServices)
