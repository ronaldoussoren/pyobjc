from PyObjCTools.TestSupport import TestCase

from .enumeration import OC_Enumeration


class DictOne(dict):
    def keys(self):
        yield "a"
        yield "b"


class DictRaises(dict):
    def keys(self):
        yield "a"
        raise ValueError("done enough")


class TestEnumerationEdges(TestCase):
    def test_enumerate_beyond_end_of_dict(self):
        import tracemalloc
        import objc

        dct = {"x": 1, "y": 2, "z": 3}

        with objc.autorelease_pool():
            value = OC_Enumeration.consumeDictKeyIteratorPlusOne_(dct)
            self.assertEqual(set(value), {"x", "y", "z"})
            del value

        tracemalloc.start(1)
        before, _ = tracemalloc.get_traced_memory()

        N = 30_000
        with objc.autorelease_pool():
            for _ in range(N):
                value = OC_Enumeration.consumeDictKeyIteratorPlusOne_(dct)
                # self.assertEqual(set(value), {"x", "y", "z"})
                del value
        after, _ = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        self.assertEqual((after - before) // N, 0)

    def test_enumerate_beyond_end(self):
        value = OC_Enumeration.consumeDictKeyIteratorPlusOne_(DictOne())
        self.assertEqual(value, ["a", "b"])

    def test_enumeration_raises(self):
        with self.assertRaisesRegex(ValueError, "done enough"):
            OC_Enumeration.consumeDictKeyIteratorPlusOne_(DictRaises())
