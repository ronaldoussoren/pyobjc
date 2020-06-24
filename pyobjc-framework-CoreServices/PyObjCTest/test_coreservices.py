from PyObjCTools.TestSupport import TestCase


class TestCoreServices(TestCase):
    def testBasicImport(self):
        import CoreServices

        # DictionaryServices
        self.assertHasAttr(CoreServices, "DCSCopyTextDefinition")

        # FSEvents
        self.assertHasAttr(CoreServices, "FSEventStreamShow")

        # SearchKit
        self.assertHasAttr(CoreServices, "SKSummaryGetSentenceSummaryInfo")

        # SharedFileList
        self.assertHasAttr(CoreServices, "LSSharedFileListItemGetTypeID")
