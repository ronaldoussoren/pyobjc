import unittest
import objc

from Foundation import NSData

rawBytes = "a\x13b\x00cd\xFFef\xEFgh"

class TestNSData(unittest.TestCase):
    def setUp(self):
        self.d = NSData.alloc().initWithBytes_length_(rawBytes, len(rawBytes))
        
    def testInitWithBytes_Length_(self):
        self.assertEquals(len(self.d), self.d.length(), "len() and -length didn't match.")
        self.assertEquals(len(self.d), len(rawBytes), "len(<data>) and len(<input>) didn't match.")

    def testBytes(self):
        bytes = self.d.bytes()
        self.assertEquals(len(bytes), len(rawBytes), "bytes() and rawBytes not equal length.")
        for i in range(0,len(bytes)):
            self.assertEquals(rawBytes[i], bytes[i], "byte %s of bytes and rawBytes are not equal." % i)
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestNSData))
    return suite

if __name__ == '__main__':
    unittest.main( )

