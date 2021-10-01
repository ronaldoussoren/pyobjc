import objc
from PyObjCTest.sockaddr import PyObjCTestSockAddr
from PyObjCTools.TestSupport import TestCase
import socket

FUNCTION_LIST = [
    (
        "getsockname",
        b"".join(
            [
                objc._C_INT,
                objc._C_INT,
                objc._C_OUT,
                objc._C_PTR,
                objc._sockaddr_type,
                objc._C_INOUT,
                objc._C_PTR,
                objc._C_UINT,
            ]
        ),
    ),
]
SOCK_FUNCTIONS = {}
objc.loadBundleFunctions(None, SOCK_FUNCTIONS, FUNCTION_LIST, skip_undefined=False)

objc.registerMetaDataForSelector(
    b"PyObjCTestSockAddr",
    b"sockAddrToValue:",
    {"arguments": {2 + 0: {"type_modifier": objc._C_IN}}},
)
objc.registerMetaDataForSelector(
    b"PyObjCTestSockAddr",
    b"getIPv4Addr:",
    {"arguments": {2 + 0: {"type_modifier": objc._C_OUT}}},
)
objc.registerMetaDataForSelector(
    b"PyObjCTestSockAddr",
    b"getIPv6Addr:",
    {"arguments": {2 + 0: {"type_modifier": objc._C_OUT}}},
)
objc.registerMetaDataForSelector(
    b"PyObjCTestSockAddr",
    b"getUnixAddr:",
    {"arguments": {2 + 0: {"type_modifier": objc._C_OUT}}},
)


class TestSockAddrSupport(TestCase):
    def testToObjC(self):
        o = PyObjCTestSockAddr

        v = o.sockAddrToValue_(("1.2.3.4", 45))
        self.assertEqual(v, ("IPv4", "1.2.3.4", 45))

        v = o.sockAddrToValue_(("::1", 90, 4, 5))
        self.assertEqual(v, ("IPv6", "::1", 90, 4, 5))

        v = o.sockAddrToValue_("/tmp/my.sock")
        self.assertEqual(v, ("UNIX", "/tmp/my.sock"))

    def testIPv4FromC(self):
        o = PyObjCTestSockAddr

        v = o.getIPv4Addr_(None)
        self.assertEqual(v, ("127.0.0.1", 80))

    def testIPv6FromC(self):
        o = PyObjCTestSockAddr

        v = o.getIPv6Addr_(None)
        self.assertEqual(v, ("::1", 443, 2, 3))

    def testUnixFromC(self):
        o = PyObjCTestSockAddr

        v = o.getUnixAddr_(None)
        self.assertEqual(v, "/tmp/socket.addr")


class TestSocketInterop(TestCase):
    def test_read_sockinfo(self):
        with self.subTest("IPv4"):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sd:
                sd.bind(("", 0))
                std_addr = sd.getsockname()
                oc_addr = SOCK_FUNCTIONS["getsockname"](sd.fileno(), None, 100)[1]
                self.assertEqual(std_addr, oc_addr)

        with self.subTest("IPv6"):
            with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as sd:
                sd.bind(("", 0))
                std_addr = sd.getsockname()
                oc_addr = SOCK_FUNCTIONS["getsockname"](sd.fileno(), None, 100)[1]
                self.assertEqual(std_addr, oc_addr)

        with self.subTest("UNIX"):
            with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sd:
                sd.bind("/tmp/sock.addr")
                std_addr = sd.getsockname()
                oc_addr = SOCK_FUNCTIONS["getsockname"](sd.fileno(), None, 100)[1]
                self.assertEqual(std_addr, oc_addr)
