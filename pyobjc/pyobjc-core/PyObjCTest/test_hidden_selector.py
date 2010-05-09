from PyObjCTools.TestSupport import *
import objc

class hidden_method (object):
     def __pyobjc_class_setup__(self, name, class_dict, instance_methods, class_methods):
         @objc.selector
         def method(self):
             return 42

         method.isHidden = True

         def clsmethod(self):
             return 99
         clsmethod=objc.selector(clsmethod, isClassMethod=True)
         clsmethod.isHidden = True

         instance_methods.add(method)
         class_methods.add(clsmethod)



class OCTestHidden (objc.lookUpClass('NSObject')):
    m = hidden_method()

    @objc.selector
    def body(self):
        return "BODY"
    body.isHidden = True


    def bodyclass(self):
        return "BODYCLASS"
    bodyclass=objc.selector(bodyclass, isClassMethod=True)
    bodyclass.isHidden=True

    @objc.selector
    def somebody(self):
        return "instance"
    somebody.isHidden = True

    def boolMethod(self):
        return 1
    boolMethod = objc.selector(boolMethod, signature=objc._C_NSBOOL + b'@:')
    boolMethod.isHidden = True

class OCTestSubHidden (OCTestHidden):
    def body(self):
        return "BODY2"

    @classmethod
    def bodyclass(self):
        return "BODYCLASS2"

    @classmethod
    def somebody(self):
        return "class"

    def boolMethod(self):
        return 0

class TestHiddenSelector (TestCase):
    def testHiddenInClassDef(self):
        o = OCTestHidden.alloc().init()
        self.assertRaises(AttributeError, getattr, o, 'body')

        v = o.performSelector_(b'body')
        self.assertEquals(v, "BODY")

        v = o.pyobjc_instanceMethods.body()
        self.assertEquals(v, "BODY")

        self.assertRaises(AttributeError, getattr, OCTestHidden, 'bodyclass')
        v = OCTestHidden.performSelector_(b'bodyclass')
        self.assertEquals(v, "BODYCLASS")

        v = OCTestHidden.pyobjc_classMethods.bodyclass()
        self.assertEquals(v, "BODYCLASS")

        o = OCTestHidden.alloc().init()
        self.assertRaises(AttributeError, getattr, o, 'boolMethod')
        v = o.pyobjc_instanceMethods.boolMethod()
        self.assertIs(v, True)


    def testHiddenInSetupHook(self):
        o = OCTestHidden.alloc().init()

        # Instance method
        self.assertRaises(AttributeError, getattr, o, 'method')

        v = o.performSelector_(b'method')
        self.assertEquals(v, 42)

        v = o.pyobjc_instanceMethods.method()
        self.assertEquals(v, 42)

        # Class method
        self.assertRaises(AttributeError, getattr, OCTestHidden, 'clsmethod')

        v = OCTestHidden.performSelector_(b'clsmethod')
        self.assertEquals(v, 99)

        v = OCTestHidden.pyobjc_classMethods.clsmethod()
        self.assertEquals(v, 99)


    def testHiddenAddMethods(self):

        @objc.selector
        def addedmethod(self):
            return "NEW"
        addedmethod.isHidden = True

        def addedclass(self):
            return "NEWCLASS"
        addedclass=objc.selector(addedclass, isClassMethod=True)
        addedclass.isHidden=True

        objc.classAddMethods(OCTestHidden, [addedmethod, addedclass])

        o = OCTestHidden.alloc().init()

        # Instance method
        self.assertRaises(AttributeError, getattr, o, 'addedmethod')

        v = o.performSelector_(b'addedmethod')
        self.assertEquals(v, "NEW")

        v = o.pyobjc_instanceMethods.addedmethod()
        self.assertEquals(v, "NEW")

        # Class method
        self.assertRaises(AttributeError, getattr, OCTestHidden, 'addedclass')

        v = OCTestHidden.performSelector_(b'addedclass')
        self.assertEquals(v, "NEWCLASS")

        v = OCTestHidden.pyobjc_classMethods.addedclass()
        self.assertEquals(v, "NEWCLASS")

    def testClassVsInstance(self):
        o = OCTestHidden.alloc().init()
        self.assertRaises(AttributeError, getattr, o, "sombody")
        v = o.performSelector_(b'somebody')
        self.assertEquals(v, "instance")

        v = OCTestSubHidden.somebody()
        self.assertEquals(v, "class")

    def testHiddenInSubClass(self):

        # Instance 
        o = OCTestSubHidden.alloc().init()
        self.assertRaises(AttributeError, getattr, o, "body")
        v = o.performSelector_(b'body')
        self.assertEquals(v, "BODY2")

        @objc.selector
        def subclassbody(self):
            return "base"
        subclassbody.isHidden = True

        @objc.selector
        def subclassbody2(self):
            return "base2"
        subclassbody.isHidden = True

        objc.classAddMethods(OCTestHidden, [subclassbody, subclassbody2])


        @objc.selector
        def subclassbody(self):
            return "sub"

        @objc.selector
        def subclassbody2(self):
            return "sub2"

        objc.classAddMethods(OCTestSubHidden, [subclassbody])
        self.assertRaises(AttributeError, getattr, o, "subclassbody")
        v = o.performSelector_(b'subclassbody')
        self.assertEquals(v, "sub")

        OCTestSubHidden.subclassbody2 = subclassbody2
        #self.assertRaises(AttributeError, getattr, o, "subclassbody2")
        v = o.performSelector_(b'subclassbody2')
        self.assertEquals(v, "sub2")

        self.assertRaises(AttributeError, getattr, o, 'boolMethod')
        v = o.pyobjc_instanceMethods.boolMethod()
        self.assertIs(v, False)

        # Class
        self.assertRaises(AttributeError, getattr, OCTestSubHidden, 'bodyclass')
        v = OCTestSubHidden.performSelector_(b'bodyclass')
        self.assertEquals(v, "BODYCLASS2")

if __name__ == "__main__":
    main()
