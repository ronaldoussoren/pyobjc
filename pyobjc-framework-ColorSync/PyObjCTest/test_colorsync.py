from PyObjCTools.TestSupport import TestCase, min_os_level

import ColorSync


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(ColorSync)

    @min_os_level("10.13")
    def test_functions(self):
        ColorSync.ColorSyncAPIVersion
