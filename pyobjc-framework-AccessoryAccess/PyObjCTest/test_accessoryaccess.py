from PyObjCTools.TestSupport import TestCase

import AccessoryAccess


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(AccessoryAccess)
