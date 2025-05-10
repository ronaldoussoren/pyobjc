"""
The tests in this file intend to perform a complete functional
test of the various alloc+init patterns in Objective-C and how
these affect PyObjC.

In summary the following sematics are present (with Python lingo
for the reference counts):

  - ``+[NSObject alloc]`` returns a new reference
  - ``-[NSObject init]`` steals a reference and returns a new reference
  - The ``init`` method can return ``self``, but can also return a
    completely different object (which is generally used for singletons
    and for class clusters)

The end result of this is that ``value = [[SomeClass alloc] init]`` is
a new reference, and users don't have to worry about the reference count
of the intermediate object even if ``init`` does not return ``self``.
"""

# XXX: Add tests for some Objective-C classes that
#      aren't by default proxied to objc.objc_object:
#      ``NSString`` cluster and ``NSNumber`` cluster.

# XXX: Add tests that invoke initializer more than once
#      (both by directly doing this, and by calling
#      ``super.init`` in an init method)
from PyObjCTools.TestSupport import TestCase
from PyObjCTest import initpatterns
import objc

NSObject = objc.lookUpClass("NSObject")
NSArray = objc.lookUpClass("NSArray")
NSMutableArray = objc.lookUpClass("NSMutableArray")


class TestObjectiveCClasses(TestCase):
    def test_basic_allocation(self):
        part = initpatterns.OC_InitReturnsSelf.alloc()
        self.assertEqual(part.retainCount(), 1)

        with objc.autorelease_pool():
            init = part.init()
            self.assertIs(part, init)

            descr = init.description()
            self.assertIsInstance(descr, str)

        self.assertEqual(init.retainCount(), 1)

    def test_init_returns_nil(self):
        part = initpatterns.OC_InitReturnsNil.alloc()
        init = part.init()

        self.assertIs(init, None)
        self.assertIs(type(part), initpatterns.OC_InitReturnsNil)

    def test_init_returns_other(self):
        part = initpatterns.OC_InitReturnsOther.alloc()
        self.assertEqual(part.retainCount(), 1)

        with objc.autorelease_pool():
            init = part.init()

            self.assertIsInstance(init, initpatterns.OC_InitReturnsOther)

            self.assertIsNot(init, part)

        self.assertEqual(init.retainCount(), 1)

        with objc.autorelease_pool():
            init2 = part.init()

            self.assertIsInstance(init2, initpatterns.OC_InitReturnsOther)
            self.assertIsNot(init2, part)
            self.assertIsNot(init2, init)

        self.assertEqual(init2.retainCount(), 1)

        self.assertEqual(part.retainCount(), 1)

    def test_alloc_singleton(self):
        part = initpatterns.OC_AllocSingleton.alloc()
        self.assertEqual(part.retainCount(), 2)

        init = part.init()
        self.assertIsInstance(init, initpatterns.OC_AllocSingleton)

        self.assertIsNot(init, part)

        init2 = part.init()

        self.assertIsInstance(init2, initpatterns.OC_AllocSingleton)
        self.assertIsNot(init2, part)
        self.assertIsNot(init2, init)

        self.assertEqual(part.retainCount(), 2)

        part2 = initpatterns.OC_AllocSingleton.alloc()
        self.assertIs(part, part2)
        self.assertEqual(part.retainCount(), 3)

    def test_alloc_singleton_init_fails(self):
        part = initpatterns.OC_AllocSingletonInitNil.alloc()
        self.assertEqual(part.retainCount(), 2)

        init = part.init()
        self.assertIs(init, None)

        self.assertEqual(part.retainCount(), 2)


class PythonInitReturnsNil(NSObject):
    def init(self):
        return None


class PythonInitReturnsSelf(NSObject):
    def init(self):
        return self


class PythonInitReturnsOther(NSObject):
    def init(self):
        return NSMutableArray.alloc().init()


class TestPythonSubclasses(TestCase):
    def test_init_returns_self(self):
        part = PythonInitReturnsSelf.alloc()
        self.assertEqual(part.retainCount(), 1)

        with objc.autorelease_pool():
            init = part.init()
            self.assertIs(init, part)

        self.assertEqual(init.retainCount(), 1)

    def test_init_returns_nil(self):
        part = PythonInitReturnsNil.alloc()
        self.assertEqual(part.retainCount(), 1)

        with objc.autorelease_pool():
            init1 = part.init()
            self.assertIs(init1, None)
            self.assertEqual(part.retainCount(), 1)

        with objc.autorelease_pool():
            init2 = part.init()
            self.assertIs(init2, None)
            self.assertEqual(part.retainCount(), 1)

    def test_init_returns_other(self):
        part = PythonInitReturnsOther.alloc()
        self.assertEqual(part.retainCount(), 1)

        with objc.autorelease_pool():
            init = part.init()
            self.assertIsInstance(init, NSArray)
            self.assertIsNot(init, part)
            self.assertEqual(part.retainCount(), 1)
            self.assertEqual(init.retainCount(), 1)

        self.assertEqual(part.retainCount(), 1)
        self.assertEqual(init.retainCount(), 1)


class TestInitPatternRegressions(TestCase):
    def test_nsarray_creation(self):
        # This explicity tests the stepwises creation of NSArray
        # because NSArray uses a singleton as the result of NSArray.alloc()
        # and that caused unwanted behaviour, see #642
        #
        # Note that the test mostly duplicates testing using
        # initpatterns.OC_AllocSingleton. This test is kept as is for
        # regression testing.
        part1 = NSArray.alloc()
        part2 = NSArray.alloc()

        init1 = part1.init()
        init2 = part2.init()

        self.assertIsInstance(init1, NSArray)
        self.assertIsInstance(init2, NSArray)

        self.assertEqual(init1, [])
        self.assertEqual(init2, [])

    def test_nsmutablearray_creation(self):
        part1 = NSMutableArray.alloc()
        part2 = NSMutableArray.alloc()

        init1 = part1.init()
        init2 = part2.init()

        self.assertIsInstance(init1, NSArray)
        self.assertIsInstance(init2, NSArray)

        self.assertEqual(init1, [])
        self.assertEqual(init2, [])

        self.assertIsNot(init1, init2)
