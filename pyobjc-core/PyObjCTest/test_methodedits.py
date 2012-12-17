# FIXME: This test suite seems to polute it's environment, other tests fail
# when this test suite is active!
from __future__ import unicode_literals
from PyObjCTools.TestSupport import *
import sys

from PyObjCTools.TestSupport import onlyPython2

import objc

NSObject = objc.lookUpClass('NSObject')

class MEClass(NSObject):
    pass

preEverythingInstance = MEClass.new()

class Methods(NSObject):
    def description(self):
        return "<methods>"

    def newMethod(self):
        return "<new-method>"

class MethodsSub(NSObject):
    def description(self):
        return "<sub-methods>"

    def newMethod(self):
        return "<sub-new-method>"

    def newSubMethod(self):
        return "<new-method-sub>"

class PurePython:
    def description(self):
        return "<pure>"

    def newMethod(self):
        return "<pure-new>"

    def purePythonMethod(self):
        return "<pure-py>"

class TestFromObjCSuperToObjCClass(TestCase):
    def testClassAddMethod(self):
        import objc._category as mod

        orig_classAddMethods = mod.classAddMethods
        try:
            l = []
            def classAddMethods(cls, values):
                self.assertIsInstance(cls, objc.objc_class)
                for item in values:
                    self.assertIsInstance(item, objc.selector)
                l.append((cls, values))

            mod.classAddMethods = classAddMethods

            def my_python_description(self):
                return "foo the bar"

            objc.classAddMethod(NSObject, b"python_description", my_python_description)
            self.assertEqual(len(l), 1)
            self.assertIs(l[0][0], NSObject)
            self.assertEqual(len(l[0][1]), 1)
            m = l[0][1][0]
            self.assertIsInstance(m, objc.selector)
            self.assertIs(m.callable, my_python_description)
            self.assertEqual(m.selector, b"python_description")
            self.assertEqual(m.signature, b"@@:")

            @objc.typedSelector(b"q@:")
            def myAction(self):
                return 1

            l[:] = []
            objc.classAddMethod(NSObject, b"value",  myAction)
            self.assertIs(l[0][0], NSObject)
            self.assertEqual(len(l[0][1]), 1)
            m = l[0][1][0]
            self.assertIsInstance(m, objc.selector)
            self.assertIs(m.callable, myAction.callable)
            self.assertEqual(m.selector, b"value")
            self.assertEqual(m.signature, b"q@:")


            # Cannot add native selectors:
            self.assertRaises(AttributeError, objc.classAddMethod, NSObject, b"descriptionAlias", NSObject.description)

        finally:
            mod.classAddMethods = orig_classAddMethods


    def testBasicBehavior(self):
        anInstance = Methods.new()
        self.assertEqual(anInstance.description(), "<methods>")
        self.assertEqual(anInstance.newMethod(), "<new-method>")

    def testDescriptionOverride(self):
        objc.classAddMethods(MEClass, [Methods.pyobjc_instanceMethods.description])

        self.assertTrue(MEClass.instancesRespondToSelector_("description"))

        newInstance = MEClass.new()

        self.assertEqual(newInstance.description(), "<methods>")
        self.assertEqual(preEverythingInstance.description(), "<methods>")

    def testNewMethod(self):
        objc.classAddMethods(MEClass, [Methods.pyobjc_instanceMethods.newMethod])

        self.assertTrue(MEClass.instancesRespondToSelector_("newMethod"))

        newInstance = MEClass.new()

        self.assertEqual(newInstance.newMethod(), "<new-method>")
        self.assertEqual(preEverythingInstance.newMethod(), "<new-method>")

    def testSubDescriptionOverride(self):
        objc.classAddMethods(MEClass, [MethodsSub.pyobjc_instanceMethods.description])

        self.assertTrue(MEClass.instancesRespondToSelector_("description"))

        newInstance = MEClass.new()

        self.assertEqual(newInstance.description(), "<sub-methods>")
        self.assertEqual(preEverythingInstance.description(), "<sub-methods>")

    def testSubNewMethod(self):
        objc.classAddMethods(MEClass, [MethodsSub.newMethod, MethodsSub.newSubMethod])

        self.assertTrue(MEClass.instancesRespondToSelector_("newMethod"))
        self.assertTrue(MEClass.instancesRespondToSelector_("newSubMethod"))

        newInstance = MEClass.new()

        self.assertEqual(newInstance.newMethod(), "<sub-new-method>")
        self.assertEqual(preEverythingInstance.newMethod(), "<sub-new-method>")
        self.assertEqual(newInstance.newSubMethod(), "<new-method-sub>")
        self.assertEqual(preEverythingInstance.newSubMethod(), "<new-method-sub>")

    def testNewClassMethod(self):

        def aNewClassMethod(cls):
            return "Foo cls"
        aNewClassMethod = classmethod(aNewClassMethod)

        self.assertTrue(not MEClass.pyobjc_classMethods.respondsToSelector_("aNewClassMethod"))
        objc.classAddMethods(MEClass, [aNewClassMethod])
        self.assertTrue(MEClass.pyobjc_classMethods.respondsToSelector_("aNewClassMethod"))

        self.assertTrue(MEClass.aNewClassMethod.isClassMethod)
        self.assertEqual(MEClass.aNewClassMethod(), 'Foo cls')

    def testAddedMethodType(self):
        def anotherNewClassMethod(cls):
            "CLS DOC STRING"
            return "BAR CLS"
        anotherNewClassMethod = classmethod(anotherNewClassMethod)

        def anotherNewMethod(self):
            "INST DOC STRING"
            return "BAR SELF"

        self.assertTrue(not MEClass.pyobjc_classMethods.respondsToSelector_("anotherNewClassMethod"))
        self.assertTrue(not MEClass.pyobjc_classMethods.instancesRespondToSelector_("anotherNewMethod"))

        objc.classAddMethods(MEClass, [anotherNewClassMethod, anotherNewMethod])
        self.assertTrue(MEClass.pyobjc_classMethods.respondsToSelector_("anotherNewClassMethod"))
        self.assertTrue(MEClass.pyobjc_classMethods.instancesRespondToSelector_("anotherNewMethod"))

        self.assertEqual(MEClass.anotherNewClassMethod.__doc__, "CLS DOC STRING")
        self.assertEqual(MEClass.anotherNewMethod.__doc__, "INST DOC STRING")




class TestFromPythonClassToObjCClass(TestCase):

    @onlyPython2
    def testPythonSourcedMethods(self):
        # 20031227, Ronald: Assigning the methods works alright, but actually
        # using them won't because the new methods are actually still methods
        # of a different class and will therefore complain about the type
        # of 'self'.
        objc.classAddMethods(MEClass, [PurePython.description,
                                                  PurePython.newMethod,
                                                  PurePython.purePythonMethod])


        self.assertTrue(MEClass.instancesRespondToSelector_("description"))
        self.assertTrue(MEClass.instancesRespondToSelector_("newMethod"))
        self.assertTrue(MEClass.instancesRespondToSelector_("purePythonMethod"))

        newInstance = MEClass.new()

        # This is bogus, see above:
        #self.assertEqual(newInstance.description(), "<pure>")
        #self.assertEqual(newInstance.newMethod(), "<pure-new>")
        #self.assertEqual(newInstance.purePythonMethod(), "<pure-py>")

        #self.assertEqual(preEverythingInstance.description(), "<pure>")
        #self.assertEqual(preEverythingInstance.newMethod(), "<pure-new>")
        #self.assertEqual(preEverythingInstance.purePythonMethod(), "<pure-py>")

        self.assertRaises(TypeError, newInstance.description)
        self.assertRaises(TypeError, newInstance.newMethod)
        self.assertRaises(TypeError, newInstance.purePythonMethod)
        self.assertRaises(TypeError, preEverythingInstance.description)
        self.assertRaises(TypeError, preEverythingInstance.newMethod)
        self.assertRaises(TypeError, preEverythingInstance.purePythonMethod)

    def testPythonSourcedFunctions(self):
        # Same as testPythonSourcedMethods, but using function objects instead
        # of method objects.


        if sys.version_info[0] == 2:
            objc.classAddMethods(MEClass, [
                PurePython.description.im_func,
                PurePython.newMethod.im_func,
                PurePython.purePythonMethod.im_func,
            ])
        else:
            objc.classAddMethods(MEClass, [
                PurePython.description,
                PurePython.newMethod,
                PurePython.purePythonMethod,
            ])

        self.assertTrue(MEClass.instancesRespondToSelector_("description"))
        self.assertTrue(MEClass.instancesRespondToSelector_("newMethod"))
        self.assertTrue(MEClass.instancesRespondToSelector_("purePythonMethod"))

        newInstance = MEClass.new()

        self.assertEqual(newInstance.description(), "<pure>")
        self.assertEqual(newInstance.newMethod(), "<pure-new>")
        self.assertEqual(newInstance.purePythonMethod(), "<pure-py>")

        self.assertEqual(preEverythingInstance.description(), "<pure>")
        self.assertEqual(preEverythingInstance.newMethod(), "<pure-new>")
        self.assertEqual(preEverythingInstance.purePythonMethod(), "<pure-py>")



class TestClassAsignments (TestCase):
    def testAssignAMethod(self):
        MEClass.doSomethingElse = lambda self: 2*2
        MEClass.doDuplicate_ = lambda self, x: 2*x

        self.assertTrue(MEClass.instancesRespondToSelector_("doSomethingElse"))
        self.assertTrue(MEClass.instancesRespondToSelector_("doDuplicate:"))

        o = MEClass.alloc().init()

        self.assertEqual(4, o.doSomethingElse())
        self.assertEqual(8, o.doDuplicate_(4))

    def testAssignAClassMethod(self):
        MEClass.classSomethingElse = classmethod(lambda self: 2*2)
        MEClass.classDuplicate_ = classmethod(lambda self, x: 2*x)

        self.assertTrue(MEClass.pyobjc_classMethods.respondsToSelector_(b"classSomethingElse"))
        self.assertTrue(MEClass.pyobjc_classMethods.respondsToSelector_(b"classDuplicate:"))

        self.assertEqual(4, MEClass.classSomethingElse())
        self.assertEqual(8, MEClass.classDuplicate_(4))

    def testAssignFuzzyMethod(self):
        self.assertRaises((ValueError, TypeError), setattr, MEClass, 'fuzzyMethod', objc.selector(None, selector=b'fuzzy', signature=b'@@:'))

    def testRemovingMethods(self):
        theClass = NSObject

        self.assertRaises(AttributeError, delattr, theClass, 'alloc')
        self.assertRaises(AttributeError, delattr, theClass, 'init')

class TestCategory (TestCase):
    # Tests of objc.Category

    def testPyClassCategory(self):
        global Methods

        o = Methods.alloc().init()
        self.assertRaises(AttributeError, getattr, o, 'categoryMethod')

        class Methods (objc.Category(Methods)):
            def categoryMethod(self):
                return True

            def categoryMethod2(self):
                return False

            def anotherClassMethod(self):
                return "hello"
            anotherClassMethod = classmethod(anotherClassMethod)

        self.assertTrue(o.categoryMethod())
        self.assertTrue(not o.categoryMethod2())
        self.assertEqual(Methods.anotherClassMethod(), "hello")

    def testNoInstanceVariables(self):
        global Methods

        try:
            class Methods(objc.Category(Methods)):
                outlet = objc.IBOutlet()

        except TypeError:
            pass

        else:
            self.fail("Can add instance variable in a category")

    def testObjCClassCategory(self):
        NSObject = objc.lookUpClass('NSObject')

        o = NSObject.alloc().init()
        self.assertRaises(AttributeError, getattr, o, 'myCategoryMethod')

        class NSObject (objc.Category(NSObject)):
            def myCategoryMethod(self):
                return True

            def myCategoryMethod2(self):
                return False

        self.assertTrue(o.myCategoryMethod())
        self.assertTrue(not o.myCategoryMethod2())

    def testCategoryMultipleInheritance(self):

        NSObject = objc.lookUpClass('NSObject')


        try:

            class NSObject ( objc.Category(NSObject), object ):
                pass

            self.fail("Can use objc.Category with MI")
        except TypeError:
            pass

    def testCategoryName(self):
        try:
            class NSFoo (objc.Category(NSObject)):
                pass

            self.fail("Category name != class name")

        except TypeError:
            pass

    def testCategoryOnPurePython(self):
        try:
            global list

            class list (objc.Category(list)):
                pass

            self.fail("Category on list???")

        except TypeError:
            pass

    def testCategoryRedefiningPythonMethod(self):
        class BaseClassRedef(NSObject):
            def foo(self):
                return 1

        class BaseClassRedef(objc.Category(BaseClassRedef)):
            def foo(self):
                return 2

        obj = BaseClassRedef.alloc().init()

        self.assertEqual(obj.foo(), 2)

        def foo(self):
            return 3
        BaseClassRedef.foo = foo

        self.assertEqual(obj.foo(), 3)

    def testCategeryWithDocString (self):
        class NSObjectCat (NSObject):
            pass

        class NSObjectCat (objc.Category(NSObjectCat)):
            """
            This is a docstring
            """

            def withDocStringMethod(self):
                return 42

        o = NSObjectCat.alloc().init()
        self.assertEqual(o.withDocStringMethod(), 42)

    def testCategoryWithClassMethod(self):
        class NSObjectCat2 (NSObject):
            pass

        class NSObjectCat2 (objc.Category(NSObjectCat2)):
            @classmethod
            def aClassMethod(cls):
                return 1

        self.assertEqual(NSObjectCat2.aClassMethod(), 1)

    def testCategoryWithVariables(self):
        class NSObjectCat3 (NSObject):
            pass

        class NSObjectCat3 (objc.Category(NSObjectCat3)):
            classValue = "aap"

            def getClassValue(self):
                return self.classValue


        self.assertHasAttr(NSObjectCat3, "classValue")
        o = NSObjectCat3.alloc().init()
        self.assertEqual(o.getClassValue(), "aap")




if __name__ == '__main__':
    main()
