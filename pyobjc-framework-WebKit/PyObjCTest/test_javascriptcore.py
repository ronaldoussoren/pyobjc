from PyObjCTools.TestSupport import TestCase

import JavaScriptCore


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(
            JavaScriptCore,
            exclude_attrs={
                # Private classes on macOS 10.13
                "ABCDContact_ABCDContact_",
                "ABCDGroup_ABCDGroup_",
            },
        )
