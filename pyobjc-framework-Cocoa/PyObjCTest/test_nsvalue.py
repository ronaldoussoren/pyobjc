from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSValue (TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(NSNumber.numberWithBool_, 0)
        self.assertArgIsBOOL(NSNumber.initWithBool_, 0)
        self.assertResultIsBOOL(NSNumber.boolValue)
        self.assertResultIsBOOL(NSNumber.isEqualToNumber_)

        self.assertResultIsBOOL(NSValue.isEqualToValue_)

        self.assertArgIsIn(NSValue.initWithBytes_objCType_, 0)
        self.assertArgIsVariableSize(NSValue.initWithBytes_objCType_, 0)
        self.assertArgHasType(NSValue.initWithBytes_objCType_, 1, b'n^t')
        self.assertArgIsNullTerminated(NSValue.initWithBytes_objCType_, 1)

        self.assertArgIsIn(NSValue.valueWithBytes_objCType_, 0)
        self.assertArgIsVariableSize(NSValue.valueWithBytes_objCType_, 0)
        self.assertArgHasType(NSValue.valueWithBytes_objCType_, 1, b'n^t')
        self.assertArgIsNullTerminated(NSValue.valueWithBytes_objCType_, 1)

        self.assertArgIsIn(NSValue.value_withObjCType_, 0)
        self.assertArgIsVariableSize(NSValue.value_withObjCType_, 0)
        self.assertArgHasType(NSValue.value_withObjCType_, 1, b'n^t')
        self.assertArgIsNullTerminated(NSValue.value_withObjCType_, 1)

        self.assertResultIsNullTerminated(NSValue.objCType)
        self.assertResultHasType(NSValue.objCType, b'^t')

if __name__ == "__main__":
    main()
