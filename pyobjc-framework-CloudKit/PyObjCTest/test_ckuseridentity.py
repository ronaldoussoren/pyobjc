import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CloudKit

    class TestCKUserIdentity (TestCase):
        @min_os_level("10.12")
        def testMethods10_12(self):
            self.assertResultIsBOOL(CloudKit.CKUserIdentity.hasiCloudAccount)

if __name__ == "__main__":
    main()
