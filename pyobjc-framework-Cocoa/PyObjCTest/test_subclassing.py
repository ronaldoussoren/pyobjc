import Foundation
from PyObjCTools.TestSupport import TestCase


class TestSubclassing(TestCase):
    def testBasicSubclassing(self):
        class NSObjectSubclass(Foundation.NSObject):
            def someRandomMethod(self):
                return 42

        subclassClass = Foundation.NSClassFromString("NSObjectSubclass")

        self.assertIsNot(subclassClass, None, "Failed to subclass NSObject.")

        subclassInstance = subclassClass.new()
        self.assertIsInstance(subclassInstance, subclassClass)
        self.assertIsInstance(subclassInstance, Foundation.NSObject)
        self.assertNotIsInstance(subclassInstance, Foundation.NSArray)

        subclassInstance.description()
        self.assertEqual(subclassInstance.someRandomMethod(), 42)

        self.assertIs(subclassInstance, subclassInstance, "Identity check failed.")
        self.assertIs(
            subclassInstance, subclassInstance.self(), "Identity check failed."
        )
