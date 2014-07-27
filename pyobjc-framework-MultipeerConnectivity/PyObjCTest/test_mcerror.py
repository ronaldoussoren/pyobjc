import sys

try:
    unicode
except NameError:
    unicode = str

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import MultipeerConnectivity

    class TestMCError (TestCase):
        @min_os_level("10.10")
        def testContents(self)
            self.assertIsInstance(MultipeerConnectivity.MCErrorUnknown, 0)
            self.assertIsInstance(MultipeerConnectivity.MCErrorNotConnected, 1)
            self.assertIsInstance(MultipeerConnectivity.MCErrorInvalidParameter, 2)
            self.assertIsInstance(MultipeerConnectivity.MCErrorUnsupported, 3)
            self.assertIsInstance(MultipeerConnectivity.MCErrorTimedOut, 4)
            self.assertIsInstance(MultipeerConnectivity.MCErrorCancelled, 5)
            self.assertIsInstance(MultipeerConnectivity.MCErrorUnavailable, 6)

if __name__ == "__main__":
    main()
