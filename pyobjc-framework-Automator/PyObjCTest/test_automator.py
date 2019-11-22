"""
Some simple tests to check that the framework is properly wrapped.
"""
import objc
from PyObjCTools.TestSupport import *
import Automator


class TestAutomator(TestCase):
    def testClasses(self):
        self.assertHasAttr(Automator, "AMAction")
        self.assertIsInstance(Automator.AMAction, objc.objc_class)

        self.assertHasAttr(Automator, "AMAppleScriptAction")
        self.assertIsInstance(Automator.AMAppleScriptAction, objc.objc_class)

    def testInformalProtocols(self):
        self.assertNotHasAttr(Automator, "protocols")


if __name__ == "__main__":
    main()
