import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import MultipeerConnectivity

    class TestMCAdvertiserAssistant (TestCase):
        @min_os_level("10.10")
        def testClasses(self):
            self.assertIsInstance(MultipeerConnectivity.MCAdvertiserAssistant, objc.objc_class)

        @min_os_level("10.10")
        def testProtocols(self):
            self.assertIsInstance(objc.protocolNamed("MCAdvertiserAssistantDelegate"), objc.formal_protocol)

if __name__ == "__main__":
    main()
