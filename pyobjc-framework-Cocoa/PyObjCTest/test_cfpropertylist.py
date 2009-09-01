from PyObjCTools.TestSupport import *
from CoreFoundation import *


class TestPropertyList (TestCase):
    def testFunctions(self):
        dta = CFPropertyListCreateXMLData(None, {u"key": 42, u"key2": 1})
        self.failUnless(isinstance(dta, CFDataRef))

        self.failUnlessArgIsOut(CFPropertyListCreateFromXMLData, 3)
        v, err = CFPropertyListCreateFromXMLData(None, dta, 0, None)
        self.failUnless(err is None)
        self.failUnless(isinstance(v, CFDictionaryRef))
        self.failUnless('key' in v)
        self.failUnless('key2' in v)
        self.failUnless(v['key'] == 42)
        self.failUnless(v['key2'] == True)

        v = CFPropertyListCreateDeepCopy(None, {u"key": 42, u"key2": True}, 0)
        self.failUnless(isinstance(v, CFDictionaryRef))
        self.failUnless('key' in v)
        self.failUnless('key2' in v)
        self.failUnless(v['key'] == 42)
        self.failUnless(v['key2'] == True)

        valid = CFPropertyListIsValid({u"key": 42, u"key2": True}, kCFPropertyListBinaryFormat_v1_0)
        self.failUnless(valid is True)

    def testStreams(self):

        stream = CFWriteStreamCreateWithAllocatedBuffers(kCFAllocatorDefault, kCFAllocatorDefault)
        r = CFWriteStreamOpen(stream)
        self.failUnless(r)

        value = {u'key1': 42, u'key2': 1}

        self.failUnlessArgIsOut(CFPropertyListWriteToStream, 3)
        rval, errorString = CFPropertyListWriteToStream(value, stream, 
                kCFPropertyListXMLFormat_v1_0, None)
        self.failUnless(isinstance(rval, (int, long)))
        self.failUnless(rval)
        self.failUnless(errorString is None)

        buf = CFWriteStreamCopyProperty(stream, kCFStreamPropertyDataWritten)
        self.failUnless(isinstance(buf, CFDataRef))
        buf = CFDataGetBytes(buf, (0, CFDataGetLength(buf)), None)
        self.failUnless(isinstance(buf, str))

        self.failUnless('<key>key1</key>' in buf)
        self.failUnless('<integer>42</integer>' in buf)
        self.failUnless('<key>key2</key>' in buf)
        self.failUnless('<integer>1</integer>' in buf)

        stream = CFReadStreamCreateWithBytesNoCopy(None, buf, len(buf), kCFAllocatorNull)
        r = CFReadStreamOpen(stream)
        self.failUnless(r)

        self.failUnlessArgIsOut(CFPropertyListCreateFromStream, 4)
        self.failUnlessArgIsOut(CFPropertyListCreateFromStream, 5)
        res, format, errorString = CFPropertyListCreateFromStream(None, stream, 0, 0, None, None)
        self.assertEquals(format, kCFPropertyListXMLFormat_v1_0)
        self.failUnless(errorString is None)
        self.assertEquals(res, value)



    def testConstants(self):
        self.failUnless(kCFPropertyListImmutable == 0)
        self.failUnless(kCFPropertyListMutableContainers == 1)
        self.failUnless(kCFPropertyListMutableContainersAndLeaves == 2)

        self.failUnless(kCFPropertyListOpenStepFormat == 1)
        self.failUnless(kCFPropertyListXMLFormat_v1_0 == 100)
        self.failUnless(kCFPropertyListBinaryFormat_v1_0 == 200)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessEqual(kCFPropertyListReadCorruptError, 3840)
        self.failUnlessEqual(kCFPropertyListReadUnknownVersionError, 3841)
        self.failUnlessEqual(kCFPropertyListReadStreamError, 3842)
        self.failUnlessEqual(kCFPropertyListWriteStreamError, 3851)

    @min_os_level('10.6')
    def testFunctions10_6(self):
        dta = CFPropertyListCreateXMLData(None, {u"key": 42, u"key2": 1})
        self.failUnless(isinstance(dta, CFDataRef))

        bytes = CFDataGetBytes(dta, (0, CFDataGetLength(dta)), None)
        self.failIf(bytes is None)

        self.failUnlessResultIsCFRetained(CFPropertyListCreateWithData)
        self.failUnlessArgIsOut(CFPropertyListCreateWithData, 3)
        self.failUnlessArgIsOut(CFPropertyListCreateWithData, 4)
        v, fmt, err = CFPropertyListCreateWithData(None, dta, 0, None, None)
        self.failIf(v is None)
        self.failUnlessIsInstance(fmt, (int, long))
        self.failUnless(err is None)

        stream = CFReadStreamCreateWithBytesNoCopy(None, bytes, len(bytes), kCFAllocatorNull)
        CFReadStreamOpen(stream)

        self.failUnlessResultIsCFRetained(CFPropertyListCreateWithStream)
        self.failUnlessArgIsOut(CFPropertyListCreateWithStream, 4)
        self.failUnlessArgIsOut(CFPropertyListCreateWithStream, 5)
        v, fmt, err = CFPropertyListCreateWithStream(None, stream, len(bytes), 0, None, None)
        self.failIf(v is None)
        self.failUnlessIsInstance(fmt, (int, long))
        self.failUnless(err is None)

        import array
        buf = array.array('b', ' '*1024)

        stream = CFWriteStreamCreateWithBuffer(None, buf, 1024)
        CFWriteStreamOpen(stream)

        self.failUnlessArgIsOut(CFPropertyListWrite, 4)
        cnt, err = CFPropertyListWrite({'key':42}, stream, kCFPropertyListBinaryFormat_v1_0, 0, None)
        self.failIfEqual(cnt, 0)
        self.failUnlessEqual(err, None)

        self.failUnlessResultIsCFRetained(CFPropertyListCreateData)
        self.failUnlessArgIsOut(CFPropertyListCreateData, 4)
        dta, err = CFPropertyListCreateData(None, {'key':'value'}, kCFPropertyListBinaryFormat_v1_0, 0, None)
        self.failUnlessIsInstance(dta, CFDataRef)
        self.failUnlessEqual(err, None)



if __name__ == "__main__":
    main()
