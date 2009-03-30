# This just tests the definitions in the NSKeyedArchiver header
from PyObjCTools.TestSupport import *
from Foundation import *


class TestNSKeyedArchiver (TestCase):
    def testConstants(self):
        self.failUnless(isinstance(NSInvalidArchiveOperationException, unicode))
        self.failUnless(isinstance(NSInvalidUnarchiveOperationException, unicode))

    def testOutput(self):
        o = NSKeyedUnarchiver.alloc().initForReadingWithData_(
                NSKeyedArchiver.archivedDataWithRootObject_(u"foobar"))
        self.failUnless( isinstance(o, NSKeyedUnarchiver))

        m = o.decodeBytesForKey_returnedLength_.__metadata__()
        self.assertEquals(m['retval']['type'], '^v')
        self.failUnless(m['arguments'][3]['type'].startswith('o^'))

        data = NSMutableData.alloc().init()
        o = NSArchiver.alloc().initForWritingWithMutableData_(data)
        m = o.encodeBytes_length_forKey_.__metadata__()
        self.assertEquals(m['arguments'][2]['type'], 'n^v')

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSKeyedArchiver.archiveRootObject_toFile_)
        self.failUnlessArgIsBOOL(NSKeyedArchiver.encodeBool_forKey_, 0)
        self.failUnlessArgHasType(NSKeyedArchiver.encodeBytes_length_forKey_, 0, 'n^v')
        self.failUnlessArgSizeInArg(NSKeyedArchiver.encodeBytes_length_forKey_, 0, 1)

        self.failUnlessResultIsBOOL(NSKeyedUnarchiver.containsValueForKey_)
        self.failUnlessResultIsBOOL(NSKeyedUnarchiver.decodeBoolForKey_)

        self.failUnlessResultHasType(NSKeyedUnarchiver.decodeBytesForKey_returnedLength_, '^v')
        self.failUnlessResultSizeInArg(NSKeyedUnarchiver.decodeBytesForKey_returnedLength_, 1)
        self.failUnlessArgIsOut(NSKeyedUnarchiver.decodeBytesForKey_returnedLength_, 1)

        self.failUnlessArgHasType(NSCoder.encodePoint_forKey_, 0, NSPoint.__typestr__)
        self.failUnlessArgHasType(NSCoder.encodeSize_forKey_, 0, NSSize.__typestr__)
        self.failUnlessArgHasType(NSCoder.encodeRect_forKey_, 0, NSRect.__typestr__)
        self.failUnlessResultHasType(NSCoder.decodePointForKey_, NSPoint.__typestr__)
        self.failUnlessResultHasType(NSCoder.decodeSizeForKey_, NSSize.__typestr__)
        self.failUnlessResultHasType(NSCoder.decodeRectForKey_, NSRect.__typestr__)


if __name__ == "__main__":
    main()

