import objc
import objc.test

NSObject = objc.lookUpClass('NSObject')


class TestBasicIMP (objc.test.TestCase):
    # Test the basic functionality of IMP's. Imp's are basically unbound
    # selectors if you look at the interface. The implementation refers to
    # the actual functions that implements the method for calling the IMP
    # instead of passing through the usual message sending machinery.
    #
    def testIMPType(self):
        self.assert_(hasattr(objc, "IMP"))

    def testAlloc(self):
        cls = NSObject
        m = cls.pyobjc_classMethods.methodForSelector_("alloc")
        self.assert_(isinstance(m, objc.IMP))
        self.assert_(m.__metadata__()['classmethod'])
        self.assertEquals(m.__metadata__()['retval']['already_retained'], cls.alloc.__metadata__()['retval']['already_retained'])
        self.assertEquals(m.selector, 'alloc')

        o = m(cls).init()
        self.assert_(isinstance(o, cls))

    def testInit1(self):
        cls = NSObject
        m = cls.instanceMethodForSelector_("init")
        self.assert_(isinstance(m, objc.IMP))
        self.assert_(not m.__metadata__()['classmethod'])
        self.assertEquals(m.__metadata__()['retval']['already_retained'], cls.init.__metadata__()['retval']['already_retained'])
        self.assertEquals(m.selector, 'init')

        o = m(cls.alloc())
        self.assert_(isinstance(o, cls))

    def testInit2(self):
        cls = NSObject
        o = cls.alloc().init()

        m = o.methodForSelector_("init")
        self.assert_(isinstance(m, objc.IMP))
        self.assert_(not m.__metadata__()['classmethod'])
        self.assertEquals(m.__metadata__()['retval']['already_retained'], cls.init.__metadata__()['retval']['already_retained'])
        self.assertEquals(m.selector, 'init')

        o = m(cls.alloc())
        self.assert_(isinstance(o, cls))

    def testDescription(self):
        o = NSObject.alloc().init()

        self.assertEquals(o.description(), o.methodForSelector_('description')(o))




if __name__ == "__main__":
    objc.test.main()
