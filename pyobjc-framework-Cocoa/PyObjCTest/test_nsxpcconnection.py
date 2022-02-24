import Foundation
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class XPCHelper(Foundation.NSObject):
    def remoteObjectProxyWithErrorHandler_(self, a):
        pass

    def listener_shouldAcceptNewConnection_(self, a, b):
        pass


class TestNSXPCConnection(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSXPCConnectionOptions)

    @min_os_level("10.8")
    def testProtocolObjects(self):
        objc.protocolNamed("NSXPCProxyCreating")
        objc.protocolNamed("NSXPCListenerDelegate")

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertEqual(Foundation.NSXPCConnectionPrivileged, 1 << 12)

    @min_os_level("10.8")
    def testProtocol10_8(self):
        self.assertArgIsBlock(XPCHelper.remoteObjectProxyWithErrorHandler_, 0, b"v@")
        self.assertResultIsBOOL(XPCHelper.listener_shouldAcceptNewConnection_)

    @min_os_level("10.8")
    def testMethods10_8(self):
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
    def testMethods10_11(self):
        self.assertArgIsBlock(
            Foundation.NSXPCConnection.synchronousRemoteObjectProxyWithErrorHandler_,
            0,
            b"v@",
        )

    @min_os_level("10.15")  # Not actually on 10.14...
    def testMethods10_14(self):
        self.assertArgIsBOOL(
            Foundation.NSXPCInterface.setXPCType_forSelector_argumentIndex_ofReply_, 3
        )
        self.assertArgIsBOOL(
            Foundation.NSXPCInterface.XPCTypeForSelector_argumentIndex_ofReply_, 2
        )
