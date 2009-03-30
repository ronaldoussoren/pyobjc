from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSValue (TestCase):
    def testMethods(self):
        self.failUnlessArgIsBOOL(NSNumber.numberWithBool_, 0)
        self.failUnlessArgIsBOOL(NSNumber.initWithBool_, 0)
        self.failUnlessResultIsBOOL(NSNumber.boolValue)
        self.failUnlessResultIsBOOL(NSNumber.isEqualToNumber_)

        self.failUnlessResultIsBOOL(NSValue.isEqualToValue_)

        self.failUnlessArgIsIn(NSValue.initWithBytes_objCType_, 0)
        self.failUnlessArgIsVariableSize(NSValue.initWithBytes_objCType_, 0)
        self.failUnlessArgHasType(NSValue.initWithBytes_objCType_, 1, 'n^t')
        self.failUnlessArgIsNullTerminated(NSValue.initWithBytes_objCType_, 1)

        self.failUnlessArgIsIn(NSValue.valueWithBytes_objCType_, 0)
        self.failUnlessArgIsVariableSize(NSValue.valueWithBytes_objCType_, 0)
        self.failUnlessArgHasType(NSValue.valueWithBytes_objCType_, 1, 'n^t')
        self.failUnlessArgIsNullTerminated(NSValue.valueWithBytes_objCType_, 1)

        self.failUnlessArgIsIn(NSValue.value_withObjCType_, 0)
        self.failUnlessArgIsVariableSize(NSValue.value_withObjCType_, 0)
        self.failUnlessArgHasType(NSValue.value_withObjCType_, 1, 'n^t')
        self.failUnlessArgIsNullTerminated(NSValue.value_withObjCType_, 1)

        self.failUnlessResultIsNullTerminated(NSValue.objCType)
        self.failUnlessResultHasType(NSValue.objCType, '^t')

if __name__ == "__main__":
    main()
