# NOTE: This file only contains basic tests of the keyvalue coding header definitions,
# test_keyvalue contains tests for the actualy KVC/KVO mechanisms.
from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSKeyValueCoding (TestCase):
    def testConstants(self):
        self.failUnless(isinstance(NSUndefinedKeyException, unicode))
        self.failUnless(isinstance(NSAverageKeyValueOperator, unicode))
        self.failUnless(isinstance(NSCountKeyValueOperator, unicode))
        self.failUnless(isinstance(NSDistinctUnionOfArraysKeyValueOperator, unicode))
        self.failUnless(isinstance(NSDistinctUnionOfObjectsKeyValueOperator, unicode))
        self.failUnless(isinstance(NSDistinctUnionOfSetsKeyValueOperator, unicode))
        self.failUnless(isinstance(NSMaximumKeyValueOperator, unicode))
        self.failUnless(isinstance(NSMinimumKeyValueOperator, unicode))
        self.failUnless(isinstance(NSSumKeyValueOperator, unicode))
        self.failUnless(isinstance(NSUnionOfArraysKeyValueOperator, unicode))
        self.failUnless(isinstance(NSUnionOfObjectsKeyValueOperator, unicode))
        self.failUnless(isinstance(NSUnionOfSetsKeyValueOperator, unicode))

    def testDefineValidation(self):
        o = NSObject.alloc().init()

        m = o.validateValue_forKey_error_.__metadata__()
        self.assertEquals(  m['arguments'][4]['type'], 'o^@' )

        m = o.validateValue_forKeyPath_error_.__metadata__()
        self.assertEquals(  m['arguments'][4]['type'], 'o^@' )

    

if __name__ == "__main__":
    main()
