from PyObjCTools.TestSupport import *
import objc
import pickle
import collections
import sys

NSObject = objc.lookUpClass('NSObject')
NSIndexSet = objc.lookUpClass('NSIndexSet')
NSMutableIndexSet = objc.lookUpClass('NSMutableIndexSet')

class TestArrayPropertyHelper (NSObject):
    array = objc.array_property()
    array2 = objc.array_property()
    roArray = objc.array_property(read_only=True)

from PyObjCTest.test_object_property import OCObserve

class TestArrayProperty (TestCase):
    def _testMissing(self):
        self.fail("Implement tests")

    def testGetting(self):
        # Check that default value is an empty value
        # Check that value is a proxy object
        o = TestArrayPropertyHelper.alloc().init()

        v = o.array
        self.assertIsInstance(v, collections.MutableSequence)

        self.assertEqual(len(v), 0)

        v.append(1)
        self.assertEqual(len(v), 1)

        self.assertEqual(type(v).__name__, 'array_proxy')

    def testSetting(self):
        # Set value, check that
        # (1) value gets copied
        # (2) accessing the property result in proxy
        observer = OCObserve.alloc().init()
        l = [1, 2, 3]
        o = TestArrayPropertyHelper.alloc().init()
        observer.register(o, 'array')
        try:
            self.assertEqual(observer.seen, {})
            self.assertEqual(len(o.array), 0)
            self.assertEqual(observer.seen, {'array': []})
            o.array = l
            self.assertEqual(observer.seen, {'array': l})


            self.assertEqual(len(o.array), 3)

            # This shouldn't affect the property
            l.append(4)
            self.assertEqual(len(o.array), 3)

            self.assertEqual(len(l), 4)
            o.array.append(5)
            self.assertEqual(len(l), 4)
            self.assertEqual(len(o.array), 4)

        finally:
            observer.unregister(o, 'array')

        l = [1,2]
        o.array2 = l
        self.assertIsNot(o._array2, l)

        o.array2 = o.array
        self.assertEqual(o.array2, [1, 2, 3, 5])
        o.array2.append(1)
        self.assertEqual(o.array2, [1, 2, 3, 5, 1])
        self.assertEqual(o.array, [1, 2, 3, 5])


        arr = o.array2
        o._array2 = None
        self.assertEqual(arr, [])


    def testGetSetItem(self):
        # Use __getitem__, __setitem__ interface and check
        # that the correct KVO events get emitted.
        observer = OCObserve.alloc().init()
        l = [1, 2, 3]
        o = TestArrayPropertyHelper.alloc().init()
        observer.register(o, 'array')

        # FIXME: the call to len shouldn't be necessary
        len(o.array)
        try:
            IS = NSIndexSet.alloc().initWithIndex_(0)
            self.assertEqual(observer.seen, {'array': []})

            o.array.append(1)

            self.assertEqual(observer.seen, {'array': [1]})
            self.assertEqual(observer.values[-1][-1]['indexes'], IS)
            self.assertEqual(observer.values[-1][-1]['new'], [1])

            o.array.append(2)
            o.array.append(3)


            self.assertEqual(o.array[0], 1)
            o.array[0] = 4
            self.assertEqual(o.array[0], 4)
            self.assertEqual(observer.seen, { 'array': [4] })
            self.assertEqual(observer.values[-1][-1]['indexes'], IS)
            self.assertEqual(observer.values[-1][-1]['old'], [1])
            self.assertEqual(observer.values[-1][-1]['new'], [4])

            o.array[-1] = 9
            self.assertEqual(o.array[2], 9)
            IS = NSIndexSet.alloc().initWithIndex_(2)
            self.assertEqual(observer.seen, { 'array': [9] })
            self.assertEqual(observer.values[-1][-1]['indexes'], IS)
            self.assertEqual(observer.values[-1][-1]['old'], [3])
            self.assertEqual(observer.values[-1][-1]['new'], [9])

            self.assertEqual(o.array[-1], 9)

            try:
                o.array[-20] = 4
            except IndexError:
                pass

            else:
                self.fail("IndexError not raised")

        finally:
            observer.unregister(o, 'array')

    def testGetSetSlice(self):
        # Same as testGetSetItem, but using slice
        observer = OCObserve.alloc().init()
        l = [1, 2, 3]
        o = TestArrayPropertyHelper.alloc().init()
        observer.register(o, 'array')

        try:
            IS = NSIndexSet.alloc().initWithIndexesInRange_((0, 3))
            IS2 = NSIndexSet.alloc().initWithIndexesInRange_((1, 2))
            IS3 = NSMutableIndexSet.alloc().init()
            IS3.addIndex_(0)
            IS3.addIndex_(2)
            self.assertEqual(observer.seen, {})

            o.array = l

            self.assertEqual(observer.seen, {'array': l})
            self.assertNotIn('indexes', observer.values[-1][-1])
            self.assertEqual(observer.values[-1][-1]['new'], [1, 2, 3])


            o.array[1:3] = [4, 5]
            self.assertEqual(o.array[0], 1)
            self.assertEqual(o.array[1], 4)
            self.assertEqual(o.array[2], 5)
            self.assertEqual(o.array,[1, 4, 5])
            self.assertEqual(observer.seen, {'array': [4, 5]})
            self.assertEqual(observer.values[-1][-1]['indexes'], IS2)
            self.assertEqual(observer.values[-1][-1]['old'], [2, 3])
            self.assertEqual(observer.values[-1][-1]['new'], [4, 5])

            self.assertEqual(o.array[0], 1)
            o.array[0:3:2] = [9, 10]
            self.assertEqual(o.array[0], 9)
            self.assertEqual(o.array[1], 4)
            self.assertEqual(o.array[2], 10)
            self.assertEqual(observer.seen, { 'array': [9, 10]})
            self.assertEqual(observer.values[-1][-1]['indexes'], IS3)
            self.assertEqual(observer.values[-1][-1]['old'], [1, 5])
            self.assertEqual(observer.values[-1][-1]['new'], [9, 10])

        finally:
            observer.unregister(o, 'array')

    def testInsert(self):
        # Use insert method and check that the correct
        # KVO events get emitted
        # Same as testGetSetItem, but using slice
        observer = OCObserve.alloc().init()
        l = [1, 2, 3]
        o = TestArrayPropertyHelper.alloc().init()
        observer.register(o, 'array')

        self.assertEqual(o.array, [])

        try:
            IS = NSIndexSet.alloc().initWithIndex_(0)
            IS1 = NSIndexSet.alloc().initWithIndex_(4)
            self.assertEqual(observer.seen, {'array': []})

            o.array = l

            self.assertEqual(observer.seen, {'array': l})
            self.assertNotIn('indexes', observer.values[-1][-1])

            self.assertEqual(o.array[0], 1)


            o.array.insert(0, 'a')
            self.assertEqual(o.array[0], 'a')
            self.assertEqual(len(o.array), 4)

            self.assertEqual(observer.seen, {'array': ['a']})
            self.assertEqual(observer.values[-1][-1]['indexes'], IS)
            self.assertNotIn('old', observer.values[-1][-1])
            self.assertEqual(observer.values[-1][-1]['new'], ['a'])

            o.array.insert(4, 'b')
            self.assertEqual(o.array[4], 'b')
            self.assertEqual(len(o.array), 5)

            self.assertEqual(observer.seen, {'array': ['b']})
            self.assertEqual(observer.values[-1][-1]['indexes'], IS1)
            self.assertNotIn('old', observer.values[-1][-1])
            self.assertEqual(observer.values[-1][-1]['new'], ['b'])

            self.assertRaises(TypeError, o.array.insert, slice(0,2), 4)
            self.assertRaises(TypeError, o.array.insert, 'a', 4)
            o.array.insert(0, 'a')

        finally:
            observer.unregister(o, 'array')

    def testPop(self):
        # Use pop method and check that the correct
        # KVO events get emitted
        observer = OCObserve.alloc().init()
        l = [1, 2, 3, 4]
        o = TestArrayPropertyHelper.alloc().init()
        observer.register(o, 'array')

        try:
            IS = NSIndexSet.alloc().initWithIndex_(0)
            IS2 = NSIndexSet.alloc().initWithIndex_(2)
            self.assertEqual(observer.seen, {})

            o.array = l

            self.assertEqual(observer.seen, {'array': l})
            self.assertNotIn('indexes', observer.values[-1][-1])

            self.assertEqual(o.array[0], 1)


            v = o.array.pop(0)
            self.assertEqual(v, 1)
            self.assertEqual(o.array[0], 2)
            self.assertEqual(len(o.array), 3)

            self.assertEqual(observer.values[-1][-1]['indexes'], IS)
            self.assertNotIn('new', observer.values[-1][-1])
            self.assertEqual(observer.values[-1][-1]['old'], [1])

            v = o.array.pop(2)
            self.assertEqual(v, 4)
            self.assertEqual(len(o.array), 2)

            self.assertEqual(observer.values[-1][-1]['indexes'], IS2)
            self.assertNotIn('new', observer.values[-1][-1])
            self.assertEqual(observer.values[-1][-1]['old'], [4])

            self.assertRaises(TypeError, o.array.pop, slice(0, 2))
            self.assertRaises(TypeError, o.array.pop, 'a')

        finally:
            observer.unregister(o, 'array')

    def testDelItem(self):
        # Use __delitem__and check that the correct
        # KVO events get emitted
        observer = OCObserve.alloc().init()
        l = [1, 2, 3, 4]
        o = TestArrayPropertyHelper.alloc().init()
        observer.register(o, 'array')

        try:
            IS = NSIndexSet.alloc().initWithIndex_(0)
            IS2 = NSIndexSet.alloc().initWithIndex_(2)
            self.assertEqual(observer.seen, {})

            o.array = l

            self.assertEqual(observer.seen, {'array': l})
            self.assertNotIn('indexes', observer.values[-1][-1])

            self.assertEqual(o.array[0], 1)


            del o.array[0]
            self.assertEqual(o.array[0], 2)
            self.assertEqual(len(o.array), 3)

            self.assertEqual(observer.values[-1][-1]['indexes'], IS)
            self.assertNotIn('new', observer.values[-1][-1])
            self.assertEqual(observer.values[-1][-1]['old'], [1])

            del o.array[2]
            self.assertEqual(len(o.array), 2)

            self.assertEqual(observer.values[-1][-1]['indexes'], IS2)
            self.assertNotIn('new', observer.values[-1][-1])
            self.assertEqual(observer.values[-1][-1]['old'], [4])

        finally:
            observer.unregister(o, 'array')

    def testDelSlice(self):
        # As testDelItem, but using slices
        observer = OCObserve.alloc().init()
        l = [1, 2, 3, 4]
        o = TestArrayPropertyHelper.alloc().init()
        observer.register(o, 'array')

        try:
            IS = NSMutableIndexSet.alloc().init()
            IS.addIndex_(0)
            IS.addIndex_(2)
            self.assertEqual(len(observer.values), 0)

            o.array = l

            self.assertEqual(observer.seen, {'array': l})
            self.assertNotIn('indexes', observer.values[-1][-1])

            self.assertEqual(o.array[0], 1)


            del o.array[0:4:2]
            self.assertEqual(o.array[0], 2)
            self.assertEqual(o.array[1], 4)
            self.assertEqual(len(o.array), 2)

            self.assertEqual(observer.values[-1][-1]['indexes'], IS)
            self.assertNotIn('new', observer.values[-1][-1])
            self.assertEqual(observer.values[-1][-1]['old'], [1, 3])

        finally:
            observer.unregister(o, 'array')

    def testExtend(self):
        observer = OCObserve.alloc().init()
        l = [1, 2, 3, 4]
        l2 = ['a', 'b', 'c']
        o = TestArrayPropertyHelper.alloc().init()
        observer.register(o, 'array')

        try:
            o.array = l

            self.assertEqual(observer.seen, {'array': l })
            self.assertEqual(o.array[0], 1)

            o.array.extend(l2)

            self.assertEqual(len(o.array), 7)
            self.assertEqual(o.array[4], 'a')

            self.assertEqual(observer.seen, {'array': l2 })
            self.assertEqual(observer.values[-1][-1]['indexes'], NSIndexSet.alloc().initWithIndexesInRange_((4, 3)))
            self.assertNotIn('old', observer.values[-1][-1])
            self.assertEqual(observer.values[-1][-1]['new'], l2)

        finally:
            observer.unregister(o, 'array')

    def testIAdd(self):
        observer = OCObserve.alloc().init()
        l = [1, 2, 3, 4]
        l2 = ['a', 'b', 'c']
        o = TestArrayPropertyHelper.alloc().init()
        observer.register(o, 'array')

        try:
            o.array = l

            self.assertEqual(observer.seen, {'array': l})
            self.assertEqual(o.array[0], 1)

            o.array += l2

            self.assertEqual(o.array, l + l2)
            self.assertEqual(len(o.array), 7)
            self.assertEqual(o.array[4], 'a')

            self.assertEqual(observer.seen, {'array': l + l2})
            self.assertEqual(observer.values[-2][-1]['indexes'], NSIndexSet.alloc().initWithIndexesInRange_((4, 3)))
            self.assertNotIn('old', observer.values[-2][-1])
            self.assertEqual(observer.values[-2][-1]['new'], l2)

            self.assertNotIn('indexes', observer.values[-1][-1])

            before = observer.values[:]
            v = o.array + l2
            self.assertEqual(observer.values, before)
            self.assertEqual(v, l + l2 + l2)
            self.assertIsInstance(v, list)

        finally:
            observer.unregister(o, 'array')


    def testIMul(self):
        observer = OCObserve.alloc().init()
        l = [1, 2]
        o = TestArrayPropertyHelper.alloc().init()
        observer.register(o, 'array')

        try:
            o.array = l

            self.assertEqual(observer.seen, {'array': l})
            self.assertEqual(o.array[0], 1)

            observer.values[:] = []
            o.array *= 3

            self.assertEqual(len(o.array), 6)
            self.assertEqual(o.array[0], 1)
            self.assertEqual(o.array[1], 2)
            self.assertEqual(o.array[2], 1)
            self.assertEqual(o.array[3], 2)
            self.assertEqual(o.array[4], 1)
            self.assertEqual(o.array[5], 2)

            self.assertEqual(observer.seen, {'array': [ 1, 2, 1, 2, 1, 2]})
            self.assertEqual(observer.values[-2][-1]['indexes'], NSIndexSet.alloc().initWithIndexesInRange_((2, 4)))
            self.assertNotIn('old', observer.values[-2][-1])
            self.assertEqual(observer.values[-2][-1]['new'], [ 1, 2, 1, 2])

            self.assertEqual(len(observer.values), 2)
            self.assertNotIn('indexes', observer.values[-1][-1])

            before = observer.values[:]
            n = o.array * 4
            self.assertEqual(observer.values, before)
            self.assertEqual(n, [1,2]* 3 * 4)
            self.assertIsInstance(n, list)

            try:
                o.array *= 'a'
            except TypeError:
                pass

            else:
                self.fail("array * 'a' didn't raise exception")

        finally:
            observer.unregister(o, 'array')


    def testSort(self):
        # Use sort method and check that the correct
        # KVO events get emitted
        observer = OCObserve.alloc().init()
        l = [2, 4, 1, 3]
        o = TestArrayPropertyHelper.alloc().init()
        observer.register(o, 'array')

        try:
            IS = NSIndexSet.alloc().initWithIndexesInRange_((0, 4))
            self.assertEqual(observer.seen, {})

            orig_l = l[:]
            o.array = l


            self.assertEqual(observer.seen, {'array': l })
            self.assertNotIn('indexes', observer.values[-1][-1])

            self.assertEqual(o.array[0], 2)

            o.array.sort()

            self.assertEqual(o.array[0], 1)
            self.assertEqual(o.array[1], 2)
            self.assertEqual(o.array[2], 3)
            self.assertEqual(o.array[3], 4)
            self.assertEqual(len(o.array), 4)

            self.assertEqual(observer.seen, {'array': [1,2,3,4]})
            self.assertEqual(observer.values[-1][-1]['indexes'], IS)
            self.assertEqual(observer.values[-1][-1]['old'], l)
            self.assertEqual(observer.values[-1][-1]['new'], [1,2,3,4])
            self.assertEqual(orig_l, l)

        finally:
            observer.unregister(o, 'array')

    def testReverse(self):
        # Use reverse method and check that the correct
        # KVO events get emitted
        observer = OCObserve.alloc().init()
        l = [2, 4, 1, 3]
        o = TestArrayPropertyHelper.alloc().init()
        observer.register(o, 'array')

        try:
            IS = NSIndexSet.alloc().initWithIndexesInRange_((0, 4))
            self.assertEqual(observer.seen, {})

            orig_l = l[:]
            o.array = l


            self.assertEqual(observer.seen, {'array': l })
            self.assertNotIn('indexes', observer.values[-1][-1])

            self.assertEqual(o.array[0], 2)

            o.array.reverse()

            self.assertEqual(o.array[0], 3)
            self.assertEqual(o.array[1], 1)
            self.assertEqual(o.array[2], 4)
            self.assertEqual(o.array[3], 2)
            self.assertEqual(len(o.array), 4)

            self.assertEqual(observer.seen, {'array': [3, 1, 4, 2]})
            self.assertEqual(observer.values[-1][-1]['indexes'], IS)
            self.assertEqual(observer.values[-1][-1]['old'], l)
            self.assertEqual(observer.values[-1][-1]['new'], [3, 1, 4, 2])
            self.assertEqual(orig_l, l)

        finally:
            observer.unregister(o, 'array')

    def testObjCAccessors(self):
        # Check that the right ObjC array accessors are defined and work properly
        self.assertTrue(TestArrayPropertyHelper.instancesRespondToSelector_(b"setArray:"))
        self.assertTrue(TestArrayPropertyHelper.instancesRespondToSelector_(b"array"))
        self.assertTrue(TestArrayPropertyHelper.instancesRespondToSelector_(b"countOfArray"))
        self.assertTrue(TestArrayPropertyHelper.instancesRespondToSelector_(b"objectInArrayAtIndex:"))
        self.assertTrue(TestArrayPropertyHelper.instancesRespondToSelector_(b"insertObject:inArrayAtIndex:"))
        self.assertTrue(TestArrayPropertyHelper.instancesRespondToSelector_(b"removeObjectFromArrayAtIndex:"))
        self.assertTrue(TestArrayPropertyHelper.instancesRespondToSelector_(b"replaceObjectInArrayAtIndex:withObject:"))

        o = TestArrayPropertyHelper.alloc().init()
        self.assertEqual(0, o.pyobjc_instanceMethods.countOfArray())
        self.assertRaises(AttributeError, getattr, o, 'countOfArray')

        o.pyobjc_instanceMethods.insertObject_inArrayAtIndex_('a', 0)
        self.assertEqual(1, o.pyobjc_instanceMethods.countOfArray())
        self.assertEqual('a', o.array[0])
        self.assertEqual('a', o.pyobjc_instanceMethods.objectInArrayAtIndex_(0))
        o.pyobjc_instanceMethods.replaceObjectInArrayAtIndex_withObject_(0, 'b')
        self.assertEqual('b', o.array[0])
        o.pyobjc_instanceMethods.removeObjectFromArrayAtIndex_(0)
        self.assertEqual(0, o.pyobjc_instanceMethods.countOfArray())


    # Verify docs and/or implementation to check for other
    # mutating methods

    def testReadingMethods(self):
        # Check that all read-only methods work as well

        o = TestArrayPropertyHelper.alloc().init()
        o.array = [1, 2, 3, 4]

        self.assertIsNotInstance(o.array, list)

        self.assertEqual(o.array, [1,2,3,4])
        self.assertNotEqual(o.array, [1,2,3,4, 5])

        self.assertEqual(o.array.count(1), 1)
        self.assertEqual(o.array.index(4), 3)


        self.assertTrue(o.array < [1,2,3,4,5])
        self.assertTrue(o.array <= [1,2,3,4,5])
        self.assertTrue(o.array <= [1,2,3,4])
        self.assertTrue(o.array >= [1,2,3,4])
        self.assertTrue(o.array > [1,2,3])


    def testMutatingReadonlyProperty(self):
        # Check that trying to mutate a read-only property
        # will raise an exception
        o = TestArrayPropertyHelper.alloc().init()

        o._roArray = [1, 2, 3]

        self.assertEqual(list(o.roArray), [1,2,3])

        self.assertRaises(ValueError, o.roArray.append,1)
        self.assertRaises(ValueError, o.roArray.extend, [1,2])
        self.assertRaises(ValueError, o.roArray.sort)
        self.assertRaises(ValueError, o.roArray.reverse)
        self.assertRaises(ValueError, o.roArray.pop)
        try:
            o.roArray[0] = 2
        except ValueError:
            pass
        else:
            self.fail("ValueError not raised")

        try:
            del o.roArray[0]
        except ValueError:
            pass
        else:
            self.fail("ValueError not raised")

        try:
            o.roArray += [4]
        except ValueError:
            pass
        else:
            self.fail("ValueError not raised")

        try:
            o.roArray *= 4
        except ValueError:
            pass
        else:
            self.fail("TypeError not raised")


    def testMutatingReadonlyPropertyObjC(self):
        # Check that trying to mutate a read-only property
        # from ObjC will raise an exception
        o = TestArrayPropertyHelper.alloc().init()
        o._roArray = [1,2,3]
        self.assertEqual(3, o.pyobjc_instanceMethods.countOfRoArray())
        self.assertRaises(AttributeError, getattr, o, 'countOfRoArray')

        try:
            o.pyobjc_instanceMethods.insertObject_inRoArrayAtIndex_('a', 0)
        except ValueError:
            pass
        else:
            self.fail("ValueError not raised")

        self.assertEqual(3, o.pyobjc_instanceMethods.countOfRoArray())
        self.assertEqual(1, o.pyobjc_instanceMethods.objectInRoArrayAtIndex_(0))
        try:
            o.pyobjc_instanceMethods.replaceObjectInRoArrayAtIndex_withObject_(0, 'b')
        except ValueError:
            pass
        else:
            self.fail("ValueError not raised")

        try:
            o.pyobjc_instanceMethods.removeObjectFromRoArrayAtIndex_(0)
        except ValueError:
            pass
        else:
            self.fail("ValueError not raised")


    def testAssingmentInteraction(self):
        o = TestArrayPropertyHelper.alloc().init()
        array = o.array

        o.array.append(1)
        self.assertEqual(len(o.array), 1)
        self.assertEqual(len(array), 1)

    def testPickling(self):
        o = TestArrayPropertyHelper.alloc().init()
        o.array.extend([3,4,5])

        self.assertFalse(isinstance(o.array, list))

        p = pickle.dumps(o.array)
        v = pickle.loads(p)
        self.assertEqual(v, o.array)
        self.assertTrue(isinstance(v, list))

    def testRepr(self):
        o = TestArrayPropertyHelper.alloc().init()
        o.array.extend([3,4,5])

        self.assertFalse(isinstance(o.array, list))

        self.assertEqual(repr(o.array), '<array proxy for property array %r>'%([3,4,5],))

    def testFinding(self):
        o = TestArrayPropertyHelper.alloc().init()
        o.array.extend([3,4,5,4])

        self.assertEqual(0, o.array.index(3))
        self.assertEqual(2, o.array.count(4))

    def testCompare(self):
        o = TestArrayPropertyHelper.alloc().init()
        o.array.extend([3,4,5])
        o.array2.extend([4,5])

        self.assertFalse(o.array == o.array2)
        self.assertFalse(o.array ==  [4,5])
        self.assertTrue(o.array ==  [3,4,5])

        self.assertTrue(o.array != o.array2)
        self.assertTrue(o.array !=  [4,5])
        self.assertFalse(o.array !=  [3,4,5])

        o.array2.insert(0, 3)
        self.assertFalse(o.array != o.array2)
        self.assertTrue(o.array == o.array2)

        o.array2 = [4,5]
        self.assertTrue(o.array < o.array2)
        self.assertTrue(o.array < [4,5])
        self.assertFalse(o.array2 < o.array)
        self.assertFalse(o.array2 < [4,5])
        self.assertTrue(o.array2 <= o.array2)
        self.assertTrue(o.array2 <= [4,5])

        self.assertTrue(o.array <= o.array2)
        self.assertTrue(o.array <= [4,5])
        self.assertFalse(o.array2 <= o.array)

        self.assertFalse(o.array > o.array2)
        self.assertFalse(o.array > [4,5])
        self.assertTrue(o.array2 > o.array)
        self.assertFalse(o.array2 > [4,5])

        self.assertFalse(o.array >= o.array2)
        self.assertFalse(o.array >= [4,5])
        self.assertTrue(o.array2 >= o.array)
        self.assertTrue(o.array2 >= [4,5])
        self.assertTrue(o.array2 >= o.array2)

        if sys.version_info[0] == 2:
            n = cmp(o.array2, o.array)
            self.assertEqual(n, 1)

            n = cmp(o.array2, [3,4,5])
            self.assertEqual(n, 1)

            n = cmp([3,4,5], o.array2)
            self.assertEqual(n, -1)

            n = o.array2.__cmp__(o.array)
            self.assertEqual(n, 1)

            n = o.array2.__cmp__([3,4,5])
            self.assertEqual(n, 1)


    def testGetAttr(self):
        o = TestArrayPropertyHelper.alloc().init()
        o.array = [1,2,3]
        v = o.array
        self.assertEqual(v.count('a'), 0)
        self.assertEqual(list(v.__reversed__()), [3,2,1]) 

        self.assertRaises(AttributeError, getattr, o.array, 'nosuchattribute')



if __name__ == "__main__":
    main()
