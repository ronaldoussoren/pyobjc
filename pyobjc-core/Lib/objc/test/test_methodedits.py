# FIXME: This test suite seems to polute it's environment, other tests fail
# when this test suite is active!
import objc.test
import sys

import objc

NSObject = objc.lookUpClass('NSObject')

class MEClass(NSObject):
    pass

preEverythingInstance = MEClass.new()

class Methods(NSObject):
    def description(self):
        return u"<methods>"

    def newMethod(self):
        return u"<new-method>"

class MethodsSub(NSObject):
    def description(self):
        return u"<sub-methods>"

    def newMethod(self):
        return u"<sub-new-method>"

    def newSubMethod(self):
        return u"<new-method-sub>"

class PurePython:
    def description(self):
        return u"<pure>"

    def newMethod(self):
        return u"<pure-new>"

    def purePythonMethod(self):
        return u"<pure-py>"

class TestFromObjCSuperToObjCClass(objc.test.TestCase):
    def testBasicBehavior(self):
        anInstance = Methods.new()
        self.assertEquals(anInstance.description(), u"<methods>")
        self.assertEquals(anInstance.newMethod(), u"<new-method>")

    def testDescriptionOverride(self):
        objc.classAddMethods(MEClass, [Methods.pyobjc_instanceMethods.description])

        self.assert_(MEClass.instancesRespondToSelector_("description"))

        newInstance = MEClass.new()

        self.assertEquals(newInstance.description(), u"<methods>")
        self.assertEquals(preEverythingInstance.description(), u"<methods>")

    def testNewMethod(self):
        objc.classAddMethods(MEClass, [Methods.pyobjc_instanceMethods.newMethod])

        self.assert_(MEClass.instancesRespondToSelector_("newMethod"))

        newInstance = MEClass.new()

        self.assertEquals(newInstance.newMethod(), u"<new-method>")
        self.assertEquals(preEverythingInstance.newMethod(), u"<new-method>")

    def testSubDescriptionOverride(self):
        objc.classAddMethods(MEClass, [MethodsSub.pyobjc_instanceMethods.description])

        self.assert_(MEClass.instancesRespondToSelector_("description"))

        newInstance = MEClass.new()

        self.assertEquals(newInstance.description(), u"<sub-methods>")
        self.assertEquals(preEverythingInstance.description(), u"<sub-methods>")

    def testSubNewMethod(self):
        objc.classAddMethods(MEClass, [MethodsSub.newMethod, MethodsSub.newSubMethod])

        self.assert_(MEClass.instancesRespondToSelector_("newMethod"))
        self.assert_(MEClass.instancesRespondToSelector_("newSubMethod"))

        newInstance = MEClass.new()

        self.assertEquals(newInstance.newMethod(), u"<sub-new-method>")
        self.assertEquals(preEverythingInstance.newMethod(), u"<sub-new-method>")
        self.assertEquals(newInstance.newSubMethod(), u"<new-method-sub>")
        self.assertEquals(preEverythingInstance.newSubMethod(), u"<new-method-sub>")

    def testNewClassMethod(self):

        def aNewClassMethod(cls):
            return "Foo cls"
        aNewClassMethod = classmethod(aNewClassMethod)

        self.assert_(not MEClass.pyobjc_classMethods.respondsToSelector_("aNewClassMethod"))
        objc.classAddMethods(MEClass, [aNewClassMethod])
        self.assert_(MEClass.pyobjc_classMethods.respondsToSelector_("aNewClassMethod"))

        self.assert_(MEClass.aNewClassMethod.isClassMethod)
        self.assertEquals(MEClass.aNewClassMethod(), 'Foo cls')


class TestFromPythonClassToObjCClass(objc.test.TestCase):

    def testPythonSourcedMethods(self):
        # 20031227, Ronald: Assigning the methods works alright, but actually
        # using them won't because the new methods are actually still methods
        # of a different class and will therefore complain about the type
        # of 'self'.
        objc.classAddMethods(MEClass, [PurePython.description,
                                                  PurePython.newMethod,
                                                  PurePython.purePythonMethod])


        self.assert_(MEClass.instancesRespondToSelector_("description"))
        self.assert_(MEClass.instancesRespondToSelector_("newMethod"))
        self.assert_(MEClass.instancesRespondToSelector_("purePythonMethod"))

        newInstance = MEClass.new()

        # This is bogus, see above:
        #self.assertEquals(newInstance.description(), u"<pure>")
        #self.assertEquals(newInstance.newMethod(), u"<pure-new>")
        #self.assertEquals(newInstance.purePythonMethod(), u"<pure-py>")

        #self.assertEquals(preEverythingInstance.description(), u"<pure>")
        #self.assertEquals(preEverythingInstance.newMethod(), u"<pure-new>")
        #self.assertEquals(preEverythingInstance.purePythonMethod(), u"<pure-py>")

        self.assertRaises(TypeError, newInstance.description)
        self.assertRaises(TypeError, newInstance.newMethod)
        self.assertRaises(TypeError, newInstance.purePythonMethod)
        self.assertRaises(TypeError, preEverythingInstance.description)
        self.assertRaises(TypeError, preEverythingInstance.newMethod)
        self.assertRaises(TypeError, preEverythingInstance.purePythonMethod)

    def testPythonSourcedFunctions(self):
        # Same as testPythonSourcedMethods, but using function objects instead
        # of method objects.


        objc.classAddMethods(MEClass, [
            PurePython.description.im_func,
            PurePython.newMethod.im_func,
            PurePython.purePythonMethod.im_func
        ])

        self.assert_(MEClass.instancesRespondToSelector_("description"))
        self.assert_(MEClass.instancesRespondToSelector_("newMethod"))
        self.assert_(MEClass.instancesRespondToSelector_("purePythonMethod"))

        newInstance = MEClass.new()

        self.assertEquals(newInstance.description(), u"<pure>")
        self.assertEquals(newInstance.newMethod(), u"<pure-new>")
        self.assertEquals(newInstance.purePythonMethod(), u"<pure-py>")

        self.assertEquals(preEverythingInstance.description(), u"<pure>")
        self.assertEquals(preEverythingInstance.newMethod(), u"<pure-new>")
        self.assertEquals(preEverythingInstance.purePythonMethod(), u"<pure-py>")



class TestClassAsignments (objc.test.TestCase):
    def testAssignAMethod(self):
        MEClass.doSomethingElse = lambda self: 2*2
        MEClass.doDuplicate_ = lambda self, x: 2*x

        self.assert_(MEClass.instancesRespondToSelector_("doSomethingElse"))
        self.assert_(MEClass.instancesRespondToSelector_("doDuplicate:"))

        o = MEClass.alloc().init()

        self.assertEquals(4, o.doSomethingElse())
        self.assertEquals(8, o.doDuplicate_(4))

    def testAssignAClassMethod(self):
        MEClass.classSomethingElse = classmethod(lambda self: 2*2)
        MEClass.classDuplicate_ = classmethod(lambda self, x: 2*x)

        self.assert_(MEClass.pyobjc_classMethods.respondsToSelector_("classSomethingElse"))
        self.assert_(MEClass.pyobjc_classMethods.respondsToSelector_("classDuplicate:"))

        self.assertEquals(4, MEClass.classSomethingElse())
        self.assertEquals(8, MEClass.classDuplicate_(4))

    def testAssignFuzzyMethod(self):
        self.assertRaises(ValueError, setattr, MEClass, 'fuzzyMethod', objc.selector(None, selector='fuzzy', signature='@@:'))

    def testRemovingMethods(self):
        theClass = NSObject

        self.assertRaises(AttributeError, delattr, theClass, 'alloc')
        self.assertRaises(AttributeError, delattr, theClass, 'init')

class TestCategory (objc.test.TestCase):
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

        self.assert_(o.categoryMethod())
        self.assert_(not o.categoryMethod2())
        self.assertEquals(Methods.anotherClassMethod(), "hello")

    def testObjCClassCategory(self):

        NSObject = objc.lookUpClass('NSObject')

        o = NSObject.alloc().init()
        self.assertRaises(AttributeError, getattr, o, 'myCategoryMethod')

        class NSObject (objc.Category(NSObject)):
            def myCategoryMethod(self):
                return True

            def myCategoryMethod2(self):
                return False

        self.assert_(o.myCategoryMethod())
        self.assert_(not o.myCategoryMethod2())

    def testCategoryMultipleInheritance(self):

        NSObject = objc.lookUpClass('NSObject')


        try:

            class NSObject ( objc.Category(NSObject), object ):
                pass

            raise AssertionError, u"Can use objc.Category with MI"
        except TypeError:
            pass

    def testCategoryName(self):
        try:
            class NSFoo (objc.Category(NSObject)):
                    pass

            raise AssertionError, u"Category name != class name"

        except TypeError:
            pass

    def testCategoryOnPurePython(self):
        try:
            global list

            class list (objc.Category(list)):
                pass

            raise AssertionError, u"Category on list???"

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

        self.assertEquals(obj.foo(), 2)

        def foo(self):
            return 3
        BaseClassRedef.foo = foo

        self.assertEquals(obj.foo(), 3)
                


if __name__ == '__main__':
    objc.test.main()
