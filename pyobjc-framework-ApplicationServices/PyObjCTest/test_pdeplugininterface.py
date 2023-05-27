import PrintCore
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestPDEPluginInterfaceHelper(PrintCore.NSObject):
    def initWithBundle_(self, value):
        return 1

    def shouldHide(self):
        return 1

    def saveValuesAndReturnError_(self, value):
        return (1, None)

    def restoreValuesAndReturnError_(self, value):
        return (1, None)

    def shouldShowHelp(self):
        return 1

    def shouldPrint(self):
        return 1

    def printWindowWillClose_(self, value):
        pass

    def willChangePPDOptionKeyValue_ppdChoice_(self, a, b):
        return 1


class TestPDEPluginInterface(TestCase):
    @min_sdk_level("13.0")
    def test_protocols(self):
        self.assertProtocolExists("PDEPlugIn")
        self.assertProtocolExists("PDEPanel")
        self.assertProtocolExists("PDEPlugInCallbackProtocol")

    def testMethods(self):
        self.assertResultIsBOOL(TestPDEPluginInterfaceHelper.shouldHide)
        self.assertResultIsBOOL(TestPDEPluginInterfaceHelper.saveValuesAndReturnError_)
        self.assertArgIsOut(TestPDEPluginInterfaceHelper.saveValuesAndReturnError_, 0)
        self.assertResultIsBOOL(
            TestPDEPluginInterfaceHelper.restoreValuesAndReturnError_
        )
        self.assertArgIsOut(
            TestPDEPluginInterfaceHelper.restoreValuesAndReturnError_, 0
        )
        self.assertResultIsBOOL(TestPDEPluginInterfaceHelper.shouldShowHelp)
        self.assertResultIsBOOL(TestPDEPluginInterfaceHelper.shouldPrint)
        self.assertArgIsBOOL(TestPDEPluginInterfaceHelper.printWindowWillClose_, 0)
        self.assertResultIsBOOL(
            TestPDEPluginInterfaceHelper.willChangePPDOptionKeyValue_ppdChoice_
        )
