from PyObjCTools.TestSupport import TestCase

import ExtensionKit


class TestEXHostViewControllerHelper(ExtensionKit.NSObject):
    def shouldAcceptXPCConnection_(self, a):
        return 1


class TestEXHostViewController(TestCase):
    def test_methods(self):
        self.assertArgIsOut(
            ExtensionKit.EXHostViewController.makeXPCConnectionWithError_, 0
        )

    def test_protocols(self):
        self.assertProtocolExists("EXHostViewControllerDelegate")

    def test_protocol_methods(self):
        self.assertResultIsBOOL(
            TestEXHostViewControllerHelper.shouldAcceptXPCConnection_
        )
