from PyObjCTools.TestSupport import TestCase

import IMServicePlugIn


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(
            IMServicePlugIn,
            exclude_attrs={
                (
                    "NSObject",
                    "copyRenderedTextureForCGLContext_pixelFormat_bounds_isFlipped_",
                ),
            },
        )
