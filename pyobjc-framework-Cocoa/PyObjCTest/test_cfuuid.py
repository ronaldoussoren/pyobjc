from PyObjCTools.TestSupport import *
import re
from CoreFoundation import *


class TestCFUUIDAPI (TestCase):
    def testTypes(self):
        self.assertIsCFType(CFUUIDRef)

    def testTypeID(self):
        v = CFUUIDGetTypeID()
        self.assertIsInstance(v, (int, long))
    def testCreate(self):

        self.assertResultIsCFRetained(CFUUIDCreate)
        uuid = CFUUIDCreate(None)
        self.assertIsNot(uuid, None)
        self.assertIsInstance(uuid, CFUUIDRef)
        text = CFUUIDCreateString(None, uuid)
        self.assertIsInstance(text, unicode)
        m = re.match('^[0-9A-Z]{8}(-[0-9A-Z]{4}){3}-[0-9A-Z]{12}$', text)
        self.assertIsNot(m, None )
    def testCreateWithBytes(self):
        self.assertResultIsCFRetained(CFUUIDCreateWithBytes)
        uuid = CFUUIDCreateWithBytes(None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
        self.assertIsNot(uuid, None)
        self.assertIsInstance(uuid, CFUUIDRef)
        self.assertResultIsCFRetained(CFUUIDCreateString)
        text = CFUUIDCreateString(None, uuid)
        self.assertEqual(text , u'01020304-0506-0708-090A-0B0C0D0E0F10')
        self.assertRaises(ValueError, CFUUIDCreateWithBytes, None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 300)
        self.assertRaises(ValueError, CFUUIDCreateWithBytes, None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 300, 16)

    def testCreateFromString(self):
        self.assertResultIsCFRetained(CFUUIDCreateFromString)
        uuid1 = CFUUIDCreateFromString(None, u'01020304-0506-0708-090A-0B0C0D0E0F10')
        self.assertIsNot(uuid1, None)
        self.assertIsInstance(uuid1, CFUUIDRef)
        text = CFUUIDCreateString(None, uuid1)
        self.assertEqual(text , u'01020304-0506-0708-090A-0B0C0D0E0F10')
        uuid2 = CFUUIDCreateFromString(None, u'01020304-0506-0708-090A-0B0C0D0E0F10')
        text = CFUUIDCreateString(None, uuid2)
        self.assertEqual(text , u'01020304-0506-0708-090A-0B0C0D0E0F10')
        # CFUUID interns values
        self.assertIs(uuid1, uuid2)
    def testGetBytes(self):
        uuid = CFUUIDCreateWithBytes(None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
        self.assertIsNot(uuid, None)
        self.assertIsInstance(uuid, CFUUIDRef)
        bytes = CFUUIDGetUUIDBytes(uuid)
        self.assertIsInstance(bytes, CFUUIDBytes)
        self.assertEqual(bytes.byte0 , 1)
        self.assertEqual(bytes.byte1 , 2)
        self.assertEqual(bytes.byte2 , 3)
        self.assertEqual(bytes.byte3 , 4)
        self.assertEqual(bytes.byte4 , 5)
        self.assertEqual(bytes.byte5 , 6)
        self.assertEqual(bytes.byte6 , 7)
        self.assertEqual(bytes.byte7 , 8)
        self.assertEqual(bytes.byte8 , 9)
        self.assertEqual(bytes.byte9 , 10)
        self.assertEqual(bytes.byte10 , 11)
        self.assertEqual(bytes.byte11 , 12)
        self.assertEqual(bytes.byte12 , 13)
        self.assertEqual(bytes.byte13 , 14)
        self.assertEqual(bytes.byte14 , 15)
        self.assertEqual(bytes.byte15 , 16)
    def testConstant(self):
        # This is an interesting one, the result of 
        # CFUUIDGetConstantUUIDWithBytes should not be released.

        uuid = CFUUIDGetConstantUUIDWithBytes(None, *range(16))
        CFRetain(CFUUIDGetConstantUUIDWithBytes) # Ensure the value won't be released.
        self.assertIsNot(uuid, None)
        self.assertIsInstance(uuid, CFUUIDRef)
        s = CFUUIDCreateString(None, uuid)

        uuid = None
        del uuid

        uuid = CFUUIDGetConstantUUIDWithBytes(None, *range(16))
        self.assertIsNot(uuid, None)
        self.assertIsInstance(uuid, CFUUIDRef)
        t = CFUUIDCreateString(None, uuid)

        self.assertEqual(s , t)
    def testCreateFromUUIDBytes(self):
        bytes = CFUUIDBytes(*range(16, 32))
        uuid = CFUUIDCreateFromUUIDBytes(None, bytes)

        self.assertIsNot(uuid, None)
        self.assertIsInstance(uuid, CFUUIDRef)
        text = CFUUIDCreateString(None, uuid)
        self.assertEqual(text , u'10111213-1415-1617-1819-1A1B1C1D1E1F' )
    def testStructs(self):
        o = CFUUIDBytes()
        self.assertHasAttr(o, 'byte0')
        self.assertHasAttr(o, 'byte1')
        self.assertHasAttr(o, 'byte2')
        self.assertHasAttr(o, 'byte3')
        self.assertHasAttr(o, 'byte4')
        self.assertHasAttr(o, 'byte5')
        self.assertHasAttr(o, 'byte6')
        self.assertHasAttr(o, 'byte7')
        self.assertHasAttr(o, 'byte8')
        self.assertHasAttr(o, 'byte9')
        self.assertHasAttr(o, 'byte10')
        self.assertHasAttr(o, 'byte11')
        self.assertHasAttr(o, 'byte12')
        self.assertHasAttr(o, 'byte13')
        self.assertHasAttr(o, 'byte14')
        self.assertHasAttr(o, 'byte15')
if __name__ == "__main__":
    main()
