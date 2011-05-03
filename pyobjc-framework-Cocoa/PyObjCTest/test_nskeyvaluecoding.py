# NOTE: This file only contains basic tests of the keyvalue coding header definitions,
# test_keyvalue contains tests for the actualy KVC/KVO mechanisms.
from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSKeyValueCodingHelper (NSObject):
    def validateValue_forKey_error_(self, a, b, c): return 1
    def validateValue_forKeyPath_error_(self, a, b, c): return 1
    def useStoredAccessor(self): return 1


class TestNSKeyValueCoding (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSUndefinedKeyException, unicode)
        self.assertIsInstance(NSAverageKeyValueOperator, unicode)
        self.assertIsInstance(NSCountKeyValueOperator, unicode)
        self.assertIsInstance(NSDistinctUnionOfArraysKeyValueOperator, unicode)
        self.assertIsInstance(NSDistinctUnionOfObjectsKeyValueOperator, unicode)
        self.assertIsInstance(NSDistinctUnionOfSetsKeyValueOperator, unicode)
        self.assertIsInstance(NSMaximumKeyValueOperator, unicode)
        self.assertIsInstance(NSMinimumKeyValueOperator, unicode)
        self.assertIsInstance(NSSumKeyValueOperator, unicode)
        self.assertIsInstance(NSUnionOfArraysKeyValueOperator, unicode)
        self.assertIsInstance(NSUnionOfObjectsKeyValueOperator, unicode)
        self.assertIsInstance(NSUnionOfSetsKeyValueOperator, unicode)
    def testDefineValidation(self):
        o = NSObject.alloc().init()

        m = o.validateValue_forKey_error_.__metadata__()
        self.assertEqual(  m['arguments'][4]['type'], b'o^@' )

        m = o.validateValue_forKeyPath_error_.__metadata__()
        self.assertEqual(  m['arguments'][4]['type'], b'o^@' )

   
    def testMethods(self):
        self.assertResultIsBOOL(NSObject.accessInstanceVariablesDirectly)

        self.assertResultIsBOOL(TestNSKeyValueCodingHelper.validateValue_forKey_error_)
        self.assertArgIsOut(TestNSKeyValueCodingHelper.validateValue_forKey_error_, 2)
        self.assertResultIsBOOL(TestNSKeyValueCodingHelper.validateValue_forKeyPath_error_)
        self.assertArgIsOut(TestNSKeyValueCodingHelper.validateValue_forKeyPath_error_, 2)
        self.assertResultIsBOOL(TestNSKeyValueCodingHelper.useStoredAccessor)

if __name__ == "__main__":
    main()
