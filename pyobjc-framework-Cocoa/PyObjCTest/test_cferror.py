import CoreFoundation
import objc
import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestError(TestCase):
    @min_os_level("10.5")
    def testTypes(self):
        try:
            NSCFError = objc.lookUpClass("__NSCFError")
        except objc.error:
            NSCFError = objc.lookUpClass("NSCFError")

        self.assertIs(CoreFoundation.CFErrorRef, NSCFError)

    @min_os_level("10.5")
    def testTypeID(self):
        self.assertIsInstance(CoreFoundation.CFErrorGetTypeID(), int)

    @min_os_level("10.5")
    def testCreation(self):
        userInfo = {"foo": "bar"}
        err = CoreFoundation.CFErrorCreate(
            None, CoreFoundation.kCFErrorDomainPOSIX, 42, userInfo
        )
        self.assertIsInstance(err, CoreFoundation.CFErrorRef)
        self.assertResultIsCFRetained(CoreFoundation.CFErrorCopyUserInfo)
        dct = CoreFoundation.CFErrorCopyUserInfo(err)
        self.assertEqual(dct, userInfo)

        keys = ["key1", "key2"]
        values = ["value1", "value2"]

        keys = [Foundation.NSString.stringWithString_(v) for v in keys]
        values = [Foundation.NSString.stringWithString_(v) for v in values]

        self.assertArgHasType(
            CoreFoundation.CFErrorCreateWithUserInfoKeysAndValues, 3, b"n^@"
        )
        self.assertArgSizeInArg(
            CoreFoundation.CFErrorCreateWithUserInfoKeysAndValues, 3, 5
        )
        self.assertArgHasType(
            CoreFoundation.CFErrorCreateWithUserInfoKeysAndValues, 4, b"n^@"
        )
        self.assertArgSizeInArg(
            CoreFoundation.CFErrorCreateWithUserInfoKeysAndValues, 4, 5
        )
        err = CoreFoundation.CFErrorCreateWithUserInfoKeysAndValues(
            None, CoreFoundation.kCFErrorDomainPOSIX, 42, keys, values, 2
        )
        self.assertIsInstance(err, CoreFoundation.CFErrorRef)
        dct = CoreFoundation.CFErrorCopyUserInfo(err)
        self.assertEqual(dct, {"key1": "value1", "key2": "value2"})

    @min_os_level("10.5")
    def testInspection(self):
        userInfo = {
            "foo": "bar",
            CoreFoundation.kCFErrorLocalizedFailureReasonKey: "failure reason",
            CoreFoundation.kCFErrorLocalizedRecoverySuggestionKey: "recovery suggestion",
        }
        self.assertResultIsCFRetained(CoreFoundation.CFErrorCreate)
        err = CoreFoundation.CFErrorCreate(
            None, CoreFoundation.kCFErrorDomainPOSIX, 42, userInfo
        )
        self.assertIsInstance(err, CoreFoundation.CFErrorRef)
        dom = CoreFoundation.CFErrorGetDomain(err)
        self.assertEqual(dom, CoreFoundation.kCFErrorDomainPOSIX)

        code = CoreFoundation.CFErrorGetCode(err)
        self.assertEqual(code, 42)

        self.assertResultIsCFRetained(CoreFoundation.CFErrorCopyDescription)
        v = CoreFoundation.CFErrorCopyDescription(err)
        self.assertIn(
            v,
            (
                "Operation could not be completed. failure reason",
                "The operation couldn%st be completed. failure reason" % (chr(0x2019),),
            ),
        )

        self.assertResultIsCFRetained(CoreFoundation.CFErrorCopyFailureReason)
        v = CoreFoundation.CFErrorCopyFailureReason(err)
        self.assertEqual(v, "failure reason")

        self.assertResultIsCFRetained(CoreFoundation.CFErrorCopyRecoverySuggestion)
        v = CoreFoundation.CFErrorCopyRecoverySuggestion(err)
        self.assertEqual(v, "recovery suggestion")

    @min_os_level("10.5")
    def testConstants(self):
        self.assertIsInstance(CoreFoundation.kCFErrorDomainPOSIX, str)
        self.assertIsInstance(CoreFoundation.kCFErrorDomainOSStatus, str)
        self.assertIsInstance(CoreFoundation.kCFErrorDomainMach, str)
        self.assertIsInstance(CoreFoundation.kCFErrorDomainCocoa, str)
        self.assertIsInstance(CoreFoundation.kCFErrorLocalizedDescriptionKey, str)
        self.assertIsInstance(CoreFoundation.kCFErrorLocalizedFailureReasonKey, str)
        self.assertIsInstance(
            CoreFoundation.kCFErrorLocalizedRecoverySuggestionKey, str
        )
        self.assertIsInstance(CoreFoundation.kCFErrorDescriptionKey, str)
        self.assertIsInstance(CoreFoundation.kCFErrorUnderlyingErrorKey, str)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(CoreFoundation.kCFErrorURLKey, str)
        self.assertIsInstance(CoreFoundation.kCFErrorFilePathKey, str)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(CoreFoundation.kCFErrorLocalizedFailureKey, str)
