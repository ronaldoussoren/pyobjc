import unittest
import objc

# Most usefull systems will at least have 'NSObject'.
NSObject = objc.lookUpClass('NSObject')

class TestSubclassing(unittest.TestCase):
    def testSubclassOfSubclass(self):
        import string
        class Level1Class (NSObject):
            def hello(self):
                return "level1"

        class Level2Class (Level1Class):
            def hello(self):
                return "level2"

            def superHello(self):
                return super(Level2Class, self).hello()

            def description(self):
                return super(Level2Class, self).description()

        obj = Level1Class.alloc().init()
        v = obj.hello()
        self.assertEquals(v, "level1")

        obj = Level2Class.alloc().init()
        v = obj.hello()
        self.assertEquals(v, "level2")

        v = obj.superHello()
        self.assertEquals(v, "level1")

        v = obj.description()
        # this may be a bit hardwired for comfort
        self.assert_(string.index(v, "<Level2Class") == 0)
    
    def testUniqueNames(self):
        class SomeClass (NSObject): pass

        try:
            class SomeClass (NSObject): pass

            fail("Should not have been able to redefine the SomeClass class!")
        except objc.error, msg:
            self.assertEquals(str(msg), "Class already exists in Objective-C runtime")

class TestSelectors(unittest.TestCase):
    def testSelectorRepr(self):
        class SelectorRepr(NSObject):
            def foo(self):
                pass

        self.assert_(repr(SelectorRepr.foo) == '<unbound selector foo of SelectorRepr>')


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSubclassing))
    suite.addTest(unittest.makeSuite(TestSelectors))
    return suite

if __name__ == '__main__':
    unittest.main()
