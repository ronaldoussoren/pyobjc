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
NSURL = objc.lookUpClass("NSURL")


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
        baseCount = initpatterns.OC_AllocSingleton.singletonRetainCount()

        part = initpatterns.OC_AllocSingleton.alloc()
        self.assertEqual(part.retainCount(), baseCount + 1)

        init = part.init()
        self.assertIsInstance(init, initpatterns.OC_AllocSingleton)

        self.assertIsNot(init, part)

        init2 = part.init()

        self.assertIsInstance(init2, initpatterns.OC_AllocSingleton)
        self.assertIsNot(init2, part)
        self.assertIsNot(init2, init)

        self.assertEqual(part.retainCount(), baseCount + 1)

        part2 = initpatterns.OC_AllocSingleton.alloc()
        self.assertIs(part, part2)
        self.assertEqual(part.retainCount(), baseCount + 1)

    def test_alloc_singleton_init_fails(self):
        baseCount = initpatterns.OC_AllocSingletonInitNil.singletonRetainCount()

        part = initpatterns.OC_AllocSingletonInitNil.alloc()
        self.assertEqual(part.retainCount(), baseCount + 1)

        init = part.init()
        self.assertIs(init, None)

        self.assertEqual(part.retainCount(), baseCount + 1)


class TestObjectiveCClassesFromObjC(TestCase):
    def test_basic_allocation(self):
        value = initpatterns.OC_InitPatterns.newValueFor_(
            initpatterns.OC_InitReturnsSelf
        )
        self.assertEqual(value.retainCount(), 1)

        part = initpatterns.OC_InitReturnsSelf.alloc()
        self.assertEqual(part.retainCount(), 1)

        with objc.autorelease_pool():
            with objc.autorelease_pool():
                init = initpatterns.OC_InitPatterns.callInitOn_(part)
            self.assertIs(part, init)

            descr = init.description()
            self.assertIsInstance(descr, str)

        self.assertEqual(init.retainCount(), 1)

    def test_init_returns_nil(self):
        value = initpatterns.OC_InitPatterns.newValueFor_(
            initpatterns.OC_InitReturnsNil
        )
        self.assertIs(value, None)

        part = initpatterns.OC_InitReturnsNil.alloc()
        with objc.autorelease_pool():
            init = initpatterns.OC_InitPatterns.callInitOn_(part)

        self.assertIs(init, None)
        self.assertIs(type(part), initpatterns.OC_InitReturnsNil)

    def test_init_returns_other(self):
        value = initpatterns.OC_InitPatterns.newValueFor_(
            initpatterns.OC_InitReturnsOther
        )
        self.assertEqual(value.retainCount(), 1)

        part = initpatterns.OC_InitReturnsOther.alloc()
        self.assertEqual(part.retainCount(), 1)

        with objc.autorelease_pool():
            with objc.autorelease_pool():
                init = initpatterns.OC_InitPatterns.callInitOn_(part)

            self.assertIsInstance(init, initpatterns.OC_InitReturnsOther)

            self.assertIsNot(init, part)

        self.assertEqual(init.retainCount(), 1)

        with objc.autorelease_pool():
            with objc.autorelease_pool():
                init2 = initpatterns.OC_InitPatterns.callInitOn_(part)

            self.assertIsInstance(init2, initpatterns.OC_InitReturnsOther)
            self.assertIsNot(init2, part)
            self.assertIsNot(init2, init)

        self.assertEqual(init2.retainCount(), 1)

        self.assertEqual(part.retainCount(), 1)

    def test_alloc_singleton(self):
        baseCount = initpatterns.OC_AllocSingleton.singletonRetainCount()

        value = initpatterns.OC_InitPatterns.newValueFor_(
            initpatterns.OC_AllocSingleton
        )
        self.assertIsInstance(value, initpatterns.OC_AllocSingleton)
        del value

        part = initpatterns.OC_AllocSingleton.alloc()
        self.assertEqual(part.retainCount(), baseCount + 1)

        with objc.autorelease_pool():
            init = initpatterns.OC_InitPatterns.callInitOn_(part)
        self.assertIsInstance(init, initpatterns.OC_AllocSingleton)

        self.assertIsNot(init, part)

        with objc.autorelease_pool():
            init2 = initpatterns.OC_InitPatterns.callInitOn_(part)

        self.assertIsInstance(init2, initpatterns.OC_AllocSingleton)
        self.assertIsNot(init2, part)
        self.assertIsNot(init2, init)

        self.assertEqual(part.retainCount(), baseCount + 1)

        part2 = initpatterns.OC_AllocSingleton.alloc()
        self.assertIs(part, part2)
        self.assertEqual(part.retainCount(), baseCount + 1)

    def test_alloc_singleton_init_fails(self):
        value = initpatterns.OC_InitPatterns.newValueFor_(
            initpatterns.OC_AllocSingletonInitNil
        )
        self.assertIs(value, None)

        part = initpatterns.OC_AllocSingletonInitNil.alloc()
        self.assertEqual(part.retainCount(), 2)

        with objc.autorelease_pool():
            init = initpatterns.OC_InitPatterns.callInitOn_(part)
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


class TestPythonSubclassesFromObjC(TestCase):
    def test_init_returns_self(self):
        value = initpatterns.OC_InitPatterns.newValueFor_(PythonInitReturnsSelf)
        self.assertEqual(value.retainCount(), 1)

        part = PythonInitReturnsSelf.alloc()
        self.assertEqual(part.retainCount(), 1)

        with objc.autorelease_pool():
            with objc.autorelease_pool():
                init = initpatterns.OC_InitPatterns.callInitOn_(part)
            self.assertIs(init, part)

        self.assertEqual(init.retainCount(), 1)

    def test_init_returns_nil(self):
        value = initpatterns.OC_InitPatterns.newValueFor_(PythonInitReturnsNil)
        self.assertIs(value, None)

        part = PythonInitReturnsNil.alloc()
        self.assertEqual(part.retainCount(), 1)

        with objc.autorelease_pool():
            with objc.autorelease_pool():
                init1 = initpatterns.OC_InitPatterns.callInitOn_(part)
            self.assertIs(init1, None)
            self.assertEqual(part.retainCount(), 1)

        with objc.autorelease_pool():
            with objc.autorelease_pool():
                init2 = initpatterns.OC_InitPatterns.callInitOn_(part)
            self.assertIs(init2, None)
            self.assertEqual(part.retainCount(), 1)

    def test_init_returns_other(self):
        value = initpatterns.OC_InitPatterns.newValueFor_(PythonInitReturnsOther)
        self.assertIsInstance(value, NSArray)

        part = PythonInitReturnsOther.alloc()
        self.assertEqual(part.retainCount(), 1)

        with objc.autorelease_pool():
            with objc.autorelease_pool():
                init = initpatterns.OC_InitPatterns.callInitOn_(part)
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

        self.assertIsInitializer(part1.init)
        self.assertIsNotInitializer(init1.count)

    def test_nsurl_creation(self):
        u = NSURL.alloc()
        del u
        u = NSURL.alloc()
        del u
