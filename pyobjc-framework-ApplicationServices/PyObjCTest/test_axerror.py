import HIServices
from PyObjCTools.TestSupport import *

class TestAXActionConstants (TestCase):
    def testConstants(self):
        self.assertEqual(HIServices.kAXErrorSuccess, 0)
        self.assertEqual(HIServices.kAXErrorFailure, -25200)
        self.assertEqual(HIServices.kAXErrorIllegalArgument, -25201)
        self.assertEqual(HIServices.kAXErrorInvalidUIElement, -25202)
        self.assertEqual(HIServices.kAXErrorInvalidUIElementObserver, -25203)
        self.assertEqual(HIServices.kAXErrorCannotComplete, -25204)
        self.assertEqual(HIServices.kAXErrorAttributeUnsupported, -25205)
        self.assertEqual(HIServices.kAXErrorActionUnsupported, -25206)
        self.assertEqual(HIServices.kAXErrorNotificationUnsupported, -25207)
        self.assertEqual(HIServices.kAXErrorNotImplemented, -25208)
        self.assertEqual(HIServices.kAXErrorNotificationAlreadyRegistered, -25209)
        self.assertEqual(HIServices.kAXErrorNotificationNotRegistered, -25210)
        self.assertEqual(HIServices.kAXErrorAPIDisabled, -25211)
        self.assertEqual(HIServices.kAXErrorNoValue, -25212)
        self.assertEqual(HIServices.kAXErrorParameterizedAttributeUnsupported, -25213)
        self.assertEqual(HIServices.kAXErrorNotEnoughPrecision, -25214)

if __name__ == "__main__":
    main()
