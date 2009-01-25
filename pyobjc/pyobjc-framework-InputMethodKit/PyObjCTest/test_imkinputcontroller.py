
from PyObjCTools.TestSupport import *
from InputMethodKit import *

class TestIMKInputControllerHelper (NSObject):
    def inputText_key_modifiers_client_(self, s, k, m, snd):
        return True

    def inputText_client_(self, s, snd):
        return True

    def handleEvent_client_(self, s, snd):
        return True

    def didCommandBySelector_client_(self, s, snd):
        return False

    # IMKMouseHandling

    def mouseDownOnCharacterIndex_coordinate_withModifier_continueTracking_client_(self,
            v1, v2, v3, v4, v5):
        return True

    def mouseUpOnCharacterIndex_coordinate_withModifier_client_(self,
            v1, v2, v3, v4):
        return True

    def mouseMovedOnCharacterIndex_coordinate_withModifier_client_(self,
            v1, v2, v3, v4):
        return True






class TestIMKInputController (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(kIMKCommandMenuItemName, unicode)
        self.failUnlessIsInstance(kIMKCommandClientName, unicode)

    def testProtocols(self):
        self.failUnlessIsInstance(protocols.IMKServerInput, objc.informal_protocol)

        self.failUnlessResultIsBOOL(TestIMKInputControllerHelper.inputText_key_modifiers_client_)
        self.failUnlessArgHasType(TestIMKInputControllerHelper.inputText_key_modifiers_client_, 1, objc._C_NSInteger)

        self.failUnlessResultIsBOOL(TestIMKInputControllerHelper.inputText_client_)
        self.failUnlessResultIsBOOL(TestIMKInputControllerHelper.handleEvent_client_)
        self.failUnlessResultIsBOOL(TestIMKInputControllerHelper.didCommandBySelector_client_)
        self.failUnlessArgHasType(TestIMKInputControllerHelper.didCommandBySelector_client_, 0, objc._C_SEL)


    def testIMKMouseHandling(self):
        self.failUnlessResultIsBOOL(TestIMKInputControllerHelper.mouseDownOnCharacterIndex_coordinate_withModifier_continueTracking_client_)
        self.failUnlessArgHasType(TestIMKInputControllerHelper.mouseDownOnCharacterIndex_coordinate_withModifier_continueTracking_client_, 0, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestIMKInputControllerHelper.mouseDownOnCharacterIndex_coordinate_withModifier_continueTracking_client_, 1, NSPoint.__typestr__)
        self.failUnlessArgHasType(TestIMKInputControllerHelper.mouseDownOnCharacterIndex_coordinate_withModifier_continueTracking_client_, 2, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestIMKInputControllerHelper.mouseDownOnCharacterIndex_coordinate_withModifier_continueTracking_client_, 3, objc._C_OUT+objc._C_PTR+objc._C_NSBOOL)

        self.failUnlessResultIsBOOL(TestIMKInputControllerHelper.mouseUpOnCharacterIndex_coordinate_withModifier_client_)
        self.failUnlessArgHasType(TestIMKInputControllerHelper.mouseUpOnCharacterIndex_coordinate_withModifier_client_, 0, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestIMKInputControllerHelper.mouseUpOnCharacterIndex_coordinate_withModifier_client_, 1, NSPoint.__typestr__)
        self.failUnlessArgHasType(TestIMKInputControllerHelper.mouseUpOnCharacterIndex_coordinate_withModifier_client_, 2, objc._C_NSUInteger)

        self.failUnlessResultIsBOOL(TestIMKInputControllerHelper.mouseMovedOnCharacterIndex_coordinate_withModifier_client_)
        self.failUnlessArgHasType(TestIMKInputControllerHelper.mouseMovedOnCharacterIndex_coordinate_withModifier_client_, 0, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestIMKInputControllerHelper.mouseMovedOnCharacterIndex_coordinate_withModifier_client_, 1, NSPoint.__typestr__)
        self.failUnlessArgHasType(TestIMKInputControllerHelper.mouseMovedOnCharacterIndex_coordinate_withModifier_client_, 2, objc._C_NSUInteger)

        

if __name__ == "__main__":
    main()
