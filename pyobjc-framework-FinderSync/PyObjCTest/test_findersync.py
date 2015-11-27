import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import FinderSync

    class TestFinderSync (TestCase):
        @min_os_level("10.10")
        def testClasses(self):
            self.assertIsInstance(FinderSync.FIFinderSyncController, objc.objc_class)
            self.assertIsInstance(FinderSync.FIFinderSync, objc.objc_class)

        @min_os_level("10.10")
        def testProtocols(self):
            self.assertIsInstance(objc.protocolNamed("FIFinderSync"), objc.formal_protocol)

        @min_os_level("10.10")
        def testConstants(self):
            self.assertEqual(FinderSync.FIMenuKindContextualMenuForItems, 0)
            self.assertEqual(FinderSync.FIMenuKindContextualMenuForContainer, 1)
            self.assertEqual(FinderSync.FIMenuKindContextualMenuForSidebar, 2)
            self.assertEqual(FinderSync.FIMenuKindToolbarItemMenu, 3)


if __name__ == "__main__":
    main()
