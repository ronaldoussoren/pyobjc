from PyObjCTools.TestSupport import TestCase

import GameCenter


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(
            GameCenter,
            exclude_attrs={
                (
                    "NSObject",
                    "copyRenderedTextureForCGLContext_pixelFormat_bounds_isFlipped_",
                ),
            },
        )
