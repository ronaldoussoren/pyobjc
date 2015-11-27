import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CloudKit

    class TestCKReference (TestCase):
        @min_os_level("10.10")
        def testClasses(self):
            self.assertHasAttr(CloudKit, "CKReference")
            self.assertIsInstance(CloudKit.CKReference, objc.objc_class)

        @min_os_level("10.10")
        def testConstants(self):
            self.assertEqual(CloudKit.CKReferenceActionNone, 0)
            self.assertEqual(CloudKit.CKReferenceActionDeleteSelf, 1)

if __name__ == "__main__":
    main()
