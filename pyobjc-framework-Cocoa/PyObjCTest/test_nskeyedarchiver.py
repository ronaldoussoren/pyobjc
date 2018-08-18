# This just tests the definitions in the NSKeyedArchiver header
from PyObjCTools.TestSupport import *
from Foundation import *


class TestNSKeyedArchiver (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSInvalidArchiveOperationException, unicode)
        self.assertIsInstance(NSInvalidUnarchiveOperationException, unicode)

    @min_os_level('10.9')
    def testConstants10_9(self):
        self.assertIsInstance(NSKeyedArchiveRootObjectKey, unicode)

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

    @min_os_level('10.8')
    def testMethods10_8(self):
        self.assertResultIsBOOL(NSKeyedArchiver.requiresSecureCoding)
        self.assertArgIsBOOL(NSKeyedArchiver.setRequiresSecureCoding_, 0)
        self.assertResultIsBOOL(NSKeyedUnarchiver.requiresSecureCoding)
        self.assertArgIsBOOL(NSKeyedUnarchiver.setRequiresSecureCoding_, 0)

    @min_os_level('10.13')
    def testMethods10_13(self):
        self.assertArgIsBOOL(NSKeyedArchiver.initRequiringSecureCoding_, 0)
        self.assertArgIsBOOL(NSKeyedArchiver.archivedDataWithRootObject_requiringSecureCoding_error_, 1)
        self.assertArgIsOut(NSKeyedArchiver.archivedDataWithRootObject_requiringSecureCoding_error_, 2)

        self.assertArgIsOut(NSKeyedUnarchiver.initForReadingFromData_error_, 1)
        self.assertArgIsOut(NSKeyedUnarchiver.unarchivedObjectOfClass_fromData_error_, 2)
        self.assertArgIsOut(NSKeyedUnarchiver.unarchivedObjectOfClasses_fromData_error_, 2)

    @min_sdk_level('10.7')
    def testProtocols(self):
        objc.protocolNamed('NSKeyedArchiverDelegate')
        objc.protocolNamed('NSKeyedUnarchiverDelegate')

if __name__ == "__main__":
    main()
