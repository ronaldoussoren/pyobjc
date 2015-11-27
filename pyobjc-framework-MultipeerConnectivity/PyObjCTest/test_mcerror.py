import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import MultipeerConnectivity

    class TestMCError (TestCase):
        @min_os_level("10.10")
        def testContents(self):
            self.assertEqual(MultipeerConnectivity.MCErrorUnknown, 0)
            self.assertEqual(MultipeerConnectivity.MCErrorNotConnected, 1)
            self.assertEqual(MultipeerConnectivity.MCErrorInvalidParameter, 2)
            self.assertEqual(MultipeerConnectivity.MCErrorUnsupported, 3)
            self.assertEqual(MultipeerConnectivity.MCErrorTimedOut, 4)
            self.assertEqual(MultipeerConnectivity.MCErrorCancelled, 5)
            self.assertEqual(MultipeerConnectivity.MCErrorUnavailable, 6)

if __name__ == "__main__":
    main()
