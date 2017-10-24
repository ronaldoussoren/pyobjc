from PyObjCTools.TestSupport import *

class TestCoreServices (TestCase):
    def testBasicImport (self):
        import CoreServices

        # DictionaryServices
        self.assertHasAttr(CoreServices, 'DCSCopyTextDefinition')

        # FSEvents
        self.assertHasAttr(CoreServices, 'FSEventStreamShow')

        # SearchKit
        self.assertHasAttr(CoreServices, 'SKSummaryGetSentenceSummaryInfo')

        # SharedFileList
        self.assertHasAttr(CoreServices, 'LSSharedFileListItemGetTypeID')

if __name__ == "__main__":
    main()
