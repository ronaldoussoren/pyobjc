import array
from collections import UserDict, UserList
import datetime
import sys

from PyObjCTest.classes import OCTestClasses
from PyObjCTools.TestSupport import TestCase
import objc


class TestBridgedClasses(TestCase):
    def test_dict(self):
        value = {}
        cls = OCTestClasses.classForObject_(value)
        self.assertEqual(cls.__name__, "OC_BuiltinPythonDictionary")

    def test_mapping(self):
        value = UserDict()
        cls = OCTestClasses.classForObject_(value)
        self.assertEqual(cls.__name__, "OC_PythonDictionary")

        class D(dict):
            pass

        value = D()
        cls = OCTestClasses.classForObject_(value)
        self.assertEqual(cls.__name__, "OC_PythonDictionary")

    def test_tuple(self):
        value = ()
        cls = OCTestClasses.classForObject_(value)
        self.assertEqual(cls.__name__, "OC_BuiltinPythonArray")

    def test_list(self):
        value = []
        cls = OCTestClasses.classForObject_(value)
        self.assertEqual(cls.__name__, "OC_BuiltinPythonArray")

    def test_sequence(self):
        value = UserList()
        cls = OCTestClasses.classForObject_(value)
        self.assertEqual(cls.__name__, "OC_PythonArray")

        class L(list):
            pass

        value = L()
        cls = OCTestClasses.classForObject_(value)
        self.assertEqual(cls.__name__, "OC_PythonArray")

        class T(tuple):
            pass

        value = T()
        cls = OCTestClasses.classForObject_(value)
        self.assertEqual(cls.__name__, "OC_PythonArray")

    def test_set(self):
        value = set()
        cls = OCTestClasses.classForObject_(value)
        self.assertEqual(cls.__name__, "OC_BuiltinPythonSet")

        value = frozenset()
        cls = OCTestClasses.classForObject_(value)
        self.assertEqual(cls.__name__, "OC_BuiltinPythonSet")

    def test_set_subclass(self):
        class S(set):
            pass

        value = S()
        cls = OCTestClasses.classForObject_(value)
        self.assertEqual(cls.__name__, "OC_PythonSet")

    def test_unicode(self):
        value = "hello"
        cls = OCTestClasses.classForObject_(value)
        self.assertEqual(cls.__name__, "OC_BuiltinPythonUnicode")

    def test_unicode_subclass(self):
        class U(str):
            pass

        value = U()
        cls = OCTestClasses.classForObject_(value)
        self.assertEqual(cls.__name__, "OC_PythonUnicode")

    def test_bytes(self):
        value = b""
        cls = OCTestClasses.classForObject_(value)
        self.assertEqual(cls.__name__, "OC_BuiltinPythonData")

    def test_bytes_subclass(self):
        class B(bytes):
            pass

        value = B()
        cls = OCTestClasses.classForObject_(value)
        self.assertEqual(cls.__name__, "OC_PythonData")

    def test_bool(self):
        value = True
        cls = OCTestClasses.classForObject_(value)
        self.assertTrue(issubclass(cls, objc.lookUpClass("NSNumber")))

        value = False
        cls = OCTestClasses.classForObject_(value)
        self.assertTrue(issubclass(cls, objc.lookUpClass("NSNumber")))

    def test_integers(self):
        value = sys.maxsize
        cls = OCTestClasses.classForObject_(value)
        self.assertEqual(cls.__name__, "OC_BuiltinPythonNumber")

        value = sys.maxsize**2
        cls = OCTestClasses.classForObject_(value)
        self.assertEqual(cls.__name__, "OC_BuiltinPythonNumber")

    def test_integer_subclass(self):
        class I(int):  # noqa: E742
            pass

        value = I()
        cls = OCTestClasses.classForObject_(value)
        self.assertEqual(cls.__name__, "OC_PythonNumber")

        class L(type(sys.maxsize * 2)):
            pass

        value = L()
        cls = OCTestClasses.classForObject_(value)
        self.assertEqual(cls.__name__, "OC_PythonNumber")

    def test_float(self):
        value = 0.5
        cls = OCTestClasses.classForObject_(value)
        self.assertEqual(cls.__name__, "OC_BuiltinPythonNumber")

    def test_float_subclass(self):
        class F(float):
            pass

        value = F()
        cls = OCTestClasses.classForObject_(value)
        self.assertEqual(cls.__name__, "OC_PythonNumber")

    def test_date(self):
        value = datetime.date.today()
        cls = OCTestClasses.classForObject_(value)
        self.assertEqual(cls.__name__, "OC_BuiltinPythonDate")

        value = datetime.datetime.now()
        cls = OCTestClasses.classForObject_(value)
        self.assertEqual(cls.__name__, "OC_BuiltinPythonDate")

        class MyDate(datetime.datetime):
            pass

        value = MyDate.now()
        cls = OCTestClasses.classForObject_(value)
        self.assertEqual(cls.__name__, "OC_PythonDate")

    def test_array(self):
        value = array.array("B", [200, 150, 80, 20])
        cls = OCTestClasses.classForObject_(value)
        self.assertEqual(cls.__name__, "OC_PythonData")

        d = objc.lookUpClass("NSData").dataWithData_(value)
        self.assertIsNot(d, None)

    def test_memoryview(self):
        value = memoryview(b"hello")
        cls = OCTestClasses.classForObject_(value)
        self.assertEqual(cls.__name__, "OC_PythonData")

    def test_arbitrary(self):
        value = object()
        cls = OCTestClasses.classForObject_(value)
        self.assertEqual(cls.__name__, "OC_PythonObject")

        value = object
        cls = OCTestClasses.classForObject_(value)
        self.assertEqual(cls.__name__, "OC_PythonObject")

        class O:  # noqa: E742
            pass

        value = O()
        cls = OCTestClasses.classForObject_(value)
        self.assertEqual(cls.__name__, "OC_PythonObject")
