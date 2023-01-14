from PyObjCTools.TestSupport import TestCase

import PHASE


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(
            PHASE,
            exclude_attrs={
                ("NSObject", "isKeyExcludedFromWebScript_"),
                ("NSObject", "newTaggedNSStringWithASCIIBytes__length__"),
                ("NSObject", "utf8ValueSafe"),
                ("NSObject", "utf8ValueSafe_"),
                "CMTimebaseRef",
                "CMBlockBufferRef",
                "CMSimpleQueueef",
                "CMSimpleQueueRef",
                "CMSampleBufferrRef",
                "CMSampleBufferRef",
                "CMMemoryPoolRef",
                "CMFormatDescriptionRef",
                "CMBufferQueueRef",
                "CMClockRef",
            },
        )
