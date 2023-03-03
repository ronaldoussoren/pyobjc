import objc
from PyObjCTest.NULL import OCTestNULL
from PyObjCTools.TestSupport import TestCase
import sys

objc.registerMetaDataForSelector(
    b"OCTestNULL",
    b"callOut:",
    {"arguments": {2: {"type_modifier": b"o", "null_accepted": True}}},
)
objc.registerMetaDataForSelector(
    b"OCTestNULL",
    b"callList:andInOut2:",
    {"arguments": {3: {"type_modifier": b"o", "null_accepted": True}}},
)
objc.registerMetaDataForSelector(
    b"OCTestNULL",
    b"callList:andInOut:",
    {"arguments": {3: {"type_modifier": b"N", "null_accepted": True}}},
)
objc.registerMetaDataForSelector(
    b"OCTestNULL",
    b"callList:andIn:",
    {"arguments": {3: {"type_modifier": b"n", "null_accepted": True}}},
)
objc.registerMetaDataForSelector(
    b"OCTestNULL",
    b"callList:andOut:",
    {"arguments": {3: {"type_modifier": b"o", "null_accepted": True}}},
)
objc.registerMetaDataForSelector(
    b"OCTestNULL",
    b"on:callList:andInOut:",
    {"arguments": {4: {"type_modifier": b"N", "null_accepted": True}}},
)
objc.registerMetaDataForSelector(
    b"OCTestNULL",
    b"on:callList:andIn:",
    {"arguments": {4: {"type_modifier": b"n", "null_accepted": True}}},
)
objc.registerMetaDataForSelector(
    b"OCTestNULL",
    b"on:callList:andOut:",
    {
        "arguments": {4: {"type_modifier": b"N", "null_accepted": True}}
    },  # N is by design
)
objc.registerMetaDataForSelector(
    b"OCTestNULL",
    b"on:callOut:",
    {
        "arguments": {3: {"type_modifier": b"N", "null_accepted": True}}
    },  # N is by design
)


class TestNULL(TestCase):
    def testNULL(self):
        self.assertHasAttr(objc, "NULL")
        self.assertEqual(repr(objc.NULL), "objc.NULL")
        with self.assertRaisesRegex(
            TypeError, "cannot create 'objc._NULL_type' instances"
        ):
            type(objc.NULL)()

        if sys.version_info[:2] >= (3, 10):
            with self.assertRaisesRegex(
                TypeError,
                "cannot set 'foo' attribute of immutable type 'objc._NULL_type'",
            ):
                type(objc.NULL).foo = 1


class TestNullArgumentsHelper(objc.lookUpClass("NSObject")):
    def callList_andInOut_(self, lst, value):
        lst.append(str(value))
        if value is objc.NULL:
            return (13, value)
        else:
            return (13, value * 2)

    callList_andInOut_ = objc.selector(callList_andInOut_, signature=b"i@:@N^i")

    def callList_andInOut2_(self, lst, value):
        lst.append(repr(value))
        if value is objc.NULL:
            return 29
        else:
            return 29

    callList_andInOut2_ = objc.selector(callList_andInOut2_, signature=b"i@:@^i")

    def callList_andIn_(self, lst, value):
        lst.append(repr(value))
        return 26

    callList_andIn_ = objc.selector(callList_andIn_, signature=b"i@:@n^i")

    def callList_andOut_(self, lst, value):
        assert value is None or value is objc.NULL
        lst.append("Nothing here")
        return (27, 99)

    callList_andOut_ = objc.selector(callList_andOut_, signature=b"i@:@o^i")

    def callOut_(self, value):
        assert value is None or value is objc.NULL
        return 441

    callOut_ = objc.selector(callOut_, signature=b"v@:o^i")


class TestNULLArguments(TestCase):
    def testCallInOutNULL(self):
        obj = OCTestNULL.alloc().init()

        v = []
        rv = obj.callList_andInOut_(v, 42)
        self.assertEqual(v, ["42"])
        self.assertEqual(rv, (12, 21))

        v = []
        rv = obj.callList_andInOut_(v, objc.NULL)
        self.assertEqual(v, ["NULL"])
        self.assertEqual(rv, (12, objc.NULL))

    def testCallInOutNULL2(self):
        # If nothing is specified the bridge assumes the argument behaves
        # like an 'in' argument.

        obj = OCTestNULL.alloc().init()

        v = []

        with self.assertRaisesRegex(ValueError, "argument 1 must be None or objc.NULL"):
            obj.callList_andInOut2_(v, 42)
        self.assertEqual(v, [])

        v = []
        rv = obj.callList_andInOut2_(v, objc.NULL)
        self.assertEqual(v, ["NULL"])
        self.assertEqual(rv, (12, objc.NULL))

        v = []
        rv = obj.callList_andInOut2_(v, None)
        self.assertEqual(v, ["0"])
        self.assertEqual(rv, (12, 0))

    def testCallOut(self):
        obj = OCTestNULL.alloc().init()

        r = obj.callOut_(None)
        self.assertEqual(r, 144)

        v = []
        r = obj.callList_andOut_(v, None)
        self.assertEqual(r, (24, 99))
        self.assertEqual(v, ["POINTER"])

        v = []
        r = obj.callList_andOut_(v, objc.NULL)
        self.assertEqual(r, (24, objc.NULL))
        self.assertEqual(v, ["NULL"])

    def testCallInNULL(self):
        obj = OCTestNULL.alloc().init()

        v = []
        rv = obj.callList_andIn_(v, 42)
        self.assertEqual(v, ["42"])
        self.assertEqual(rv, 24)

        v = []
        rv = obj.callList_andIn_(v, objc.NULL)
        self.assertEqual(v, ["NULL"])
        self.assertEqual(rv, 24)

    def testCalledInOutNULL(self):
        helper = OCTestNULL.alloc().init()
        obj = TestNullArgumentsHelper.alloc().init()

        v = []
        rv = helper.on_callList_andInOut_(obj, v, 42)
        self.assertEqual(v, ["42"])
        self.assertEqual(rv, (13, 84))

        v = []
        rv = helper.on_callList_andInOut_(obj, v, objc.NULL)
        self.assertEqual(v, ["objc.NULL"])
        self.assertEqual(rv, (13, objc.NULL))

    def testCalledInNULL(self):
        helper = OCTestNULL.alloc().init()
        obj = TestNullArgumentsHelper.alloc().init()

        v = []
        rv = helper.on_callList_andIn_(obj, v, 42)
        self.assertEqual(v, ["42"])
        self.assertEqual(rv, 26)

        v = []
        rv = helper.on_callList_andIn_(obj, v, objc.NULL)
        self.assertEqual(v, ["objc.NULL"])
        self.assertEqual(rv, 26)

    def testCalledOutNULL(self):
        helper = OCTestNULL.alloc().init()
        obj = TestNullArgumentsHelper.alloc().init()

        v = []
        rv = helper.on_callList_andOut_(obj, v, 42)
        self.assertEqual(v, ["Nothing here"])
        self.assertEqual(rv, (27, 99))

        v = []
        rv = helper.on_callList_andOut_(obj, v, objc.NULL)
        self.assertEqual(v, ["Nothing here"])
        self.assertEqual(rv, (27, objc.NULL))

        rv = helper.on_callOut_(obj, 42)
        self.assertEqual(rv, 441)

        rv = helper.on_callOut_(obj, objc.NULL)
        self.assertEqual(rv, objc.NULL)

    def dont_testCalledOutNULL(self):
        """
        XXX: I'm not happy about these semantics!

        Current semantics: called method doesn't know about the NULL argument,
        the result from Python is ignored.

        New semantics:
        - If the last argument is 'out' use new semantics, otherwise keep
          current semantics
        - If function has an optional last param stuf this with objc.NULL if
          the argument is NULL, otherwise don't provide
        - If the functioin has a required last param: stuff with objc.NULL or
          None
        """

    def dont_testCallOutNULL(self):
        """
        Call a method with an 'out' argument with an additional method

        - if not objc.NULL: raise TypeError
        - argument should be NULL in objC
        - result should be objc.NULL
        """
