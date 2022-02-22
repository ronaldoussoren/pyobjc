# NOTE: This file only contains basic tests of the keyvalue coding header definitions,
# test_keyvalue contains tests for the actualy KVC/KVO mechanisms.
import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSKeyValueCodingHelper(Foundation.NSObject):
    def validateValue_forKey_error_(self, a, b, c):
        return 1

    def validateValue_forKeyPath_error_(self, a, b, c):
        return 1

    def useStoredAccessor(self):
        return 1


class TestNSKeyValueCoding(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(Foundation.NSKeyValueOperator, str)

    def testConstants(self):
        self.assertIsInstance(Foundation.NSUndefinedKeyException, str)
        self.assertIsInstance(Foundation.NSAverageKeyValueOperator, str)
        self.assertIsInstance(Foundation.NSCountKeyValueOperator, str)
        self.assertIsInstance(Foundation.NSDistinctUnionOfArraysKeyValueOperator, str)
        self.assertIsInstance(Foundation.NSDistinctUnionOfObjectsKeyValueOperator, str)
        self.assertIsInstance(Foundation.NSDistinctUnionOfSetsKeyValueOperator, str)
        self.assertIsInstance(Foundation.NSMaximumKeyValueOperator, str)
        self.assertIsInstance(Foundation.NSMinimumKeyValueOperator, str)
        self.assertIsInstance(Foundation.NSSumKeyValueOperator, str)
        self.assertIsInstance(Foundation.NSUnionOfArraysKeyValueOperator, str)
        self.assertIsInstance(Foundation.NSUnionOfObjectsKeyValueOperator, str)
        self.assertIsInstance(Foundation.NSUnionOfSetsKeyValueOperator, str)

    def testDefineValidation(self):
        o = Foundation.NSObject.alloc().init()

        m = o.validateValue_forKey_error_.__metadata__()
        self.assertEqual(m["arguments"][4]["type"], b"o^@")

        m = o.validateValue_forKeyPath_error_.__metadata__()
        self.assertEqual(m["arguments"][4]["type"], b"o^@")

    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSObject.accessInstanceVariablesDirectly)

        self.assertResultIsBOOL(TestNSKeyValueCodingHelper.validateValue_forKey_error_)
        self.assertArgIsOut(TestNSKeyValueCodingHelper.validateValue_forKey_error_, 2)
        self.assertResultIsBOOL(
            TestNSKeyValueCodingHelper.validateValue_forKeyPath_error_
        )

        self.assertArgIsInOut(
            TestNSKeyValueCodingHelper.validateValue_forKeyPath_error_, 0
        )
        self.assertArgIsOut(
            TestNSKeyValueCodingHelper.validateValue_forKeyPath_error_, 2
        )
        self.assertResultIsBOOL(TestNSKeyValueCodingHelper.useStoredAccessor)
