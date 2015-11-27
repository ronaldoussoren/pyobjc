import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import MultipeerConnectivity

    class TestMCPeerID (TestCase):
        @min_os_level("10.10")
        def testClasses(self):
            self.assertIsInstance(MultipeerConnectivity.MCPeerID, objc.objc_class)

if __name__ == "__main__":
    main()
