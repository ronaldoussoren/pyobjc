import socket
import struct

import CoreFoundation
from PyObjCTools.TestSupport import TestCase, skipUnless

cached_info = None


def onTheNetwork():
    global cached_info
    if cached_info is not None:
        return cached_info

    try:
        socket.gethostbyname("www.apple.com")

        sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sd.settimeout(1.0)
        try:
            sd.connect(("www.apple.com", 80))
        finally:
            sd.close()

    except OSError:
        cached_info = False
        return False

    cached_info = True
    return True


class TestSocket(TestCase):
    def testTypes(self):
        self.assertIsCFType(CoreFoundation.CFSocketRef)

    def testTypeID(self):
        self.assertIsInstance(CoreFoundation.CFSocketGetTypeID(), int)

    def testConstants(self):
        self.assertEqual(CoreFoundation.kCFSocketSuccess, 0)
        self.assertEqual(CoreFoundation.kCFSocketError, -1)
        self.assertEqual(CoreFoundation.kCFSocketTimeout, -2)
        self.assertEqual(CoreFoundation.kCFSocketNoCallBack, 0)
        self.assertEqual(CoreFoundation.kCFSocketReadCallBack, 1)
        self.assertEqual(CoreFoundation.kCFSocketAcceptCallBack, 2)
        self.assertEqual(CoreFoundation.kCFSocketDataCallBack, 3)
        self.assertEqual(CoreFoundation.kCFSocketConnectCallBack, 4)
        self.assertEqual(CoreFoundation.kCFSocketWriteCallBack, 8)
        self.assertEqual(CoreFoundation.kCFSocketAutomaticallyReenableReadCallBack, 1)
        self.assertEqual(CoreFoundation.kCFSocketAutomaticallyReenableAcceptCallBack, 2)
        self.assertEqual(CoreFoundation.kCFSocketAutomaticallyReenableDataCallBack, 3)
        self.assertEqual(CoreFoundation.kCFSocketAutomaticallyReenableWriteCallBack, 8)
        self.assertEqual(CoreFoundation.kCFSocketCloseOnInvalidate, 128)
        self.assertIsInstance(CoreFoundation.kCFSocketCommandKey, str)
        self.assertIsInstance(CoreFoundation.kCFSocketNameKey, str)
        self.assertIsInstance(CoreFoundation.kCFSocketValueKey, str)
        self.assertIsInstance(CoreFoundation.kCFSocketResultKey, str)
        self.assertIsInstance(CoreFoundation.kCFSocketErrorKey, str)
        self.assertIsInstance(CoreFoundation.kCFSocketRegisterCommand, str)
        self.assertIsInstance(CoreFoundation.kCFSocketRetrieveCommand, str)
        self.assertEqual(CoreFoundation.kCFSocketLeaveErrors, 64)

    def testStructs(self):
        o = CoreFoundation.CFSocketSignature()
        self.assertHasAttr(o, "protocolFamily")
        self.assertHasAttr(o, "socketType")
        self.assertHasAttr(o, "protocol")
        self.assertHasAttr(o, "address")

        self.assertPickleRoundTrips(o)

    def testNameRegistry(self):
        p1 = CoreFoundation.CFSocketGetDefaultNameRegistryPortNumber()
        self.assertIsInstance(p1, int)
        CoreFoundation.CFSocketSetDefaultNameRegistryPortNumber(p1 + 1)
        p2 = CoreFoundation.CFSocketGetDefaultNameRegistryPortNumber()
        self.assertIsInstance(p2, int)
        self.assertEqual(p2, p1 + 1)

        CoreFoundation.CFSocketSetDefaultNameRegistryPortNumber(p1)

    @skipUnless(onTheNetwork(), "Test requires a working Internet connection")
    def testSocketFunctions(self):
        data = {}
        state = []

        def callback(sock, kind, address, data, info):
            state.append((sock, kind, address, data, info))

        sock = CoreFoundation.CFSocketCreate(
            None,
            socket.AF_INET,
            socket.SOCK_STREAM,
            0,
            CoreFoundation.kCFSocketReadCallBack
            | CoreFoundation.kCFSocketWriteCallBack,
            callback,
            data,
        )
        self.assertIsInstance(sock, CoreFoundation.CFSocketRef)
        localaddr = struct.pack(">BBHBBBB", 16, socket.AF_INET, 0, 127, 0, 0, 1)
        localaddr += b"\0" * 8

        _ = CoreFoundation.CFSocketCopyAddress(sock)
        err = CoreFoundation.CFSocketSetAddress(sock, localaddr)
        self.assertEqual(err, CoreFoundation.kCFSocketSuccess)

        sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        try:
            sock = CoreFoundation.CFSocketCreateWithNative(
                None,
                sd.fileno(),
                CoreFoundation.kCFSocketReadCallBack
                | CoreFoundation.kCFSocketWriteCallBack,
                callback,
                data,
            )
            self.assertIsInstance(sock, CoreFoundation.CFSocketRef)
            n = CoreFoundation.CFSocketGetNative(sock)
            self.assertIsInstance(n, int)
            self.assertEqual(n, sd.fileno())

            ctx = CoreFoundation.CFSocketGetContext(sock, None)
            self.assertIs(ctx, data)
            flags = CoreFoundation.CFSocketGetSocketFlags(sock)
            self.assertIsInstance(flags, int)
            CoreFoundation.CFSocketSetSocketFlags(
                sock,
                CoreFoundation.kCFSocketAutomaticallyReenableReadCallBack
                | CoreFoundation.kCFSocketAutomaticallyReenableAcceptCallBack,
            )
            flags2 = CoreFoundation.CFSocketGetSocketFlags(sock)
            self.assertIsInstance(flags2, int)
            self.assertEqual(
                flags2,
                CoreFoundation.kCFSocketAutomaticallyReenableReadCallBack
                | CoreFoundation.kCFSocketAutomaticallyReenableAcceptCallBack,
            )

            # Note: I don't expect anyone to actually use this api, building
            # struct sockaddr buffers by hand is madness in python.
            ip = socket.gethostbyname("www.apple.com")
            ip = map(int, ip.split("."))

            sockaddr = struct.pack(">BBHBBBB", 16, socket.AF_INET, 80, *ip)
            sockaddr += b"\0" * 8

            e = CoreFoundation.CFSocketConnectToAddress(sock, sockaddr, 1.0)
            self.assertIsInstance(e, int)
            self.assertEqual(e, CoreFoundation.kCFSocketSuccess)

            self.assertResultIsCFRetained(CoreFoundation.CFSocketCopyPeerAddress)
            addr = CoreFoundation.CFSocketCopyPeerAddress(sock)
            self.assertIsInstance(addr, CoreFoundation.CFDataRef)
            self.assertResultIsCFRetained(CoreFoundation.CFSocketCopyAddress)
            addr = CoreFoundation.CFSocketCopyAddress(sock)
            self.assertIsInstance(addr, CoreFoundation.CFDataRef)
            CoreFoundation.CFSocketDisableCallBacks(
                sock,
                CoreFoundation.kCFSocketReadCallBack
                | CoreFoundation.kCFSocketAcceptCallBack,
            )
            CoreFoundation.CFSocketEnableCallBacks(
                sock,
                CoreFoundation.kCFSocketReadCallBack
                | CoreFoundation.kCFSocketAcceptCallBack,
            )

            err = CoreFoundation.CFSocketSendData(sock, None, b"GET / HTTP/1.0", 1.0)
            self.assertEqual(err, CoreFoundation.kCFSocketSuccess)

            ok = CoreFoundation.CFSocketIsValid(sock)
            self.assertIs(ok, True)
            CoreFoundation.CFSocketInvalidate(sock)
            self.assertResultIsBOOL(CoreFoundation.CFSocketIsValid)
            ok = CoreFoundation.CFSocketIsValid(sock)
            self.assertIs(ok, False)
            localaddr = struct.pack(">BBHBBBB", 16, socket.AF_INET, 0, 127, 0, 0, 1)
            localaddr += b"\0" * 8
            signature = CoreFoundation.CFSocketSignature(
                socket.AF_INET, socket.SOCK_STREAM, 0, localaddr
            )

            sock = CoreFoundation.CFSocketCreateWithSocketSignature(
                None,
                signature,
                CoreFoundation.kCFSocketReadCallBack
                | CoreFoundation.kCFSocketWriteCallBack,
                callback,
                data,
            )
            self.assertIsInstance(sock, CoreFoundation.CFSocketRef)
            signature = CoreFoundation.CFSocketSignature(
                socket.AF_INET, socket.SOCK_STREAM, 0, sockaddr
            )
            sock = CoreFoundation.CFSocketCreateConnectedToSocketSignature(
                None,
                signature,
                CoreFoundation.kCFSocketReadCallBack
                | CoreFoundation.kCFSocketWriteCallBack,
                callback,
                data,
                1.0,
            )
            self.assertIsInstance(sock, CoreFoundation.CFSocketRef)
            self.assertResultIsCFRetained(CoreFoundation.CFSocketCreateRunLoopSource)
            src = CoreFoundation.CFSocketCreateRunLoopSource(None, sock, 0)
            self.assertIsInstance(src, CoreFoundation.CFRunLoopSourceRef)

        finally:
            sd.close()

    def testSocketNameServer(self):
        # The documentation says:
        #   Name server functionality is currently inoperable in macOS.
        #
        # Therefore these functions are not available from Python
        self.assertNotHasAttr(CoreFoundation, "CFSocketCopyRegisteredSocketSignature")
        self.assertNotHasAttr(CoreFoundation, "CFSocketCopyRegisteredValue")
        self.assertNotHasAttr(CoreFoundation, "CFSocketRegisterSocketSignature")
        self.assertNotHasAttr(CoreFoundation, "CFSocketRegisterValue")
        self.assertNotHasAttr(CoreFoundation, "CFSocketUnregister")
