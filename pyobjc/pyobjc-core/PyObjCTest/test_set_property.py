from PyObjCTools.TestSupport import *
import objc
from PyObjCTest.test_object_property import OCObserve

NSObject = objc.lookUpClass('NSObject')

class TestSetPropertyHelper (NSObject):
    aSet = objc.set_property()

class TestSetProperty (TestCase):
    def testCopying(self):
        o = TestSetPropertyHelper.alloc().init()
        aSet = set([1,2])
        o.aSet = aSet

        self.assertEquals(len(o.aSet), 2)
        self.assertEquals(len(aSet), 2)
        aSet.add(3)
        self.assertEquals(len(o.aSet), 2)
        self.assertEquals(len(aSet), 3)

    def testDefault(self):
        with OCObserve.alloc().init() as observer:
            o = TestSetPropertyHelper.alloc().init()

            observer.register(o, 'aSet')

            o.aSet = set()
            self.assertEquals(len(observer.values), 1)

            self.assertEquals(len(o.aSet), 0)
            o.aSet.add('a')
            o.aSet.add('b')
            self.assertEquals(len(o.aSet), 2)
            self.assertEquals(len(observer.values), 3)

            self.assertEquals(observer.values[-2][-1]['kind'], 2)
            self.assertNotIn('old', observer.values[-2][-1])
            self.assertEquals(observer.values[-2][-1]['new'], set('a'))

            self.assertEquals(observer.values[-1][-1]['kind'], 2)
            self.assertNotIn('old', observer.values[-1][-1])
            self.assertEquals(observer.values[-1][-1]['new'], set('b'))

            v = list(o.aSet)
            v.sort()
            self.assertEquals(v, ['a', 'b'])

            self.assertEqual(o.aSet, set(['a', 'b']))

            proxy = o.aSet


            o.aSet.clear()
            self.assertEquals(len(o.aSet), 0)
            self.assertEquals(len(proxy), 0)

            self.assertEquals(len(observer.values), 4)
            self.assertEquals(observer.values[-1][-1]['old'], set(['a', 'b']))
            self.assertNotIn('new', observer.values[-1][-1])

    def testDifferenceUpdate(self):
        with OCObserve.alloc().init() as observer:
            o = TestSetPropertyHelper.alloc().init()

            o.aSet.add(1)
            o.aSet.add(2)
            o.aSet.add(3)

            observer.register(o, 'aSet')

            o.aSet.difference_update(set([1,4]))
            self.assertEquals(o.aSet, set([2,3]))

            self.assertEquals(len(observer.values), 1)
            self.assertEquals(observer.values[-1][-1]['kind'], 3)
            self.assertNotIn('new', observer.values[-1][-1])
            self.assertEquals(observer.values[-1][-1]['old'], set([1]))

    def testSymmetricDifferenceUpdate(self):
        with OCObserve.alloc().init() as observer:
            o = TestSetPropertyHelper.alloc().init()

            o.aSet = set([1,2,3])

            observer.register(o, 'aSet')

            self.assertEquals(len(observer.values), 0)
            o.aSet.symmetric_difference_update(set([1,4]))
            self.assertEquals(o.aSet, set([2, 3, 4]))

            self.assertEquals(len(observer.values), 2)

            haveAdd = False
            haveRemove = False

            for i in 0, 1:
                if observer.values[i][-1]['kind'] == 3:
                    # Remove
                    self.assertNotIn('new', observer.values[i][-1])
                    self.assertEquals(observer.values[i][-1]['old'], set([1]))
                    haveRemove = True

                elif observer.values[i][-1]['kind'] == 2:
                    # Remove
                    self.assertNotIn('old', observer.values[i][-1])
                    self.assertEquals(observer.values[i][-1]['new'], set([4]))
                    haveAdd = True

                else:
                    self.fail("Unexpected update kind")

            if not haveAdd and haveRemove:
                self.fail("Do not have both an add and remove notification")

    def testUpdate(self):
        with OCObserve.alloc().init() as observer:
            o = TestSetPropertyHelper.alloc().init()
            observer.register(o, 'aSet')

            o.aSet.update([1,2,3])
            self.assertEquals(len(observer.values), 1)
            self.assertEquals(observer.values[-1][-1]['kind'], 2)
            self.assertNotIn('old', observer.values[-1][-1])
            self.assertEquals(observer.values[-1][-1]['new'], set([1, 2, 3]))

            o.aSet.update(set([3,4,5]))
            self.assertEquals(len(observer.values), 2)
            self.assertEquals(observer.values[-1][-1]['kind'], 2)
            self.assertNotIn('old', observer.values[-1][-1])
            self.assertEquals(observer.values[-1][-1]['new'], set([4, 5]))



    def testAddDiscard(self): 
        with OCObserve.alloc().init() as observer:
            o = TestSetPropertyHelper.alloc().init()
            observer.register(o, 'aSet')

            o.aSet.add(1)
            self.assertEquals(len(observer.values), 1)
            self.assertNotIn('old', observer.values[-1][-1])
            self.assertEquals(observer.values[-1][-1]['new'], set([1]))

            o.aSet.discard(1)
            self.assertEquals(len(observer.values), 2)
            self.assertNotIn('new', observer.values[-1][-1])
            self.assertEquals(observer.values[-1][-1]['old'], set([1]))

            o.aSet.discard(2)
            self.assertEquals(len(observer.values), 3)
            self.assertNotIn('new', observer.values[-1][-1])
            self.assertEquals(observer.values[-1][-1]['old'], set([]))


    def testAddRemove(self): 
        with OCObserve.alloc().init() as observer:
            o = TestSetPropertyHelper.alloc().init()
            observer.register(o, 'aSet')

            o.aSet.add(1)
            self.assertEquals(len(observer.values), 1)
            self.assertNotIn('old', observer.values[-1][-1])
            self.assertEquals(observer.values[-1][-1]['new'], set([1]))

            o.aSet.remove(1)
            self.assertEquals(len(observer.values), 2)
            self.assertNotIn('new', observer.values[-1][-1])
            self.assertEquals(observer.values[-1][-1]['old'], set([1]))

            self.assertRaises(KeyError, o.aSet.remove, 2)
            self.assertEquals(len(observer.values), 3)
            self.assertNotIn('new', observer.values[-1][-1])
            self.assertEquals(observer.values[-1][-1]['old'], set([]))

    def testInplace(self):
        with OCObserve.alloc().init() as observer:
            o = TestSetPropertyHelper.alloc().init()
            o.aSet.add(1)
            observer.register(o, 'aSet')


            # The inplace operators aren't actually implemented, which means
            # "o.aSet |= value" is actually  "o.aSet = o.aSet | value" and
            # we get the some KVO notificatons as when a new value is set.

            o.aSet |= set([2,3])
            self.assertEquals(o.aSet, set([1,2,3]))
            self.assertEquals(len(observer.values), 1)
            self.assertEquals(observer.values[-1][-1]['kind'], 1)
            self.assertEquals(observer.values[-1][-1]['old'], set([1]))
            self.assertEquals(observer.values[-1][-1]['new'], set([1,2,3]))

            o.aSet &= set([3, 4])
            self.assertEquals(o.aSet, set([3]))
            self.assertEquals(len(observer.values), 2)
            self.assertEquals(observer.values[-1][-1]['kind'], 1)
            self.assertEquals(observer.values[-1][-1]['old'], set([1,2,3]))
            self.assertEquals(observer.values[-1][-1]['new'], set([3]))

            o.aSet -= set([3])
            self.assertEquals(o.aSet, set([]))
            self.assertEquals(len(observer.values), 3)
            self.assertEquals(observer.values[-1][-1]['kind'], 1)
            self.assertEquals(observer.values[-1][-1]['old'], set([3]))
            self.assertEquals(observer.values[-1][-1]['new'], set())

            o.aSet = set([1,2,3])
            self.assertEquals(len(observer.values), 4)

            o.aSet ^= set([1, 4])
            self.assertEquals(o.aSet, set([2, 3, 4]))
            self.assertEquals(len(observer.values), 5)
            self.assertEquals(observer.values[-1][-1]['kind'], 1)
            self.assertEquals(observer.values[-1][-1]['old'], set([1,2,3]))
            self.assertEquals(observer.values[-1][-1]['new'], set([2,3,4]))

    def testObjCAccessors(self):
        # Check that the right ObjC array accessors are defined and work properly
        self.assertTrue(TestSetPropertyHelper.instancesRespondToSelector_(b"setASet:"))
        self.assertTrue(TestSetPropertyHelper.instancesRespondToSelector_(b"aSet"))
        self.assertTrue(TestSetPropertyHelper.instancesRespondToSelector_(b"countOfASet"))
        self.assertTrue(TestSetPropertyHelper.instancesRespondToSelector_(b"enumeratorOfASet"))
        self.assertTrue(TestSetPropertyHelper.instancesRespondToSelector_(b"memberOfASet:"))
        self.assertTrue(TestSetPropertyHelper.instancesRespondToSelector_(b"addASet:"))
        self.assertTrue(TestSetPropertyHelper.instancesRespondToSelector_(b"addASetObject:"))
        self.assertTrue(TestSetPropertyHelper.instancesRespondToSelector_(b"removeASet:"))
        self.assertTrue(TestSetPropertyHelper.instancesRespondToSelector_(b"removeASetObject:"))

        o = TestSetPropertyHelper.alloc().init()
        self.assertEquals(0, o.pyobjc_instanceMethods.countOfASet())
        self.assertRaises(AttributeError, getattr, o, 'countOfASet')
        o.aSet.add(1)
        o.aSet.add(2)

        v = list(sorted(o.pyobjc_instanceMethods.enumeratorOfASet()))
        self.assertEquals(v, [1,2])

        class Testing (object):
            def __hash__(self):
                return 42

            def __eq__(self, other):
                return isinstance(other, Testing)
    
        p = Testing()
        o.aSet.add(p)

        v = o.pyobjc_instanceMethods.memberOfASet_(Testing())
        self.assertIs(p, v)

        self.assertNotIn(9, o.aSet)
        o.pyobjc_instanceMethods.addASet_(9)
        self.assertIn(9, o.aSet)

        self.assertNotIn(10, o.aSet)
        o.pyobjc_instanceMethods.addASetObject_(10)
        self.assertIn(10, o.aSet)

        self.assertIn(9, o.aSet)
        o.pyobjc_instanceMethods.removeASet_(9)
        self.assertNotIn(9, o.aSet)

        self.assertIn(10, o.aSet)
        o.pyobjc_instanceMethods.removeASetObject_(10)
        self.assertNotIn(10, o.aSet)


if __name__ == "__main__":
    main()
