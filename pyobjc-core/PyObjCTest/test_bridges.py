from PyObjCTools.TestSupport import *
from PyObjCTest.testbndl import OC_TestClass2
import objc
import collections
import sys

if sys.version_info[0] == 2:
    from UserList import  UserList
    from UserDict import  IterableUserDict

else:
    from collections import UserDict as IterableUserDict, UserList

NSMutableArray = objc.lookUpClass("NSMutableArray")
NSMutableDictionary = objc.lookUpClass("NSMutableDictionary")

def classOfProxy(value):
    return OC_TestClass2.classOfObject_(value)


class TestBridges (TestCase):
    # NOTE: the two "register" functions from objc._bridges aren't
    # tested explictly, but the tests in this class do verify that
    # the default registrations (which are made through those two
    # functions) work properly.

    def test_xrange(self):
        range_type = range if sys.version_info[0] == 3 else xrange

        v = range_type(0, 10)
        self.assertTrue(issubclass(classOfProxy(v), NSMutableArray))

    def test_user_collectons(self):
        # Note: Not "UserDict" because UserDict doesn't implement
        # __iter__ and hence isn't a collections.Mapping, and doesn't
        # implement enough API to implement the NSDictionary interface.
        v = IterableUserDict()
        self.assertTrue(issubclass(classOfProxy(v), NSMutableDictionary))

        v = UserList()
        self.assertTrue(issubclass(classOfProxy(v), NSMutableArray))

    def test_abc(self):
        class MySequence (collections.Sequence):
            def __getitem__(self, idx):
                raise IndexError(idx)

            def __len__(self):
                return 0

        class MyDictionary (collections.Mapping):
            def __getitem__(self, key):
                raise KeyError(key)

            def __len__(self):
                return 0

            def __iter__(self):
                return
                yield

        v = MyDictionary()
        self.assertTrue(issubclass(classOfProxy(v), NSMutableDictionary))

        v = MySequence()
        self.assertTrue(issubclass(classOfProxy(v), NSMutableArray))


if __name__ == "__main__":
    main()
