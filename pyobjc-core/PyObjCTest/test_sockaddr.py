from PyObjCTools.TestSupport import *
import objc
from PyObjCTest.sockaddr import PyObjCTestSockAddr

objc.registerMetaDataForSelector("PyObjCTestSockAddr", "sockAddrToValue:",
           dict(
               arguments={
                   2+0: dict(type_modifier=objc._C_IN),
               }
))
objc.registerMetaDataForSelector("PyObjCTestSockAddr", "getIPv4Addr:",
           dict(
               arguments={
                   2+0: dict(type_modifier=objc._C_OUT),
               }
))
objc.registerMetaDataForSelector("PyObjCTestSockAddr", "getIPv6Addr:",
           dict(
               arguments={
                   2+0: dict(type_modifier=objc._C_OUT),
               }
))



class TestSockAddrSupport (TestCase):
    def testToObjC(self):
        o = PyObjCTestSockAddr
        
        v = o.sockAddrToValue_(('1.2.3.4', 45))
        self.assertEquals(v, ('IPv4', '1.2.3.4', 45))

        v = o.sockAddrToValue_(('::1', 90, 4, 5))
        self.assertEquals(v, ('IPv6', '::1', 90, 4, 5))
        
    def testIPv4FromC(self):
        o = PyObjCTestSockAddr
        
        v = o.getIPv4Addr_(None)
        self.assertEquals(v, ('127.0.0.1', 80))
        
    def testIPv6FromC(self):
        o = PyObjCTestSockAddr

        v = o.getIPv6Addr_(None)
        self.assertEquals(v, ('::1', 443, 2, 3))
        
if __name__ == "__main__":
	main()
