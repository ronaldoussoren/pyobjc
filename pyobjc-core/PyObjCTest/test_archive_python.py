"""
Testcases for NSArchive-ing python objects.

(Implementation is incomplete)
"""
import os

import sys
import pickle

if sys.version_info[0] == 3:
    import copyreg

else:
    import copy_reg as copyreg

from PyObjCTools.TestSupport import *
import objc._pycoder as pycoder

from PyObjCTest.fnd import NSArchiver, NSUnarchiver
from PyObjCTest.fnd import NSKeyedArchiver, NSKeyedUnarchiver
from PyObjCTest.fnd import NSData, NSArray, NSDictionary
from PyObjCTest.fnd import NSMutableArray, NSMutableDictionary

#
# First set of tests: the stdlib tests for pickling, this
# should test everything but mixed Python/Objective-C
# object-graphs.
#

if sys.version_info[0] == 3:
    unicode = str
    long = int

import test.pickletester

MyList = test.pickletester.MyList

class reduce_global (object):
    def __reduce__(self):
        return "reduce_global"
reduce_global = reduce_global()

# Quick hack to add a proper __repr__ to class C in
# pickletester, makes it a lot easier to debug.
def C__repr__(self):
    return '<%s instance at %#x: %r>'%(
        self.__class__.__name__, id(self), self.__dict__)
test.pickletester.C.__repr__ = C__repr__
del C__repr__

class myobject :
    def __init__(self):
        pass

    def __getinitargs__(self):
        return (1,2)

class state_obj_1:
    def __getstate__(self):
        return ({'a': 1, 42: 3}, {'b': 2})


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
        return {'a': 1}

    def __setstate__(self, state):
        for k, v in state.items():
            setattr(self, k, v)

class a_newstyle_class (object):
    pass

class newstyle_with_slots (object):
    __slots__ = ('a', 'b', '__dict__')

class newstyle_with_setstate (object):
    def __setstate__(self, state):
        self.state = state



def make_instance(state):
    o = a_reducing_class()
    o.__dict__.update(state)
    return o

class a_reducing_class (object):
    def __reduce__(self):
        return make_instance, (self.__dict__,)




class TestKeyedArchiveSimple (TestCase):
    def setUp(self):
        self.archiverClass = NSKeyedArchiver
        self.unarchiverClass = NSKeyedUnarchiver

    def test_unknown_type(self):
        try:
            orig = pycoder.decode_dispatch[pycoder.kOP_GLOBAL]
            del pycoder.decode_dispatch[pycoder.kOP_GLOBAL]

            o = TestKeyedArchiveSimple
            buf = self.archiverClass.archivedDataWithRootObject_(o)
            self.assertRaises(pickle.UnpicklingError, self.unarchiverClass.unarchiveObjectWithData_, buf)


        finally:
            pycoder.decode_dispatch[pycoder.kOP_GLOBAL] = orig



    def test_reducing_issues(self):
        class Error1 (object):
            def __reduce__(self):
                return dir, 'foo'
        object1 = Error1()

        self.assertRaises(pickle.PicklingError, self.archiverClass.archivedDataWithRootObject_,
                object1)

        class Error2 (object):
            def __reduce__(self):
                return 'foo', (1, 2)
        object2 = Error2()

        self.assertRaises(pickle.PicklingError, self.archiverClass.archivedDataWithRootObject_,
                object2)

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


    def test_misc_globals(self):
        global mystr 
        orig = mystr
        try:
            del mystr

            o = orig('hello')
            self.assertRaises(pickle.PicklingError, self.archiverClass.archivedDataWithRootObject_, o)

        finally:
            mystr = orig

        try:
            mystr = None

            o = orig('hello')
            self.assertRaises(pickle.PicklingError, self.archiverClass.archivedDataWithRootObject_, o)

        finally:
            mystr = orig


        try:
            copyreg.add_extension(a_newstyle_class.__module__, a_newstyle_class.__name__, 42)
            self.assertIn((a_newstyle_class.__module__, a_newstyle_class.__name__), copyreg._extension_registry)

            o = a_newstyle_class
            buf = self.archiverClass.archivedDataWithRootObject_(o)
            self.assertIsInstance(buf, NSData)
            v = self.unarchiverClass.unarchiveObjectWithData_(buf)
            self.assertIs(v, o)

            self.assertIsInstance(buf, NSData)
            v = self.unarchiverClass.unarchiveObjectWithData_(buf)
            self.assertIs(v, o)

            copyreg.remove_extension(a_newstyle_class.__module__, a_newstyle_class.__name__, 42)
            self.assertRaises(ValueError, self.unarchiverClass.unarchiveObjectWithData_, buf)

        finally:
            mystr = orig
            try:
                copyreg.remove_extension(a_newstyle_class.__module__, a_newstyle_class.__name__, 42)
            except ValueError:
                pass


        def f(): pass
        del f.__module__
        try:
            sys.f = f

            buf = self.archiverClass.archivedDataWithRootObject_(f)
            self.assertIsInstance(buf, NSData)
            v = self.unarchiverClass.unarchiveObjectWithData_(buf)
            self.assertIs(v, f)

        finally:
            del f

    @onlyPython2
    def test_invalid_initargs(self):
        v = myobject()
        buf = self.archiverClass.archivedDataWithRootObject_(v)
        self.assertIsInstance(buf, NSData)
        self.assertRaises(TypeError, self.unarchiverClass.unarchiveObjectWithData_, buf)

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

    @onlyPython2
    def test_class_with_state(self):
        o = state_obj_1()
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, state_obj_1)
        self.assertEqual(v.a, 1)
        self.assertEqual(v.b, 2)
        self.assertEqual(v.__dict__[42], 3)

    def test_class_with_setstate(self):
        o = newstyle_with_setstate()
        o.a = 1
        o.b = 2
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, newstyle_with_setstate)
        self.assertEqual(v.state, {'a': 1, 'b': 2})
        
    def test_reduce_as_global(self):
        # Test class where __reduce__ returns a string (the name of a global)

        o = reduce_global
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIs(v, reduce_global)


    def test_reduce_invalid(self):
        class invalid_reduce (object):
            def __reduce__(self):
                return 42
        self.assertRaises(pickle.PicklingError, self.archiverClass.archivedDataWithRootObject_, invalid_reduce())

        class invalid_reduce (object):
            def __reduce__(self):
                return (1,)
        self.assertRaises(pickle.PicklingError, self.archiverClass.archivedDataWithRootObject_, invalid_reduce())

        class invalid_reduce (object):
            def __reduce__(self):
                return (1,2,3,4,5,6)
        self.assertRaises(pickle.PicklingError, self.archiverClass.archivedDataWithRootObject_, invalid_reduce())


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

        for o in (None,  [None], (None,), {None,}):
            buf = self.archiverClass.archivedDataWithRootObject_(o)
            self.assertIsInstance(buf, NSData)
            v = self.unarchiverClass.unarchiveObjectWithData_(buf)
            self.assertEqual(o, v)

        for o in (True, False, [True]):
            buf = self.archiverClass.archivedDataWithRootObject_(o)
            self.assertIsInstance(buf, NSData)
            v = self.unarchiverClass.unarchiveObjectWithData_(buf)
            self.assertEqual(o, v)

        o = ('aap', 42)
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, tuple)
        self.assertEqual(o, v)

        o = ['aap', 42]
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, list)
        self.assertEqual(o, v)

        o = {'aap': 'monkey', 'noot': 'nut' }
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, dict)
        self.assertEqual(o, v)

        o = {1, 2, 3}
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, set)
        self.assertEqual(o, v)

        o = 'hello world'
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, str)
        self.assertEqual(o, v)

        o = b'hello world'
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, bytes)
        self.assertEqual(o, v)

        o = b'hello world'.decode('ascii')
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, type(o))
        self.assertEqual(o, v)


        o = mystr('hello world')
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


        if sys.version_info[0] == 2:
            buf = self.archiverClass.archivedDataWithRootObject_(unicode("hello"))
            self.assertIsInstance(buf, NSData)
            v = self.unarchiverClass.unarchiveObjectWithData_(buf)
            self.assertIsInstance(v, unicode)

        buf = self.archiverClass.archivedDataWithRootObject_("hello")
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, str)
        self.assertEqual(v, "hello")

        buf = self.archiverClass.archivedDataWithRootObject_(sys.maxsize * 4)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, long)
        self.assertEqual(v, sys.maxsize * 4)

        buf = self.archiverClass.archivedDataWithRootObject_(sys.maxsize ** 4)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, long)
        self.assertEqual(v, sys.maxsize ** 4)

    def testSimpleLists(self):
        o = []
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, list)
        self.assertEqual(v, o)

        o = [unicode("hello"), 42]
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, list)
        self.assertEqual(v, o)

    def testSimpleTuples(self):
        o = ()
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, tuple)
        self.assertEqual(v, o)

        o = (unicode("hello"), 42)
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, tuple)
        self.assertEqual(v, o)

    def testSimpleDicts(self):
        o = {}
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, dict)
        self.assertEqual(v, o)

        o = {unicode("hello"): unicode("bar"), 42: 1.5 }
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, dict)
        self.assertEqual(v, o)

    def testNestedDicts(self):
        o = {
                unicode("hello"): { 1:2 },
                unicode("world"): unicode("foobar")
            }
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, dict)
        self.assertEqual(v, o)

        o = {}
        o[unicode('self')] = o
        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, dict)
        self.assertIs(v[unicode('self')], v)

    def testNestedSequences(self):
        o = [ 1, 2, 3, (5, (unicode('a'), unicode('b')), 6), {1:2} ]
        o[-1] = o

        buf = self.archiverClass.archivedDataWithRootObject_(o)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIsInstance(v, list)
        self.assertIs(v[-1], v)
        self.assertEqual(v[:-1], o[:-1])

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
        o2 = pickle.loads(b)

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
        l = []
        d = {1:l}
        i = a_classic_class()
        i.attr = d
        l.append(i)

        buf = self.archiverClass.archivedDataWithRootObject_(l)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)

        self.assertEqual(len(v), 1)
        self.assertEqual(dir(v[0]), dir(i))
        self.assertEqual(list(v[0].attr.keys()), [1])
        self.assertIs(v[0].attr[1], v)

        buf = self.archiverClass.archivedDataWithRootObject_(d)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)
        self.assertIs(v[1][0].attr, v)



    def testTupleOfObjects(self):
        o = a_classic_class()
        t = (o, o, o)

        buf = self.archiverClass.archivedDataWithRootObject_(t)
        self.assertIsInstance(buf, NSData)
        v = self.unarchiverClass.unarchiveObjectWithData_(buf)

        self.assertIsInstance(v, tuple)
        self.assertEqual(len(v), 3)
        self.assertIsInstance(v[0], a_classic_class)
        self.assertIs(v[0], v[1])
        self.assertIs(v[0], v[2])

class TestArchiveSimple (TestKeyedArchiveSimple):
    def setUp(self):
        self.archiverClass = NSArchiver
        self.unarchiverClass = NSUnarchiver


class TestKeyedArchivePlainPython (TestCase, test.pickletester.AbstractPickleTests):
    # Ensure that we don't run every test case three times
    def setUp(self):
        self._protocols = test.pickletester.protocols
        test.pickletester.protocols = (2,)

    def tearDown(self):
        test.pickletester.protocols = self._protocols


    def dumps(self, arg, proto=0, fast=0):
        # Ignore proto and fast
        return NSKeyedArchiver.archivedDataWithRootObject_(arg)

    def loads(self, buf):
        return NSKeyedUnarchiver.unarchiveObjectWithData_(buf)


    # Disable a number of methods, these test things we're not interested in.
    # (Most of these look at the generated byte-stream, as we're not writing data in pickle's
    # format such tests are irrelevant to archiving support)
    @onlyIf(0, "python unittest not relevant for archiving")
    def test_negative_put(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_int_pickling_efficiency(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_dynamic_class(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_ellipsis(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_notimplemented(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_load_classic_instance(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_insecure_strings(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_load_from_canned_string(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_maxint64(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_dict_chunking(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_float_format(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_garyp(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_list_chunking(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_singletons(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_simple_newobj(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_short_tuples(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_proto(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_long1(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_long4(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_get(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_load_from_data0(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_load_from_data1(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_load_from_data2(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_unpickle_from_2x(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_pickle_to_2x(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_bad_getattr(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_unicode(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_maxsize64(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_empty_bytestring(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_pop_empty_stack(self): pass


    def test_long(self):
        # The real test_long method takes way to much time, test a subset
        x = 12345678910111213141516178920 << (256*8)
        buf = self.dumps(x)
        v = self.loads(buf)
        self.assertEqual(v, x)

        x = -x

        buf = self.dumps(x)
        v = self.loads(buf)

        self.assertEqual(v, x)

        for val in (long(0), long(1), long(sys.maxsize), long(sys.maxsize * 128)):
            for x in val, -val:
                buf = self.dumps(x)
                v = self.loads(buf)
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
        for proto in 2,:
            x = test.pickletester.REX_one()
            self.assertEqual(x._reduce_called, 0)
            s = self.dumps(x, proto)
            self.assertEqual(x._reduce_called, 1)
            y = self.loads(s)
            self.assertEqual(y._reduce_called, 0)

    def test_reduce_ex_called(self):
        for proto in 2,:
            x = test.pickletester.REX_two()
            self.assertEqual(x._proto, None)
            s = self.dumps(x, proto)
            self.assertEqual(x._proto, proto)
            y = self.loads(s)
            self.assertEqual(y._proto, None)

    def test_reduce_ex_overrides_reduce(self):
        for proto in 2,:
            x = test.pickletester.REX_three()
            self.assertEqual(x._proto, None)
            s = self.dumps(x, proto)
            self.assertEqual(x._proto, proto)
            y = self.loads(s)
            self.assertEqual(y._proto, None)

    def test_reduce_ex_calls_base(self):
        for proto in 2,:
            x = test.pickletester.REX_four()
            self.assertEqual(x._proto, None)
            s = self.dumps(x, proto)
            self.assertEqual(x._proto, proto)
            y = self.loads(s)
            self.assertEqual(y._proto, proto)

    def test_reduce_calls_base(self):
        for proto in 2,:
            x = test.pickletester.REX_five()
            self.assertEqual(x._reduce_called, 0)
            s = self.dumps(x, proto)
            self.assertEqual(x._reduce_called, 1)
            y = self.loads(s)
            self.assertEqual(y._reduce_called, 1)

class TestArchivePlainPython (TestKeyedArchivePlainPython):
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

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_negative_put(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_int_pickling_efficiency(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_negative_32b_binunicode(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_negative_32b_binput(self): pass

    @onlyIf(0, "python unittest not relevant for archiving")
    def test_negative_32b_binbytes(self): pass


#
# Disable testing of plain Archiving for now, need full support
# for keyed-archiving first, then worry about adding "classic"
# archiving.
#
#class TestArchivePlainPython (TestKeyedArchivePlainPython):
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
class TestKeyedArchiveMixedGraphs (TestCase):
    def dumps(self, arg, proto=0, fast=0):
        # Ignore proto and fast
        return NSKeyedArchiver.archivedDataWithRootObject_(arg)

    def loads(self, buf):
        return NSKeyedUnarchiver.unarchiveObjectWithData_(buf)

    def test_list1(self):
        o1 = a_classic_class()
        o2 = a_newstyle_class()
        o2.lst = NSArray.arrayWithObject_(o1)
        l = NSArray.arrayWithArray_([o1, o2, [o1, o2]])

        buf = self.dumps(l)
        self.assertIsInstance(buf, NSData)

        out = self.loads(buf)
        self.assertIsInstance(out, NSArray)
        self.assertEqual(len(out), 3)

        p1 = out[0]
        p2 = out[1]
        p3 = out[2]

        self.assertIsInstance(p1, a_classic_class)
        self.assertIsInstance(p2, a_newstyle_class)
        self.assertIsInstance(p3, list)
        self.assertIs(p3[0], p1)
        self.assertIs(p3[1], p2)
        self.assertIsInstance(p2.lst , NSArray)
        self.assertIs(p2.lst[0], p1)


class TestArchiveMixedGraphs (TestKeyedArchiveMixedGraphs):
    def dumps(self, arg, proto=0, fast=0):
        # Ignore proto and fast
        return NSArchiver.archivedDataWithRootObject_(arg)

    def loads(self, buf):
        return NSUnarchiver.unarchiveObjectWithData_(buf)



#
# And finally some tests to check if archiving of Python
# subclasses of NSObject works correctly.
#
class TestArchivePythonObjCSubclass (TestCase):
    pass

if __name__ == "__main__":
    main()
