from PyObjCTools.TestSupport import TestCase

import ContactsUI


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(
            ContactsUI,
            exclude_attrs={
                (
                    "NSObject",
                    "copyRenderedTextureForCGLContext_pixelFormat_bounds_isFlipped_",
                ),
            },
        )
