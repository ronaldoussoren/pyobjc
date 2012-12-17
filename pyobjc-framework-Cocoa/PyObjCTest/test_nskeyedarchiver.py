# This just tests the definitions in the NSKeyedArchiver header
from PyObjCTools.TestSupport import *
from Foundation import *

try:
    unicode
except NameError:
    unicode = str


class TestNSKeyedArchiver (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSInvalidArchiveOperationException, unicode)
        self.assertIsInstance(NSInvalidUnarchiveOperationException, unicode)

    def testOutput(self):
        o = NSKeyedUnarchiver.alloc().initForReadingWithData_(
                NSKeyedArchiver.archivedDataWithRootObject_(b"foobar".decode('ascii')))
        self.assertIsInstance(o, NSKeyedUnarchiver)
        m = o.decodeBytesForKey_returnedLength_.__metadata__()
        self.assertEqual(m['retval']['type'], b'^v')
        self.assertTrue(m['arguments'][3]['type'].startswith(b'o^'))

        data = NSMutableData.alloc().init()
        o = NSArchiver.alloc().initForWritingWithMutableData_(data)
        m = o.encodeBytes_length_forKey_.__metadata__()
        self.assertEqual(m['arguments'][2]['type'], b'n^v')

    def testMethods(self):
        self.assertResultIsBOOL(NSKeyedArchiver.archiveRootObject_toFile_)
        self.assertArgIsBOOL(NSKeyedArchiver.encodeBool_forKey_, 0)
        self.assertArgHasType(NSKeyedArchiver.encodeBytes_length_forKey_, 0, b'n^v')
        self.assertArgSizeInArg(NSKeyedArchiver.encodeBytes_length_forKey_, 0, 1)

        self.assertResultIsBOOL(NSKeyedUnarchiver.containsValueForKey_)
        self.assertResultIsBOOL(NSKeyedUnarchiver.decodeBoolForKey_)

        self.assertResultHasType(NSKeyedUnarchiver.decodeBytesForKey_returnedLength_, b'^v')
        self.assertResultSizeInArg(NSKeyedUnarchiver.decodeBytesForKey_returnedLength_, 1)
        self.assertArgIsOut(NSKeyedUnarchiver.decodeBytesForKey_returnedLength_, 1)

        self.assertArgHasType(NSCoder.encodePoint_forKey_, 0, NSPoint.__typestr__)
        self.assertArgHasType(NSCoder.encodeSize_forKey_, 0, NSSize.__typestr__)
        self.assertArgHasType(NSCoder.encodeRect_forKey_, 0, NSRect.__typestr__)
        self.assertResultHasType(NSCoder.decodePointForKey_, NSPoint.__typestr__)
        self.assertResultHasType(NSCoder.decodeSizeForKey_, NSSize.__typestr__)
        self.assertResultHasType(NSCoder.decodeRectForKey_, NSRect.__typestr__)


if __name__ == "__main__":
    main()
