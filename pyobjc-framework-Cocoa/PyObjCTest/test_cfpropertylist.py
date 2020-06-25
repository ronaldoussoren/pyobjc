import CoreFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestPropertyList(TestCase):
    def testFunctions(self):
        dta = CoreFoundation.CFPropertyListCreateXMLData(None, {"key": 42, "key2": 1})
        self.assertIsInstance(dta, CoreFoundation.CFDataRef)
        self.assertArgIsOut(CoreFoundation.CFPropertyListCreateFromXMLData, 3)
        v, err = CoreFoundation.CFPropertyListCreateFromXMLData(None, dta, 0, None)
        self.assertIs(err, None)
        self.assertIsInstance(v, CoreFoundation.CFDictionaryRef)
        self.assertIn("key", v)
        self.assertIn("key2", v)
        self.assertEqual(v["key"], 42)
        self.assertEqual(v["key2"], True)
        v = CoreFoundation.CFPropertyListCreateDeepCopy(
            None, {"key": 42, "key2": True}, 0
        )
        self.assertIsInstance(v, CoreFoundation.CFDictionaryRef)
        self.assertIn("key", v)
        self.assertIn("key2", v)
        self.assertEqual(v["key"], 42)
        self.assertEqual(v["key2"], True)
        valid = CoreFoundation.CFPropertyListIsValid(
            {"key": 42, "key2": True}, CoreFoundation.kCFPropertyListBinaryFormat_v1_0
        )
        self.assertIs(valid, True)

    def testStreams(self):
        stream = CoreFoundation.CFWriteStreamCreateWithAllocatedBuffers(
            CoreFoundation.kCFAllocatorDefault, CoreFoundation.kCFAllocatorDefault
        )
        r = CoreFoundation.CFWriteStreamOpen(stream)
        self.assertTrue(r)

        value = {"key1": 42, "key2": 1}

        self.assertArgIsOut(CoreFoundation.CFPropertyListWriteToStream, 3)
        rval, errorString = CoreFoundation.CFPropertyListWriteToStream(
            value, stream, CoreFoundation.kCFPropertyListXMLFormat_v1_0, None
        )
        self.assertIsInstance(rval, int)
        self.assertTrue(rval)
        self.assertIs(errorString, None)
        buf = CoreFoundation.CFWriteStreamCopyProperty(
            stream, CoreFoundation.kCFStreamPropertyDataWritten
        )
        self.assertIsInstance(buf, CoreFoundation.CFDataRef)
        buf = CoreFoundation.CFDataGetBytes(
            buf, (0, CoreFoundation.CFDataGetLength(buf)), None
        )
        self.assertIsInstance(buf, bytes)
        self.assertIn(b"<key>key1</key>", buf)
        self.assertIn(b"<integer>42</integer>", buf)
        self.assertIn(b"<key>key2</key>", buf)
        self.assertIn(b"<integer>1</integer>", buf)
        stream = CoreFoundation.CFReadStreamCreateWithBytesNoCopy(
            None, buf, len(buf), CoreFoundation.kCFAllocatorNull
        )
        r = CoreFoundation.CFReadStreamOpen(stream)
        self.assertTrue(r)

        self.assertArgIsOut(CoreFoundation.CFPropertyListCreateFromStream, 4)
        self.assertArgIsOut(CoreFoundation.CFPropertyListCreateFromStream, 5)
        res, plist_format, errorString = CoreFoundation.CFPropertyListCreateFromStream(
            None, stream, 0, 0, None, None
        )
        self.assertEqual(plist_format, CoreFoundation.kCFPropertyListXMLFormat_v1_0)
        self.assertIs(errorString, None)
        self.assertEqual(res, value)

    def testConstants(self):
        self.assertEqual(CoreFoundation.kCFPropertyListImmutable, 0)
        self.assertEqual(CoreFoundation.kCFPropertyListMutableContainers, 1 << 0)
        self.assertEqual(
            CoreFoundation.kCFPropertyListMutableContainersAndLeaves, 1 << 1
        )

        self.assertEqual(CoreFoundation.kCFPropertyListOpenStepFormat, 1)
        self.assertEqual(CoreFoundation.kCFPropertyListXMLFormat_v1_0, 100)
        self.assertEqual(CoreFoundation.kCFPropertyListBinaryFormat_v1_0, 200)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(CoreFoundation.kCFPropertyListReadCorruptError, 3840)
        self.assertEqual(CoreFoundation.kCFPropertyListReadUnknownVersionError, 3841)
        self.assertEqual(CoreFoundation.kCFPropertyListReadStreamError, 3842)
        self.assertEqual(CoreFoundation.kCFPropertyListWriteStreamError, 3851)

    @min_os_level("10.6")
    def testFunctions10_6(self):
        dta = CoreFoundation.CFPropertyListCreateXMLData(None, {"key": 42, "key2": 1})
        self.assertIsInstance(dta, CoreFoundation.CFDataRef)
        bytes_value = CoreFoundation.CFDataGetBytes(
            dta, (0, CoreFoundation.CFDataGetLength(dta)), None
        )
        self.assertIsNot(bytes_value, None)
        self.assertResultIsCFRetained(CoreFoundation.CFPropertyListCreateWithData)
        self.assertArgIsOut(CoreFoundation.CFPropertyListCreateWithData, 3)
        self.assertArgIsOut(CoreFoundation.CFPropertyListCreateWithData, 4)
        v, fmt, err = CoreFoundation.CFPropertyListCreateWithData(
            None, dta, 0, None, None
        )
        self.assertIsNot(v, None)
        self.assertIsInstance(fmt, int)
        self.assertIs(err, None)
        stream = CoreFoundation.CFReadStreamCreateWithBytesNoCopy(
            None, bytes_value, len(bytes_value), CoreFoundation.kCFAllocatorNull
        )
        CoreFoundation.CFReadStreamOpen(stream)

        self.assertResultIsCFRetained(CoreFoundation.CFPropertyListCreateWithStream)
        self.assertArgIsOut(CoreFoundation.CFPropertyListCreateWithStream, 4)
        self.assertArgIsOut(CoreFoundation.CFPropertyListCreateWithStream, 5)
        v, fmt, err = CoreFoundation.CFPropertyListCreateWithStream(
            None, stream, len(bytes_value), 0, None, None
        )
        self.assertIsNot(v, None)
        self.assertIsInstance(fmt, int)
        self.assertIs(err, None)
        import array

        buf = array.array("b", b" " * 1024)

        stream = CoreFoundation.CFWriteStreamCreateWithBuffer(None, buf, 1024)
        CoreFoundation.CFWriteStreamOpen(stream)

        self.assertArgIsOut(CoreFoundation.CFPropertyListWrite, 4)
        cnt, err = CoreFoundation.CFPropertyListWrite(
            {"key": 42},
            stream,
            CoreFoundation.kCFPropertyListBinaryFormat_v1_0,
            0,
            None,
        )
        self.assertNotEqual(cnt, 0)
        self.assertEqual(err, None)

        self.assertResultIsCFRetained(CoreFoundation.CFPropertyListCreateData)
        self.assertArgIsOut(CoreFoundation.CFPropertyListCreateData, 4)
        dta, err = CoreFoundation.CFPropertyListCreateData(
            None,
            {"key": "value"},
            CoreFoundation.kCFPropertyListBinaryFormat_v1_0,
            0,
            None,
        )
        self.assertIsInstance(dta, CoreFoundation.CFDataRef)
        self.assertEqual(err, None)
