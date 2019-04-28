from PyObjCTools.TestSupport import *
from PyObjCTest.testbndl import OC_TestClass2
import objc
import sys

if sys.version_info[0] == 2:
    from UserList import UserList
    from UserDict import IterableUserDict
    import collections as collections_abc

else:
    from collections import UserDict as IterableUserDict, UserList
    import collections.abc as collections_abc

NSMutableArray = objc.lookUpClass("NSMutableArray")
NSMutableDictionary = objc.lookUpClass("NSMutableDictionary")


def classOfProxy(value):
    return OC_TestClass2.classOfObject_(value)


class TestBridges(TestCase):
    # NOTE: the two "register" functions from objc._bridges aren't
    # tested explictly, but the tests in this class do verify that
    # the default registrations (which are made through those two
    # functions) work properly.

    def test_xrange(self):
        range_type = range if sys.version_info[0] == 3 else xrange

        v = range_type(0, 10)
        self.assertIsSubclass(classOfProxy(v), NSMutableArray)

    def test_user_collections(self):
        # Note: Not "UserDict" because UserDict doesn't implement
        # __iter__ and hence isn't a collections_abc.Mapping, and doesn't
        # implement enough API to implement the NSDictionary interface.
        v = IterableUserDict()
        self.assertIsSubclass(classOfProxy(v), NSMutableDictionary)

        v = UserList()
        self.assertIsSubclass(classOfProxy(v), NSMutableArray)

    def test_abc(self):
        class MySequence(collections_abc.Sequence):
            def __getitem__(self, idx):
                raise IndexError(idx)

            def __len__(self):
                return 0

        class MyDictionary(collections_abc.Mapping):
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


if __name__ == "__main__":
    main()
