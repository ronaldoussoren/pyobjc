from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit


class TestCKShare(TestCase):
    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(CloudKit.CKRecordTypeShare, str)
        self.assertIsInstance(CloudKit.CKShareTitleKey, str)
        self.assertIsInstance(CloudKit.CKShareThumbnailImageDataKey, str)
        self.assertIsInstance(CloudKit.CKShareTypeKey, str)

    @min_os_level("12.0")
    def testConstants12_0(self):
        self.assertIsInstance(CloudKit.CKRecordNameZoneWideShare, str)

    @min_os_level("26.0")
    def test_methods(self):
        self.assertResultIsBOOL(CloudKit.CKShare.allowsAccessRequests)
        self.assertArgIsBOOL(CloudKit.CKShare.setAllowsAccessRequests_, 0)
