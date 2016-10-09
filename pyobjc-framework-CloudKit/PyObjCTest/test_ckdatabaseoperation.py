
import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CloudKit

    class TestCKDatabaseOperation (TestCase):
        @min_os_level("10.10")
        def testClasses(self):
            self.assertHasAttr(CloudKit, "CKDatabaseOperation")
            self.assertIsInstance(CloudKit.CKDatabaseOperation, objc.objc_class)

if __name__ == "__main__":
    main()
