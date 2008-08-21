import unittest
from CoreFoundation import *


class TestPropertyList (unittest.TestCase):
    def testFunctions(self):
        # FIXME: this doesn't work as expected:
        # dta = CFPropertyListCreateXMLData(None, {u"key": 42, u"key2": 1})


        dta = CFPropertyListCreateXMLData(None, {u"key": 42, u"key2": 1})
        self.failUnless(isinstance(dta, CFDataRef))

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
        #CFPropertyListWriteToStream(CFPropertyListRef propertyList, CFWriteStreamRef stream, CFPropertyListFormat format, CFStringRef *errorString);
        #CFPropertyListRef CFPropertyListCreateFromStream(CFAllocatorRef allocator, CFReadStreamRef stream, CFIndex streamLength, CFOptionFlags mutabilityOption, CFPropertyListFormat *format, CFStringRef *errorString);
        self.fail("Implement stream related tests")



    def testConstants(self):
        self.failUnless(kCFPropertyListImmutable == 0)
        self.failUnless(kCFPropertyListMutableContainers == 1)
        self.failUnless(kCFPropertyListMutableContainersAndLeaves == 2)

        self.failUnless(kCFPropertyListOpenStepFormat == 1)
        self.failUnless(kCFPropertyListXMLFormat_v1_0 == 100)
        self.failUnless(kCFPropertyListBinaryFormat_v1_0 == 200)




if __name__ == "__main__":
    unittest.main()
