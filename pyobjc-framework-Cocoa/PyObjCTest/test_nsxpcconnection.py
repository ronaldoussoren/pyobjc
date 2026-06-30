import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class XPCHelper(Foundation.NSObject):
    def remoteObjectProxyWithErrorHandler_(self, a):
        pass

    def listener_shouldAcceptNewConnection_(self, a, b):
        pass


class TestNSXPCConnection(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Foundation.NSXPCConnectionOptions)
        self.assertEqual(Foundation.NSXPCConnectionPrivileged, 1 << 12)

    def test_methods(self):
        self.assertArgIsBlock(
            Foundation.NSXPCConnection.remoteObjectProxyWithErrorHandler_, 0, b"v@"
        )
        self.assertResultIsBlock(Foundation.NSXPCConnection.interruptionHandler, b"v")
        self.assertArgIsBlock(
            Foundation.NSXPCConnection.setInterruptionHandler_, 0, b"v"
        )
        self.assertResultIsBlock(Foundation.NSXPCConnection.invalidationHandler, b"v")
        self.assertArgIsBlock(
            Foundation.NSXPCConnection.setInvalidationHandler_, 0, b"v"
        )

        self.assertArgIsBOOL(
            Foundation.NSXPCInterface.setClasses_forSelector_argumentIndex_ofReply_, 3
        )
        self.assertArgIsBOOL(
            Foundation.NSXPCInterface.classesForSelector_argumentIndex_ofReply_, 2
        )
        self.assertArgIsBOOL(
            Foundation.NSXPCInterface.setInterface_forSelector_argumentIndex_ofReply_, 3
        )
        self.assertArgIsBOOL(
            Foundation.NSXPCInterface.interfaceForSelector_argumentIndex_ofReply_, 2
        )

    @min_os_level("10.11")
    def test_methods10_11(self):
        self.assertArgIsBlock(
            Foundation.NSXPCConnection.synchronousRemoteObjectProxyWithErrorHandler_,
            0,
            b"v@",
        )

    @min_os_level("10.15")  # Not actually on 10.14...
    def test_methods10_14(self):
        self.assertArgIsBOOL(
            Foundation.NSXPCInterface.setXPCType_forSelector_argumentIndex_ofReply_, 3
        )
        self.assertArgIsBOOL(
            Foundation.NSXPCInterface.XPCTypeForSelector_argumentIndex_ofReply_, 2
        )

    def test_protocols(self):
        self.assertProtocolExists("NSXPCProxyCreating", Foundation)
        self.assertProtocolExists("NSXPCListenerDelegate", Foundation)

    def test_protocol_methods(self):
        self.assertArgIsBlock(XPCHelper.remoteObjectProxyWithErrorHandler_, 0, b"v@")
        self.assertResultIsBOOL(XPCHelper.listener_shouldAcceptNewConnection_)
