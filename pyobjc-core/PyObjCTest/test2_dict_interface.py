"""
test.test_dict from python 2.7 adapted for testing NSMutableDictionary
"""
from PyObjCTools.TestSupport import *

import objc
import operator
NSDictionary = objc.lookUpClass('NSDictionary')
NSMutableDictionary = objc.lookUpClass('NSMutableDictionary')

import test.test_dict


class TestDict (test.test_dict.DictTest, TestCase):
    def setUp(self):
        test.test_dict.dict = NSMutableDictionary

    def tearDown(self):
        del test.test_dict.dict

    def test_literal_constructor(self): pass

    def test_pyobjc_update(self):
        value  = NSMutableDictionary(a=1, b=2)
        self.assertRaises(TypeError, value.update, {'a':3}, {'b':4})
        self.assertEqual(value, dict(a=1, b=2))

        value.update(a=3, c=4)
        self.assertEqual(value, dict(a=3, b=2, c=4))

    def test_bool(self):
        self.assertIs(not NSMutableDictionary(), True)
        self.assertTrue(NSMutableDictionary({1: 2}))
        self.assertIs(bool(NSMutableDictionary()), False)
        self.assertIs(bool(NSMutableDictionary({1: 2})), True)

    def test_keys(self):
        d = NSMutableDictionary()
        self.assertEqual(d.keys(), [])
        d = NSMutableDictionary({'a': 1, 'b': 2})
        k = d.keys()
        self.assertTrue(d.has_key('a'))
        self.assertTrue(d.has_key('b'))

        self.assertRaises(TypeError, d.keys, None)

    def test_values(self):
        d = NSMutableDictionary({})
        self.assertEqual(d.values(), [])
        d = NSMutableDictionary({1:2})
        self.assertEqual(d.values(), [2])

        self.assertRaises(TypeError, d.values, None)

    def test_items(self):
        d = NSMutableDictionary({})
        self.assertEqual(d.items(), [])

        d = NSMutableDictionary({1:2})
        self.assertEqual(d.items(), [(1, 2)])

        self.assertRaises(TypeError, d.items, None)

    def test_has_key(self):
        d = NSMutableDictionary({})
        self.assertFalse(d.has_key('a'))
        d = NSMutableDictionary({'a': 1, 'b': 2})
        k = list(d.keys())
        k.sort()
        self.assertEqual(k, ['a', 'b'])

        self.assertRaises(TypeError, d.has_key)

    def test_contains(self):
        d = NSMutableDictionary({})
        self.assertNotIn('a', d)
        self.assertFalse('a' in d)
        self.assertTrue('a' not in d)
        d = NSMutableDictionary({'a': 1, 'b': 2})
        self.assertIn('a', d)
        self.assertIn('b', d)
        self.assertNotIn('c', d)

        self.assertRaises(TypeError, d.__contains__)

    def test_len(self):
        d = NSMutableDictionary({})
        self.assertEqual(len(d), 0)
        d = NSMutableDictionary({'a': 1, 'b': 2})
        self.assertEqual(len(d), 2)

    def test_getitem(self):
        d = NSMutableDictionary({'a': 1, 'b': 2})
        self.assertEqual(d['a'], 1)
        self.assertEqual(d['b'], 2)
        d['c'] = 3
        d['a'] = 4
        self.assertEqual(d['c'], 3)
        self.assertEqual(d['a'], 4)
        del d['b']
        self.assertEqual(d, {'a': 4, 'c': 3})

        self.assertRaises(TypeError, d.__getitem__)

        class BadEq(object):
            def __eq__(self, other):
                raise Exc()
            def __hash__(self):
                return 24

        d = NSMutableDictionary({})
        d[BadEq()] = 42
        self.assertRaises(KeyError, d.__getitem__, 23)

        class Exc(Exception): pass

        class BadHash(object):
            fail = False
            def __hash__(self):
                if self.fail:
                    raise Exc()
                else:
                    return 42

        #x = BadHash()
        #d[x] = 42
        #x.fail = True
        #self.assertRaises(Exc, d.__getitem__, x)

    def test_clear(self):
        d = NSMutableDictionary({1:1, 2:2, 3:3})
        d.clear()
        self.assertEqual(d, {})

        self.assertRaises(TypeError, d.clear, None)

    def test_update(self):
        d = NSMutableDictionary({})
        d.update({1:100})
        d.update({2:20})
        d.update({1:1, 2:2, 3:3})
        self.assertEqual(d, {1:1, 2:2, 3:3})

        d.update()
        self.assertEqual(d, {1:1, 2:2, 3:3})

        self.assertRaises((TypeError, AttributeError), d.update, None)

        class SimpleUserDict:
            def __init__(self):
                self.d = {1:1, 2:2, 3:3}
            def keys(self):
                return self.d.keys()
            def __getitem__(self, i):
                return self.d[i]
        d.clear()
        d.update(SimpleUserDict())
        self.assertEqual(d, {1:1, 2:2, 3:3})

        class Exc(Exception): pass

        d.clear()
        class FailingUserDict:
            def keys(self):
                raise Exc()
        self.assertRaises(Exc, d.update, FailingUserDict())

        class FailingUserDict:
            def keys(self):
                class BogonIter:
                    def __init__(self):
                        self.i = 1
                    def __iter__(self):
                        return self
                    def next(self):
                        if self.i:
                            self.i = 0
                            return 'a'
                        raise Exc()
                return BogonIter()
            def __getitem__(self, key):
                return key
        self.assertRaises(Exc, d.update, FailingUserDict())

        class FailingUserDict:
            def keys(self):
                class BogonIter:
                    def __init__(self):
                        self.i = ord('a')
                    def __iter__(self):
                        return self
                    def next(self):
                        if self.i <= ord('z'):
                            rtn = chr(self.i)
                            self.i += 1
                            return rtn
                        raise StopIteration()
                return BogonIter()
            def __getitem__(self, key):
                raise Exc()
        self.assertRaises(Exc, d.update, FailingUserDict())

        class badseq(object):
            def __iter__(self):
                return self
            def next(self):
                raise Exc()

        self.assertRaises(Exc, NSMutableDictionary({}).update, badseq())

        self.assertRaises(ValueError, NSMutableDictionary({}).update, [(1, 2, 3)])

    def test_fromkeys(self):
        self.assertEqual(NSMutableDictionary.fromkeys('abc'), {'a':None, 'b':None, 'c':None})
        d = NSMutableDictionary({})
        self.assertIsNot(d.fromkeys('abc'), d)
        self.assertEqual(d.fromkeys('abc'), {'a':None, 'b':None, 'c':None})
        self.assertEqual(d.fromkeys((4,5),0), {4:0, 5:0})
        self.assertEqual(d.fromkeys([]), {})
        def g():
            yield 1
        self.assertEqual(d.fromkeys(g()), {1:None})
        self.assertRaises(TypeError, NSMutableDictionary({}).fromkeys, 3)
        #class dictlike(dict): pass
        #self.assertEqual(dictlike.fromkeys('a'), {'a':None})
        #self.assertEqual(dictlike().fromkeys('a'), {'a':None})
        #self.assertIsInstance(dictlike.fromkeys('a'), dictlike)
        #self.assertIsInstance(dictlike().fromkeys('a'), dictlike)
        #class mydict(dict):
        #    def __new__(cls):
        #        return UserDict.UserDict()
        #ud = mydict.fromkeys('ab')
        #self.assertEqual(ud, {'a':None, 'b':None})
        #self.assertIsInstance(ud, UserDict.UserDict)
        #self.assertRaises(TypeError, dict.fromkeys)

        class Exc(Exception): pass

        #class baddict1(dict):
        #    def __init__(self):
        #        raise Exc()

        #self.assertRaises(Exc, baddict1.fromkeys, [1])

        class BadSeq(object):
            def __iter__(self):
                return self
            def next(self):
                raise Exc()

        self.assertRaises(Exc, NSMutableDictionary.fromkeys, BadSeq())

        #class baddict2(dict):
        #    def __setitem__(self, key, value):
        #        raise Exc()

        #self.assertRaises(Exc, baddict2.fromkeys, [1])

        # test fast path for dictionary inputs
        d = NSMutableDictionary(zip(range(6), range(6)))
        self.assertEqual(NSMutableDictionary.fromkeys(d, 0), NSMutableDictionary(zip(range(6), [0]*6)))

    def test_copy(self):
        d = NSMutableDictionary({1:1, 2:2, 3:3})
        self.assertEqual(d.copy(), {1:1, 2:2, 3:3})
        self.assertEqual(NSMutableDictionary({}).copy(), {})
        self.assertRaises(TypeError, d.copy, None)

    def test_get(self):
        d = NSMutableDictionary({})
        self.assertIs(d.get('c'), None)
        self.assertEqual(d.get('c', 3), 3)
        d = NSMutableDictionary({'a': 1, 'b': 2})
        self.assertIs(d.get('c'), None)
        self.assertEqual(d.get('c', 3), 3)
        self.assertEqual(d.get('a'), 1)
        self.assertEqual(d.get('a', 3), 1)
        self.assertRaises(TypeError, d.get)
        self.assertRaises(TypeError, d.get, None, None, None)

    def test_setdefault(self):
        # dict.setdefault()
        d = NSMutableDictionary({})
        self.assertIs(d.setdefault('key0'), None)
        d.setdefault('key0', [])
        self.assertIs(d.setdefault('key0'), None)
        d.setdefault('key', []).append(3)
        self.assertEqual(d['key'][0], 3)
        d.setdefault('key', []).append(4)
        self.assertEqual(len(d['key']), 2)
        self.assertRaises(TypeError, d.setdefault)

        class Exc(Exception): pass

        class BadHash(object):
            fail = False
            def __hash__(self):
                if self.fail:
                    raise Exc()
                else:
                    return 42

        #x = BadHash()
        #d[x] = 42
        #x.fail = True
        #self.assertRaises(Exc, d.setdefault, x, [])

    def test_popitem(self):
        # dict.popitem()
        for copymode in -1, +1:
            # -1: b has same structure as a
            # +1: b is a.copy()
            for log2size in range(12):
                size = 2**log2size
                a = NSMutableDictionary({})
                b = NSMutableDictionary({})
                for i in range(size):
                    a[repr(i)] = i
                    if copymode < 0:
                        b[repr(i)] = i
                if copymode > 0:
                    b = a.mutableCopy()
                for i in range(size):
                    ka, va = ta = a.popitem()
                    self.assertEqual(va, int(ka))
                    kb, vb = tb = b.popitem()
                    self.assertEqual(vb, int(kb))
                    self.assertFalse(copymode < 0 and ta != tb)
                self.assertFalse(a)
                self.assertFalse(b)

        d = NSMutableDictionary({})
        self.assertRaises(KeyError, d.popitem)

    def test_pop(self):
        # Tests for pop with specified key
        d = NSMutableDictionary({})
        k, v = 'abc', 'def'
        d[k] = v
        self.assertRaises(KeyError, d.pop, 'ghi')

        self.assertEqual(d.pop(k), v)
        self.assertEqual(len(d), 0)

        self.assertRaises(KeyError, d.pop, k)

        # verify longs/ints get same value when key > 32 bits
        # (for 64-bit archs).  See SF bug #689659.
        x = 4503599627370496L
        y = 4503599627370496
        h = NSMutableDictionary({x: 'anything', y: 'something else'})
        self.assertEqual(h[x], h[y])

        self.assertEqual(d.pop(k, v), v)
        d[k] = v
        self.assertEqual(d.pop(k, 1), v)

        self.assertRaises(TypeError, d.pop)

        class Exc(Exception): pass

        class BadHash(object):
            fail = False
            def __hash__(self):
                if self.fail:
                    raise Exc()
                else:
                    return 42

        #x = BadHash()
        #d[x] = 42
        #x.fail = True
        #self.assertRaises(Exc, d.pop, x)

    def test_mutatingiteration(self):
        # XXX: Reimplement iteration using NSFastIteration,
        return

        # changing dict size during iteration
        d = NSMutableDictionary({})
        d[1] = 1
        try:
            for i in d:
                d[i+1] = 1
        except RuntimeError:
            pass
        else:
            self.fail("RuntimeError not raised")

    def test_repr(self): pass
    def test_le(self): pass
    def test_missing(self): pass
    def test_tuple_keyerror(self):
        # SF #1576657
        d = NSMutableDictionary()
        try:
            d[(1,)]
        except KeyError as exc:
            pass
        else:
            fail("KeyError not raised")
        self.assertEqual(exc.args, ((1,),))

    @onlyIf(0, "Test not relevant for PyObjC")
    def test_bad_key(self): pass

    @onlyIf(0, "Test not relevant for PyObjC")
    def test_resize1(self): pass

    @onlyIf(0, "Test not relevant for PyObjC")
    def test_resize2(self): pass

    @onlyIf(0, "Test not relevant for PyObjC")
    def test_empty_presized_dict_in_freelist(self): pass

    @onlyIf(0, "Test not relevant for PyObjC")
    def test_container_iterator(self): pass

    @onlyIf(0, "Test not relevant for PyObjC")
    def test_track_literals(self): pass

    @onlyIf(0, "Test not relevant for PyObjC")
    def test_track_dynamic(self): pass

    @onlyIf(0, "Test not relevant for PyObjC")
    def test_track_subtypes(self): pass

    @onlyIf(0, "Test not relevant for PyObjC")
    def test_free_after_iterating(self): pass

class GeneralMappingTests (test.test_dict.GeneralMappingTests):
    type2test = NSMutableDictionary


class TestPyObjCDict (TestCase):
    #def test_comparison(self):
    #    self.fail()

    def test_creation(self):
        for dict_type in (NSDictionary, NSMutableDictionary):
            v = dict_type()
            self.assertIsInstance(v, dict_type)
            self.assertEqual(len(v), 0)

            v = dict_type({1:2, 2:3})
            self.assertIsInstance(v, dict_type)
            self.assertEqual(len(v), 2)
            self.assertEqual(v[1], 2)
            self.assertEqual(v[2], 3)

            v = dict_type([(1, -1), (2, 9)])
            self.assertIsInstance(v, dict_type)
            self.assertEqual(len(v), 2)
            self.assertEqual(v[1], -1)
            self.assertEqual(v[2], 9)

            v = dict_type(v for v in [(1, -1), (2, 9)])
            self.assertIsInstance(v, dict_type)
            self.assertEqual(len(v), 2)
            self.assertEqual(v[1], -1)
            self.assertEqual(v[2], 9)

            self.assertRaises(TypeError, dict_type, (1,2), (3,4))

            v = dict_type(a=3, b=4)
            self.assertEqual(len(v), 2)
            self.assertEqual(v['a'], 3)
            self.assertEqual(v['b'], 4)

            v = dict_type((v for v in [(1, -1), (2, 9)]), a='hello', b='world')
            self.assertIsInstance(v, dict_type)
            self.assertEqual(len(v), 4)
            self.assertEqual(v[1], -1)
            self.assertEqual(v[2], 9)
            self.assertEqual(v['a'], 'hello')
            self.assertEqual(v['b'], 'world')

    def test_values(self):
        py = dict(a=4, b=3)
        oc = NSDictionary(a=4, b=3)

        self.assertIn(4, py.values())
        self.assertIn(4, oc.values())
        self.assertNotIn(9, py.values())
        self.assertNotIn(9, oc.values())

    def test_view_set(self):
        oc = NSDictionary(a=1, b=2, c=3, d=4, e=5)

        v = oc.viewkeys() | {'a', 'f' }
        self.assertEqual(v, {'a', 'b', 'c', 'd', 'e', 'f' })
        self.assertIsInstance(v, set)
        self.assertRaises(TypeError, operator.or_, oc.viewkeys(), ('a', 'f'))
        self.assertRaises(TypeError, operator.or_, ('a', 'f'), oc.keys())

        v = oc.viewkeys() & {'a', 'f' }
        self.assertEqual(v, {'a'})
        self.assertIsInstance(v, set)
        self.assertRaises(TypeError, operator.and_, oc.viewkeys(), ('a', 'f'))
        self.assertRaises(TypeError, operator.and_, ('a', 'f'), oc.keys())

        v = oc.viewkeys() ^ {'a', 'f' }
        self.assertEqual(v, {'b', 'c', 'd', 'e', 'f'})
        self.assertIsInstance(v, set)
        self.assertRaises(TypeError, operator.xor, oc.viewkeys(), ('a', 'f'))
        self.assertRaises(TypeError, operator.xor, ('a', 'f'), oc.keys())

        v = oc.viewkeys() - {'a', 'f' }
        self.assertEqual(v, {'b', 'c', 'd', 'e'})
        self.assertIsInstance(v, set)
        self.assertRaises(TypeError, operator.sub, oc.viewkeys(), ('a', 'f'))
        self.assertRaises(TypeError, operator.sub, ('a', 'f'), oc.keys())

        self.assertTrue(operator.lt(oc.viewkeys(), ('a', 'f')))
        self.assertTrue(operator.le(oc.viewkeys(), ('a', 'f')))
        self.assertFalse(operator.gt(oc.viewkeys(), ('a', 'f')))
        self.assertFalse(operator.ge(oc.viewkeys(), ('a', 'f')))



        v = oc.viewvalues() | {1, 9 }
        self.assertEqual(v, {1,2,3,4,5,9})
        self.assertIsInstance(v, set)
        self.assertRaises(TypeError, operator.or_, oc.viewvalues(), (1, 9))
        self.assertRaises(TypeError, operator.or_, (1, 9), oc.viewvalues())

        v = oc.viewvalues() & {1, 9 }
        self.assertEqual(v, {1})
        self.assertIsInstance(v, set)
        self.assertRaises(TypeError, operator.and_, oc.viewvalues(), (1, 9))
        self.assertRaises(TypeError, operator.and_, (1, 9), oc.viewvalues())

        v = oc.viewvalues() ^ {1, 9 }
        self.assertEqual(v, {2, 3, 4, 5, 9})
        self.assertIsInstance(v, set)
        self.assertRaises(TypeError, operator.xor, oc.viewvalues(), (1, 9))
        self.assertRaises(TypeError, operator.xor, (1, 9), oc.viewvalues())

        v = oc.viewvalues() - {1, 9 }
        self.assertEqual(v, {2,3,4,5})
        self.assertIsInstance(v, set)
        self.assertRaises(TypeError, operator.sub, oc.viewvalues(), (1, 9))
        self.assertRaises(TypeError, operator.sub, (1, 9), oc.viewvalues())

        self.assertTrue(operator.lt(oc.viewvalues(), (1, 9)))
        self.assertTrue(operator.le(oc.viewvalues(), (1, 9)))
        self.assertFalse(operator.gt(oc.viewvalues(), (1, 9)))
        self.assertFalse(operator.ge(oc.viewvalues(), (1, 9)))



        v = oc.viewitems() | {('a', 1), ('f', 9) }
        self.assertEqual(v, {('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 9)})
        self.assertIsInstance(v, set)
        self.assertRaises(TypeError, operator.or_, oc.viewitems(), (('a', 1), ('f', 9)))
        self.assertRaises(TypeError, operator.or_, (1, 9), oc.viewitems())

        v = oc.viewitems() & {('a',1), ('f',9)}
        self.assertEqual(v, {('a', 1)})
        self.assertIsInstance(v, set)
        self.assertRaises(TypeError, operator.and_, oc.viewitems(), (('a', 1), ('f', 9)))
        self.assertRaises(TypeError, operator.and_, (('a', 1), ('f', 9)), oc.viewitems())

        v = oc.viewitems() ^ {('a',1), ('f',9)}
        self.assertEqual(v, {('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 9)})
        self.assertIsInstance(v, set)
        self.assertRaises(TypeError, operator.xor, oc.viewitems(), (('a', 1), ('f', 9)))
        self.assertRaises(TypeError, operator.xor, (('a', 1), ('f', 9)), oc.viewitems())

        v = oc.viewitems() - {('a',1), ('f',9)}
        self.assertEqual(v, {('b', 2), ('c', 3), ('d', 4), ('e', 5)})
        self.assertIsInstance(v, set)
        self.assertRaises(TypeError, operator.sub, oc.viewitems(), (('a', 1), ('f', 9)))
        self.assertRaises(TypeError, operator.sub, (('a', 1), ('f', 9)), oc.viewitems())

        self.assertTrue(operator.lt(oc.viewitems(), (('a', 1), ('f', 9))))
        self.assertTrue(operator.le(oc.viewitems(), (('a', 1), ('f', 9))))
        self.assertFalse(operator.gt(oc.viewitems(), (('a', 1), ('f', 9))))
        self.assertFalse(operator.ge(oc.viewitems(), (('a', 1), ('f', 9))))


if __name__ == "__main__":
    main()
