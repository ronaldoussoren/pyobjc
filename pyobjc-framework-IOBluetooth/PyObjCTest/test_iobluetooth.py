from PyObjCTools.TestSupport import TestCase

import IOBluetooth


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(
            IOBluetooth,
            exclude_attrs={
                (
                    "NSObject",
                    "isKeyExcludedFromWebScript_",
                ),
                (
                    "NSObject",
                    "utf8ValueSafe_",
                ),
                (
                    "NSObject",
                    "utf8ValueSafe",
                ),
                (
                    "NSObject",
                    "newTaggedNSStringWithASCIIBytes__length__",
                ),
            },
        )
