from PyObjCTools.TestSupport import *
from CoreFoundation import *


try:
    long
except NameError:
    long = int


class TestPropertyList (TestCase):
    def testFunctions(self):
        dta = CFPropertyListCreateXMLData(None, {b"key".decode('ascii'): 42, b"key2".decode('ascii'): 1})
        self.assertIsInstance(dta, CFDataRef)
        self.assertArgIsOut(CFPropertyListCreateFromXMLData, 3)
        v, err = CFPropertyListCreateFromXMLData(None, dta, 0, None)
        self.assertIs(err, None)
        self.assertIsInstance(v, CFDictionaryRef)
        self.assertIn('key', v)
        self.assertIn('key2', v)
        self.assertEqual(v['key'] , 42)
        self.assertEqual(v['key2'] , True)
        v = CFPropertyListCreateDeepCopy(None, {b"key".decode('ascii'): 42, b"key2".decode('ascii'): True}, 0)
        self.assertIsInstance(v, CFDictionaryRef)
        self.assertIn('key', v)
        self.assertIn('key2', v)
        self.assertEqual(v['key'] , 42)
        self.assertEqual(v['key2'] , True)
        valid = CFPropertyListIsValid({b"key".decode('ascii'): 42, b"key2".decode('ascii'): True}, kCFPropertyListBinaryFormat_v1_0)
        self.assertIs(valid, True)

    def testStreams(self):
        stream = CFWriteStreamCreateWithAllocatedBuffers(kCFAllocatorDefault, kCFAllocatorDefault)
        r = CFWriteStreamOpen(stream)
        self.assertTrue(r)

        value = {b'key1'.decode('ascii'): 42, b'key2'.decode('ascii'): 1}

        self.assertArgIsOut(CFPropertyListWriteToStream, 3)
        rval, errorString = CFPropertyListWriteToStream(value, stream,
                kCFPropertyListXMLFormat_v1_0, None)
        self.assertIsInstance(rval, (int, long))
        self.assertTrue(rval)
        self.assertIs(errorString, None)
        buf = CFWriteStreamCopyProperty(stream, kCFStreamPropertyDataWritten)
        self.assertIsInstance(buf, CFDataRef)
        buf = CFDataGetBytes(buf, (0, CFDataGetLength(buf)), None)
        self.assertIsInstance(buf, bytes)
        self.assertIn(b'<key>key1</key>', buf)
        self.assertIn(b'<integer>42</integer>', buf)
        self.assertIn(b'<key>key2</key>', buf)
        self.assertIn(b'<integer>1</integer>', buf)
        stream = CFReadStreamCreateWithBytesNoCopy(None, buf, len(buf), kCFAllocatorNull)
        r = CFReadStreamOpen(stream)
        self.assertTrue(r)

        self.assertArgIsOut(CFPropertyListCreateFromStream, 4)
        self.assertArgIsOut(CFPropertyListCreateFromStream, 5)
        res, format, errorString = CFPropertyListCreateFromStream(None, stream, 0, 0, None, None)
        self.assertEqual(format, kCFPropertyListXMLFormat_v1_0)
        self.assertIs(errorString, None)
        self.assertEqual(res, value)

    def testConstants(self):
        self.assertEqual(kCFPropertyListImmutable , 0)
        self.assertEqual(kCFPropertyListMutableContainers , 1)
        self.assertEqual(kCFPropertyListMutableContainersAndLeaves , 2)

        self.assertEqual(kCFPropertyListOpenStepFormat , 1)
        self.assertEqual(kCFPropertyListXMLFormat_v1_0 , 100)
        self.assertEqual(kCFPropertyListBinaryFormat_v1_0 , 200)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(kCFPropertyListReadCorruptError, 3840)
        self.assertEqual(kCFPropertyListReadUnknownVersionError, 3841)
        self.assertEqual(kCFPropertyListReadStreamError, 3842)
        self.assertEqual(kCFPropertyListWriteStreamError, 3851)

    @min_os_level('10.6')
    def testFunctions10_6(self):
        dta = CFPropertyListCreateXMLData(None, {b"key".decode('ascii'): 42, b"key2".decode('ascii'): 1})
        self.assertIsInstance(dta, CFDataRef)
        bytes = CFDataGetBytes(dta, (0, CFDataGetLength(dta)), None)
        self.assertIsNot(bytes, None)
        self.assertResultIsCFRetained(CFPropertyListCreateWithData)
        self.assertArgIsOut(CFPropertyListCreateWithData, 3)
        self.assertArgIsOut(CFPropertyListCreateWithData, 4)
        v, fmt, err = CFPropertyListCreateWithData(None, dta, 0, None, None)
        self.assertIsNot(v, None)
        self.assertIsInstance(fmt, (int, long))
        self.assertIs(err, None)
        stream = CFReadStreamCreateWithBytesNoCopy(None, bytes, len(bytes), kCFAllocatorNull)
        CFReadStreamOpen(stream)

        self.assertResultIsCFRetained(CFPropertyListCreateWithStream)
        self.assertArgIsOut(CFPropertyListCreateWithStream, 4)
        self.assertArgIsOut(CFPropertyListCreateWithStream, 5)
        v, fmt, err = CFPropertyListCreateWithStream(None, stream, len(bytes), 0, None, None)
        self.assertIsNot(v, None)
        self.assertIsInstance(fmt, (int, long))
        self.assertIs(err, None)
        import array
        buf = array.array('b', b' '*1024)

        stream = CFWriteStreamCreateWithBuffer(None, buf, 1024)
        CFWriteStreamOpen(stream)

        self.assertArgIsOut(CFPropertyListWrite, 4)
        cnt, err = CFPropertyListWrite({'key':42}, stream, kCFPropertyListBinaryFormat_v1_0, 0, None)
        self.assertNotEqual(cnt, 0)
        self.assertEqual(err, None)

        self.assertResultIsCFRetained(CFPropertyListCreateData)
        self.assertArgIsOut(CFPropertyListCreateData, 4)
        dta, err = CFPropertyListCreateData(None, {'key':'value'}, kCFPropertyListBinaryFormat_v1_0, 0, None)
        self.assertIsInstance(dta, CFDataRef)
        self.assertEqual(err, None)

if __name__ == "__main__":
    main()
