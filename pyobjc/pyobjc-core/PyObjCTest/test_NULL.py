from PyObjCTools.TestSupport import *
import objc

setSignature = objc.setSignatureForSelector
#setSignature(b"OCTestNULL", "callOut:", "i@:o^i")
#setSignature(b"OCTestNULL", "callList:andInOut2:", "i@:@^i")
#setSignature(b"OCTestNULL", "callList:andInOut:", "i@:@N^i")
#setSignature(b"OCTestNULL", "callList:andIn:", "i@:@n^i")
#setSignature(b"OCTestNULL", "callList:andOut:", "i@:@o^i")
#setSignature(b"OCTestNULL", "on:callList:andInOut:", "i@:@@N^i")
#setSignature(b"OCTestNULL", "on:callList:andIn:", "i@:@@n^i")
#setSignature(b"OCTestNULL", "on:callList:andOut:", "i@:@@N^i") # 'N' is by design
#setSignature(b"OCTestNULL", "on:callOut:", "v@:@N^i") # 'N' is by design

objc.registerMetaDataForSelector(b"OCTestNULL", b"callOut:", dict(
            arguments={
                2: dict(type_modifier=b'o', null_accepted=True),
            },
        ))
objc.registerMetaDataForSelector(b"OCTestNULL", b"callList:andInOut2:", dict(
            arguments={
                3: dict(type_modifier=b'o', null_accepted=True),
            },
        ))
objc.registerMetaDataForSelector(b"OCTestNULL", b"callList:andInOut:", dict(
            arguments={
                3: dict(type_modifier=b'N', null_accepted=True),
            },
        ))
objc.registerMetaDataForSelector(b"OCTestNULL", b"callList:andIn:", dict(
            arguments={
                3: dict(type_modifier=b'n', null_accepted=True),
            },
        ))
objc.registerMetaDataForSelector(b"OCTestNULL", b"callList:andOut:", dict(
            arguments={
                3: dict(type_modifier=b'o', null_accepted=True),
            },
        ))
objc.registerMetaDataForSelector(b"OCTestNULL", b"on:callList:andInOut:", dict(
            arguments={
                4: dict(type_modifier=b'N', null_accepted=True),
            },
        ))
objc.registerMetaDataForSelector(b"OCTestNULL", b"on:callList:andIn:", dict(
            arguments={
                4: dict(type_modifier=b'n', null_accepted=True),
            },
        ))
objc.registerMetaDataForSelector(b"OCTestNULL", b"on:callList:andOut:", dict(
            arguments={
                4: dict(type_modifier=b'N', null_accepted=True), # N is by design
            },
        ))
objc.registerMetaDataForSelector(b"OCTestNULL", b"on:callOut:", dict(
            arguments={
                3: dict(type_modifier=b'N', null_accepted=True), # N is by design
            },
        ))

from PyObjCTest.NULL import *

class TestNULL (TestCase):
    def testNULL(self):
        self.assertHasAttr(objc, 'NULL')
        self.assertEquals(repr(objc.NULL), 'objc.NULL')
        self.assertRaises(TypeError, type(objc.NULL))


class TestNullArgumentsHelper (objc.lookUpClass("NSObject")):

    def callList_andInOut_(self, lst, value):
        lst.append(str(value))
        if value is objc.NULL:
            return (13, value)
        else:
            return (13, value * 2)

    callList_andInOut_ = objc.selector(callList_andInOut_,
            signature=b"i@:@N^i")

    def callList_andInOut2_(self, lst, value):
        lst.append(repr(value))
        if value is objc.NULL:
            return 29
        else:
            return 29
    callList_andInOut2_ = objc.selector(callList_andInOut2_,
            signature=b"i@:@^i")

    def callList_andIn_(self, lst, value):
        lst.append(repr(value))
        return 26

    callList_andIn_ = objc.selector(callList_andIn_,
            signature=b"i@:@n^i")

    def callList_andOut_(self, lst, value):
        assert value is None or value is objc.NULL
        lst.append("Nothing here")
        return (27, 99)
    callList_andOut_ = objc.selector(callList_andOut_,
            signature=b"i@:@o^i")

    def callOut_(self, value):
        assert value is None or value is objc.NULL
        return 441;
    callOut_ = objc.selector(callOut_, signature=b'v@:o^i')    

class TestNULLArguments (TestCase):
    def testCallInOutNULL(self):
        obj = OCTestNULL.alloc().init()

        v = []
        rv = obj.callList_andInOut_(v, 42)
        self.assertEquals(v, ["42"])
        self.assertEquals(rv, (12, 21))

        v = []
        rv = obj.callList_andInOut_(v, objc.NULL)
        self.assertEquals(v, ["NULL"])
        self.assertEquals(rv,  (12, objc.NULL))

    def testCallInOutNULL2(self):
        # If nothing is specified the bridge assumes the argument behaves
        # like an 'in' argument.

        obj = OCTestNULL.alloc().init()

        v = []
        self.assertRaises(ValueError, obj.callList_andInOut2_, v, 42)
        self.assertEquals(v, [])

        v = []
        rv = obj.callList_andInOut2_(v, objc.NULL)
        self.assertEquals(v, ["NULL"])
        self.assertEquals(rv,  (12, objc.NULL))

    def testCallInNULL(self):
        obj = OCTestNULL.alloc().init()

        v = []
        rv = obj.callList_andIn_(v, 42)
        self.assertEquals(v, ["42"])
        self.assertEquals(rv, 24)

        v = []
        rv = obj.callList_andIn_(v, objc.NULL)
        self.assertEquals(v, ["NULL"])
        self.assertEquals(rv,  24)


    def testCalledInOutNULL(self):
        helper = OCTestNULL.alloc().init()
        obj = TestNullArgumentsHelper.alloc().init()

        v = []
        rv = helper.on_callList_andInOut_(obj, v, 42)
        self.assertEquals(v, ['42'])
        self.assertEquals(rv, (13, 84))

        v = []
        rv = helper.on_callList_andInOut_(obj, v, objc.NULL)
        self.assertEquals(v, ['objc.NULL'])
        self.assertEquals(rv, (13, objc.NULL))

    def testCalledInNULL(self):
        helper = OCTestNULL.alloc().init()
        obj = TestNullArgumentsHelper.alloc().init()

        v = []
        rv = helper.on_callList_andIn_(obj, v, 42)
        self.assertEquals(v, ['42'])
        self.assertEquals(rv, 26)

        v = []
        rv = helper.on_callList_andIn_(obj, v, objc.NULL)
        self.assertEquals(v, ['objc.NULL'])
        self.assertEquals(rv, 26)

    def testCalledOutNULL(self):

        helper = OCTestNULL.alloc().init()
        obj = TestNullArgumentsHelper.alloc().init()

        v = []
        rv = helper.on_callList_andOut_(obj, v, 42)
        self.assertEquals(v, ['Nothing here'])
        self.assertEquals(rv, (27, 99))

        v = []
        rv = helper.on_callList_andOut_(obj, v, objc.NULL)
        self.assertEquals(v, ['Nothing here'])
        self.assertEquals(rv, (27, objc.NULL))

        rv = helper.on_callOut_(obj, 42)
        self.assertEquals(rv, 441)

        rv = helper.on_callOut_(obj, objc.NULL)
        self.assertEquals(rv, objc.NULL)

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

        


if __name__ == "__main__":
    main()
