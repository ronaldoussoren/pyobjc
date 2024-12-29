"""
Testcases for NSArchive-ing python objects.

(Implementation is incomplete)
"""

import pickle
import sys
import test.pickletester
import collections
import pathlib

import objc
import objc._pycoder as pycoder
from PyObjCTest.fnd import (
    NSArchiver,
    NSArray,
    NSData,
    NSDictionary,
    NSKeyedArchiver,
    NSKeyedUnarchiver,
    NSMutableArray,
    NSMutableData,
    NSMutableDictionary,
    NSSet,
    NSString,
    NSUnarchiver,
    NSURL,
)
from PyObjCTools.TestSupport import (
    TestCase,
    skipUnless,
    expectedFailure,
    expectedFailureIf,
    min_os_level,
    os_level_key,
    os_release,
    pyobjc_options,
    cast_ulonglong,
)

import copyreg

#
# First set of tests: the stdlib tests for pickling, this
# should test everything but mixed Python/Objective-C
# object-graphs.
#

MyList = test.pickletester.MyList


class float_subclass(float):
    pass


class tuple_subclass(tuple):
    pass


class list_subclass(list):
    pass


class dict_subclass(dict):
    pass


class set_subclass(set):
    pass


class frozenset_subclass(frozenset):
    pass


class with_getstate:
    def __init__(self, value=None):
        self.value = value

    def __getstate__(self):
        return self.value

    def __setstate__(self, value):
        self.value = value


class only_getstate:
    def __init__(self, slots=None, dct=None):
        self._slots = slots
        self._dct = dct

    def __getstate__(self):
        return (self._dct, self._slots)


class with_reduce_func:
    def __init__(self, *args):
        self.args = args

    def __reduce__(self):
        return with_reduce_func, self.args


class reduce_global:
    def __reduce__(self):
        return "reduce_global"


reduce_global = reduce_global()


def C__repr__(self):
    # Quick hack to add a proper __repr__ to class C in
    # pickletester, makes it a lot easier to debug.
    return "<{} instance at {:#x}: {!r}>".format(
        self.__class__.__name__,
        id(self),
        self.__dict__,
    )


test.pickletester.C.__repr__ = C__repr__
del C__repr__


class myobject:
    def __init__(self):
        pass

    def __getinitargs__(self):
        return (1, 2)


class state_obj_1:
    def __getstate__(self):
        return ({"a": 1, 42: 3}, {"b": 2})


class mystr(str):
    __slots__ = ()


class myint(int):
    __slots__ = ()


def a_function():
    pass


class a_classic_class:
    pass


class a_classic_class_with_state:
    def __getstate__(self):
        return {"a": 1}

    def __setstate__(self, state):
        for k, v in state.items():
            # XXX: BPO 46903: In a --with-pydebug build the
            #      attribute name must have the exact type 'str'.
            #
            #      This workaround makes is possible to run
            #      the test suite.
            # assert isinstance(k, (str, objc.pyobjc_unicode))
            # setattr(self, str(k), v)
            setattr(self, k, v)


class a_newstyle_class:
    pass


class newstyle_with_slots:
    __slots__ = ("a", "b", "__dict__")


class newstyle_with_setstate:
    def __setstate__(self, state):
        self.state = state


def make_instance(state):
    o = a_reducing_class()
    o.__dict__.update(state)
    return o


class a_reducing_class:
    def __reduce__(self):
        return make_instance, (self.__dict__,)


class TestInterning(TestCase):
    def test_intern_string(self):
        v = "hello"
        w = "hel"
        w += "lo"
        self.assertIsNot(v, w)
        self.assertEqual(v, w)

        iv = pycoder.intern(v)
        iw = pycoder.intern(w)
        self.assertIs(iv, iw)
        self.assertEqual(iv, v)

    def test_intern_oc_string(self):
        v = NSString.stringWithString_("hello")
        w = "hel"
        w += "lo"

        iv = pycoder.intern(v)
        iw = pycoder.intern(w)
        self.assertEqual(iv, v)
        self.assertIsInstance(iv, str)
        self.assertIs(iv, iw)

    def test_intern_other(self):
        v = 400000 - 1
        w = 400000 - 2
        v += 1
        w += 2

        self.assertIsNot(v, w)
        self.assertEqual(v, w)

        iv = pycoder.intern(v)
        iw = pycoder.intern(w)

        self.assertEqual(iv, iw)
        self.assertEqual(iv, v)

        self.assertIs(iv, v)
        self.assertIs(iw, w)
        self.assertIsNot(iw, iv)


class TestKeyedArchiveSimple(TestCase):
    def setUp(self):
        self.isKeyed = True
        self.archiverClass = NSKeyedArchiver
        self.unarchiverClass = NSKeyedUnarchiver

    def test_without_helper(self):
        orig = objc.options._nscoding_decoder
        try:
            objc.options._nscoding_decoder = None

            p = object()

            buf = self.archiverClass.archivedDataWithRootObject_(p)
            self.assertIsInstance(buf, NSData)

            with self.assertRaisesRegex(
                ValueError, "decoding Python objects is not supported"
            ):
                self.unarchiverClass.unarchiveObjectWithData_(buf)

        finally:
            objc.options._nscoding_decoder = orig

    def test_roundtrip_pathlib_path(self):
        p = pathlib.Path(__file__)

        buf = self.archiverClass.archivedDataWithRootObject_(p)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertNotIsInstance(v, pathlib.Path)
        self.assertIsInstance(v, NSURL)
        self.assertEqual(v, p)

    def test_global_from_main(self):
        import __main__ as mod

        class Foo:
            pass

        Foo.__module__ = None
        Foo.__qualname__ = "Foo"
        mod.Foo = Foo
        objc.Foo = "hello"
        self.assertIs(mod.Foo.__module__, None)
        self.assertEqual(mod.Foo.__qualname__, "Foo")

        buf = self.archiverClass.archivedDataWithRootObject_(Foo)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIs(v, Foo)

        del mod.Foo
        del objc.Foo

        with self.assertRaises(pickle.PicklingError):
            buf = self.archiverClass.archivedDataWithRootObject_(Foo)

    def test_unknown_type(self):
        try:
            orig = pycoder.decode_dispatch[pycoder.kOP_GLOBAL]
            del pycoder.decode_dispatch[pycoder.kOP_GLOBAL]

            o = TestKeyedArchiveSimple
            buf = self.archiverClass.archivedDataWithRootObject_(o)

            if os_level_key(os_release()) >= os_level_key("10.11"):
                # On OSX 10.11 (un)archivers modify exceptions, which looses
                # enough information that PyObjC can no longer reconstruct
                # the correct Python exception
                exception = (objc.error, pickle.UnpicklingError)
            else:
                exception = pickle.UnpicklingError

            with self.assertRaises(exception):
                self.unarchiverClass.unarchiveObjectWithData_(buf)

        finally:
            pycoder.decode_dispatch[pycoder.kOP_GLOBAL] = orig

    def test_reducing_issues(self):
        class Error1:
            def __reduce__(self):
                return dir, "foo"

        object1 = Error1()

        data = NSMutableData.alloc().init()
        archiver = self.archiverClass.alloc().initForWritingWithMutableData_(data)
        with self.assertRaises(pickle.PicklingError):
            archiver.encodeRootObject_(object1)

        if self.archiverClass is NSKeyedArchiver:
            archiver.finishEncoding()

        class Error2:
            def __reduce__(self):
                return "foo", (1, 2)

        object2 = Error2()

        data = NSMutableData.alloc().init()
        archiver = self.archiverClass.alloc().initForWritingWithMutableData_(data)
        with self.assertRaises(pickle.PicklingError):
            archiver.encodeRootObject_(object2)
        if self.archiverClass is NSKeyedArchiver:
            archiver.finishEncoding()

    def test_local_function(self):
        def function():
            pass

        with self.assertRaises(pickle.PicklingError):
            self.archiverClass.archivedDataWithRootObject_(function)

    def test_various_objects(self):
        o = a_newstyle_class()
        o.attr1 = False
        o.attr2 = None
        o.__dict__[42] = 3

        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, a_newstyle_class)
        self.assertEqual(v.__dict__, o.__dict__)

    # XXX: Disabled due to deadlock?
    def test_misc_globals(self):
        global mystr
        orig = mystr
        try:
            del mystr

            o = orig("hello")

            data = NSMutableData.alloc().init()
            archiver = self.archiverClass.alloc().initForWritingWithMutableData_(data)
            with self.assertRaises(pickle.PicklingError):
                archiver.encodeRootObject_(o)

            if self.archiverClass is NSKeyedArchiver:
                archiver.finishEncoding()

        finally:
            mystr = orig

        try:
            mystr = None

            o = orig("hello")
            data = NSMutableData.alloc().init()
            archiver = self.archiverClass.alloc().initForWritingWithMutableData_(data)
            with self.assertRaises(pickle.PicklingError):
                archiver.encodeRootObject_(o)
            if self.archiverClass is NSKeyedArchiver:
                archiver.finishEncoding()

        finally:
            mystr = orig  # noqa: F841

        try:
            copyreg.add_extension(
                a_newstyle_class.__module__, a_newstyle_class.__name__, 42
            )
            self.assertIn(
                (a_newstyle_class.__module__, a_newstyle_class.__name__),
                copyreg._extension_registry,
            )

            o = a_newstyle_class
            buf = self.archiverClass.archivedDataWithRootObject_(o)
            self.assertIsInstance(buf, NSData)
            v = self.unarchiverClass.unarchiveObjectWithData_(buf)
            self.assertIs(v, o)

            self.assertIsInstance(buf, NSData)
            v = self.unarchiverClass.unarchiveObjectWithData_(buf)
            self.assertIs(v, o)

            copyreg.remove_extension(
                a_newstyle_class.__module__, a_newstyle_class.__name__, 42
            )

            if os_level_key(os_release()) >= os_level_key("10.11"):
                # On OSX 10.11 (un)archivers modify exceptions, which looses
                # enough information that PyObjC can no longer reconstruct
                # the correct Python exception
                exception = (objc.error, ValueError)
            else:
                exception = ValueError

            with self.assertRaises(exception):
                self.unarchiverClass.unarchiveObjectWithData_(buf)

        finally:
            try:
                copyreg.remove_extension(
                    a_newstyle_class.__module__, a_newstyle_class.__name__, 42
                )
            except ValueError:
                pass

        def f():
            pass

        del f.__module__
        if hasattr(f, "__qualname__"):
            f.__qualname__ = f.__name__
        try:
            sys.f = f

            buf = self.archiverClass.archivedDataWithRootObject_(f)
            self.assertIsInstance(buf, NSData)
            v = self.unarchiverClass.unarchiveObjectWithData_(buf)
            self.assertIs(v, f)

        finally:
            del f

    def test_class_with_slots(self):
        # Test dumpling a class with slots
        o = newstyle_with_slots()
        o.a = 1
        o.b = 2
        o.c = 3

        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, newstyle_with_slots)
        self.assertEqual(v.a, 1)
        self.assertEqual(v.b, 2)
        self.assertEqual(v.c, 3)

    def test_class_with_setstate(self):
        o = newstyle_with_setstate()
        o.a = 1
        o.b = 2
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, newstyle_with_setstate)
        self.assertEqual(v.state, {"a": 1, "b": 2})

    def test_reduce_as_global(self):
        # Test class where __reduce__ returns a string (the name of a global)

        o = reduce_global
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIs(v, reduce_global)

    def test_reduce_invalid(self):
        class invalid_reduce:
            def __reduce__(self):
                return 42

        data = NSMutableData.alloc().init()
        archiver = self.archiverClass.alloc().initForWritingWithMutableData_(data)
        with self.assertRaises(pickle.PicklingError):
            archiver.encodeRootObject_(invalid_reduce())
        if self.archiverClass is NSKeyedArchiver:
            archiver.finishEncoding()

        data = NSMutableData.alloc().init()
        archiver = self.archiverClass.alloc().initForWritingWithMutableData_(data)
        with self.assertRaises(pickle.PicklingError):
            archiver.encodeRootObject_([1, 2, invalid_reduce()])
        if self.archiverClass is NSKeyedArchiver:
            archiver.finishEncoding()

        data = NSMutableData.alloc().init()
        archiver = self.archiverClass.alloc().initForWritingWithMutableData_(data)
        with self.assertRaises(pickle.PicklingError):
            archiver.encodeRootObject_({1, 2, invalid_reduce()})
        if self.archiverClass is NSKeyedArchiver:
            archiver.finishEncoding()

        data = NSMutableData.alloc().init()
        archiver = self.archiverClass.alloc().initForWritingWithMutableData_(data)
        with self.assertRaises(pickle.PicklingError):
            archiver.encodeRootObject_({1: 2, 2: invalid_reduce()})
        if self.archiverClass is NSKeyedArchiver:
            archiver.finishEncoding()

        data = NSMutableData.alloc().init()
        archiver = self.archiverClass.alloc().initForWritingWithMutableData_(data)
        with self.assertRaises(pickle.PicklingError):
            archiver.encodeRootObject_({1: 2, invalid_reduce(): 4})
        if self.archiverClass is NSKeyedArchiver:
            archiver.finishEncoding()

        class List(list):
            pass

        data = NSMutableData.alloc().init()
        archiver = self.archiverClass.alloc().initForWritingWithMutableData_(data)
        with self.assertRaises(pickle.PicklingError):
            archiver.encodeRootObject_(List([invalid_reduce()]))
        if self.archiverClass is NSKeyedArchiver:
            archiver.finishEncoding()

        class invalid_reduce:
            def __reduce__(self):
                return (1,)

        data = NSMutableData.alloc().init()
        archiver = self.archiverClass.alloc().initForWritingWithMutableData_(data)
        with self.assertRaises(pickle.PicklingError):
            archiver.encodeRootObject_(invalid_reduce())
        if self.archiverClass is NSKeyedArchiver:
            archiver.finishEncoding()

        class invalid_reduce:
            def __reduce__(self):
                return (1, 2, 3, 4, 5, 6)

        data = NSMutableData.alloc().init()
        archiver = self.archiverClass.alloc().initForWritingWithMutableData_(data)
        with self.assertRaises(pickle.PicklingError):
            archiver.encodeRootObject_(invalid_reduce())

        if self.archiverClass is NSKeyedArchiver:
            archiver.finishEncoding()

    def test_basic_objects(self):
        buf = self.archiverClass.archivedDataWithRootObject_(a_function)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIs(v, a_function)

        buf = self.archiverClass.archivedDataWithRootObject_(a_classic_class)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIs(v, a_classic_class)

        buf = self.archiverClass.archivedDataWithRootObject_(a_newstyle_class)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIs(v, a_newstyle_class)

        o = a_classic_class()
        o.x = 42
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, a_classic_class)
        self.assertEqual(v.x, 42)

        o = a_classic_class_with_state()
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, a_classic_class_with_state)
        self.assertEqual(v.a, 1)

        for o in (None, [None], (None,), {None}):
            buf = self.archiverClass.archivedDataWithRootObject_(o)
            self.assertIsInstance(buf, NSData)
            v = self.unarchiverClass.unarchiveObjectWithData_(buf)
            self.assertEqual(v, o)

        for o in (True, False, [True]):
            buf = self.archiverClass.archivedDataWithRootObject_(o)
            self.assertIsInstance(buf, NSData)
            v = self.unarchiverClass.unarchiveObjectWithData_(buf)
            self.assertEqual(v, o)

        o = ("aap", 42)
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, tuple if self.isKeyed else NSArray)
        self.assertEqual(o, v)

        o = ["aap", 42]
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, list if self.isKeyed else NSArray)
        self.assertEqual(o, v)

        o = {"aap": "monkey", "noot": "nut"}
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, dict if self.isKeyed else NSDictionary)
        self.assertEqual(o, v)

        o = {1, 2, 3}
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, set if self.isKeyed else NSSet)
        self.assertEqual(v, o)

        o = "hello world"
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, str)
        self.assertEqual(o, v)

        o = b"hello world"
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, bytes if self.isKeyed else NSData)
        self.assertEqual(o, v)

        o = "hello world"
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, type(o))
        self.assertEqual(o, v)

        o = mystr("hello world")
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, mystr)
        self.assertEqual(o, v)

        o = myint(4)
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, myint)
        self.assertEqual(o, v)

        o = 42.5
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, float)
        self.assertEqual(o, v)

        buf = self.archiverClass.archivedDataWithRootObject_("hello")
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, str)
        self.assertEqual(v, "hello")

        buf = self.archiverClass.archivedDataWithRootObject_(sys.maxsize * 4)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, int)
        self.assertEqual(v, sys.maxsize * 4)

        buf = self.archiverClass.archivedDataWithRootObject_(sys.maxsize**4)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, int)
        self.assertEqual(v, sys.maxsize**4)

    def testSimpleLists(self):
        o = []
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        if self.isKeyed:
            self.assertIsInstance(v, list)
            self.assertEqual(v, o)
        else:
            self.assertIsInstance(v, NSMutableArray)
            self.assertEqual(list(v), o)

        o = ["hello", 42]
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        if self.isKeyed:
            self.assertIsInstance(v, list)
            self.assertEqual(v, o)
        else:
            self.assertIsInstance(v, NSMutableArray)
            self.assertEqual(list(v), o)

    def testSimpleListSubclass(self):
        o = list_subclass([])
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, list_subclass)
        self.assertEqual(v, o)

        o = list_subclass(["hello", 42])
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, list_subclass)
        self.assertEqual(v, o)

    def testSimpleTuples(self):
        o = ()
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        if self.isKeyed:
            self.assertIsInstance(v, tuple)
            self.assertEqual(v, o)
        else:
            self.assertIsInstance(v, NSArray)
            self.assertEqual(tuple(v), o)

        o = ("hello", 42)
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        if self.isKeyed:
            self.assertIsInstance(v, tuple)
            self.assertEqual(v, o)
        else:
            self.assertIsInstance(v, NSArray)
            self.assertEqual(tuple(v), o)

    def testSimpleTupleSubclass(self):
        o = tuple_subclass()
        o.a = 42
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, tuple_subclass)
        self.assertEqual(v, o)
        self.assertEqual(v.a, o.a)

        o = tuple_subclass(["hello", 42])
        o.a = 99
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, tuple_subclass)
        self.assertEqual(v, o)
        self.assertEqual(v.a, o.a)

    def testSimpleDicts(self):
        o = {}
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, dict if self.isKeyed else NSDictionary)
        self.assertEqual(dict(v), o)

        o = {"hello": "bar", 42: 1.5}
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, dict if self.isKeyed else NSDictionary)
        self.assertEqual(dict(v), o)

    def testSimpleDictSubclass(self):
        o = dict_subclass({})
        o.a = 1
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, dict_subclass)
        self.assertEqual(v, o)
        self.assertEqual(v.a, o.a)

        o = dict_subclass({"hello": "bar", 42: 1.5})
        o.a = 99
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, dict_subclass)
        self.assertEqual(v, o)
        self.assertEqual(v.a, o.a)

    def testSimpleSetSubclass(self):
        o = set_subclass({1, 2, 3})
        o.a = 1

        self.assertIn(1, o)

        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, set_subclass)
        self.assertEqual(v, o)
        self.assertEqual(v.a, o.a)

    def testNestedDicts(self):
        o = {"hello": {1: 2}, "world": "foobar"}
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, dict if self.isKeyed else NSMutableDictionary)
        self.assertEqual(v, o)

        o = {}
        o["self"] = o
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, dict if self.isKeyed else NSMutableDictionary)

        if self.isKeyed:
            self.assertIs(v["self"], v)

        else:
            # See 'TestArchiveNative'
            self.assertIsNot(v["self"], v)

    def testNestedSequences(self):
        o = [1, 2, 3, (5, ("a", "b"), 6), {1: 2}]
        o[-1] = o

        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, list if self.isKeyed else NSMutableArray)
        self.assertEqual(v[:-1], o[:-1])

        if self.isKeyed:
            self.assertIs(v[-1], v)

        else:
            # See 'TestArchiveNative'
            self.assertIsNot(v[-1], v)

    def testNestedInstance(self):
        o = a_classic_class()
        o.value = o

        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)

        self.assertIsInstance(v, a_classic_class)
        self.assertIs(v.value, v)

    def dont_testNestedInstanceWithReduce(self):
        # Test recursive instantation with a __reduce__ method
        #
        # This test is disabled because pickle doesn't support
        # this (and we don't either)
        o = a_reducing_class()
        o.value = o

        import pickle

        b = pickle.dumps(o)
        pickle.loads(b)

        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)

        self.assertIsInstance(v, a_reducing_class)
        self.assertIs(v.value, v)

    def test_reducing_object(self):
        o = a_reducing_class()
        o.value = 42
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, a_reducing_class)
        self.assertEqual(o.value, 42)

    def testRecusiveNesting(self):
        lst = []
        d = {1: lst}
        i = a_classic_class()
        i.attr = d
        lst.append(i)

        buf = self.archiverClass.archivedDataWithRootObject_(lst)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)

        self.assertEqual(len(v), 1)
        self.assertEqual(dir(v[0]), dir(i))
        self.assertEqual(list(v[0].attr.keys()), [1])

        if self.isKeyed:
            self.assertIs(v[0].attr[1], v)
        else:
            # See 'TestArchiveNative'
            self.assertIsNot(v[0].attr[1], v)

        buf = self.archiverClass.archivedDataWithRootObject_(d)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)

        if self.isKeyed:
            self.assertIs(v[1][0].attr, v)
        else:
            # See 'TestArchiveNative'
            self.assertIsNot(v[1][0].attr, v)

    def testTupleOfObjects(self):
        o = a_classic_class()
        t = (o, o, o)

        buf = self.archiverClass.archivedDataWithRootObject_(t)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)

        self.assertIsInstance(v, tuple if self.isKeyed else NSArray)
        v = tuple(v)
        self.assertEqual(len(v), 3)
        self.assertIsInstance(v[0], a_classic_class)
        self.assertIs(v[0], v[1])
        self.assertIs(v[0], v[2])


class TestArchiveSimple(TestKeyedArchiveSimple):
    def setUp(self):
        self.isKeyed = False
        self.archiverClass = NSArchiver
        self.unarchiverClass = NSUnarchiver


class TestKeyedArchivePlainPython(TestCase, test.pickletester.AbstractPickleTests):
    # Ensure that we don't run every test case three times
    def setUp(self):
        self._protocols = test.pickletester.protocols
        test.pickletester.protocols = (2,)

    def tearDown(self):
        test.pickletester.protocols = self._protocols

    def assert_is_copy(self, a, b):
        return self.assertEqual(a, b)

    def dumps(self, arg, proto=0, fast=0):
        # Ignore proto and fast
        return NSKeyedArchiver.archivedDataWithRootObject_(arg)

    def loads(self, buf):
        return NSKeyedUnarchiver.unarchiveObjectWithData_(buf)

    # Disable a number of methods, these test things we're not interested in.
    # (Most of these look at the generated byte-stream, as we're not writing data in pickle's
    # format such tests are irrelevant to archiving support)
    @skipUnless(0, "python unittest not relevant for archiving")
    def test_inband_accept_default_buffers_argument(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_buffers_numpy(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_buffers_error(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_bytearray(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_oob_buffers(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_in_band_buffers(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_buffer_callback_error(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_buffer_error(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_oob_buffers_writable_to_readonly(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_picklebuffer_error(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_negative_put(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_framed_write_sizes_with_delayed_writer(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_badly_quoted_string(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_correctly_quoted_string(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_badly_escaped_string(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_appends_on_non_lists(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_setitems_on_non_dicts(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_int_pickling_efficiency(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_dynamic_class(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_ellipsis(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_notimplemented(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_load_classic_instance(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_insecure_strings(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_load_from_canned_string(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_maxint64(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_dict_chunking(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_float_format(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_garyp(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_list_chunking(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_singletons(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_simple_newobj(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_short_tuples(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_proto(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_long1(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_long4(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_get(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_load_from_data0(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_load_from_data1(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_load_from_data2(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_unpickle_from_2x(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_pickle_to_2x(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_bad_getattr(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_unicode(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    # XXX: fixme: currently gives abort in debug builds of 3.4, that shouldn't happen!
    def test_unicode_high_plane(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_maxsize64(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_empty_bytestring(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_pop_empty_stack(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_framing_many_objects(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_set_chunking(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_optional_frames(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_framing_large_objects(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_load_long_python2_str_as_bytes(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_load_python2_unicode_as_str(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_load_python2_str_as_bytes(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_complex_newobj(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_compat_pickle(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_compat_unpickle(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_frame_readline(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_complex_newobj_ex(self):
        pass

    def test_builtin_exceptions(self):
        import builtins

        for t in builtins.__dict__.values():
            if isinstance(t, type) and issubclass(t, BaseException):
                s = self.dumps(t)
                u = self.loads(s)
                self.assertIs(u, t)

    @expectedFailure
    def test_newobj_not_class(self):
        # Exception handling in NSCoder is dodgy
        test.pickletester.AbstractPickleTests.test_newobj_not_class(self)

    @expectedFailure
    def test_recursive_list_and_inst(self):
        test.pickletester.AbstractPickleTests.test_recursive_list_and_inst(self)

    @expectedFailure
    def test_recursive_tuple_and_list(self):
        test.pickletester.AbstractPickleTests.test_recursive_tuple_and_list(self)

    @expectedFailure
    def test_recursive_tuple_and_inst(self):
        test.pickletester.AbstractPickleTests.test_recursive_tuple_and_inst(self)

    @expectedFailure
    def test_recursive_dict_and_inst(self):
        test.pickletester.AbstractPickleTests.test_recursive_dict_and_inst(self)

    @expectedFailure
    def test_recursive_set_and_inst(self):
        test.pickletester.AbstractPickleTests.test_recursive_set_and_inst(self)

    @expectedFailure
    def test_recursive_set(self):
        # XXX: Need further investigation
        test.pickletester.AbstractPickleTests.test_recursive_set(self)

    @expectedFailure
    def test_recursive_frozenset_and_inst(self):
        test.pickletester.AbstractPickleTests.test_recursive_frozenset_and_inst(self)

    @expectedFailure
    def test_recursive_list_subclass_and_inst(self):
        test.pickletester.AbstractPickleTests.test_recursive_list_subclass_and_inst(
            self
        )

    @expectedFailure
    def test_recursive_tuple_subclass_and_inst(self):
        test.pickletester.AbstractPickleTests.test_recursive_tuple_subclass_and_inst(
            self
        )

    @expectedFailure
    def test_recursive_dict_subclass_and_inst(self):
        test.pickletester.AbstractPickleTests.test_recursive_dict_subclass_and_inst(
            self
        )

    @expectedFailure
    def test_recursive_set_subclass_and_inst(self):
        test.pickletester.AbstractPickleTests.test_recursive_set_subclass_and_inst(self)

    @expectedFailure
    def test_recursive_frozenset_subclass_and_inst(self):
        test.pickletester.AbstractPickleTests.test_recursive_frozenset_subclass_and_inst(
            self
        )

    def test_long(self):
        # The real test_long method takes way to much time, test a subset
        x = 12_345_678_910_111_213_141_516_178_920 << (256 * 8)
        buf = self.dumps(x)
        v = self.loads(buf)
        self.assertEqual(v, x)

        x = -x

        buf = self.dumps(x)
        v = self.loads(buf)

        self.assertEqual(v, x)

        for val in (
            int(0),
            int(1),
            int(sys.maxsize),
            int(sys.maxsize * 128),
            2**63 + 1,
        ):
            for x in val, -val:
                with self.subTest(x=x):
                    buf = self.dumps(x)
                    v = self.loads(buf)
                    if (val == 2**63 + 1) and os_level_key(
                        os_release()
                    ) < os_level_key("10.15"):
                        # Bug in NSNumber...
                        self.assertEqual(cast_ulonglong(v), cast_ulonglong(x))
                    else:
                        self.assertEqual(v, x)

    # Overriden tests for extension codes, the test code checks
    # the actual byte stream.
    def produce_global_ext(self, extcode, opcode):
        e = test.pickletester.ExtensionSaver(extcode)
        try:
            copyreg.add_extension(__name__, "MyList", extcode)
            x = MyList([1, 2, 3])
            x.foo = 42
            x.bar = "hello"

            s1 = self.dumps(x, 1)
            y = self.loads(s1)
            self.assertEqual(list(x), list(y))
            self.assertEqual(x.__dict__, y.__dict__)
        finally:
            e.restore()

    #
    # The test_reduce* methods iterate over various protocol
    # versions. Override to only look at protocol version 2.
    #
    def test_reduce_overrides_default_reduce_ex(self):
        for proto in (2,):
            x = test.pickletester.REX_one()
            self.assertEqual(x._reduce_called, 0)
            s = self.dumps(x, proto)
            self.assertEqual(x._reduce_called, 1)
            y = self.loads(s)
            self.assertEqual(y._reduce_called, 0)

    def test_reduce_ex_called(self):
        for proto in (2,):
            x = test.pickletester.REX_two()
            self.assertEqual(x._proto, None)
            s = self.dumps(x, proto)
            self.assertEqual(x._proto, proto)
            y = self.loads(s)
            self.assertEqual(y._proto, None)

    def test_reduce_ex_overrides_reduce(self):
        for proto in (2,):
            x = test.pickletester.REX_three()
            self.assertEqual(x._proto, None)
            s = self.dumps(x, proto)
            self.assertEqual(x._proto, proto)
            y = self.loads(s)
            self.assertEqual(y._proto, None)

    def test_reduce_ex_calls_base(self):
        for proto in (2,):
            x = test.pickletester.REX_four()
            self.assertEqual(x._proto, None)
            s = self.dumps(x, proto)
            self.assertEqual(x._proto, proto)
            y = self.loads(s)
            self.assertEqual(y._proto, proto)

    def test_reduce_calls_base(self):
        for proto in (2,):
            x = test.pickletester.REX_five()
            self.assertEqual(x._reduce_called, 0)
            s = self.dumps(x, proto)
            self.assertEqual(x._reduce_called, 1)
            y = self.loads(s)
            self.assertEqual(y._reduce_called, 1)


class TestArchivePlainPython(TestKeyedArchivePlainPython):
    def setUp(self):
        self._protocols = test.pickletester.protocols
        test.pickletester.protocols = (2,)

    def tearDown(self):
        test.pickletester.protocols = self._protocols

    def dumps(self, arg, proto=0, fast=0):
        # Ignore proto and fast
        return NSArchiver.archivedDataWithRootObject_(arg)

    def loads(self, buf):
        return NSUnarchiver.unarchiveObjectWithData_(buf)

    @expectedFailure
    def test_recursive_dict_like_key(self):
        # XXX: Needs further investigation...
        test.pickletester.AbstractPickleTests.test_recursive_dict_like_key(self)

    @expectedFailure
    def test_recursive_tuple_and_dict_key(self):
        # XXX: Needs further investigation...
        test.pickletester.AbstractPickleTests.test_recursive_tuple_and_dict_key(self)

    @expectedFailure
    def test_recursive_tuple_and_dict_like_key(self):
        # XXX: Needs further investigation...
        test.pickletester.AbstractPickleTests.test_recursive_tuple_and_dict_like_key(
            self
        )

    @expectedFailure
    def test_recursive_tuple_and_dict_subclass_key(self):
        # XXX: Needs further investigation...
        test.pickletester.AbstractPickleTests.test_recursive_tuple_and_dict_subclass_key(
            self
        )

    @expectedFailure
    def test_recursive_tuple_and_inst_state(self):
        # XXX: Needs further investigation...
        test.pickletester.AbstractPickleTests.test_recursive_tuple_and_inst_state(self)

    @expectedFailure
    def test_recursive_tuple_and_dict(self):
        # XXX: Needs further investigation...
        test.pickletester.AbstractPickleTests.test_recursive_tuple_and_dict(self)

    @expectedFailure
    def test_recursive_tuple_and_dict_subclass(self):
        # XXX: Needs further investigation...
        test.pickletester.AbstractPickleTests.test_recursive_tuple_and_dict_subclass(
            self
        )

    @expectedFailure
    def test_recursive_tuple_and_list_like(self):
        # XXX: Needs further investigation...
        test.pickletester.AbstractPickleTests.test_recursive_tuple_and_list_like(self)

    @expectedFailure
    def test_recursive_tuple_and_list_subclass(self):
        # XXX: Needs further investigation...
        test.pickletester.AbstractPickleTests.test_recursive_tuple_and_list_subclass(
            self
        )

    @expectedFailure
    def test_recursive_set(self):
        # XXX: Needs further investigation...
        test.pickletester.AbstractPickleTests.test_recursive_set(self)

    @expectedFailure
    def test_recursive_dict(self):
        # See 'TestArchiveNative'
        test.pickletester.AbstractPickleTests.test_recursive_dict(self)

    @expectedFailure
    def test_recursive_tuple_and_dict_like(self):
        # See 'TestArchiveNative'
        test.pickletester.AbstractPickleTests.test_recursive_tuple_and_dict_like(self)

    @expectedFailure
    def test_recursive_dict_key(self):
        # See 'TestArchiveNative'
        test.pickletester.AbstractPickleTests.test_recursive_dict_key(self)

    @expectedFailure
    def test_recursive_frozenset(self):
        # See 'TestArchiveNative'
        try:
            test.pickletester.AbstractPickleTests.test_recursive_frozenset(self)
        except SystemError:
            self.fail("SystemError during test")

    @expectedFailure
    def test_recursive_list(self):
        # See 'TestArchiveNative'
        test.pickletester.AbstractPickleTests.test_recursive_list(self)

    @expectedFailure
    def test_recursive_multi(self):
        # See 'TestArchiveNative'
        test.pickletester.AbstractPickleTests.test_recursive_multi(self)

    @expectedFailure
    def test_recursive_tuple(self):
        # See 'TestArchiveNative'
        test.pickletester.AbstractPickleTests.test_recursive_tuple(self)

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_unicode_memoization(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_evil_class_mutating_dict(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_oob_buffers(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_in_band_buffers(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_buffer_callback_error(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_buffer_error(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_oob_buffers_writable_to_readonly(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_picklebuffer_error(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_negative_put(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_int_pickling_efficiency(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_negative_32b_binunicode(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_negative_32b_binput(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_negative_32b_binbytes(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_framing_many_objects(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_complex_newobj(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_compat_pickle(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_compat_unpickle(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_frame_readline(self):
        pass

    @skipUnless(0, "python unittest not relevant for archiving")
    def test_framed_write_sizes_with_delayed_writer(self):
        pass

    @expectedFailure
    def test_recursive_dict_subclass_key(self):
        test.pickletester.AbstractPickleTests.test_recursive_dict_subclass_key(self)

    @expectedFailure
    def test_recursive_tuple_and_list(self):
        test.pickletester.AbstractPickleTests.test_recursive_tuple_and_list(self)

    @expectedFailure
    def test_recursive_list_and_inst(self):
        test.pickletester.AbstractPickleTests.test_recursive_list_and_inst(self)

    @expectedFailure
    def test_recursive_tuple_and_inst(self):
        test.pickletester.AbstractPickleTests.test_recursive_tuple_and_inst(self)

    @expectedFailure
    def test_recursive_dict_and_inst(self):
        test.pickletester.AbstractPickleTests.test_recursive_dict_and_inst(self)

    @expectedFailure
    def test_recursive_set_and_inst(self):
        test.pickletester.AbstractPickleTests.test_recursive_set_and_inst(self)

    @expectedFailure
    def test_recursive_frozenset_and_inst(self):
        test.pickletester.AbstractPickleTests.test_recursive_frozenset_and_inst(self)

    @expectedFailure
    def test_recursive_list_subclass_and_inst(self):
        test.pickletester.AbstractPickleTests.test_recursive_list_subclass_and_inst(
            self
        )

    @expectedFailure
    def test_recursive_tuple_subclass_and_inst(self):
        test.pickletester.AbstractPickleTests.test_recursive_tuple_subclass_and_inst(
            self
        )

    @expectedFailure
    def test_recursive_dict_subclass_and_inst(self):
        test.pickletester.AbstractPickleTests.test_recursive_dict_subclass_and_inst(
            self
        )

    @expectedFailure
    def test_recursive_set_subclass_and_inst(self):
        test.pickletester.AbstractPickleTests.test_recursive_set_subclass_and_inst(self)

    @expectedFailure
    def test_recursive_frozenset_subclass_and_inst(self):
        test.pickletester.AbstractPickleTests.test_recursive_frozenset_subclass_and_inst(
            self
        )


#
# Disable testing of plain Archiving for now, need full support
# for keyed-archiving first, then worry about adding "classic"
# archiving.
#
# class TestArchivePlainPython (TestKeyedArchivePlainPython):
#    def dumps(self, arg, proto=0, fast=0):
#        # Ignore proto and fast
#        return NSArchiver.archivedDataWithRootObject_(arg)
#
#    def loads(self, buf):
#        return NSUnarchiver.unarchiveObjectWithData_(buf)


#
# Second set of tests: test if archiving a graph that
# contains both python and objective-C objects works correctly.
#
class TestKeyedArchiveMixedGraphs(TestCase):
    isKeyed = True

    def dumps(self, arg, proto=0, fast=0):
        # Ignore proto and fast
        return NSKeyedArchiver.archivedDataWithRootObject_(arg)

    def loads(self, buf):
        return NSKeyedUnarchiver.unarchiveObjectWithData_(buf)

    def test_list1(self):
        o1 = a_classic_class()
        o2 = a_newstyle_class()
        o2.lst = NSArray.arrayWithObject_(o1)
        lst = NSArray.arrayWithArray_([o1, o2, [o1, o2]])

        buf = self.dumps(lst)
        self.assertIsInstance(buf, NSData)

        out = self.loads(buf)
        self.assertIsInstance(out, NSArray)
        self.assertEqual(len(out), 3)

        p1 = out[0]
        p2 = out[1]
        p3 = out[2]

        self.assertIsInstance(p1, a_classic_class)
        self.assertIsInstance(p2, a_newstyle_class)
        self.assertIsInstance(p3, list if self.isKeyed else NSArray)
        self.assertIs(p3[0], p1)
        self.assertIs(p3[1], p2)
        self.assertIsInstance(p2.lst, NSArray)
        self.assertIs(p2.lst[0], p1)


class TestArchiveMixedGraphs(TestKeyedArchiveMixedGraphs):
    isKeyed = False

    def dumps(self, arg, proto=0, fast=0):
        # Ignore proto and fast
        return NSArchiver.archivedDataWithRootObject_(arg)

    def loads(self, buf):
        return NSUnarchiver.unarchiveObjectWithData_(buf)


class TestArchiveNative(TestCase):
    # Self-referential graphs with collections are broken
    # in Cocoa, these are tested here because this behavior
    # is mentioned in PyObjC's documentation, that documentation
    # needs to be updated when these tests start to pass.
    #
    # Filed RADAR #13429469 for this.

    def dumps(self, arg, proto=0, fast=0):
        # Ignore proto and fast
        return NSArchiver.archivedDataWithRootObject_(arg)

    def loads(self, buf):
        return NSUnarchiver.unarchiveObjectWithData_(buf)

    @expectedFailure
    def test_self_referential_array(self):
        s1 = NSString.stringWithString_("hello")
        s2 = NSString.stringWithString_("world")

        a = NSMutableArray.arrayWithArray_([s1, s2])
        a.addObject_(a)

        buf = self.dumps(a)
        self.assertIsInstance(buf, NSData)

        b = self.loads(buf)
        self.assertEqual(b[0], s1)
        self.assertEqual(b[1], s2)
        self.assertIs(b[2], b)

    @expectedFailure
    def test_self_referential_dictionary(self):
        s1 = NSString.stringWithString_("hello")
        s2 = NSString.stringWithString_("world")

        a = NSMutableDictionary.dictionary()
        a.setValue_forKey_(s1, s2)
        a.setValue_forKey_(a, s1)

        buf = self.dumps(a)
        self.assertIsInstance(buf, NSData)

        b = self.loads(buf)
        self.assertEqual(b.valueForKey_(s2), s1)
        self.assertIs(b.valueForKey_(s1), b)

    def test_numbers(self):
        a = 1
        buf = self.dumps(a)
        self.assertIsInstance(buf, NSData)
        b = self.loads(buf)
        self.assertEqual(a, b)
        self.assertIsInstance(b, int)

        a = 1.5
        buf = self.dumps(a)
        self.assertIsInstance(buf, NSData)
        b = self.loads(buf)
        self.assertEqual(a, b)
        self.assertIsInstance(b, float)

        a = float_subclass(1.5)
        buf = self.dumps(a)
        self.assertIsInstance(buf, NSData)
        b = self.loads(buf)
        self.assertEqual(a, b)
        self.assertIsInstance(b, float_subclass)

    @expectedFailureIf(os_level_key(os_release()) <= os_level_key("10.6"))
    def test_more_state(self):
        a = with_getstate(1.5)
        self.assertEqual(a.value, 1.5)
        buf = self.dumps(a)
        self.assertIsInstance(buf, NSData)
        b = self.loads(buf)
        self.assertIsInstance(b, with_getstate)
        self.assertEqual(a.value, b.value)
        self.assertIsInstance(b.value, float)

        a = with_getstate(42)
        self.assertEqual(a.value, 42)
        buf = self.dumps(a)
        self.assertIsInstance(buf, NSData)
        b = self.loads(buf)
        self.assertIsInstance(b, with_getstate)
        self.assertEqual(a.value, b.value)
        self.assertIsInstance(b.value, int)

        a = with_getstate(1 << 100)
        self.assertEqual(a.value, 1 << 100)
        buf = self.dumps(a)
        self.assertIsInstance(buf, NSData)
        b = self.loads(buf)
        self.assertIsInstance(b, with_getstate)
        self.assertEqual(a.value, b.value)
        self.assertIsInstance(b.value, int)

        a = with_getstate((1, 2))
        self.assertEqual(a.value, (1, 2))
        buf = self.dumps(a)
        self.assertIsInstance(buf, NSData)
        b = self.loads(buf)
        self.assertIsInstance(b, with_getstate)
        self.assertEqual(a.value, b.value)
        self.assertIsInstance(b.value, tuple)

        a = only_getstate(
            {"a": 42, "b": 9, NSString("otherstr"): "b"},
            {"c": 4, "d": 7, 42: "b", "a": 1, NSString("nsstr"): NSString("xx")},
        )
        buf = self.dumps(a)
        self.assertIsInstance(buf, NSData)
        b = self.loads(buf)
        self.assertIsInstance(b, only_getstate)
        self.assertEqual(
            b.__dict__,
            {"a": 42, "b": 9, "c": 4, "d": 7, 42: "b", "nsstr": "xx", "otherstr": "b"},
        )
        for k in b.__dict__:
            self.assertNotIsInstance(k, objc.pyobjc_unicode)
            self.assertNotIsInstance(k, bytes)

        a = with_reduce_func([1, 2], (3, 4), {"a": 4}, {"d", "e"}, frozenset(["f"]), id)
        buf = self.dumps(a)
        self.assertIsInstance(buf, NSData)
        b = self.loads(buf)
        self.assertIsInstance(b, with_reduce_func)
        self.assertEqual(a.args, b.args)
        self.assertIsInstance(b.args[0], list)
        self.assertIsInstance(b.args[1], tuple)
        self.assertIsInstance(b.args[2], dict)
        self.assertIsInstance(b.args[3], set)
        self.assertIsInstance(b.args[4], frozenset)


class TestKeyedArchiveNative(TestArchiveNative):
    def dumps(self, arg, proto=0, fast=0):
        # Ignore proto and fast
        return NSKeyedArchiver.archivedDataWithRootObject_(arg)

    def loads(self, buf):
        return NSKeyedUnarchiver.unarchiveObjectWithData_(buf)


#
# And finally some tests to check if archiving of Python
# subclasses of NSObject works correctly.
#
# XXX: This class is empty!
#
class TestArchivePythonObjCSubclass(TestCase):
    pass


class TestSecureArchivingPython(TestCase):
    @min_os_level("10.13")
    def test_secure_archive_sequence(self):
        archive = NSKeyedArchiver.alloc().initRequiringSecureCoding_(True)
        sequence = collections.UserList()
        sequence.append(1)
        sequence.append(2)

        with self.assertRaisesRegex(
            objc.error,
            "Class 'OC_PythonArray' disallows secure coding. It must return YES from supportsSecureCoding",
        ):
            archive.encodeObject_forKey_(sequence, "sequence")

        archive.finishEncoding()

    @min_os_level("10.13")
    def test_secure_archive_mapping(self):
        archive = NSKeyedArchiver.alloc().initRequiringSecureCoding_(True)
        mapping = collections.UserDict()
        mapping["key"] = 1

        with self.assertRaisesRegex(
            objc.error,
            "Class 'OC_PythonDictionary' disallows secure coding. It must return YES from supportsSecureCoding",
        ):
            archive.encodeObject_forKey_(mapping, "mapping")

        archive.finishEncoding()

    @min_os_level("10.13")
    def test_secure_archive_set(self):
        archive = NSKeyedArchiver.alloc().initRequiringSecureCoding_(True)

        class UserSet(set):
            pass

        bag = UserSet()
        bag.add(1)

        with self.assertRaisesRegex(
            objc.error,
            "Class 'OC_PythonSet' disallows secure coding. It must return YES from supportsSecureCoding",
        ):
            archive.encodeObject_forKey_(bag, "bag")

        archive.finishEncoding()

    @min_os_level("10.13")
    def test_secure_archive_object(self):
        archive = NSKeyedArchiver.alloc().initRequiringSecureCoding_(True)

        value = object()

        with self.assertRaisesRegex(
            objc.error,
            "This decoder will only decode classes that adopt NSSecureCoding. Class 'OC_PythonObject' does not adopt it.",
        ):
            archive.encodeObject_forKey_(value, "value")

        archive.finishEncoding()

    def test_archive_without_encoder(self):
        with pyobjc_options(_nscoding_encoder=None):
            with self.assertRaisesRegex(
                ValueError,
                "encoding Python objects is not supported",
            ):
                NSKeyedArchiver.archivedDataWithRootObject_(object())

        buf = NSKeyedArchiver.archivedDataWithRootObject_(object())

        with pyobjc_options(_nscoding_decoder=None):
            with self.assertRaisesRegex(
                ValueError,
                "decoding Python objects is not supported",
            ):
                NSKeyedUnarchiver.unarchiveObjectWithData_(buf)
