import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSValue(TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(Foundation.NSNumber.numberWithBool_, 0)
        self.assertArgIsBOOL(Foundation.NSNumber.initWithBool_, 0)
        self.assertResultIsBOOL(Foundation.NSNumber.boolValue)
        self.assertResultIsBOOL(Foundation.NSNumber.isEqualToNumber_)

        self.assertResultIsBOOL(Foundation.NSValue.isEqualToValue_)

        self.assertArgIsIn(Foundation.NSValue.initWithBytes_objCType_, 0)
        self.assertArgIsVariableSize(Foundation.NSValue.initWithBytes_objCType_, 0)
        self.assertArgHasType(Foundation.NSValue.initWithBytes_objCType_, 1, b"n^t")
        self.assertArgIsNullTerminated(Foundation.NSValue.initWithBytes_objCType_, 1)

        self.assertArgIsIn(Foundation.NSValue.valueWithBytes_objCType_, 0)
        self.assertArgIsVariableSize(Foundation.NSValue.valueWithBytes_objCType_, 0)
        self.assertArgHasType(Foundation.NSValue.valueWithBytes_objCType_, 1, b"n^t")
        self.assertArgIsNullTerminated(Foundation.NSValue.valueWithBytes_objCType_, 1)

        self.assertArgIsIn(Foundation.NSValue.value_withObjCType_, 0)
        self.assertArgIsVariableSize(Foundation.NSValue.value_withObjCType_, 0)
        self.assertArgHasType(Foundation.NSValue.value_withObjCType_, 1, b"n^t")
        self.assertArgIsNullTerminated(Foundation.NSValue.value_withObjCType_, 1)

        self.assertResultIsNullTerminated(Foundation.NSValue.objCType)
        self.assertResultHasType(Foundation.NSValue.objCType, b"^t")
