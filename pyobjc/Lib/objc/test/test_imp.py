import objc
import unittest

NSObject = objc.lookUpClass('NSObject')


class TestBasicIMP (unittest.TestCase):
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
        self.assert_(m.isClassMethod)
        self.assertEquals(m.isAlloc, cls.alloc.isAlloc)
        self.assertEquals(m.doesDonateReference, cls.alloc.doesDonateReference)
        self.assertEquals(m.selector, 'alloc')

        o = m(cls).init()
        self.assert_(isinstance(o, cls))

    def testInit1(self):
        cls = NSObject
        m = cls.instanceMethodForSelector_("init")
        self.assert_(isinstance(m, objc.IMP))
        self.assert_(not m.isClassMethod)
        self.assertEquals(m.isAlloc, cls.init.isAlloc)
        self.assertEquals(m.doesDonateReference, cls.init.doesDonateReference)
        self.assertEquals(m.selector, 'init')

        o = m(cls.alloc())
        self.assert_(isinstance(o, cls))

    def testInit2(self):
        cls = NSObject
        o = cls.alloc().init()

        m = o.methodForSelector_("init")
        self.assert_(isinstance(m, objc.IMP))
        self.assert_(not m.isClassMethod)
        self.assertEquals(m.isAlloc, cls.init.isAlloc)
        self.assertEquals(m.doesDonateReference, cls.init.doesDonateReference)
        self.assertEquals(m.selector, 'init')

        o = m(cls.alloc())
        self.assert_(isinstance(o, cls))

    def testDescription(self):
        o = NSObject.alloc().init()

        self.assertEquals(o.description(), o.methodForSelector_('description')(o))




if __name__ == "__main__":
    unittest.main()
