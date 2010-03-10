from PyObjCTools.TestSupport import *
import objc


class TestHiddenSelector (TestCase):
    def testHiddenInClassDef(self):
        self.fail("todo")

        # define method in a class definition
        # and make the method read only (while
        # still in the class body). Check that
        # the method is not present in the class
        # __dict__, but is callable.
        #
        # (Callable means through pyobjc_instanceMethods,
        # not directly)

    def testHiddenAddMethods(self):
        self.fail("todo")

        # Add a hidden selector using objc.classAddMethods
        # and check that the selector is callable but not
        # present in the class __dict__
        #
        # (Callable means through pyobjc_instanceMethods,
        # not directly)

    def testHiddenInSetupHook(self):
        self.fail("todo")

        # Use a helper class with a __pyobjc_class_setup__ 
        # hook to insert hidden selectors in the class 
        # dict and/or the instance and class methods lists,
        # check that this behaves correctly.

    def testHiddenClassMethods(self):
        self.fail("todo")

        # Same as testHiddenAddMethods, testHiddenInSetupHook 
        # and testHiddenInClassDef, but now using a class method.

if __name__ == "__main__":
    main()
