# FIXME: This test suite seems to polute it's environment, other tests fail
# when this test suite is active!
import unittest
import sys

import objc

class MEClass(objc.runtime.NSObject):
   pass

preEverythingInstance = MEClass.new()

class Methods(objc.runtime.NSObject):
    def description(self):
        return "<methods>"

    def newMethod(self):
        return "<new-method>"

class MethodsSub(objc.runtime.NSObject):
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

class TestFromObjCSuperToObjCClass(unittest.TestCase):
    def testBasicBehavior(self):
        anInstance = Methods.new()
        self.assertEquals(anInstance.description(), "<methods>")
        self.assertEquals(anInstance.newMethod(), "<new-method>")

    def testDescriptionOverride(self):
        objc.classAddMethods(MEClass, [Methods.description])

        self.assert_(MEClass.instancesRespondToSelector_("description"))

        newInstance = MEClass.new()

        self.assertEquals(newInstance.description(), "<methods>")
        self.assertEquals(preEverythingInstance.description(), "<methods>")

    def testNewMethod(self):
        objc.classAddMethods(MEClass, [Methods.newMethod])

        self.assert_(MEClass.instancesRespondToSelector_("newMethod"))

        newInstance = MEClass.new()
        
        self.assertEquals(newInstance.newMethod(), "<new-method>")
        self.assertEquals(preEverythingInstance.newMethod(), "<new-method>")

    def testSubDescriptionOverride(self):
        objc.classAddMethods(MEClass, [MethodsSub.description])

        self.assert_(MEClass.instancesRespondToSelector_("description"))

        newInstance = MEClass.new()

        self.assertEquals(newInstance.description(), "<sub-methods>")
        self.assertEquals(preEverythingInstance.description(), "<sub-methods>")

    def testSubNewMethod(self):
        objc.classAddMethods(MEClass, [MethodsSub.newMethod, MethodsSub.newSubMethod])

        self.assert_(MEClass.instancesRespondToSelector_("newMethod"))
        self.assert_(MEClass.instancesRespondToSelector_("newSubMethod"))

        newInstance = MEClass.new()
        
        self.assertEquals(newInstance.newMethod(), "<sub-new-method>")
        self.assertEquals(preEverythingInstance.newMethod(), "<sub-new-method>")
        self.assertEquals(newInstance.newSubMethod(), "<new-method-sub>")
        self.assertEquals(preEverythingInstance.newSubMethod(), "<new-method-sub>")


class TestFromPythonClassToObjCClass(unittest.TestCase):

    def testPythonSourcedMethods(self):
        objc.classAddMethods(MEClass, [PurePython.description,
                                                  PurePython.newMethod,
                                                  PurePython.purePythonMethod])

        
        self.assert_(MEClass.instancesRespondToSelector_("description"))
        self.assert_(MEClass.instancesRespondToSelector_("newMethod"))
        self.assert_(MEClass.instancesRespondToSelector_("purePythonMethod"))

        newInstance = MEClass.new()

        self.assertEquals(newInstance.description(), "<pure>")
        self.assertEquals(newInstance.newMethod(), "<pure-new>")
        self.assertEquals(newInstance.purePythonMethod(), "<pure-py>")

        self.assertEquals(preEverythingInstance.description(), "<pure>")
        self.assertEquals(preEverythingInstance.newMethod(), "<pure-new>")
        self.assertEquals(preEverythingInstance.purePythonMethod(), "<pure-py>")

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

        self.assertEquals(newInstance.description(), "<pure>")
        self.assertEquals(newInstance.newMethod(), "<pure-new>")
        self.assertEquals(newInstance.purePythonMethod(), "<pure-py>")

        self.assertEquals(preEverythingInstance.description(), "<pure>")
        self.assertEquals(preEverythingInstance.newMethod(), "<pure-new>")
        self.assertEquals(preEverythingInstance.purePythonMethod(), "<pure-py>")

if __name__ == '__main__':
    unittest.main()
