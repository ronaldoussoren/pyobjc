import pickle

import objc
from PyObjCTest.test_object_property import OCObserve
from PyObjCTools.TestSupport import TestCase

NSObject = objc.lookUpClass("NSObject")


class TestSetPropertyHelper(NSObject):
    aSet = objc.set_property()
    aSet2 = objc.set_property()
    aROSet = objc.set_property(read_only=True)


class TestSetProperty(TestCase):
    def testCopying(self):
        o = TestSetPropertyHelper.alloc().init()
        aSet = {1, 2}
        o.aSet = aSet

        self.assertEqual(len(o.aSet), 2)
        self.assertEqual(len(aSet), 2)
        aSet.add(3)
        self.assertEqual(len(o.aSet), 2)
        self.assertEqual(len(aSet), 3)

    def testRepr(self):
        o = TestSetPropertyHelper.alloc().init()
        aSet = {1, 2}
        o.aSet = aSet

        self.assertEqual(repr(o.aSet), f"<set proxy for property aSet {aSet!r}>")

    def testDefault(self):
        with OCObserve.alloc().init() as observer:
            o = TestSetPropertyHelper.alloc().init()

            observer.register(o, "aSet")

            o.aSet = set()
            self.assertEqual(observer.seen, {"aSet": set()})

            self.assertEqual(len(o.aSet), 0)
            o.aSet.add("a")
            o.aSet.add("b")
            self.assertEqual(len(o.aSet), 2)
            self.assertEqual(observer.seen, {"aSet": {"b"}})

            self.assertEqual(observer.values[-2][-1]["kind"], 2)
            self.assertNotIn("old", observer.values[-2][-1])
            self.assertEqual(observer.values[-2][-1]["new"], set("a"))

            self.assertEqual(observer.values[-1][-1]["kind"], 2)
            self.assertNotIn("old", observer.values[-1][-1])
            self.assertEqual(observer.values[-1][-1]["new"], set("b"))

            v = list(o.aSet)
            v.sort()
            self.assertEqual(v, ["a", "b"])

            self.assertEqual(o.aSet, {"a", "b"})

            proxy = o.aSet

            o.aSet.clear()
            self.assertEqual(len(o.aSet), 0)
            self.assertEqual(len(proxy), 0)

            self.assertEqual(observer.values[-1][-1]["old"], {"a", "b"})
            self.assertNotIn("new", observer.values[-1][-1])

    def testForwarding(self):
        o = TestSetPropertyHelper.alloc().init()
        o.aSet = set()

        self.assertTrue(o.aSet.issubset({1, 2}))

    def testSetting(self):
        o = TestSetPropertyHelper.alloc().init()
        s = {1, 2}
        o.aSet = s
        self.assertEqual(o.aSet, s)
        s.add(3)
        self.assertNotEqual(o.aSet, s)
        o.aSet2 = o.aSet
        o.aSet.add(4)
        self.assertNotEqual(o.aSet, o.aSet2)

        v = o.aSet
        o._aSet = None
        self.assertEqual(v, set())

    def testDifferenceUpdate(self):
        with OCObserve.alloc().init() as observer:
            o = TestSetPropertyHelper.alloc().init()

            o.aSet.add(1)
            o.aSet.add(2)
            o.aSet.add(3)

            observer.register(o, "aSet")

            o.aSet.difference_update({1, 4})
            self.assertEqual(o.aSet, {2, 3})

            self.assertEqual(len(observer.values), 1)
            self.assertEqual(observer.values[-1][-1]["kind"], 3)
            self.assertNotIn("new", observer.values[-1][-1])
            self.assertEqual(observer.values[-1][-1]["old"], {1})

    def testSymmetricDifferenceUpdate(self):
        with OCObserve.alloc().init() as observer:
            o = TestSetPropertyHelper.alloc().init()

            o.aSet = {1, 2, 3}

            observer.register(o, "aSet")

            self.assertEqual(len(observer.values), 0)
            o.aSet.symmetric_difference_update({1, 4})
            self.assertEqual(o.aSet, {2, 3, 4})

            self.assertEqual(len(observer.values), 2)

            haveAdd = False
            haveRemove = False

            for i in 0, 1:
                if observer.values[i][-1]["kind"] == 3:
                    # Remove
                    self.assertNotIn("new", observer.values[i][-1])
                    self.assertEqual(observer.values[i][-1]["old"], {1})
                    haveRemove = True

                elif observer.values[i][-1]["kind"] == 2:
                    # Remove
                    self.assertNotIn("old", observer.values[i][-1])
                    self.assertEqual(observer.values[i][-1]["new"], {4})
                    haveAdd = True

                else:
                    self.fail("Unexpected update kind")

            if not haveAdd and haveRemove:
                self.fail("Do not have both an add and remove notification")

    def testUpdate(self):
        with OCObserve.alloc().init() as observer:
            o = TestSetPropertyHelper.alloc().init()
            observer.register(o, "aSet")
            self.assertEqual(o.aSet, set())
            self.assertEqual(len(observer.values), 1)

            o.aSet.update([1, 2, 3])
            self.assertEqual(len(observer.values), 2)
            self.assertEqual(observer.values[-1][-1]["kind"], 2)
            self.assertNotIn("old", observer.values[-1][-1])
            self.assertEqual(observer.values[-1][-1]["new"], {1, 2, 3})

            o.aSet.update({3, 4, 5})
            self.assertEqual(len(observer.values), 3)
            self.assertEqual(observer.values[-1][-1]["kind"], 2)
            self.assertNotIn("old", observer.values[-1][-1])
            self.assertEqual(observer.values[-1][-1]["new"], {4, 5})

    def testAddDiscard(self):
        with OCObserve.alloc().init() as observer:
            o = TestSetPropertyHelper.alloc().init()
            observer.register(o, "aSet")

            o.aSet.add(1)
            self.assertEqual(observer.seen, {"aSet": {1}})
            self.assertNotIn("old", observer.values[-1][-1])
            self.assertEqual(observer.values[-1][-1]["new"], {1})

            o.aSet.discard(1)
            self.assertNotIn("new", observer.values[-1][-1])
            self.assertEqual(observer.values[-1][-1]["old"], {1})

            o.aSet.discard(2)
            self.assertNotIn("new", observer.values[-1][-1])
            self.assertEqual(observer.values[-1][-1]["old"], set())

    def testAddRemove(self):
        with OCObserve.alloc().init() as observer:
            o = TestSetPropertyHelper.alloc().init()
            observer.register(o, "aSet")

            o.aSet.add(1)
            self.assertEqual(observer.seen, {"aSet": {1}})
            self.assertNotIn("old", observer.values[-1][-1])
            self.assertEqual(observer.values[-1][-1]["new"], {1})

            o.aSet.remove(1)
            self.assertNotIn("new", observer.values[-1][-1])
            self.assertEqual(observer.values[-1][-1]["old"], {1})

            with self.assertRaisesRegex(KeyError, "2"):
                o.aSet.remove(2)
            self.assertNotIn("new", observer.values[-1][-1])
            self.assertEqual(observer.values[-1][-1]["old"], set())

            o.aSet.add(1)
            o.aSet.add(2)
            v = o.aSet.pop()
            self.assertTrue(v in (1, 2))
            self.assertNotIn("new", observer.values[-1][-1])
            self.assertEqual(observer.values[-1][-1]["old"], {v})

            o.aSet = set()
            with self.assertRaisesRegex(KeyError, "'Empty set'"):
                o.aSet.pop()

    def testOperators(self):
        with OCObserve.alloc().init() as observer:
            o = TestSetPropertyHelper.alloc().init()
            o.aSet = {1, 2, 3}

            observer.register(o, "aSet")
            self.assertEqual(observer.seen, {})

            self.assertEqual(o.aSet - {2}, {1, 3})
            self.assertEqual(o.aSet, {1, 2, 3})

            self.assertEqual(o.aSet | {4}, {1, 2, 3, 4})
            self.assertEqual(o.aSet, {1, 2, 3})

            self.assertEqual(o.aSet & {3, 4}, {3})
            self.assertEqual(o.aSet, {1, 2, 3})

            self.assertEqual(o.aSet ^ {3, 4}, {1, 2, 4})
            self.assertEqual(o.aSet, {1, 2, 3})

    def testInplace(self):
        # FIXME: the disabled lines in this test indicate a problem in
        # either the set_proxy implementation, or my understanding of
        # unordered collection properties.
        with OCObserve.alloc().init() as observer:
            o = TestSetPropertyHelper.alloc().init()
            o.aSet.add(1)
            observer.register(o, "aSet")

            # The inplace operators aren't actually implemented, which means
            # "o.aSet |= value" is actually  "o.aSet = o.aSet | value" and
            # we get the some KVO notificatons as when a new value is set.

            self.assertEqual(o.aSet, {1})
            o.aSet |= {2, 3}
            self.assertEqual(o.aSet, {1, 2, 3})
            self.assertEqual(len(observer.values), 2)
            self.assertEqual(observer.values[-1][-1]["kind"], 1)
            # self.assertEqual(observer.values[-1][-1]['old'], {1})
            self.assertEqual(observer.values[-1][-1]["new"], {1, 2, 3})

            self.assertEqual(o.aSet, {1, 2, 3})
            o.aSet &= {3, 4}
            self.assertEqual(o.aSet, {3})
            self.assertEqual(len(observer.values), 4)
            self.assertEqual(observer.values[-1][-1]["kind"], 1)
            # self.assertEqual(observer.values[-1][-1]['old'], {1,2,3})
            # self.assertEqual(observer.values[-1][-1]['new'], {3})

            self.assertEqual(o.aSet, {3})
            o.aSet -= {3}
            self.assertEqual(o.aSet, set())
            self.assertEqual(len(observer.values), 6)
            self.assertEqual(observer.values[-1][-1]["kind"], 1)
            # self.assertEqual(observer.values[-1][-1]['old'], {3})
            # self.assertEqual(observer.values[-1][-1]['new'], set())

            o.aSet = {1, 2, 3}
            # self.assertEqual(len(observer.values), 8)

            self.assertEqual(o.aSet, {1, 2, 3})
            o.aSet ^= {1, 4}
            self.assertEqual(o.aSet, {2, 3, 4})
            # self.assertEqual(len(observer.values), 9)
            self.assertEqual(observer.values[-1][-1]["kind"], 1)
            # self.assertEqual(observer.values[-1][-1]['old'], {1,2,3})
            # self.assertEqual(observer.values[-1][-1]['new'], {2,3,4})

    def testObjCAccessors(self):
        # Check that the right ObjC array accessors are defined and work properly
        self.assertTrue(TestSetPropertyHelper.instancesRespondToSelector_(b"setASet:"))
        self.assertTrue(TestSetPropertyHelper.instancesRespondToSelector_(b"aSet"))
        self.assertTrue(
            TestSetPropertyHelper.instancesRespondToSelector_(b"countOfASet")
        )
        self.assertTrue(
            TestSetPropertyHelper.instancesRespondToSelector_(b"enumeratorOfASet")
        )
        self.assertTrue(
            TestSetPropertyHelper.instancesRespondToSelector_(b"memberOfASet:")
        )
        self.assertTrue(TestSetPropertyHelper.instancesRespondToSelector_(b"addASet:"))
        self.assertTrue(
            TestSetPropertyHelper.instancesRespondToSelector_(b"addASetObject:")
        )
        self.assertTrue(
            TestSetPropertyHelper.instancesRespondToSelector_(b"removeASet:")
        )
        self.assertTrue(
            TestSetPropertyHelper.instancesRespondToSelector_(b"removeASetObject:")
        )

        o = TestSetPropertyHelper.alloc().init()
        self.assertEqual(0, o.pyobjc_instanceMethods.countOfASet())
        with self.assertRaisesRegex(
            AttributeError,
            "'TestSetPropertyHelper' object has no attribute 'countOfASet'",
        ):
            o.countOfASet
        o.aSet.add(1)
        o.aSet.add(2)

        v = sorted(o.pyobjc_instanceMethods.enumeratorOfASet())
        self.assertEqual(v, [1, 2])

        class Testing:
            def __hash__(self):
                return 42

            def __eq__(self, other):
                return isinstance(other, Testing)

        p = Testing()
        o.aSet.add(p)

        v = o.pyobjc_instanceMethods.memberOfASet_(Testing())
        self.assertIs(p, v)
        v = o.pyobjc_instanceMethods.memberOfASet_(9)
        self.assertIs(v, None)

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

    def test_ro_set(self):
        o = TestSetPropertyHelper.alloc().init()
        o._aROSet = {1, 2, 3, 4}

        self.assertEqual(o.aROSet, {1, 2, 3, 4})
        self.assertIsNot(type(o.aROSet), set)

        with self.assertRaisesRegex(ValueError, "Property 'aROSet' is read-only"):
            o.aROSet.add(1)
        with self.assertRaisesRegex(ValueError, "Property 'aROSet' is read-only"):
            o.aROSet.clear()
        with self.assertRaisesRegex(ValueError, "Property 'aROSet' is read-only"):
            o.aROSet.pop()
        with self.assertRaisesRegex(ValueError, "Property 'aROSet' is read-only"):
            o.aROSet.remove(1)
        with self.assertRaisesRegex(ValueError, "Property 'aROSet' is read-only"):
            o.aROSet.difference_update({1, 2})
        with self.assertRaisesRegex(ValueError, "Property 'aROSet' is read-only"):
            o.aROSet.intersection_update({1, 2})
        with self.assertRaisesRegex(ValueError, "Property 'aROSet' is read-only"):
            o.aROSet.symmetric_difference_update({1, 2})
        with self.assertRaisesRegex(ValueError, "Property 'aROSet' is read-only"):
            o.aROSet.update({1, 2})
        with self.assertRaisesRegex(ValueError, "Property 'aROSet' is read-only"):
            o.aROSet.discard(4)

        try:
            o.aROSet |= {1, 2}
        except ValueError:
            pass
        else:
            self.fail()

        try:
            o.aROSet -= {1, 2}
        except ValueError:
            pass
        else:
            self.fail()

        try:
            o.aROSet ^= {1, 2}
        except ValueError:
            pass
        else:
            self.fail()

        try:
            o.aROSet &= {1, 2}
        except ValueError:
            pass
        else:
            self.fail()

    def test_compare(self):
        o = TestSetPropertyHelper.alloc().init()
        o.aSet = {1, 2, 3}
        o.aSet2 = {1, 2, 3}

        self.assertTrue(o.aSet == o.aSet2)
        self.assertTrue(o.aSet == {1, 2, 3})
        self.assertTrue(o.aSet <= o.aSet2)
        self.assertTrue(o.aSet <= {1, 2, 3})
        self.assertTrue(o.aSet >= o.aSet2)
        self.assertTrue(o.aSet >= {1, 2, 3})
        self.assertFalse(o.aSet != o.aSet2)
        self.assertFalse(o.aSet != {1, 2, 3})

        o.aSet2 = {2, 3}
        self.assertTrue(o.aSet != o.aSet2)
        self.assertTrue(o.aSet != {1, 2})
        self.assertFalse(o.aSet == o.aSet2)
        self.assertFalse(o.aSet == {1, 2})

        o.aSet2 = {1, 2, 3, 4}
        self.assertTrue(o.aSet < o.aSet2)
        self.assertTrue(o.aSet < {1, 2, 3, 4})
        self.assertTrue(o.aSet <= o.aSet2)
        self.assertTrue(o.aSet <= {1, 2, 3, 4})
        self.assertFalse(o.aSet > o.aSet2)
        self.assertFalse(o.aSet > {1, 2, 3, 4})
        self.assertFalse(o.aSet >= o.aSet2)
        self.assertFalse(o.aSet >= {1, 2, 3, 4})

        o.aSet2 = {1}
        self.assertTrue(o.aSet > o.aSet2)
        self.assertTrue(o.aSet > {1})
        self.assertTrue(o.aSet >= o.aSet2)
        self.assertTrue(o.aSet >= {1})
        self.assertFalse(o.aSet < o.aSet2)
        self.assertFalse(o.aSet < {1})
        self.assertFalse(o.aSet <= o.aSet2)
        self.assertFalse(o.aSet <= {1})

    def testPickling(self):
        o = TestSetPropertyHelper.alloc().init()
        o.aSet = {1, 2, 3}

        self.assertFalse(isinstance(o.aSet, set))

        p = pickle.dumps(o.aSet)
        v = pickle.loads(p)
        self.assertEqual(o.aSet, v)
        self.assertTrue(isinstance(v, set))
