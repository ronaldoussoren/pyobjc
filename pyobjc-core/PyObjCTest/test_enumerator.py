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
    def test_enumerate_beyond_end(self):
        value = OC_Enumeration.consumeDictKeyIteratorPlusOne_(DictOne())
        self.assertEqual(value, ["a", "b"])

    def test_enumeration_raises(self):
        with self.assertRaisesRegex(ValueError, "done enough"):
            OC_Enumeration.consumeDictKeyIteratorPlusOne_(DictRaises())
