import objc
import socket
import os
from PyObjCTest.sockaddr import PyObjCTestSockAddr
from PyObjCTools.TestSupport import TestCase, skipUnless

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


def host_valid(hostname):
    """
    Return true iff *hostname* resolves
    """
    try:
        socket.gethostbyname(hostname)
    except OSError:
        return False
    else:
        return True


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
objc.registerMetaDataForSelector(
    b"PyObjCTestSockAddr",
    b"getSystemAddr:",
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

        v = o.sockAddrToValue_(b"/tmp/my.sock")
        self.assertEqual(v, ("UNIX", "/tmp/my.sock"))

        with self.assertRaisesRegex(UnicodeEncodeError, "can't encode characters"):
            o.sockAddrToValue_("\ud800\udc00")

        v = o.sockAddrToValue_(("<broadcast>", 99))
        self.assertEqual(v, ("IPv4", "255.255.255.255", 99))

        with self.assertRaisesRegex(socket.error, "address family mismatched"):
            o.sockAddrToValue_(("<broadcast>", 99, 0))

        v = o.sockAddrToValue_(("", 100))
        self.assertEqual(v, ("IPv4", "0.0.0.0", 100))

        v = o.sockAddrToValue_(("", 100, 0))
        self.assertEqual(v, ("IPv6", "::", 100, 0, 0))

        with self.assertRaisesRegex(
            TypeError,
            "('str' object cannot be interpreted as an integer)|"
            r"(an integer is required \(got type str\))",
        ):
            o.sockAddrToValue_(("127.0.0.1", "http"))

        with self.assertRaisesRegex(
            TypeError,
            "('str' object cannot be interpreted as an integer)|"
            r"(an integer is required \(got type str\))",
        ):
            o.sockAddrToValue_(("::1", "http", 0))

        with self.assertRaisesRegex(
            TypeError, r"function takes at most 4 arguments \(7 given\)"
        ):
            o.sockAddrToValue_(("::1", 80, 0, 0, 0, 0, 0))

        info = o.sockAddrToValue_(("mail.python.org", 99))
        sockinfo = socket.getaddrinfo("mail.python.org", 99, socket.AF_INET)
        self.assertEqual(info, ("IPv4",) + sockinfo[0][4])

        info = o.sockAddrToValue_(("mail.python.org", 99, 0))
        sockinfo = socket.getaddrinfo("mail.python.org", 99, socket.AF_INET6)
        self.assertEqual(info, ("IPv6",) + sockinfo[0][4])

    @skipUnless(
        not host_valid("nosuchhost.python.org"), "'nosuchhost.python.org' resolves"
    )
    def testToObjCForNonExistingHost(self):
        o = PyObjCTestSockAddr

        with self.assertRaisesRegex(
            socket.gaierror, "nodename nor servname provided, or not known"
        ):
            o.sockAddrToValue_(("nosuchhost.python.org", 99, 0))

        with self.assertRaisesRegex(
            socket.gaierror, "nodename nor servname provided, or not known"
        ):
            o.sockAddrToValue_(("nosuchhost.python.org", 99))

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

    def testSystemFromC(self):
        o = PyObjCTestSockAddr

        with self.assertRaisesRegex(
            ValueError, r"Don't know how to convert sockaddr family \d+"
        ):
            o.getSystemAddr_(None)


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
            if os.path.exists("/tmp/pyobjc.sock.addr"):
                os.unlink("/tmp/pyobjc.sock.addr")
            try:
                with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sd:
                    sd.bind("/tmp/pyobjc.sock.addr")
                    std_addr = sd.getsockname()
                    oc_addr = SOCK_FUNCTIONS["getsockname"](sd.fileno(), None, 100)[1]
                    self.assertEqual(std_addr, oc_addr)
            finally:
                if os.path.exists("/tmp/pyobjc.sock.addr"):
                    os.unlink("/tmp/pyobjc.sock.addr")
