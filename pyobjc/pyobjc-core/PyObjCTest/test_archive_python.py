"""
Testcases for NSArchive-ing python objects.

(Implementation is incomplete)
"""
import os

import sys, copy_reg

from PyObjCTools.TestSupport import *

from PyObjCTest.fnd import NSArchiver, NSUnarchiver
from PyObjCTest.fnd import NSKeyedArchiver, NSKeyedUnarchiver
from PyObjCTest.fnd import NSData, NSArray, NSDictionary
from PyObjCTest.fnd import NSMutableArray, NSMutableDictionary

# 
# First set of tests: the stdlib tests for pickling, this
# should test everything but mixed Python/Objective-C 
# object-graphs.
#

import test.pickletester

MyList = test.pickletester.MyList

# Quick hack to add a proper __repr__ to class C in
# pickletester, makes it a lot easier to debug.
def C__repr__(self):
    return '<%s instance at %#x: %r>'%(
        self.__class__.__name__, id(self), self.__dict__)
test.pickletester.C.__repr__ = C__repr__
del C__repr__

def a_function():
    pass

class a_classic_class:
    pass

class a_newstyle_class (object):
    pass

def make_instance(state):
    o = a_reducing_class()
    o.__dict__.update(state)
    return o

class a_reducing_class (object):
    def __reduce__(self):
        return make_instance, (self.__dict__,)


if int(os.uname()[2].split('.')[0]) >= 9:

    # For some reason NSCoding support doesn't work on OSX 10.4 yet, ignore these
    # tests for now
    class TestKeyedArchiveSimple (TestCase):
        def setUp(self):
            self.archiverClass = NSKeyedArchiver
            self.unarchiverClass = NSKeyedUnarchiver
        
        def testBasicObjects(self):
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
            self.assertEquals(o.x, 42)

            buf = self.archiverClass.archivedDataWithRootObject_(u"hello")
            self.assertIsInstance(buf, NSData)
            v = self.unarchiverClass.unarchiveObjectWithData_(buf)
            self.assertIsInstance(v, unicode)

            buf = self.archiverClass.archivedDataWithRootObject_("hello")
            self.assertIsInstance(buf, NSData)
            v = self.unarchiverClass.unarchiveObjectWithData_(buf)
            self.assertIsInstance(v, str)
            self.assertEquals(v, "hello")

            buf = self.archiverClass.archivedDataWithRootObject_(sys.maxint * 4)
            self.assertIsInstance(buf, NSData)
            v = self.unarchiverClass.unarchiveObjectWithData_(buf)
            self.assertIsInstance(v, long)
            self.assertEquals(v, sys.maxint * 4)

            buf = self.archiverClass.archivedDataWithRootObject_(sys.maxint ** 4)
            self.assertIsInstance(buf, NSData)
            v = self.unarchiverClass.unarchiveObjectWithData_(buf)
            self.assertIsInstance(v, long)
            self.assertEquals(v, sys.maxint ** 4)

        def testSimpleLists(self):
            o = []
            buf = self.archiverClass.archivedDataWithRootObject_(o)
            self.assertIsInstance(buf, NSData)
            v = self.unarchiverClass.unarchiveObjectWithData_(buf)
            self.assertIsInstance(v, list)
            self.assertEquals(v, o)

            o = [u"hello", 42]
            buf = self.archiverClass.archivedDataWithRootObject_(o)
            self.assertIsInstance(buf, NSData)
            v = self.unarchiverClass.unarchiveObjectWithData_(buf)
            self.assertIsInstance(v, list)
            self.assertEquals(v, o)

        def testSimpleTuples(self):
            o = ()
            buf = self.archiverClass.archivedDataWithRootObject_(o)
            self.assertIsInstance(buf, NSData)
            v = self.unarchiverClass.unarchiveObjectWithData_(buf)
            self.assertIsInstance(v, tuple)
            self.assertEquals(v, o)

            o = (u"hello", 42)
            buf = self.archiverClass.archivedDataWithRootObject_(o)
            self.assertIsInstance(buf, NSData)
            v = self.unarchiverClass.unarchiveObjectWithData_(buf)
            self.assertIsInstance(v, tuple)
            self.assertEquals(v, o)

        def testSimpleDicts(self):
            o = {}
            buf = self.archiverClass.archivedDataWithRootObject_(o)
            self.assertIsInstance(buf, NSData)
            v = self.unarchiverClass.unarchiveObjectWithData_(buf)
            self.assertIsInstance(v, dict)
            self.assertEquals(v, o)

            o = {u"hello": u"bar", 42: 1.5 }
            buf = self.archiverClass.archivedDataWithRootObject_(o)
            self.assertIsInstance(buf, NSData)
            v = self.unarchiverClass.unarchiveObjectWithData_(buf)
            self.assertIsInstance(v, dict)
            self.assertEquals(v, o)

        def testNestedDicts(self):
            o = {
                    u"hello": { 1:2 },
                    u"world": u"foobar"
                }
            buf = self.archiverClass.archivedDataWithRootObject_(o)
            self.assertIsInstance(buf, NSData)
            v = self.unarchiverClass.unarchiveObjectWithData_(buf)
            self.assertIsInstance(v, dict)
            self.assertEquals(v, o)

            o = {}
            o[u'self'] = o
            buf = self.archiverClass.archivedDataWithRootObject_(o)
            self.assertIsInstance(buf, NSData)
            v = self.unarchiverClass.unarchiveObjectWithData_(buf)
            self.assertIsInstance(v, dict)
            self.assertIs(v[u'self'], v)

        def testNestedSequences(self):
            o = [ 1, 2, 3, (5, (u'a', u'b'), 6), {1:2} ]
            o[-1] = o

            buf = self.archiverClass.archivedDataWithRootObject_(o)
            self.assertIsInstance(buf, NSData)
            v = self.unarchiverClass.unarchiveObjectWithData_(buf)
            self.assertIsInstance(v, list)
            self.assertIs(v[-1], v)
            self.assertEquals(v[:-1], o[:-1])

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
            print "+++", o2.value is o2

            buf = self.archiverClass.archivedDataWithRootObject_(o)
            self.assertIsInstance(buf, NSData)
            v = self.unarchiverClass.unarchiveObjectWithData_(buf)

            self.assertIsInstance(v, a_reducing_class)
            print type(v.value)
            print v.value
            print v
            self.assertIs(v.value, v)

        def testRecusiveNesting(self):
            l = []
            d = {1:l}
            i = a_classic_class()
            i.attr = d
            l.append(i)

            buf = self.archiverClass.archivedDataWithRootObject_(l)
            self.assertIsInstance(buf, NSData)
            v = self.unarchiverClass.unarchiveObjectWithData_(buf)

            self.assertEquals(len(v), 1)
            self.assertEquals(dir(v[0]), dir(i))
            self.assertEquals(v[0].attr.keys(), [1])
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
            self.assertEquals(len(v), 3)
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


        def test_long(self):
            # The real test_long method takes way to much time, test a subset
            x = 12345678910111213141516178920L << (256*8)
            buf = self.dumps(x)
            v = self.loads(buf)
            self.assertEquals(v, x)

            x = -x

            buf = self.dumps(x)
            v = self.loads(buf)

            self.assertEquals(v, x)

            for val in (0L, 1L, long(sys.maxint), long(sys.maxint * 128)):
                for x in val, -val:
                    buf = self.dumps(x)
                    v = self.loads(buf)
                    self.assertEquals(v, x)





        # Overriden tests for extension codes, the test code checks
        # the actual byte stream.
        def produce_global_ext(self, extcode, opcode):
            e = test.pickletester.ExtensionSaver(extcode)
            try:
                copy_reg.add_extension(__name__, "MyList", extcode)
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
            self.assertEquals(len(out), 3)

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
