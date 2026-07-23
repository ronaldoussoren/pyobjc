import socket
import struct

import CoreFoundation
from PyObjCTools.TestSupport import TestCase, skipUnless, NoObjCClass
from .runloophelper import check_cfrunloop_side_effects

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
    def test_types(self):
        self.assertIsCFType(CoreFoundation.CFSocketRef)

    def test_typeid(self):
        self.assertIsInstance(CoreFoundation.CFSocketGetTypeID(), int)

    def test_constants(self):
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

    def test_structs(self):
        o = CoreFoundation.CFSocketSignature()
        self.assertHasAttr(o, "protocolFamily")
        self.assertHasAttr(o, "socketType")
        self.assertHasAttr(o, "protocol")
        self.assertHasAttr(o, "address")

        self.assertPickleRoundTrips(o)

    def test_nameregistry(self):
        p1 = CoreFoundation.CFSocketGetDefaultNameRegistryPortNumber()
        self.assertIsInstance(p1, int)
        CoreFoundation.CFSocketSetDefaultNameRegistryPortNumber(p1 + 1)
        p2 = CoreFoundation.CFSocketGetDefaultNameRegistryPortNumber()
        self.assertIsInstance(p2, int)
        self.assertEqual(p2, p1 + 1)

        CoreFoundation.CFSocketSetDefaultNameRegistryPortNumber(p1)

    @skipUnless(onTheNetwork(), "Test requires a working Internet connection")
    @check_cfrunloop_side_effects
    def test_socket_functions(self):
        data = {}
        state = []

        def callback(sock, kind, address, data, info):
            state.append((sock, kind, address, data, info))

        with self.assertRaisesRegex(TypeError, "expected 7 arguments, got 0"):
            CoreFoundation.CFSocketCreate()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            CoreFoundation.CFSocketCreate(
                NoObjCClass(),
                socket.AF_INET,
                socket.SOCK_STREAM,
                0,
                CoreFoundation.kCFSocketReadCallBack
                | CoreFoundation.kCFSocketWriteCallBack,
                callback,
                data,
            )

        with self.assertRaisesRegex(ValueError, "depythonifying 'int', got 'str'"):
            CoreFoundation.CFSocketCreate(
                None,
                "socket.AF_INET",
                socket.SOCK_STREAM,
                0,
                CoreFoundation.kCFSocketReadCallBack
                | CoreFoundation.kCFSocketWriteCallBack,
                callback,
                data,
            )

        with self.assertRaisesRegex(ValueError, "depythonifying 'int', got 'str'"):
            CoreFoundation.CFSocketCreate(
                None,
                socket.AF_INET,
                "socket.SOCK_STREAM",
                0,
                CoreFoundation.kCFSocketReadCallBack
                | CoreFoundation.kCFSocketWriteCallBack,
                callback,
                data,
            )

        with self.assertRaisesRegex(ValueError, "depythonifying 'int', got 'str'"):
            CoreFoundation.CFSocketCreate(
                None,
                socket.AF_INET,
                socket.SOCK_STREAM,
                "0",
                CoreFoundation.kCFSocketReadCallBack
                | CoreFoundation.kCFSocketWriteCallBack,
                callback,
                data,
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned long long', got 'str'"
        ):
            CoreFoundation.CFSocketCreate(
                None,
                socket.AF_INET,
                socket.SOCK_STREAM,
                0,
                "read-write",
                callback,
                data,
            )

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
            with self.assertRaisesRegex(TypeError, "expected 5 arguments, got 0"):
                CoreFoundation.CFSocketCreateWithNative()

            with self.assertRaisesRegex(TypeError, "Cannot proxy"):
                CoreFoundation.CFSocketCreateWithNative(
                    NoObjCClass(),
                    sd.fileno(),
                    CoreFoundation.kCFSocketReadCallBack
                    | CoreFoundation.kCFSocketWriteCallBack,
                    callback,
                    data,
                )

            with self.assertRaisesRegex(ValueError, "depythonifying 'int', got 'str'"):
                CoreFoundation.CFSocketCreateWithNative(
                    None,
                    "sd.fileno()",
                    CoreFoundation.kCFSocketReadCallBack
                    | CoreFoundation.kCFSocketWriteCallBack,
                    callback,
                    data,
                )

            with self.assertRaisesRegex(
                ValueError, "depythonifying 'unsigned long long', got 'str'"
            ):
                CoreFoundation.CFSocketCreateWithNative(
                    None,
                    sd.fileno(),
                    "read-write",
                    callback,
                    data,
                )

            with self.assertRaisesRegex(
                ValueError, "depythonifying 'unsigned long long', got 'str'"
            ):
                CoreFoundation.CFSocketCreate(
                    None,
                    socket.AF_INET,
                    socket.SOCK_STREAM,
                    0,
                    "read-write",
                    callback,
                    data,
                )

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

            with self.assertRaisesRegex(TypeError, "expected 2 arguments, got 0"):
                CoreFoundation.CFSocketGetContext()
            with self.assertRaisesRegex(TypeError, "Cannot proxy"):
                CoreFoundation.CFSocketGetContext(NoObjCClass(), None)
            with self.assertRaisesRegex(ValueError, "context argument must be None"):
                CoreFoundation.CFSocketGetContext(sock, 42)

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

            self.assertResultIsCFRetained(CoreFoundation.CFSocketCopyPeerAddress)

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

            del sock

            with self.assertRaisesRegex(TypeError, "expected 5 arguments, got 0"):
                CoreFoundation.CFSocketCreateWithSocketSignature()

            with self.assertRaisesRegex(TypeError, "Cannot proxy"):
                CoreFoundation.CFSocketCreateWithSocketSignature(
                    NoObjCClass(),
                    signature,
                    CoreFoundation.kCFSocketReadCallBack
                    | CoreFoundation.kCFSocketWriteCallBack,
                    callback,
                    data,
                )

            with self.assertRaisesRegex(
                TypeError, "depythonifying struct, got no sequence"
            ):
                CoreFoundation.CFSocketCreateWithSocketSignature(
                    None,
                    42.5,
                    CoreFoundation.kCFSocketReadCallBack
                    | CoreFoundation.kCFSocketWriteCallBack,
                    callback,
                    data,
                )

            with self.assertRaisesRegex(
                ValueError, "depythonifying 'unsigned long long', got 'str'"
            ):
                CoreFoundation.CFSocketCreateWithSocketSignature(
                    None,
                    signature,
                    "read-write",
                    callback,
                    data,
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
            ip = socket.gethostbyname("www.python.org")
            ip = map(int, ip.split("."))
            sockaddr = struct.pack(">BBHBBBB", 16, socket.AF_INET, 443, *ip)
            sockaddr += b"\0" * 8
            signature = CoreFoundation.CFSocketSignature(
                socket.AF_INET, socket.SOCK_STREAM, 0, sockaddr
            )

            with self.assertRaisesRegex(TypeError, "expected 6 arguments, got 0"):
                CoreFoundation.CFSocketCreateConnectedToSocketSignature()

            with self.assertRaisesRegex(TypeError, "Cannot proxy"):
                CoreFoundation.CFSocketCreateConnectedToSocketSignature(
                    NoObjCClass(),
                    signature,
                    CoreFoundation.kCFSocketReadCallBack
                    | CoreFoundation.kCFSocketWriteCallBack,
                    callback,
                    data,
                    1.0,
                )

            with self.assertRaisesRegex(
                TypeError, "depythonifying struct, got no sequence"
            ):
                CoreFoundation.CFSocketCreateConnectedToSocketSignature(
                    None,
                    42.5,
                    CoreFoundation.kCFSocketReadCallBack
                    | CoreFoundation.kCFSocketWriteCallBack,
                    callback,
                    data,
                    1.0,
                )

            with self.assertRaisesRegex(
                ValueError, "depythonifying 'unsigned long long', got 'str'"
            ):
                CoreFoundation.CFSocketCreateConnectedToSocketSignature(
                    None,
                    signature,
                    "read-write",
                    callback,
                    data,
                    1.0,
                )

            with self.assertRaisesRegex(
                ValueError, "depythonifying 'double', got 'str'"
            ):
                CoreFoundation.CFSocketCreateConnectedToSocketSignature(
                    None,
                    signature,
                    CoreFoundation.kCFSocketReadCallBack
                    | CoreFoundation.kCFSocketWriteCallBack,
                    callback,
                    data,
                    "timeout",
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
            CoreFoundation.CFSocketInvalidate(sock)

            signature = CoreFoundation.CFSocketSignature(
                socket.AF_INET, socket.SOCK_STREAM, 0, sockaddr[:-5]
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
            self.assertIs(sock, None)

        finally:
            sd.close()

    @check_cfrunloop_side_effects
    def test_socket_loop(self):
        rl = CoreFoundation.CFRunLoopGetCurrent()
        context = object()

        rls1 = None
        rls2 = None
        rls3 = None
        rlsFail = None

        sock3 = None

        client_log = []
        fail_log = []
        server_log = []

        def keep_data(data):
            if data is None:
                return None
            elif isinstance(data, int):
                return data
            else:
                return bytes(data)

        def fail_callback(sock, kind, address, data, info):
            fail_log.append((sock, kind, keep_data(address), keep_data(data), info))
            if kind == CoreFoundation.kCFSocketDataCallBack:
                raise RuntimeError("data")

        def client_callback(sock, kind, address, data, info):
            client_log.append((sock, kind, keep_data(address), keep_data(data), info))
            if kind == CoreFoundation.kCFSocketWriteCallBack:
                CoreFoundation.CFSocketSendData(sock, None, b"PING", 1.0)

        def server_callback(sock, kind, address, data, info):
            nonlocal sock3, rls3
            server_log.append((sock, kind, keep_data(address), keep_data(data), info))

            if kind == CoreFoundation.kCFSocketAcceptCallBack:
                sock3 = CoreFoundation.CFSocketCreateWithNative(
                    None,
                    data,
                    CoreFoundation.kCFSocketWriteCallBack
                    | CoreFoundation.kCFSocketConnectCallBack
                    | CoreFoundation.kCFSocketDataCallBack,
                    server_callback,
                    context,
                )
                rls3 = CoreFoundation.CFSocketCreateRunLoopSource(None, sock3, 0)
                CoreFoundation.CFRunLoopAddSource(
                    rl, rls3, CoreFoundation.kCFRunLoopDefaultMode
                )

                CoreFoundation.CFSocketInvalidate(sock)
            elif kind == CoreFoundation.kCFSocketDataCallBack:
                CoreFoundation.CFSocketSendData(sock, None, data.lower(), 1.0)

        try:
            sock1 = CoreFoundation.CFSocketCreate(
                None,
                socket.AF_INET,
                socket.SOCK_STREAM,
                0,
                CoreFoundation.kCFSocketAcceptCallBack,
                server_callback,
                context,
            )
            CoreFoundation.CFSocketSetSocketFlags(
                sock1,
                CoreFoundation.CFSocketGetSocketFlags(sock1)
                | CoreFoundation.kCFSocketAutomaticallyReenableAcceptCallBack,
            )

            sock2 = CoreFoundation.CFSocketCreate(
                None,
                socket.AF_INET,
                socket.SOCK_STREAM,
                0,
                CoreFoundation.kCFSocketWriteCallBack
                | CoreFoundation.kCFSocketConnectCallBack
                | CoreFoundation.kCFSocketDataCallBack,
                client_callback,
                context,
            )

            sockFail = CoreFoundation.CFSocketCreate(
                None,
                socket.AF_INET,
                socket.SOCK_STREAM,
                0,
                CoreFoundation.kCFSocketConnectCallBack
                | CoreFoundation.kCFSocketDataCallBack,
                fail_callback,
                context,
            )

            sockaddr = struct.pack(">BBHBBBB", 16, socket.AF_INET, 0, 127, 0, 0, 1)
            sockaddr += b"\0" * 8
            CoreFoundation.CFSocketSetAddress(sock1, sockaddr)
            sockaddr = CoreFoundation.CFSocketCopyAddress(sock1)

            sockaddr2 = struct.pack(">BBHBBBB", 16, socket.AF_INET, 1, 127, 0, 0, 1)
            sockaddr2 += b"\0" * 8

            rls1 = CoreFoundation.CFSocketCreateRunLoopSource(None, sock1, 0)
            rls2 = CoreFoundation.CFSocketCreateRunLoopSource(None, sock2, 0)
            rlsFail = CoreFoundation.CFSocketCreateRunLoopSource(None, sockFail, 0)

            CoreFoundation.CFRunLoopAddSource(
                rl, rls1, CoreFoundation.kCFRunLoopDefaultMode
            )
            CoreFoundation.CFRunLoopAddSource(
                rl, rls2, CoreFoundation.kCFRunLoopDefaultMode
            )
            CoreFoundation.CFRunLoopAddSource(
                rl, rlsFail, CoreFoundation.kCFRunLoopDefaultMode
            )

            def timer_callback(*args):
                CoreFoundation.CFSocketConnectToAddress(sock2, sockaddr, 1)
                CoreFoundation.CFSocketConnectToAddress(sockFail, sockaddr2, -1)

            timer = CoreFoundation.CFRunLoopTimerCreateWithHandler(
                None,
                CoreFoundation.CFAbsoluteTimeGetCurrent() + 0.5,
                0,
                0,
                0,
                timer_callback,
            )
            CoreFoundation.CFRunLoopAddTimer(
                rl, timer, CoreFoundation.kCFRunLoopCommonModes
            )

            with self.assertRaisesRegex(RuntimeError, "data"):
                CoreFoundation.CFRunLoopRunInMode(
                    CoreFoundation.kCFRunLoopDefaultMode, 1.0, False
                )

            CoreFoundation.CFRunLoopRunInMode(
                CoreFoundation.kCFRunLoopDefaultMode, 2.0, False
            )

            CoreFoundation.CFRunLoopRemoveTimer(
                rl, timer, CoreFoundation.kCFRunLoopCommonModes
            )

            self.assertEqual(len(client_log), 3)
            self.assertEqual(client_log[0][1], CoreFoundation.kCFSocketConnectCallBack)
            self.assertEqual(client_log[1][1], CoreFoundation.kCFSocketWriteCallBack)
            self.assertEqual(client_log[2][1], CoreFoundation.kCFSocketDataCallBack)

            self.assertEqual(len(server_log), 4)
            self.assertEqual(server_log[0][1], CoreFoundation.kCFSocketAcceptCallBack)
            self.assertEqual(server_log[1][1], CoreFoundation.kCFSocketConnectCallBack)
            self.assertEqual(server_log[2][1], CoreFoundation.kCFSocketDataCallBack)
            self.assertEqual(server_log[3][1], CoreFoundation.kCFSocketWriteCallBack)

            self.assertEqual(len(fail_log), 2)
            self.assertIs(fail_log[0][0], sockFail)
            self.assertEqual(fail_log[0][1], CoreFoundation.kCFSocketConnectCallBack)
            self.assertEqual(fail_log[0][2], None)
            self.assertIsInstance(fail_log[0][3], int)
            self.assertIs(fail_log[0][4], context)

            self.assertIs(fail_log[1][0], sockFail)
            self.assertEqual(fail_log[1][1], CoreFoundation.kCFSocketDataCallBack)
            self.assertEqual(fail_log[1][2], b"")
            self.assertIs(fail_log[1][3], b"")
            self.assertIs(fail_log[1][4], context)

            for item in client_log + server_log:
                self.assertIn(item[0], (sock1, sock2, sock3))
                self.assertIsInstance(item[2], (bytes, type(None)))
                self.assertIsInstance(item[3], (bytes, int, type(None)))
                self.assertIs(item[4], context)

        finally:
            if rls1 is not None:
                CoreFoundation.CFRunLoopRemoveSource(
                    rl, rls1, CoreFoundation.kCFRunLoopDefaultMode
                )
            if rls2 is not None:
                CoreFoundation.CFRunLoopRemoveSource(
                    rl, rls2, CoreFoundation.kCFRunLoopDefaultMode
                )
            if rls3 is not None:
                CoreFoundation.CFRunLoopRemoveSource(
                    rl, rls3, CoreFoundation.kCFRunLoopDefaultMode
                )
            if rlsFail is not None:
                CoreFoundation.CFRunLoopRemoveSource(
                    rl, rlsFail, CoreFoundation.kCFRunLoopDefaultMode
                )

    def test_socket_nameserver(self):
        # The documentation says:
        #   Name server functionality is currently inoperable in macOS.
        #
        # Therefore these functions are not available from Python
        self.assertNotHasAttr(CoreFoundation, "CFSocketCopyRegisteredSocketSignature")
        self.assertNotHasAttr(CoreFoundation, "CFSocketCopyRegisteredValue")
        self.assertNotHasAttr(CoreFoundation, "CFSocketRegisterSocketSignature")
        self.assertNotHasAttr(CoreFoundation, "CFSocketRegisterValue")
        self.assertNotHasAttr(CoreFoundation, "CFSocketUnregister")
