from PyObjCTools.TestSupport import TestCase

import ExtensionKit


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(ExtensionKit)
