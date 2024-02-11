import objc
import pathlib
from PyObjCTools.TestSupport import TestCase

NSMutableArray = objc.lookUpClass("NSMutableArray")
NSURL = objc.lookUpClass("NSURL")


class TestURLProxy(TestCase):
    def test_basic_construction(self):
        a = NSMutableArray.array()
        p = pathlib.Path(__file__)
        a.addObject_(p)

        self.assertIn(p, a)

        (valueClass,) = a.valueForKeyPath_("@unionOfObjects.class")
        self.assertEqual(valueClass.__name__, "OC_PythonURL")

        (description,) = a.valueForKeyPath_("@unionOfObjects.description")
        self.assertEqual(description, "file://" + __file__)
