from PyObjCTools.TestSupport import *
import objc
import array

from Foundation import *
from PyObjCTest.testhelper import PyObjC_TestClass3

rawBytes = "a\x13b\x00cd\xFFef\xEFgh"
otherBytes = array.array('c')
otherBytes.fromstring('12345678901234567890' * 5)

class TestNSData(TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSData.writeToFile_atomically_)
        self.failUnlessArgIsBOOL(NSData.writeToFile_atomically_, 1)
        self.failUnlessResultIsBOOL(NSData.writeToURL_atomically_)
        self.failUnlessArgIsBOOL(NSData.writeToURL_atomically_, 1)
        self.failUnlessResultIsBOOL(NSData.writeToFile_options_error_)
        self.failUnlessArgIsOut(NSData.writeToFile_options_error_, 2)
        self.failUnlessResultIsBOOL(NSData.writeToURL_options_error_)
        self.failUnlessArgIsOut(NSData.writeToURL_options_error_, 2)
        self.failUnlessArgIsOut(NSData.dataWithContentsOfFile_options_error_, 2)
        self.failUnlessArgIsOut(NSData.dataWithContentsOfURL_options_error_, 2)
        self.failUnlessArgIsOut(NSData.initWithContentsOfFile_options_error_, 2)
        self.failUnlessArgIsOut(NSData.initWithContentsOfURL_options_error_, 2)

    def testConstants(self):
        self.assertEquals(NSMappedRead, 1)
        self.assertEquals(NSUncachedRead, 2)

        self.assertEquals(NSAtomicWrite, 1)

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

    def testAppendBytes_length_(self):
        self.failUnlessArgIsIn(NSMutableData.appendBytes_length_, 0)
        self.failUnlessArgSizeInArg(NSMutableData.appendBytes_length_, 0, 1)

    def testreplaceBytesInRange_withBytes_(self):
        self.failUnlessArgIsIn(NSMutableData.replaceBytesInRange_withBytes_, 1)
        self.failUnlessArgSizeInArg(NSMutableData.replaceBytesInRange_withBytes_, 1, 0)

    def testreplaceBytesInRange_withBytes_length_(self):
        self.failUnlessArgIsIn(NSMutableData.replaceBytesInRange_withBytes_length_, 1)
        self.failUnlessArgSizeInArg(NSMutableData.replaceBytesInRange_withBytes_length_, 1, 2)

    def testDataWithBytesNoCopy_length_freeWhenDone_(self):
        data = NSData.dataWithBytesNoCopy_length_freeWhenDone_(rawBytes, len(rawBytes), False)
        mutableData = NSMutableData.dataWithBytesNoCopy_length_freeWhenDone_(rawBytes, len(rawBytes), False)
        self.assertDataContents(data, mutableData, rawBytes)

    def testInitWithBytes_length_(self):
        """Test -initWithBytes:length:"""
        data = NSData.alloc().initWithBytes_length_(rawBytes, len(rawBytes))
        mutableData = NSMutableData.alloc().initWithBytes_length_(rawBytes, len(rawBytes))
        self.assertDataContents(data, mutableData, rawBytes)

    def testInitWithBytesNoCopy_length_freeWhenDone_(self):
        """Test -initWithBytesNoCopy:length:"""
        data = NSData.alloc().initWithBytesNoCopy_length_freeWhenDone_(rawBytes, len(rawBytes), False)
        mutableData = NSMutableData.alloc().initWithBytesNoCopy_length_freeWhenDone_(rawBytes, len(rawBytes), False)
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

    def testInitWithContents(self):
        b, err = NSData.alloc().initWithContentsOfFile_options_error_(
                "/etc/hosts", 0, None)
        self.failUnless(isinstance(b, NSData))
        self.failUnless(err is None)

        b2, err = NSData.alloc().initWithContentsOfFile_options_error_(
                "/etc/hosts.nosuchfile", 0, None)
        self.failUnless(b2 is None)
        self.failUnless(isinstance(err, NSError))

        url = NSURL.fileURLWithPath_isDirectory_('/etc/hosts', False)
        b, err = NSData.alloc().initWithContentsOfURL_options_error_(
                url, 0, None)
        self.failUnless(isinstance(b, NSData))
        self.failUnless(err is None)

        url = NSURL.fileURLWithPath_isDirectory_('/etc/hosts.nosuchfile', False)
        b2, err = NSData.alloc().initWithContentsOfURL_options_error_(
                url, 0, None)
        self.failUnless(b2 is None)
        self.failUnless(isinstance(err, NSError))


class MyData (NSData):
    def dataWithBytes_length_(self, bytes, length):
        return ("data", bytes, length)

BYTES="dummy bytes"
class MyData2 (NSData):
    def initWithBytes_length_(self, bytes, length):
        return ("init", bytes, length)

    def length(self):
        return 42

    def bytes(self):
        return BYTES


class MyData3 (NSData):
    def initWithBytes_length_(self, bytes, length):
        self._bytes = bytes
        self._length = length
        return self

    def bytes(self):
        return self._bytes

    def length(self):
        if hasattr(self, '_length'):
            return self._length
        return -1

class MyData4 (NSData):
    def initWithBytes_length_(self, bytes, length):
        return self

    def bytes(self):
        return None

    def length(self):
        return -1

class MyData5(NSData):
    def initWithBytes_length_(self, bytes, length):
        return self

    def bytes(self):
        raise ValueError, "No bytes available"

    def length(self):
        return -1



class TestMyData (TestCase):
    # 'initWithBytes:length:' and 'dataWithBytes:length:' have custom IMP's
    def testData(self):
        r = PyObjC_TestClass3.makeDataWithBytes_method_(MyData, 0)
        self.assertEquals(r, ('data', 'hello world', 11))

    def testInit(self):
        r = PyObjC_TestClass3.makeDataWithBytes_method_(MyData2, 1)
        self.assertEquals(r, ('init', 'hello world', 11))

    def testBytes(self):
        r = PyObjC_TestClass3.makeDataWithBytes_method_(MyData3, 1)
        b = PyObjC_TestClass3.getBytes_(r)
        self.assertEquals(str(b.bytes()), 'hello world')

        self.assertEquals(b.getBytes_length_(None, 4), 'hell')
        self.assertEquals(b.getBytes_range_(None, NSRange(2, 4)), 'llo ')


    def testBytesNone(self):
        b = PyObjC_TestClass3.makeDataWithBytes_method_(MyData4, 1)
        self.assertEquals(b.bytes(), None)

    def testBytesRaises(self):
        b = PyObjC_TestClass3.makeDataWithBytes_method_(MyData5, 1)
        self.assertRaises(ValueError, b.bytes)



import array
class TestBuffer(TestCase):
    def testArray(self):
        a = array.array('c', 'foo')
        m = NSMutableData.dataWithData_(a)
        self.assertEquals(a.tostring(), m[:])
        self.assert_(objc.repythonify(a) is a)
        a.fromstring(m)
        self.assertEquals(a.tostring(), 'foofoo')
        m.appendData_(a)
        self.assertEquals(m[:], 'foofoofoo')
        m[3:6] = 'bar'
        self.assertEquals(m[:], 'foobarfoo')

    def testBuffer(self):
        b = buffer('foo')
        m = NSMutableData.dataWithData_(b)
        self.assertEquals(b[:], m[:])
        self.assert_(objc.repythonify(b) is b)
        self.assertEquals(buffer(m)[:], m[:])





if __name__ == '__main__':
    main( )
