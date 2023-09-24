from PyObjCTools.TestSupport import TestCase


import CoreServices


class TestCoreServices(TestCase):
    def testBasicImport(self):
        # DictionaryServices
        self.assertHasAttr(CoreServices, "DCSCopyTextDefinition")

        # FSEvents
        self.assertHasAttr(CoreServices, "FSEventStreamShow")

        # SearchKit
        self.assertHasAttr(CoreServices, "SKSummaryGetSentenceSummaryInfo")

        # SharedFileList
        self.assertHasAttr(CoreServices, "LSSharedFileListItemGetTypeID")


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(
            CoreServices,
            exclude_attrs=(
                "MDQuerySetCreateResultFunction",
                "MDQuerySetCreateValueFunction",
            ),
        )
