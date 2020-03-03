import HIServices
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAXUIElement(TestCase):
    def testTypes(self):
        self.assertIsCFType(HIServices.AXUIElementRef)
        self.assertIsCFType(HIServices.AXObserverRef)

    def testFunctions(self):
        self.assertResultIsBOOL(HIServices.AXAPIEnabled)
        self.assertResultIsBOOL(HIServices.AXIsProcessTrusted)

        HIServices.AXMakeProcessTrusted

        self.assertIsInstance(HIServices.AXUIElementGetTypeID(), int)

        self.assertArgIsOut(HIServices.AXUIElementCopyAttributeNames, 1)
        self.assertArgIsCFRetained(HIServices.AXUIElementCopyAttributeNames, 1)

        self.assertArgIsOut(HIServices.AXUIElementCopyAttributeValue, 2)
        self.assertArgIsCFRetained(HIServices.AXUIElementCopyAttributeValue, 2)

        self.assertArgIsOut(HIServices.AXUIElementGetAttributeValueCount, 2)

        self.assertArgIsOut(HIServices.AXUIElementCopyAttributeValues, 4)
        self.assertArgIsCFRetained(HIServices.AXUIElementCopyAttributeValues, 4)

        self.assertArgIsOut(HIServices.AXUIElementIsAttributeSettable, 2)

        HIServices.AXUIElementSetAttributeValue

        self.assertArgIsOut(HIServices.AXUIElementCopyMultipleAttributeValues, 3)
        self.assertArgIsCFRetained(HIServices.AXUIElementCopyMultipleAttributeValues, 3)

        self.assertArgIsOut(HIServices.AXUIElementCopyParameterizedAttributeNames, 1)
        self.assertArgIsCFRetained(
            HIServices.AXUIElementCopyParameterizedAttributeNames, 1
        )

        self.assertArgIsOut(HIServices.AXUIElementCopyParameterizedAttributeValue, 3)
        self.assertArgIsCFRetained(
            HIServices.AXUIElementCopyParameterizedAttributeValue, 3
        )

        self.assertArgIsOut(HIServices.AXUIElementCopyActionNames, 1)
        self.assertArgIsCFRetained(HIServices.AXUIElementCopyActionNames, 1)

        self.assertArgIsOut(HIServices.AXUIElementCopyActionDescription, 2)
        self.assertArgIsCFRetained(HIServices.AXUIElementCopyActionDescription, 2)

        HIServices.AXUIElementPerformAction

        self.assertArgIsOut(HIServices.AXUIElementCopyElementAtPosition, 3)
        self.assertArgIsCFRetained(HIServices.AXUIElementCopyElementAtPosition, 3)

        self.assertResultIsCFRetained(HIServices.AXUIElementCreateApplication)
        self.assertResultIsCFRetained(HIServices.AXUIElementCreateSystemWide)

        self.assertArgIsOut(HIServices.AXUIElementGetPid, 1)

        HIServices.AXUIElementSetMessagingTimeout

        self.assertArgIsBOOL(HIServices.AXUIElementPostKeyboardEvent, 3)

        AXObserverCallback = b"v^{__AXObserver=}^{__AXUIElement=}^{__CFString=}^v"
        # AXObserverCallbackWithInfo = (
        #     b"v^{__AXObserver=}^{__AXUIElement=}^{__CFString=}^{__CFDictionary=}^v"
        # )

        self.assertIsInstance(HIServices.AXObserverGetTypeID(), int)

        self.assertArgIsFunction(
            HIServices.AXObserverCreate, 1, AXObserverCallback, True
        )
        self.assertArgIsOut(HIServices.AXObserverCreate, 2)
        self.assertArgIsCFRetained(HIServices.AXObserverCreate, 2)

        HIServices.AXObserverAddNotification
        HIServices.AXObserverRemoveNotification

        self.assertResultIsNotCFRetained(HIServices.AXObserverGetRunLoopSource)

    @min_os_level("10.9")
    def testFunctions10_9(self):
        AXObserverCallbackWithInfo = (
            b"v^{__AXObserver=}^{__AXUIElement=}^{__CFString=}^{__CFDictionary=}^v"
        )

        self.assertResultIsBOOL(HIServices.AXIsProcessTrustedWithOptions)

        self.assertArgIsFunction(
            HIServices.AXObserverCreateWithInfoCallback,
            1,
            AXObserverCallbackWithInfo,
            True,
        )
        self.assertArgIsOut(HIServices.AXObserverCreateWithInfoCallback, 2)
        self.assertArgIsCFRetained(HIServices.AXObserverCreateWithInfoCallback, 2)

    def testConstants(self):
        self.assertEqual(HIServices.kAXCopyMultipleAttributeOptionStopOnError, 1)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(HIServices.kAXTrustedCheckOptionPrompt, str)
