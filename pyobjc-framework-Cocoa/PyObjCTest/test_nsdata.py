import array
import sys

import Foundation
from PyObjCTest.testhelper import PyObjC_TestClass3
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

rawBytes = b"a\x13b\x00cd\xFFef\xEFgh"
otherBytes = array.array("B")
otherBytes.frombytes(b"12345678901234567890" * 5)


class TestNSData(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSDataBase64DecodingOptions)
        self.assertIsEnumType(Foundation.NSDataBase64EncodingOptions)
        self.assertIsEnumType(Foundation.NSDataCompressionAlgorithm)
        self.assertIsEnumType(Foundation.NSDataReadingOptions)
        self.assertIsEnumType(Foundation.NSDataSearchOptions)
        self.assertIsEnumType(Foundation.NSDataWritingOptions)

    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSData.isEqualToData_)
        self.assertResultIsBOOL(Foundation.NSData.writeToFile_atomically_)
        self.assertArgIsBOOL(Foundation.NSData.writeToFile_atomically_, 1)
        self.assertResultIsBOOL(Foundation.NSData.writeToURL_atomically_)
        self.assertArgIsBOOL(Foundation.NSData.writeToURL_atomically_, 1)
        self.assertResultIsBOOL(Foundation.NSData.writeToFile_options_error_)
        self.assertArgIsOut(Foundation.NSData.writeToFile_options_error_, 2)
        self.assertResultIsBOOL(Foundation.NSData.writeToURL_options_error_)
        self.assertArgIsOut(Foundation.NSData.writeToURL_options_error_, 2)
        self.assertArgIsOut(Foundation.NSData.dataWithContentsOfFile_options_error_, 2)
        self.assertArgIsOut(Foundation.NSData.dataWithContentsOfURL_options_error_, 2)
        self.assertArgIsOut(Foundation.NSData.initWithContentsOfFile_options_error_, 2)
        self.assertArgIsOut(Foundation.NSData.initWithContentsOfURL_options_error_, 2)
        self.assertArgIsIn(Foundation.NSData.dataWithBytesNoCopy_length_, 0)
        self.assertArgSizeInArg(Foundation.NSData.dataWithBytes_length_, 0, 1)
        self.assertArgIsIn(Foundation.NSData.initWithBytesNoCopy_length_, 0)
        self.assertArgSizeInArg(Foundation.NSData.initWithBytes_length_, 0, 1)

    def testConstants(self):
        self.assertEqual(Foundation.NSMappedRead, 1)
        self.assertEqual(Foundation.NSUncachedRead, 2)

        self.assertEqual(Foundation.NSAtomicWrite, 1)

        self.assertEqual(Foundation.NSDataWritingFileProtectionNone, 0x10000000)
        self.assertEqual(Foundation.NSDataWritingFileProtectionComplete, 0x20000000)
        self.assertEqual(
            Foundation.NSDataWritingFileProtectionCompleteUnlessOpen, 0x30000000
        )
        self.assertEqual(
            Foundation.NSDataWritingFileProtectionCompleteUntilFirstUserAuthentication,
            0x40000000,
        )
        self.assertEqual(Foundation.NSDataWritingFileProtectionMask, 0xF0000000)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(Foundation.NSDataReadingMapped, 1 << 0)
        self.assertEqual(Foundation.NSDataReadingUncached, 1 << 1)
        self.assertEqual(Foundation.NSDataWritingAtomic, 1 << 0)
        self.assertEqual(Foundation.NSDataSearchBackwards, 1 << 0)
        self.assertEqual(Foundation.NSDataSearchAnchored, 1 << 1)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertEqual(Foundation.NSDataReadingMappedAlways, 1 << 3)

        self.assertEqual(Foundation.NSDataReadingMappedIfSafe, 1 << 0)
        self.assertEqual(Foundation.NSDataReadingUncached, 1 << 1)

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertEqual(Foundation.NSDataWritingWithoutOverwriting, 1 << 1)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertEqual(Foundation.NSDataBase64Encoding64CharacterLineLength, 1 << 0)
        self.assertEqual(Foundation.NSDataBase64Encoding76CharacterLineLength, 1 << 1)
        self.assertEqual(
            Foundation.NSDataBase64EncodingEndLineWithCarriageReturn, 1 << 4
        )
        self.assertEqual(Foundation.NSDataBase64EncodingEndLineWithLineFeed, 1 << 5)

        self.assertEqual(Foundation.NSDataBase64DecodingIgnoreUnknownCharacters, 1 << 0)

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertEqual(Foundation.NSDataCompressionAlgorithmLZFSE, 0)
        self.assertEqual(Foundation.NSDataCompressionAlgorithmLZ4, 1)
        self.assertEqual(Foundation.NSDataCompressionAlgorithmLZMA, 2)
        self.assertEqual(Foundation.NSDataCompressionAlgorithmZlib, 3)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultHasType(
            Foundation.NSData.rangeOfData_options_range_, Foundation.NSRange.__typestr__
        )
        self.assertArgHasType(
            Foundation.NSData.rangeOfData_options_range_,
            2,
            Foundation.NSRange.__typestr__,
        )

    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertArgIsBlock(
            Foundation.NSData.enumerateByteRangesUsingBlock_,
            0,
            b"vn^v" + Foundation.NSRange.__typestr__ + b"o^Z",
        )
        data = Foundation.NSData.dataWithBytes_length_(rawBytes, len(rawBytes))

        lst = []

        def cb(buf, rng, done):
            lst.append((buf, rng, done))
            return False

        data.enumerateByteRangesUsingBlock_(cb)
        self.assertEqual(lst, [(rawBytes, Foundation.NSRange(0, len(rawBytes)), None)])

        self.assertArgIsBlock(
            Foundation.NSData.initWithBytesNoCopy_length_deallocator_,
            2,
            b"vn^v" + objc._C_NSUInteger,
        )

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertResultIsBOOL(
            Foundation.NSMutableData.decompressUsingAlgorithm_error_
        )
        self.assertArgIsOut(Foundation.NSMutableData.decompressUsingAlgorithm_error_, 1)

        self.assertResultIsBOOL(Foundation.NSMutableData.compressUsingAlgorithm_error_)
        self.assertArgIsOut(Foundation.NSMutableData.compressUsingAlgorithm_error_, 1)

    def assertDataContents(self, d1, d2, rawData):
        self.assertEqual(len(d1), d1.length(), "d1: len() and -length didn't match.")
        self.assertEqual(
            len(d1),
            len(rawData),
            "d1: len(<data>) and len(<input>) didn't match. %d vs %d"
            % (len(d1), len(rawData)),
        )
        self.assertEqual(len(d2), d2.length(), "d2: len() and -length didn't match.")
        self.assertEqual(
            len(d2),
            len(rawData),
            "d2: len(<data>) and len(<input>) didn't match. %d vs %d"
            % (len(d2), len(rawData)),
        )

    def testDataWithBytes_length_(self):
        # Test +dataWithBytes:length
        data = Foundation.NSData.dataWithBytes_length_(rawBytes, len(rawBytes))
        mutableData = Foundation.NSMutableData.dataWithBytes_length_(
            rawBytes, len(rawBytes)
        )
        self.assertDataContents(data, mutableData, rawBytes)

    def testAppendBytes_length_(self):
        self.assertArgIsIn(Foundation.NSMutableData.appendBytes_length_, 0)
        self.assertArgSizeInArg(Foundation.NSMutableData.appendBytes_length_, 0, 1)

    def testreplaceBytesInRange_withBytes_(self):
        self.assertArgIsIn(Foundation.NSMutableData.replaceBytesInRange_withBytes_, 1)
        self.assertArgSizeInArg(
            Foundation.NSMutableData.replaceBytesInRange_withBytes_, 1, 0
        )

    def testreplaceBytesInRange_withBytes_length_(self):
        self.assertArgIsIn(
            Foundation.NSMutableData.replaceBytesInRange_withBytes_length_, 1
        )
        self.assertArgSizeInArg(
            Foundation.NSMutableData.replaceBytesInRange_withBytes_length_, 1, 2
        )

    def testDataWithBytesNoCopy_length_freeWhenDone_(self):
        data = Foundation.NSData.dataWithBytesNoCopy_length_freeWhenDone_(
            rawBytes, len(rawBytes), False
        )
        mutableData = Foundation.NSMutableData.dataWithBytesNoCopy_length_freeWhenDone_(
            rawBytes, len(rawBytes), False
        )
        self.assertDataContents(data, mutableData, rawBytes)

    def testInitWithBytes_length_(self):
        # Test -initWithBytes:length:
        data = Foundation.NSData.alloc().initWithBytes_length_(rawBytes, len(rawBytes))
        mutableData = Foundation.NSMutableData.alloc().initWithBytes_length_(
            rawBytes, len(rawBytes)
        )
        self.assertDataContents(data, mutableData, rawBytes)

    def testInitWithBytesNoCopy_length_freeWhenDone_(self):
        # Test -initWithBytesNoCopy:length:
        data = Foundation.NSData.alloc().initWithBytesNoCopy_length_freeWhenDone_(
            rawBytes, len(rawBytes), False
        )
        mutableData = (
            Foundation.NSMutableData.alloc().initWithBytesNoCopy_length_freeWhenDone_(
                rawBytes, len(rawBytes), False
            )
        )
        self.assertDataContents(data, mutableData, rawBytes)

    def testBytes(self):
        # Test -bytes
        data = Foundation.NSData.alloc().initWithBytes_length_(rawBytes, len(rawBytes))
        bytesValue = data.bytes()
        self.assertEqual(
            len(bytesValue), len(rawBytes), "bytes() and rawBytes not equal length."
        )

        self.assertEqual(rawBytes, bytesValue)

        try:
            bytesValue[3] = b"\xAE"
        except TypeError as r:
            if str(r).find("buffer is read-only") == 0:
                pass
            elif str(r).find("cannot modify read-only memory") == 0:
                pass
            else:
                raise

    def testMutableBytes(self):
        # Test -mutableBytes
        mutableData = Foundation.NSMutableData.dataWithBytes_length_(
            rawBytes, len(rawBytes)
        )
        mutableBytes = mutableData.mutableBytes()
        for i in range(0, len(mutableBytes)):
            if sys.version_info[:2] >= (3, 3):
                mutableBytes[i] = (otherBytes[i : i + 1]).tobytes()[0]
            else:
                mutableBytes[i] = (otherBytes[i : i + 1]).tobytes()
        mutableBytes[1:8] = (otherBytes[1:8]).tobytes()

        try:
            mutableBytes[2:10] = (otherBytes[1:5]).tobytes()
        except (TypeError, ValueError) as r:
            if str(r).find("right operand length must match slice length") == 0:
                pass
            elif str(r).find("lvalue and rvalue have different structures") != -1:
                pass
            elif "cannot modify size of memoryview object" in str(r):
                pass
            elif (
                "ndarray assignment: lvalue and rvalue have different structures"
                in str(r)
            ):
                pass
            else:
                raise

    def testVariousDataLengths(self):
        # Test data of different lengths.
        #
        # Data of different lengths may be stored in different subclasses
        # within the class cluster.
        testFactor = list(range(1, 64)) + [1000, 10000, 1_000_000]
        for aFactor in testFactor:
            bigRawBytes = b"1234567890" * aFactor

            mutableData = Foundation.NSMutableData.dataWithBytes_length_(
                bigRawBytes, len(bigRawBytes)
            )
            data = Foundation.NSData.dataWithBytes_length_(
                bigRawBytes, len(bigRawBytes)
            )

            self.assertDataContents(data, mutableData, bigRawBytes)

            mutableBytes = mutableData.mutableBytes()
            bytes_value = data.bytes()

            self.assertEqual(len(bytes_value), data.length())
            self.assertEqual(len(mutableBytes), mutableData.length())
            self.assertEqual(bytes_value, mutableBytes)

            mutableBytes[0 : len(mutableBytes)] = bytes_value[0 : len(bytes_value)]

    def testInitWithContents(self):
        b, err = Foundation.NSData.alloc().initWithContentsOfFile_options_error_(
            "/etc/hosts", 0, None
        )
        self.assertIsInstance(b, Foundation.NSData)
        self.assertIs(err, None)
        b2, err = Foundation.NSData.alloc().initWithContentsOfFile_options_error_(
            "/etc/hosts.nosuchfile", 0, None
        )
        self.assertIs(b2, None)
        self.assertIsInstance(err, Foundation.NSError)
        url = Foundation.NSURL.fileURLWithPath_isDirectory_("/etc/hosts", False)
        b, err = Foundation.NSData.alloc().initWithContentsOfURL_options_error_(
            url, 0, None
        )
        self.assertIsInstance(b, Foundation.NSData)
        self.assertIs(err, None)
        url = Foundation.NSURL.fileURLWithPath_isDirectory_(
            "/etc/hosts.nosuchfile", False
        )
        b2, err = Foundation.NSData.alloc().initWithContentsOfURL_options_error_(
            url, 0, None
        )
        self.assertIs(b2, None)
        self.assertIsInstance(err, Foundation.NSError)


class MyData(Foundation.NSData):
    def dataWithBytes_length_(self, data, length):
        return ("data", data, length)


BYTES = "dummy bytes"


class MyData2(Foundation.NSData):
    def initWithBytes_length_(self, data, length):
        return ("init", data, length)

    def length(self):
        return 42

    def bytes(self):  # noqa: A003
        return BYTES


class MyData3(Foundation.NSData):
    def initWithBytes_length_(self, value, length):
        self._bytes = value
        self._length = length
        return self

    def bytes(self):  # noqa: A003
        return self._bytes

    def length(self):
        if hasattr(self, "_length"):
            return self._length
        return -1


class MyData4(Foundation.NSData):
    def initWithBytes_length_(self, value, length):
        return self

    def bytes(self):  # noqa: A003
        return None

    def length(self):
        return -1


class MyData5(Foundation.NSData):
    def initWithBytes_length_(self, value, length):
        return self

    def bytes(self):  # noqa: A003
        raise ValueError("No bytes available")

    def length(self):
        return -1


class TestMyData(TestCase):
    # 'initWithBytes:length:' and 'dataWithBytes:length:' have custom IMP's
    def testData(self):
        r = PyObjC_TestClass3.makeDataWithBytes_method_(MyData, 0)
        self.assertEqual(r, ("data", b"hello world", 11))

    def testInit(self):
        r = PyObjC_TestClass3.makeDataWithBytes_method_(MyData2, 1)
        self.assertEqual(r, ("init", b"hello world", 11))

    def testBytes(self):
        r = PyObjC_TestClass3.makeDataWithBytes_method_(MyData3, 1)
        b = PyObjC_TestClass3.getBytes_(r)

        # Check for memoryview
        if isinstance(b.bytes(), memoryview):
            self.assertEqual(b.bytes().tobytes(), b"hello world")
        else:
            self.assertEqual(bytes(b.bytes()), b"hello world")

        self.assertEqual(b.getBytes_length_(None, 4), b"hell")
        self.assertEqual(b.getBytes_range_(None, Foundation.NSRange(2, 4)), b"llo ")

    def testBytesNone(self):
        b = PyObjC_TestClass3.makeDataWithBytes_method_(MyData4, 1)
        self.assertEqual(b.bytes(), None)

    def testBytesRaises(self):
        b = PyObjC_TestClass3.makeDataWithBytes_method_(MyData5, 1)
        self.assertRaises(ValueError, b.bytes)


class TestBuffer(TestCase):
    def testArray(self):
        pool = Foundation.NSAutoreleasePool.alloc().init()
        a = array.array("b", b"foo")
        m = Foundation.NSMutableData.dataWithData_(a)
        self.assertEqual(a.tobytes(), m[:])
        self.assertTrue(objc.repythonify(a) is a)
        del pool
        a.frombytes(m)
        self.assertEqual(a.tobytes(), b"foofoo")
        m.appendData_(a)
        self.assertEqual(m[:], b"foofoofoo")
        m[3:6] = b"bar"
        self.assertEqual(m[:], b"foobarfoo")

    def testBuffer(self):
        b = b"foo"
        m = Foundation.NSMutableData.dataWithData_(b)
        self.assertEqual(b[:], m[:])
        self.assertTrue(objc.repythonify(b) is b)
        self.assertEqual(memoryview(m)[:], m[:])


class TestRegressions(TestCase):
    def testDataStr(self):
        input_bytes = b"hello"
        input_str = str(input_bytes)

        buf = Foundation.NSData.dataWithData_(input_bytes)
        self.assertEqual(str(buf), input_str)
