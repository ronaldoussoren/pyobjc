import objc
from PyObjCTest.testbndl import OC_TestClass2
from PyObjCTools.TestSupport import TestCase

from collections import UserDict as IterableUserDict, UserList
import collections.abc

NSMutableArray = objc.lookUpClass("NSMutableArray")
NSMutableDictionary = objc.lookUpClass("NSMutableDictionary")


def classOfProxy(value):
    return OC_TestClass2.classOfObject_(value)


class TestBridges(TestCase):
    # NOTE: the two "register" functions from objc._bridges aren't
    # tested explictly, but the tests in this class do verify that
    # the default registrations (which are made through those two
    # functions) work properly.

    def test_range(self):
        v = range(0, 10)
        self.assertIsSubclass(classOfProxy(v), NSMutableArray)

    def test_user_collections(self):
        # Note: Not "UserDict" because UserDict doesn't implement
        # __iter__ and hence isn't a collections.abc.Mapping, and doesn't
        # implement enough API to implement the NSDictionary interface.
        v = IterableUserDict()
        self.assertIsSubclass(classOfProxy(v), NSMutableDictionary)

        v = UserList()
        self.assertIsSubclass(classOfProxy(v), NSMutableArray)

    def test_abc(self):
        class MySequence(collections.abc.Sequence):
            def __getitem__(self, idx):
                raise IndexError(idx)

            def __len__(self):
                return 0

        class MyDictionary(collections.abc.Mapping):
            def __getitem__(self, key):
                raise KeyError(key)

            def __len__(self):
                return 0

            def __iter__(self):
                return
                yield

        v = MyDictionary()
        self.assertIsSubclass(classOfProxy(v), NSMutableDictionary)

        v = MySequence()
        self.assertIsSubclass(classOfProxy(v), NSMutableArray)
