import unittest
import objc
import array

from Foundation import NSData, NSMutableData

rawBytes = "a\x13b\x00cd\xFFef\xEFgh"
otherBytes = array.array('c')
otherBytes.fromstring('12345678901234567890' * 5)

class TestNSData(unittest.TestCase):
    def assertDataContents(self, d1, d2, rawData):
        self.assertEquals(len(d1), d1.length(), "d1: len() and -length didn't match.")
        self.assertEquals(len(d1), len(rawData), "d1: len(<data>) and len(<input>) didn't match. %d vs %d"%(len(d1), len(rawData)))
        self.assertEquals(len(d2), d2.length(), "d2: len() and -length didn't match.")
        self.assertEquals(len(d2), len(rawData), "d2: len(<data>) and len(<input>) didn't match. %d vs %d"%(len(d2), len(rawData)))

    def testDataWithBytes_length_(self):
        """Test +dataWithBytes:length:"""
        data = NSData.dataWithBytes_length_(rawBytes, len(rawBytes))
        mutableData = NSMutableData.dataWithBytes_length_(rawBytes, len(rawBytes))
        self.assertDataContents(data, mutableData, rawBytes)

    def testInitWithBytes_length_(self):
        """Test -initWithBytes:length:"""
        data = NSData.alloc().initWithBytes_length_(rawBytes, len(rawBytes))
        mutableData = NSMutableData.alloc().initWithBytes_length_(rawBytes, len(rawBytes))
        self.assertDataContents(data, mutableData, rawBytes)

    def testBytes(self):
        """Test -bytes"""
        data = NSData.alloc().initWithBytes_length_(rawBytes, len(rawBytes))
        bytes = data.bytes()
        self.assertEquals(len(bytes), len(rawBytes), "bytes() and rawBytes not equal length.")
        for i in range(0,len(bytes)):
            self.assertEquals(rawBytes[i], bytes[i], "byte %s of bytes and rawBytes are not equal." % i)

        try:
            bytes[3] = 0xAE
        except TypeError, r:
            if str(r).find('buffer is read-only') is not 0:
                raise

    def testMutableBytes(self):
        """Test -mutableBytes"""
        mutableData = NSMutableData.dataWithBytes_length_(rawBytes, len(rawBytes))
        mutableBytes = mutableData.mutableBytes()
        for i in range(0, len(mutableBytes)):
            mutableBytes[i] = otherBytes[i]
        mutableBytes[1:8] = otherBytes[1:8]

        try:
            mutableBytes[2:10] = otherBytes[1:5]
        except TypeError, r:
            if str(r).find('right operand length must match slice length') is not 0:
                raise

    def testVariousDataLengths(self):
        """Test data of different lengths.

        Data of different lengths may be stored in different subclasses within the class cluster.
        """
        testFactor = range(1, 64) + [ 1000, 10000, 1000000]
        for aFactor in testFactor:
            bigRawBytes = "1234567890" * aFactor

            mutableData = NSMutableData.dataWithBytes_length_(bigRawBytes, len(bigRawBytes))
            data = NSData.dataWithBytes_length_(bigRawBytes, len(bigRawBytes))
        
            self.assertDataContents(data, mutableData, bigRawBytes)

            mutableBytes = mutableData.mutableBytes()
            bytes = data.bytes()

            self.assertEquals(len(bytes), data.length())
            self.assertEquals(len(mutableBytes), mutableData.length())
            self.assertEquals(bytes, mutableBytes)

            mutableBytes[0:len(mutableBytes)] = bytes[0:len(bytes)]

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestNSData))
    return suite

if __name__ == '__main__':
    unittest.main( )

