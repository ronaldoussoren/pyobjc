from PyObjCTools.TestSupport import *
import objc

from Foundation import *


class TestSubclassing(TestCase):
    def testBasicSubclassing(self):
        class NSObjectSubclass(NSObject):
            def someRandomMethod(self):
                return 42

        subclassClass = NSClassFromString("NSObjectSubclass")

        self.assertIsNot(subclassClass, None, "Failed to subclass NSObject.")

        subclassInstance = subclassClass.new()
        self.assertIsInstance(subclassInstance, subclassClass)
        self.assertIsInstance(subclassInstance, NSObject)
        self.assertNotIsInstance(subclassInstance, NSArray)

        subclassInstance.description()
        self.assertEqual(subclassInstance.someRandomMethod(), 42)

        self.assertIs(subclassInstance, subclassInstance, "Identity check failed.")
        self.assertIs(
            subclassInstance, subclassInstance.self(), "Identity check failed."
        )


if __name__ == "__main__":
    main()
