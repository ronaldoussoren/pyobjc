import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import MultipeerConnectivity

    class TestMCNearbyServiceBrowser (TestCase):
        @min_os_level("10.10")
        def testClasses(self):
            self.assertIsInstance(MultipeerConnectivity.MCNearbyServiceBrowser, objc.objc_class)

        @min_os_level("10.10")
        def testProtocols(self):
            self.assertIsInstance(objc.protocolNamed("MCNearbyServiceBrowserDelegate"), objc.formal_protocol)

if __name__ == "__main__":
    main()
