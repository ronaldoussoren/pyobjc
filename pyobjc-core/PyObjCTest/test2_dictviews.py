"""
test.test_dictview from python2.7 adapted
for testing NSMutableDictionary
"""
from PyObjCTools.TestSupport import *

import objc
NSDictionary = objc.lookUpClass('NSDictionary')
NSMutableDictionary = objc.lookUpClass('NSMutableDictionary')


import unittest

class DictSetTest(TestCase):

    def test_constructors_not_callable(self): pass

    def test_dict_keys(self):
        d = NSMutableDictionary({1: 10, "a": "ABC"})
        keys = d.viewkeys()
        self.assertEqual(len(keys), 2)
        self.assertEqual(set(keys), set([1, "a"]))
        self.assertEqual(keys, set([1, "a"]))
        self.assertNotEqual(keys, set([1, "a", "b"]))
        self.assertNotEqual(keys, set([1, "b"]))
        self.assertNotEqual(keys, set([1]))
        self.assertNotEqual(keys, 42)
        self.assertIn(1, keys)
        self.assertIn("a", keys)
        self.assertNotIn(10, keys)
        self.assertNotIn("Z", keys)
        self.assertEqual(d.viewkeys(), d.viewkeys())
        e = NSMutableDictionary({1: 11, "a": "def"})
        self.assertEqual(d.viewkeys(), e.viewkeys())
        del e["a"]
        self.assertNotEqual(d.viewkeys(), e.viewkeys())

    def test_dict_items(self):
        d = NSMutableDictionary({1: 10, "a": "ABC"})
        items = d.viewitems()
        self.assertEqual(len(items), 2)
        self.assertEqual(set(items), set([(1, 10), ("a", "ABC")]))
        self.assertEqual(items, set([(1, 10), ("a", "ABC")]))
        self.assertNotEqual(items, set([(1, 10), ("a", "ABC"), "junk"]))
        self.assertNotEqual(items, set([(1, 10), ("a", "def")]))
        self.assertNotEqual(items, set([(1, 10)]))
        self.assertNotEqual(items, 42)
        self.assertIn((1, 10), items)
        self.assertIn(("a", "ABC"), items)
        self.assertNotIn((1, 11), items)
        self.assertNotIn(1, items)
        self.assertNotIn((), items)
        self.assertNotIn((1,), items)
        self.assertNotIn((1, 2, 3), items)
        self.assertEqual(d.viewitems(), d.viewitems())
        e = d.mutableCopy()
        self.assertEqual(d.viewitems(), e.viewitems())
        e["a"] = "def"
        self.assertNotEqual(d.viewitems(), e.viewitems())

    def test_dict_mixed_keys_items(self):
        d = NSMutableDictionary({(1, 1): 11, (2, 2): 22})
        e = NSMutableDictionary({1: 1, 2: 2})
        self.assertEqual(d.viewkeys(), e.viewitems())
        self.assertNotEqual(d.viewitems(), e.viewkeys())

    def test_dict_values(self):
        d = NSMutableDictionary({1: 10, "a": "ABC"})
        values = d.viewvalues()
        self.assertEqual(set(values), set([10, "ABC"]))
        self.assertEqual(len(values), 2)

    def test_dict_repr(self): pass

    def test_keys_set_operations(self):
        d1 = NSMutableDictionary({u'a': 1, u'b': 2})
        d2 = NSMutableDictionary({u'b': 3, u'c': 2})
        d3 = NSMutableDictionary({u'd': 4, u'e': 5})
        self.assertEqual(d1.viewkeys() & d1.viewkeys(), set((u'a', u'b')))
        self.assertEqual(d1.viewkeys() & d2.viewkeys(), set((u'b')))
        self.assertEqual(d1.viewkeys() & d3.viewkeys(), set())
        self.assertEqual(d1.viewkeys() & set(d1.viewkeys()), set((u'a', u'b')))
        self.assertEqual(d1.viewkeys() & set(d2.viewkeys()), set((u'b')))
        self.assertEqual(d1.viewkeys() & set(d3.viewkeys()), set())

        self.assertEqual(d1.viewkeys() | d1.viewkeys(), set((u'a', u'b')))
        self.assertEqual(d1.viewkeys() | d2.viewkeys(), set((u'a', u'b', u'c')))
        self.assertEqual(d1.viewkeys() | d3.viewkeys(), set((u'a', u'b', u'd', u'e')))
        self.assertEqual(d1.viewkeys() | set(d1.viewkeys()), set((u'a', u'b')))
        self.assertEqual(d1.viewkeys() | set(d2.viewkeys()), set((u'a', u'b', u'c')))
        self.assertEqual(d1.viewkeys() | set(d3.viewkeys()),
                         set((u'a', u'b', u'd', u'e')))

        self.assertEqual(d1.viewkeys() ^ d1.viewkeys(), set())
        self.assertEqual(d1.viewkeys() ^ d2.viewkeys(), set((u'a', u'c')))
        self.assertEqual(d1.viewkeys() ^ d3.viewkeys(), set((u'a', u'b', u'd', u'e')))
        self.assertEqual(d1.viewkeys() ^ set(d1.viewkeys()), set())
        self.assertEqual(d1.viewkeys() ^ set(d2.viewkeys()), set((u'a', u'c')))
        self.assertEqual(d1.viewkeys() ^ set(d3.viewkeys()),
                         set((u'a', u'b', u'd', u'e')))

    def test_items_set_operations(self):
        d1 = NSMutableDictionary({u'a': 1, u'b': 2})
        d2 = NSMutableDictionary({u'a': 2, u'b': 2})
        d3 = NSMutableDictionary({u'd': 4, u'e': 5})
        self.assertEqual(
            d1.viewitems() & d1.viewitems(), set(((u'a', 1), (u'b', 2))))
        self.assertEqual(d1.viewitems() & d2.viewitems(), set(((u'b', 2),)))
        self.assertEqual(d1.viewitems() & d3.viewitems(), set())
        self.assertEqual(d1.viewitems() & set(d1.viewitems()),
                         set(((u'a', 1), (u'b', 2))))
        self.assertEqual(d1.viewitems() & set(d2.viewitems()), set(((u'b', 2),)))
        self.assertEqual(d1.viewitems() & set(d3.viewitems()), set())

        self.assertEqual(d1.viewitems() | d1.viewitems(),
                         set(((u'a', 1), (u'b', 2))))
        self.assertEqual(d1.viewitems() | d2.viewitems(),
                         set(((u'a', 1), (u'a', 2), (u'b', 2))))
        self.assertEqual(d1.viewitems() | d3.viewitems(),
                         set(((u'a', 1), (u'b', 2), (u'd', 4), (u'e', 5))))
        self.assertEqual(d1.viewitems() | set(d1.viewitems()),
                         set(((u'a', 1), (u'b', 2))))
        self.assertEqual(d1.viewitems() | set(d2.viewitems()),
                         set(((u'a', 1), (u'a', 2), (u'b', 2))))
        self.assertEqual(d1.viewitems() | set(d3.viewitems()),
                         set(((u'a', 1), (u'b', 2), (u'd', 4), (u'e', 5))))

        self.assertEqual(d1.viewitems() ^ d1.viewitems(), set())
        self.assertEqual(d1.viewitems() ^ d2.viewitems(),
                         set(((u'a', 1), (u'a', 2))))
        self.assertEqual(d1.viewitems() ^ d3.viewitems(),
                         set(((u'a', 1), (u'b', 2), (u'd', 4), (u'e', 5))))




if __name__ == "__main__":
    main()
