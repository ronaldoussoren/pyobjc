from PyObjCTools.TestSupport import *
import re
from CoreFoundation import *


class TestCFUUIDAPI (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CFUUIDRef)

    def testTypeID(self):
        v = CFUUIDGetTypeID()
        self.failUnless(isinstance(v, (int, long)))

    def testCreate(self):

        self.failUnlessResultIsCFRetained(CFUUIDCreate)
        uuid = CFUUIDCreate(None)
        self.failIf(uuid is None)
        self.failUnless(isinstance(uuid, CFUUIDRef))

        text = CFUUIDCreateString(None, uuid)
        self.failUnless(isinstance(text, unicode))
        m = re.match('^[0-9A-Z]{8}(-[0-9A-Z]{4}){3}-[0-9A-Z]{12}$', text)
        self.failIf( m is None )

    def testCreateWithBytes(self):
        self.failUnlessResultIsCFRetained(CFUUIDCreateWithBytes)
        uuid = CFUUIDCreateWithBytes(None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
        self.failIf(uuid is None)
        self.failUnless(isinstance(uuid, CFUUIDRef))

        self.failUnlessResultIsCFRetained(CFUUIDCreateString)
        text = CFUUIDCreateString(None, uuid)
        self.failUnless(text == u'01020304-0506-0708-090A-0B0C0D0E0F10')

        self.assertRaises(ValueError, CFUUIDCreateWithBytes, None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 300)
        self.assertRaises(ValueError, CFUUIDCreateWithBytes, None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 300, 16)

    def testCreateFromString(self):
        self.failUnlessResultIsCFRetained(CFUUIDCreateFromString)
        uuid1 = CFUUIDCreateFromString(None, u'01020304-0506-0708-090A-0B0C0D0E0F10')
        self.failIf(uuid1 is None)
        self.failUnless(isinstance(uuid1, CFUUIDRef))

        text = CFUUIDCreateString(None, uuid1)
        self.failUnless(text == u'01020304-0506-0708-090A-0B0C0D0E0F10')

        uuid2 = CFUUIDCreateFromString(None, u'01020304-0506-0708-090A-0B0C0D0E0F10')
        text = CFUUIDCreateString(None, uuid2)
        self.failUnless(text == u'01020304-0506-0708-090A-0B0C0D0E0F10')

        # CFUUID interns values
        self.failUnless(uuid1 is uuid2)

    def testGetBytes(self):
        uuid = CFUUIDCreateWithBytes(None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
        self.failIf(uuid is None)
        self.failUnless(isinstance(uuid, CFUUIDRef))

        bytes = CFUUIDGetUUIDBytes(uuid)
        self.failUnless( isinstance(bytes, CFUUIDBytes) )
        self.failUnless(bytes.byte0 == 1)
        self.failUnless(bytes.byte1 == 2)
        self.failUnless(bytes.byte2 == 3)
        self.failUnless(bytes.byte3 == 4)
        self.failUnless(bytes.byte4 == 5)
        self.failUnless(bytes.byte5 == 6)
        self.failUnless(bytes.byte6 == 7)
        self.failUnless(bytes.byte7 == 8)
        self.failUnless(bytes.byte8 == 9)
        self.failUnless(bytes.byte9 == 10)
        self.failUnless(bytes.byte10 == 11)
        self.failUnless(bytes.byte11 == 12)
        self.failUnless(bytes.byte12 == 13)
        self.failUnless(bytes.byte13 == 14)
        self.failUnless(bytes.byte14 == 15)
        self.failUnless(bytes.byte15 == 16)

    def testConstant(self):
        # This is an interesting one, the result of 
        # CFUUIDGetConstantUUIDWithBytes should not be released.

        uuid = CFUUIDGetConstantUUIDWithBytes(None, *range(16))
        CFRetain(CFUUIDGetConstantUUIDWithBytes) # Ensure the value won't be released.
        self.failIf(uuid is None)
        self.failUnless(isinstance(uuid, CFUUIDRef))

        s = CFUUIDCreateString(None, uuid)

        uuid = None
        del uuid

        uuid = CFUUIDGetConstantUUIDWithBytes(None, *range(16))
        self.failIf(uuid is None)
        self.failUnless(isinstance(uuid, CFUUIDRef))

        t = CFUUIDCreateString(None, uuid)

        self.failUnless(s == t)

    def testCreateFromUUIDBytes(self):
        bytes = CFUUIDBytes(*range(16, 32))
        uuid = CFUUIDCreateFromUUIDBytes(None, bytes)

        self.failIf(uuid is None)
        self.failUnless(isinstance(uuid, CFUUIDRef))

        text = CFUUIDCreateString(None, uuid)
        self.failUnless( text == u'10111213-1415-1617-1819-1A1B1C1D1E1F' )

    def testStructs(self):
        o = CFUUIDBytes()
        self.failUnless( hasattr(o, 'byte0') )
        self.failUnless( hasattr(o, 'byte1') )
        self.failUnless( hasattr(o, 'byte2') )
        self.failUnless( hasattr(o, 'byte3') )
        self.failUnless( hasattr(o, 'byte4') )
        self.failUnless( hasattr(o, 'byte5') )
        self.failUnless( hasattr(o, 'byte6') )
        self.failUnless( hasattr(o, 'byte7') )
        self.failUnless( hasattr(o, 'byte8') )
        self.failUnless( hasattr(o, 'byte9') )
        self.failUnless( hasattr(o, 'byte10') )
        self.failUnless( hasattr(o, 'byte11') )
        self.failUnless( hasattr(o, 'byte12') )
        self.failUnless( hasattr(o, 'byte13') )
        self.failUnless( hasattr(o, 'byte14') )
        self.failUnless( hasattr(o, 'byte15') )

if __name__ == "__main__":
    main()
