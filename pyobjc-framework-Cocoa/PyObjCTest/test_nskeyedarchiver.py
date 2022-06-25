# This just tests the definitions in the Foundation.NSKeyedArchiver header
import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestNSKeyedArchiver(TestCase):
    def testConstants(self):
        self.assertIsInstance(Foundation.NSInvalidArchiveOperationException, str)
        self.assertIsInstance(Foundation.NSInvalidUnarchiveOperationException, str)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(Foundation.NSKeyedArchiveRootObjectKey, str)

    def testOutput(self):
        o = Foundation.NSKeyedUnarchiver.alloc().initForReadingWithData_(
            Foundation.NSKeyedArchiver.archivedDataWithRootObject_("foobar")
        )
        self.assertIsInstance(o, Foundation.NSKeyedUnarchiver)
        m = o.decodeBytesForKey_returnedLength_.__metadata__()
        self.assertEqual(m["retval"]["type"], b"^v")
        self.assertTrue(m["arguments"][3]["type"].startswith(b"o^"))

        data = Foundation.NSMutableData.alloc().init()
        o = Foundation.NSArchiver.alloc().initForWritingWithMutableData_(data)
        m = o.encodeBytes_length_forKey_.__metadata__()
        self.assertEqual(m["arguments"][2]["type"], b"n^v")

    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSKeyedArchiver.archiveRootObject_toFile_)
        self.assertArgIsBOOL(Foundation.NSKeyedArchiver.encodeBool_forKey_, 0)
        self.assertArgHasType(
            Foundation.NSKeyedArchiver.encodeBytes_length_forKey_, 0, b"n^v"
        )
        self.assertArgSizeInArg(
            Foundation.NSKeyedArchiver.encodeBytes_length_forKey_, 0, 1
        )

        self.assertResultIsBOOL(Foundation.NSKeyedUnarchiver.containsValueForKey_)
        self.assertResultIsBOOL(Foundation.NSKeyedUnarchiver.decodeBoolForKey_)

        self.assertResultHasType(
            Foundation.NSKeyedUnarchiver.decodeBytesForKey_returnedLength_, b"^v"
        )
        self.assertResultSizeInArg(
            Foundation.NSKeyedUnarchiver.decodeBytesForKey_returnedLength_, 1
        )
        self.assertArgIsOut(
            Foundation.NSKeyedUnarchiver.decodeBytesForKey_returnedLength_, 1
        )

        self.assertArgHasType(
            Foundation.NSCoder.encodePoint_forKey_, 0, Foundation.NSPoint.__typestr__
        )
        self.assertArgHasType(
            Foundation.NSCoder.encodeSize_forKey_, 0, Foundation.NSSize.__typestr__
        )
        self.assertArgHasType(
            Foundation.NSCoder.encodeRect_forKey_, 0, Foundation.NSRect.__typestr__
        )
        self.assertResultHasType(
            Foundation.NSCoder.decodePointForKey_, Foundation.NSPoint.__typestr__
        )
        self.assertResultHasType(
            Foundation.NSCoder.decodeSizeForKey_, Foundation.NSSize.__typestr__
        )
        self.assertResultHasType(
            Foundation.NSCoder.decodeRectForKey_, Foundation.NSRect.__typestr__
        )

    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertResultIsBOOL(Foundation.NSKeyedArchiver.requiresSecureCoding)
        self.assertArgIsBOOL(Foundation.NSKeyedArchiver.setRequiresSecureCoding_, 0)
        self.assertResultIsBOOL(Foundation.NSKeyedUnarchiver.requiresSecureCoding)
        self.assertArgIsBOOL(Foundation.NSKeyedUnarchiver.setRequiresSecureCoding_, 0)

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsBOOL(Foundation.NSKeyedArchiver.initRequiringSecureCoding_, 0)
        self.assertArgIsBOOL(
            Foundation.NSKeyedArchiver.archivedDataWithRootObject_requiringSecureCoding_error_,
            1,
        )
        self.assertArgIsOut(
            Foundation.NSKeyedArchiver.archivedDataWithRootObject_requiringSecureCoding_error_,
            2,
        )

        self.assertArgIsOut(
            Foundation.NSKeyedUnarchiver.initForReadingFromData_error_, 1
        )
        self.assertArgIsOut(
            Foundation.NSKeyedUnarchiver.unarchivedObjectOfClass_fromData_error_, 2
        )
        self.assertArgIsOut(
            Foundation.NSKeyedUnarchiver.unarchivedObjectOfClasses_fromData_error_, 2
        )

    @min_os_level("11.0")
    def testMethods11_0(self):
        self.assertArgIsOut(
            Foundation.NSKeyedUnarchiver.unarchivedArrayOfObjectsOfClasses_fromData_error_,
            2,
        )
        self.assertArgIsOut(
            Foundation.NSKeyedUnarchiver.unarchivedDictionaryWithKeysOfClasses_objectsOfClasses_fromData_error_,
            3,
        )

    @min_sdk_level("10.7")
    def testProtocols(self):
        self.assertProtocolExists("NSKeyedArchiverDelegate")
        self.assertProtocolExists("NSKeyedUnarchiverDelegate")
