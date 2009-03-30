from Foundation import *
from PyObjCTools.TestSupport import *


class TestNSScriptKeyValueCodingHelper (NSObject):
    def insertValue_atIndex_inPropertyWithKey_(self, a, b, c): pass
    def removeValueAtIndex_fromPropertyWithKey_(self, a, b): pass
    def replaceValueAtIndex_inPropertyWithKey_withValue_(self, a, b, c): pass


class TestNSScriptKeyValueCoding (TestCase):
    def testMethods(self):
        self.failUnlessArgHasType(TestNSScriptKeyValueCodingHelper.insertValue_atIndex_inPropertyWithKey_, 1, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestNSScriptKeyValueCodingHelper.removeValueAtIndex_fromPropertyWithKey_, 0, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestNSScriptKeyValueCodingHelper.replaceValueAtIndex_inPropertyWithKey_withValue_, 0, objc._C_NSUInteger)

if __name__ == "__main__":
    main()
