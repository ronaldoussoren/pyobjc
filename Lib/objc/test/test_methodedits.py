import unittest
import sys

import objc

# NSIdEnumerator is not used anywhere else in the unittests
MEClass  = objc.runtime.NSIdEnumerator

## If you use this definition this test causes a crash.
#class MEClass(objc.runtime.NSObject):
#   pass

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
    def setUp(self):
        self.NSObjectClass = MEClass

    def testBasicBehavior(self):
        anInstance = Methods.new()
        self.assertEquals(anInstance.description(), "<methods>")
        self.assertEquals(anInstance.newMethod(), "<new-method>")

    def testDescriptionOverride(self):
        objc.classAddMethods(self.NSObjectClass, [Methods.description])

        self.assert_(self.NSObjectClass.instancesRespondToSelector_("description"))

        newInstance = self.NSObjectClass.new()

        self.assertEquals(newInstance.description(), "<methods>")
        self.assertEquals(preEverythingInstance.description(), "<methods>")

    def testNewMethod(self):
        objc.classAddMethods(self.NSObjectClass, [Methods.newMethod])

        self.assert_(self.NSObjectClass.instancesRespondToSelector_("newMethod"))

        newInstance = self.NSObjectClass.new()
        
        self.assertEquals(newInstance.newMethod(), "<new-method>")
        self.assertEquals(preEverythingInstance.newMethod(), "<new-method>")

    def testSubDescriptionOverride(self):
        objc.classAddMethods(self.NSObjectClass, [MethodsSub.description])

        self.assert_(self.NSObjectClass.instancesRespondToSelector_("description"))

        newInstance = self.NSObjectClass.new()

        self.assertEquals(newInstance.description(), "<sub-methods>")
        self.assertEquals(preEverythingInstance.description(), "<sub-methods>")

    def testSubNewMethod(self):
        objc.classAddMethods(self.NSObjectClass, [MethodsSub.newMethod, MethodsSub.newSubMethod])

        self.assert_(self.NSObjectClass.instancesRespondToSelector_("newMethod"))
        self.assert_(self.NSObjectClass.instancesRespondToSelector_("newSubMethod"))

        newInstance = self.NSObjectClass.new()
        
        self.assertEquals(newInstance.newMethod(), "<sub-new-method>")
        self.assertEquals(preEverythingInstance.newMethod(), "<sub-new-method>")
        self.assertEquals(newInstance.newSubMethod(), "<new-method-sub>")
        self.assertEquals(preEverythingInstance.newSubMethod(), "<new-method-sub>")


class TestFromPythonClassToObjCClass(unittest.TestCase):
    def setUp(self):
        self.NSObjectClass = objc.runtime.NSObject

    def testPythonSourcedMethods(self):
        objc.classAddMethods(self.NSObjectClass, [PurePython.description,
                                                  PurePython.newMethod,
                                                  PurePython.purePythonMethod])

        
        self.assert_(self.NSObjectClass.instancesRespondToSelector_("description"))
        self.assert_(self.NSObjectClass.instancesRespondToSelector_("newMethod"))
        self.assert_(self.NSObjectClass.instancesRespondToSelector_("purePythonMethod"))

        newInstance = self.NSObjectClass.new()

        self.assertEquals(newInstance.description(), "<pure>")
        self.assertEquals(newInstance.newMethod(), "<pure-new>")
        self.assertEquals(newInstance.purePythonMethod(), "<pure-py>")

        self.assertEquals(preEverythingInstance.description(), "<pure>")
        self.assertEquals(preEverythingInstance.newMethod(), "<pure-new>")
        self.assertEquals(preEverythingInstance.purePythonMethod(), "<pure-py>")

def suite():
    suite = unittest.TestSuite()
    try:
        objc.classAddMethods
    except:
        print "classAddMethods() not available.  Creating empty suite."
        return suite
    suite.addTest(unittest.makeSuite(TestFromObjCSuperToObjCClass))
    suite.addTest(unittest.makeSuite(TestFromPythonClassToObjCClass))
    return suite

if __name__ == '__main__':
    try:
        objc.classAddMethods
    except:
        print "classAddMethods() not available.  Aborting test."
        sys.exit(1)
    unittest.main()
