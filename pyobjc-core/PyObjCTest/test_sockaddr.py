import objc
from PyObjCTest.sockaddr import PyObjCTestSockAddr
from PyObjCTools.TestSupport import TestCase

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


class TestSockAddrSupport(TestCase):
    def testToObjC(self):
        o = PyObjCTestSockAddr

        v = o.sockAddrToValue_(("1.2.3.4", 45))
        self.assertEqual(v, ("IPv4", "1.2.3.4", 45))

        v = o.sockAddrToValue_(("::1", 90, 4, 5))
        self.assertEqual(v, ("IPv6", "::1", 90, 4, 5))

    def testIPv4FromC(self):
        o = PyObjCTestSockAddr

        v = o.getIPv4Addr_(None)
        self.assertEqual(v, (b"127.0.0.1", 80))

    def testIPv6FromC(self):
        o = PyObjCTestSockAddr

        v = o.getIPv6Addr_(None)
        self.assertEqual(v, (b"::1", 443, 2, 3))
