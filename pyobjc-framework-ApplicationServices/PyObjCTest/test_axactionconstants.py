import HIServices
from PyObjCTools.TestSupport import *

class TestAXActionConstants (TestCase):
    def testConstants(self):
        self.assertEqual(HIServices.kAXPressAction, "AXPress")
        self.assertEqual(HIServices.kAXIncrementAction, "AXIncrement")
        self.assertEqual(HIServices.kAXDecrementAction, "AXDecrement")
        self.assertEqual(HIServices.kAXConfirmAction, "AXConfirm")
        self.assertEqual(HIServices.kAXCancelAction, "AXCancel")
        self.assertEqual(HIServices.kAXShowAlternateUIAction, "AXShowAlternateUI")
        self.assertEqual(HIServices.kAXShowDefaultUIAction, "AXShowDefaultUI")
        self.assertEqual(HIServices.kAXRaiseAction, "AXRaise")
        self.assertEqual(HIServices.kAXShowMenuAction, "AXShowMenu")
        self.assertEqual(HIServices.kAXPickAction, "AXPick")

if __name__ == "__main__":
    main()
