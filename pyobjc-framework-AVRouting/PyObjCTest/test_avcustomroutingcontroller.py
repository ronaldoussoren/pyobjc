from PyObjCTools.TestSupport import TestCase

import AVRouting


class TestAVCustomRoutingControllerHelper(AVRouting.NSObject):
    def customRoutingController_handleEvent_completionHandler_(self, a, b, c):
        pass


class TestAVCustomRoutingController(TestCase):
    def test_constants(self):
        self.assertIsInstance(
            AVRouting.AVCustomRoutingControllerAuthorizedRoutesDidChangeNotification,
            str,
        )

    def test_protocols(self):
        self.assertProtocolExists("AVCustomRoutingControllerDelegate")

    def test_protocol_methods(self):
        self.assertArgIsBlock(
            TestAVCustomRoutingControllerHelper.customRoutingController_handleEvent_completionHandler_,
            2,
            b"vZ",
        )

    def test_methods(self):
        self.assertResultIsBOOL(AVRouting.AVCustomRoutingController.isRouteActive_)
