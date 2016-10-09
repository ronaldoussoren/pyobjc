import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CloudKit

    class TestCKShare (TestCase):
        @min_os_level("10.12")
        def testConstants10_12(self):
            self.assertIsInstance(CloudKit.CKRecordTypeShare, unicode)
            self.assertIsInstance(CloudKit.CKShareTitleKey, unicode)
            self.assertIsInstance(CloudKit.CKShareThumbnailImageDataKey, unicode)
            self.assertIsInstance(CloudKit.CKShareTypeKey, unicode)

if __name__ == "__main__":
    main()
