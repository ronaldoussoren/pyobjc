import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CloudKit

    class TestCKRecord (TestCase):
        @min_sdk_level("10.11")
        def testProtocols(self):
            objc.protocolNamed('CKRecordKeyValueSetting')

        @min_os_level("10.10")
        def testClasses(self):
            self.assertHasAttr(CloudKit, "CKRecord")
            self.assertIsInstance(CloudKit.CKRecord, objc.objc_class)

        @min_os_level("10.10")
        def testConstants(self):
            self.assertIsInstance(CloudKit.CKRecordTypeUserRecord, unicode)

        @min_os_level("10.12")
        def testConstants(self):
            self.assertIsInstance(CloudKit.CKRecordParentKey, unicode)
            self.assertIsInstance(CloudKit.CKRecordShareKey, unicode)

if __name__ == "__main__":
    main()
