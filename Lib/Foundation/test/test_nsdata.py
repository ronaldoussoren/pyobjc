import unittest
import objc
import array

from Foundation import NSData, NSMutableData

rawBytes = "a\x13b\x00cd\xFFef\xEFgh"
otherBytes = array.array('c')
otherBytes.fromstring('12345678901234567890' * 5)

class TestNSData(unittest.TestCase):
    def setUp(self):
        self.data = NSData.alloc().initWithBytes_length_(rawBytes, len(rawBytes))
        self.mutableData = NSMutableData.alloc().initWithBytes_length_(rawBytes, len(rawBytes))
        
    def testInitWithBytes_Length_(self):
        self.assertEquals(len(self.data), self.data.length(), "len() and -length didn't match.")
        self.assertEquals(len(self.data), len(rawBytes), "len(<data>) and len(<input>) didn't match.")
        self.assertEquals(len(self.mutableData), self.mutableData.length(),
                          "Mutable: len() and -length didn't match.")
        self.assertEquals(len(self.mutableData), len(rawBytes),
                          "Mutable: len(<data>) and len(<input>) didn't match.")

    def testBytes(self):
        bytes = self.data.bytes()
        self.assertEquals(len(bytes), len(rawBytes), "bytes() and rawBytes not equal length.")
        for i in range(0,len(bytes)):
            self.assertEquals(rawBytes[i], bytes[i], "byte %s of bytes and rawBytes are not equal." % i)

    def testMutableBytes(self):
        mutableBytes = self.mutableData.mutableBytes()
        for i in range(0, len(mutableBytes)):
            mutableBytes[i] = otherBytes[i]
        mutableBytes[1:8] = otherBytes[1:8]

        try:
            mutableBytes[2:10] = otherBytes[1:5]
        except TypeError:
            pass
        
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestNSData))
    return suite

if __name__ == '__main__':
    unittest.main( )

