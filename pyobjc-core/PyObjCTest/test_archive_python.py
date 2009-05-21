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
        def testBasicObjects(self):
            buf = NSKeyedArchiver.archivedDataWithRootObject_(a_function)
            self.assert_(isinstance(buf, NSData))
            v = NSKeyedUnarchiver.unarchiveObjectWithData_(buf)
            self.assert_(v is a_function)

            buf = NSKeyedArchiver.archivedDataWithRootObject_(a_classic_class)
            self.assert_(isinstance(buf, NSData))
            v = NSKeyedUnarchiver.unarchiveObjectWithData_(buf)
            self.assert_(v is a_classic_class)

            buf = NSKeyedArchiver.archivedDataWithRootObject_(a_newstyle_class)
            self.assert_(isinstance(buf, NSData))
            v = NSKeyedUnarchiver.unarchiveObjectWithData_(buf)
            self.assert_(v is a_newstyle_class)

            o = a_classic_class()
            o.x = 42
            buf = NSKeyedArchiver.archivedDataWithRootObject_(o)
            self.assert_(isinstance(buf, NSData))
            v = NSKeyedUnarchiver.unarchiveObjectWithData_(buf)
            self.assert_(isinstance(v, a_classic_class))
            self.assertEquals(o.x, 42)

            buf = NSKeyedArchiver.archivedDataWithRootObject_(u"hello")
            self.assert_(isinstance(buf, NSData))
            v = NSKeyedUnarchiver.unarchiveObjectWithData_(buf)
            self.assert_(isinstance(v, unicode))

            buf = NSKeyedArchiver.archivedDataWithRootObject_("hello")
            self.assert_(isinstance(buf, NSData))
            v = NSKeyedUnarchiver.unarchiveObjectWithData_(buf)
            self.assert_(isinstance(v, str))
            self.assertEquals(v, "hello")

            buf = NSKeyedArchiver.archivedDataWithRootObject_(sys.maxint * 4)
            self.assert_(isinstance(buf, NSData))
            v = NSKeyedUnarchiver.unarchiveObjectWithData_(buf)
            self.assert_(isinstance(v, long))
            self.assertEquals(v, sys.maxint * 4)

            buf = NSKeyedArchiver.archivedDataWithRootObject_(sys.maxint ** 4)
            self.assert_(isinstance(buf, NSData))
            v = NSKeyedUnarchiver.unarchiveObjectWithData_(buf)
            self.assert_(isinstance(v, long))
            self.assertEquals(v, sys.maxint ** 4)

        def testSimpleLists(self):
            o = []
            buf = NSKeyedArchiver.archivedDataWithRootObject_(o)
            self.assert_(isinstance(buf, NSData))
            v = NSKeyedUnarchiver.unarchiveObjectWithData_(buf)
            self.assert_(isinstance(v, list))
            self.assertEquals(v, o)

            o = [u"hello", 42]
            buf = NSKeyedArchiver.archivedDataWithRootObject_(o)
            self.assert_(isinstance(buf, NSData))
            v = NSKeyedUnarchiver.unarchiveObjectWithData_(buf)
            self.assert_(isinstance(v, list))
            self.assertEquals(v, o)

        def testSimpleTuples(self):
            o = ()
            buf = NSKeyedArchiver.archivedDataWithRootObject_(o)
            self.assert_(isinstance(buf, NSData))
            v = NSKeyedUnarchiver.unarchiveObjectWithData_(buf)
            self.assert_(isinstance(v, tuple))
            self.assertEquals(v, o)

            o = (u"hello", 42)
            buf = NSKeyedArchiver.archivedDataWithRootObject_(o)
            self.assert_(isinstance(buf, NSData))
            v = NSKeyedUnarchiver.unarchiveObjectWithData_(buf)
            self.assert_(isinstance(v, tuple))
            self.assertEquals(v, o)

        def testSimpleDicts(self):
            o = {}
            buf = NSKeyedArchiver.archivedDataWithRootObject_(o)
            self.assert_(isinstance(buf, NSData))
            v = NSKeyedUnarchiver.unarchiveObjectWithData_(buf)
            self.assert_(isinstance(v, dict))
            self.assertEquals(v, o)

            o = {u"hello": u"bar", 42: 1.5 }
            buf = NSKeyedArchiver.archivedDataWithRootObject_(o)
            self.assert_(isinstance(buf, NSData))
            v = NSKeyedUnarchiver.unarchiveObjectWithData_(buf)
            self.assert_(isinstance(v, dict))
            self.assertEquals(v, o)

        def testNestedDicts(self):
            o = {
                    u"hello": { 1:2 },
                    u"world": u"foobar"
                }
            buf = NSKeyedArchiver.archivedDataWithRootObject_(o)
            self.assert_(isinstance(buf, NSData))
            v = NSKeyedUnarchiver.unarchiveObjectWithData_(buf)
            self.assert_(isinstance(v, dict))
            self.assertEquals(v, o)

            o = {}
            o[u'self'] = o
            buf = NSKeyedArchiver.archivedDataWithRootObject_(o)
            self.assert_(isinstance(buf, NSData))
            v = NSKeyedUnarchiver.unarchiveObjectWithData_(buf)
            self.assert_(isinstance(v, dict))
            self.assert_(v[u'self'] is v)

        def testNestedSequences(self):
            o = [ 1, 2, 3, (5, (u'a', u'b'), 6), {1:2} ]
            o[-1] = o

            buf = NSKeyedArchiver.archivedDataWithRootObject_(o)
            self.assert_(isinstance(buf, NSData))
            v = NSKeyedUnarchiver.unarchiveObjectWithData_(buf)
            self.assert_(isinstance(v, list))
            self.assert_(v[-1] is v)
            self.assertEquals(v[:-1], o[:-1])

        def testNestedInstance(self):
            o = a_classic_class()
            o.value = o

            buf = NSKeyedArchiver.archivedDataWithRootObject_(o)
            self.assert_(isinstance(buf, NSData))
            v = NSKeyedUnarchiver.unarchiveObjectWithData_(buf)

            self.assert_(isinstance(v, a_classic_class))
            self.assert_(v.value is v)

        def dont_testNestedInstanceWithReduce(self):
            # Test recursive instantation with a __reduce__ method
            #
            # This test is disabled because pickle doesn't support
            # this (and we don't either)
            o = a_reducing_class()
            o.value = o

            import pickle
            b = pickle.dumps(o)
            o2 = picle.loads(b)
            print "+++", o2.value is o2

            buf = NSKeyedArchiver.archivedDataWithRootObject_(o)
            self.assert_(isinstance(buf, NSData))
            v = NSKeyedUnarchiver.unarchiveObjectWithData_(buf)

            self.assert_(isinstance(v, a_reducing_class))
            print type(v.value)
            print v.value
            print v
            self.assert_(v.value is v)

        def testRecusiveNesting(self):
            l = []
            d = {1:l}
            i = a_classic_class()
            i.attr = d
            l.append(i)

            buf = NSKeyedArchiver.archivedDataWithRootObject_(l)
            self.assert_(isinstance(buf, NSData))
            v = NSKeyedUnarchiver.unarchiveObjectWithData_(buf)

            self.assertEquals(len(v), 1)
            self.assertEquals(dir(v[0]), dir(i))
            self.assertEquals(v[0].attr.keys(), [1])
            self.assert_(v[0].attr[1] is v)

            buf = NSKeyedArchiver.archivedDataWithRootObject_(d)
            self.assert_(isinstance(buf, NSData))
            v = NSKeyedUnarchiver.unarchiveObjectWithData_(buf)
            self.assert_(v[1][0].attr is v)
            


        def testTupleOfObjects(self):
            o = a_classic_class()
            t = (o, o, o)

            buf = NSKeyedArchiver.archivedDataWithRootObject_(t)
            self.assert_(isinstance(buf, NSData))
            v = NSKeyedUnarchiver.unarchiveObjectWithData_(buf)

            self.assert_(isinstance(v, tuple))
            self.assert_(len(v) == 3)
            self.assert_(isinstance(v[0], a_classic_class))
            self.assert_(v[0] is v[1])
            self.assert_(v[0] is v[2])



    class TestKeyedArchivePlainPython (TestCase, test.pickletester.AbstractPickleTests):
        # Ensure that we don't run every test case three times
        def setUp(self):
            self._protocols = test.pickletester.protocols
            test.pickletester.protocols = (2,)

        def tearDown(self):
            test.pickletester.protoocols = self._protocols


        def dumps(self, arg, proto=0, fast=0):
            # Ignore proto and fast
            return NSKeyedArchiver.archivedDataWithRootObject_(arg)

        def loads(self, buf):
            return NSKeyedUnarchiver.unarchiveObjectWithData_(buf)

        
        # Disable a number of methods, these test things we're not interested in.
        # (Most of these look at the generated byte-stream, as we're not writing data in pickle's
        # format such tests are irrelevant to archiving support)
        def test_insecure_strings(self): pass
        def test_load_from_canned_string(self): pass
        def test_maxint64(self): pass
        def test_dict_chunking(self): pass
        def test_float_format(self): pass
        def test_garyp(self): pass
        def test_list_chunking(self): pass
        def test_singletons(self): pass
        def test_simple_newobj(self): pass
        def test_short_tuples(self): pass
        def test_proto(self): pass
        def test_long1(self): pass
        def test_long4(self): pass


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
            self.assert_(isinstance(buf, NSData))

            out = self.loads(buf)
            self.assert_(isinstance(out, NSArray))
            self.assertEquals(len(out), 3)

            p1 = out[0]
            p2 = out[1]
            p3 = out[2]

            self.assert_(isinstance(p1, a_classic_class))
            self.assert_(isinstance(p2, a_newstyle_class))
            self.assert_(isinstance(p3, list))
            self.assert_(p3[0] is p1)
            self.assert_(p3[1] is p2)
            self.assert_(isinstance(p2.lst , NSArray))
            self.assert_(p2.lst[0] is p1)
           




    #
    # And finally some tests to check if archiving of Python
    # subclasses of NSObject works correctly.
    #
    class TestArchivePythonObjCSubclass (TestCase):
        pass

if __name__ == "__main__":
    main()
