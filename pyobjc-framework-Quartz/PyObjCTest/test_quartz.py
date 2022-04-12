from PyObjCTools.TestSupport import TestCase

import Quartz


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(
            Quartz,
            exclude_attrs={
                "NSColor",
                ("NSColor", "scn_C3DColorIgnoringColorSpace_success_"),
            },
        )
