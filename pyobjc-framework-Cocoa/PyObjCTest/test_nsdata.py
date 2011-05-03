from PyObjCTools.TestSupport import *
import objc
import array
import sys

from Foundation import *
from PyObjCTest.testhelper import PyObjC_TestClass3

rawBytes = b"a\x13b\x00cd\xFFef\xEFgh"
otherBytes = array.array('b')
otherBytes.fromstring('12345678901234567890' * 5)

if sys.version_info[0] == 3:
    buffer = memoryview

try:
    memoryview
except NameError:
    memoryview = None

class TestNSData(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSData.writeToFile_atomically_)
        self.assertArgIsBOOL(NSData.writeToFile_atomically_, 1)
        self.assertResultIsBOOL(NSData.writeToURL_atomically_)
        self.assertArgIsBOOL(NSData.writeToURL_atomically_, 1)
        self.assertResultIsBOOL(NSData.writeToFile_options_error_)
        self.assertArgIsOut(NSData.writeToFile_options_error_, 2)
        self.assertResultIsBOOL(NSData.writeToURL_options_error_)
        self.assertArgIsOut(NSData.writeToURL_options_error_, 2)
        self.assertArgIsOut(NSData.dataWithContentsOfFile_options_error_, 2)
        self.assertArgIsOut(NSData.dataWithContentsOfURL_options_error_, 2)
        self.assertArgIsOut(NSData.initWithContentsOfFile_options_error_, 2)
        self.assertArgIsOut(NSData.initWithContentsOfURL_options_error_, 2)

    def testConstants(self):
        self.assertEqual(NSMappedRead, 1)
        self.assertEqual(NSUncachedRead, 2)

        self.assertEqual(NSAtomicWrite, 1)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(NSDataReadingMapped, 1<<0)
        self.assertEqual(NSDataReadingUncached, 1<<1)
        self.assertEqual(NSDataWritingAtomic, 1<<0)
        self.assertEqual(NSDataSearchBackwards, 1<<0)
        self.assertEqual(NSDataSearchAnchored, 1<<1)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultHasType(NSData.rangeOfData_options_range_, NSRange.__typestr__)
        self.assertArgHasType(NSData.rangeOfData_options_range_, 2, NSRange.__typestr__)

    def assertDataContents(self, d1, d2, rawData):
        self.assertEqual(len(d1), d1.length(), "d1: len() and -length didn't match.")
        self.assertEqual(len(d1), len(rawData), "d1: len(<data>) and len(<input>) didn't match. %d vs %d"%(len(d1), len(rawData)))
        self.assertEqual(len(d2), d2.length(), "d2: len() and -length didn't match.")
        self.assertEqual(len(d2), len(rawData), "d2: len(<data>) and len(<input>) didn't match. %d vs %d"%(len(d2), len(rawData)))

    def testDataWithBytes_length_(self):
        # Test +dataWithBytes:length
        data = NSData.dataWithBytes_length_(rawBytes, len(rawBytes))
        mutableData = NSMutableData.dataWithBytes_length_(rawBytes, len(rawBytes))
        self.assertDataContents(data, mutableData, rawBytes)

    def testAppendBytes_length_(self):
        self.assertArgIsIn(NSMutableData.appendBytes_length_, 0)
        self.assertArgSizeInArg(NSMutableData.appendBytes_length_, 0, 1)

    def testreplaceBytesInRange_withBytes_(self):
        self.assertArgIsIn(NSMutableData.replaceBytesInRange_withBytes_, 1)
        self.assertArgSizeInArg(NSMutableData.replaceBytesInRange_withBytes_, 1, 0)

    def testreplaceBytesInRange_withBytes_length_(self):
        self.assertArgIsIn(NSMutableData.replaceBytesInRange_withBytes_length_, 1)
        self.assertArgSizeInArg(NSMutableData.replaceBytesInRange_withBytes_length_, 1, 2)

    def testDataWithBytesNoCopy_length_freeWhenDone_(self):
        data = NSData.dataWithBytesNoCopy_length_freeWhenDone_(rawBytes, len(rawBytes), False)
        mutableData = NSMutableData.dataWithBytesNoCopy_length_freeWhenDone_(rawBytes, len(rawBytes), False)
        self.assertDataContents(data, mutableData, rawBytes)

    def testInitWithBytes_length_(self):
        # Test -initWithBytes:length:
        data = NSData.alloc().initWithBytes_length_(rawBytes, len(rawBytes))
        mutableData = NSMutableData.alloc().initWithBytes_length_(rawBytes, len(rawBytes))
        self.assertDataContents(data, mutableData, rawBytes)

    def testInitWithBytesNoCopy_length_freeWhenDone_(self):
        # Test -initWithBytesNoCopy:length:
        data = NSData.alloc().initWithBytesNoCopy_length_freeWhenDone_(rawBytes, len(rawBytes), False)
        mutableData = NSMutableData.alloc().initWithBytesNoCopy_length_freeWhenDone_(rawBytes, len(rawBytes), False)
        self.assertDataContents(data, mutableData, rawBytes)

    def testBytes(self):
        # Test -bytes
        data = NSData.alloc().initWithBytes_length_(rawBytes, len(rawBytes))
        bytesValue = data.bytes()
        self.assertEqual(len(bytesValue), len(rawBytes), "bytes() and rawBytes not equal length.")

        if sys.version_info[:2] <= (2,6):
            self.assertEquals(buffer(rawBytes), bytesValue)

        else:
            self.assertEquals(rawBytes, bytesValue)

        try:
            bytesValue[3] = b'\xAE'
        except TypeError, r:
            if str(r).find('buffer is read-only') == 0:
                pass
            elif str(r).find('cannot modify read-only memory') == 0:
                pass
            else:
                raise

    def testMutableBytes(self):
        # Test -mutableBytes
        mutableData = NSMutableData.dataWithBytes_length_(rawBytes, len(rawBytes))
        mutableBytes = mutableData.mutableBytes()
        for i in range(0, len(mutableBytes)):
            mutableBytes[i] = otherBytes[i:i+1].tostring()
        mutableBytes[1:8] = otherBytes[1:8].tostring()

        try:
            mutableBytes[2:10] = otherBytes[1:5].tostring()
        except (TypeError, ValueError), r:
            if str(r).find('right operand length must match slice length') == 0:
                pass
            elif 'cannot modify size of memoryview object' in str(r):
                pass
            else:
                raise

    def testVariousDataLengths(self):
        # Test data of different lengths.
        #
        # Data of different lengths may be stored in different subclasses within the class cluster.
        testFactor = range(1, 64) + [ 1000, 10000, 1000000]
        for aFactor in testFactor:
            bigRawBytes = b"1234567890" * aFactor

            mutableData = NSMutableData.dataWithBytes_length_(bigRawBytes, len(bigRawBytes))
            data = NSData.dataWithBytes_length_(bigRawBytes, len(bigRawBytes))

            self.assertDataContents(data, mutableData, bigRawBytes)

            mutableBytes = mutableData.mutableBytes()
            bytes = data.bytes()

            self.assertEqual(len(bytes), data.length())
            self.assertEqual(len(mutableBytes), mutableData.length())
            self.assertEqual(bytes, mutableBytes)

            mutableBytes[0:len(mutableBytes)] = bytes[0:len(bytes)]

    def testInitWithContents(self):
        b, err = NSData.alloc().initWithContentsOfFile_options_error_(
                "/etc/hosts", 0, None)
        self.assertIsInstance(b, NSData)
        self.assertIs(err, None)
        b2, err = NSData.alloc().initWithContentsOfFile_options_error_(
                "/etc/hosts.nosuchfile", 0, None)
        self.assertIs(b2, None)
        self.assertIsInstance(err, NSError)
        url = NSURL.fileURLWithPath_isDirectory_('/etc/hosts', False)
        b, err = NSData.alloc().initWithContentsOfURL_options_error_(
                url, 0, None)
        self.assertIsInstance(b, NSData)
        self.assertIs(err, None)
        url = NSURL.fileURLWithPath_isDirectory_('/etc/hosts.nosuchfile', False)
        b2, err = NSData.alloc().initWithContentsOfURL_options_error_(
                url, 0, None)
        self.assertIs(b2, None)
        self.assertIsInstance(err, NSError)
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
        self.assertEqual(r, ('data', b'hello world', 11))

    def testInit(self):
        r = PyObjC_TestClass3.makeDataWithBytes_method_(MyData2, 1)
        self.assertEqual(r, ('init', b'hello world', 11))

    def testBytes(self):
        r = PyObjC_TestClass3.makeDataWithBytes_method_(MyData3, 1)
        b = PyObjC_TestClass3.getBytes_(r)

        # Check for memoryview
        if isinstance(b.bytes(), memoryview):
            self.assertEqual(b.bytes().tobytes(), b'hello world')
        else:
            self.assertEqual(bytes(b.bytes()), b'hello world')

        self.assertEqual(b.getBytes_length_(None, 4), b'hell')
        self.assertEqual(b.getBytes_range_(None, NSRange(2, 4)), b'llo ')


    def testBytesNone(self):
        b = PyObjC_TestClass3.makeDataWithBytes_method_(MyData4, 1)
        self.assertEqual(b.bytes(), None)

    def testBytesRaises(self):
        b = PyObjC_TestClass3.makeDataWithBytes_method_(MyData5, 1)
        self.assertRaises(ValueError, b.bytes)



import array
class TestBuffer(TestCase):
    def testArray(self):
        a = array.array('b', b'foo')
        m = NSMutableData.dataWithData_(a)
        self.assertEqual(a.tostring(), m[:])
        self.assert_(objc.repythonify(a) is a)
        a.fromstring(m)
        self.assertEqual(a.tostring(), b'foofoo')
        m.appendData_(a)
        self.assertEqual(m[:], b'foofoofoo')
        m[3:6] = b'bar'
        self.assertEqual(m[:], b'foobarfoo')

    def testBuffer(self):
        if sys.version_info[0] == 3:
            b = b'foo'
        else:
            b = buffer('foo')
        m = NSMutableData.dataWithData_(b)
        self.assertEqual(b[:], m[:])
        self.assert_(objc.repythonify(b) is b)
        self.assertEqual(buffer(m)[:], m[:])


class TestRegressions (TestCase):
    def testDataStr(self):
        if sys.version_info[0] == 2:
            input = buffer("hello")
            input_str = "hello"
        else:
            input = b"hello"
            input_str = str(input)

        buf = NSData.dataWithData_(input)
        self.assertEquals(str(buf), input_str)


if __name__ == '__main__':
    main( )
