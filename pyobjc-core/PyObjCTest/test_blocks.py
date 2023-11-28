# Tests for interaction with ObjC "blocks".
#
# These tests are fairly minimal at the moment.

import objc
from PyObjCTest.block import OCTestBlock
from PyObjCTools.TestSupport import TestCase, min_os_level

NSRect_tp = b"{CGRect={CGPoint=dd}{CGSize=dd}}"

objc.registerMetaDataForSelector(
    b"OCTestBlock",
    b"getStructBlock",
    {
        "retval": {
            "callable": {
                "retval": {"type": NSRect_tp},
                "arguments": {
                    0: {"type": b"^v"},
                    1: {"type": b"d"},
                    2: {"type": b"d"},
                    3: {"type": b"d"},
                    4: {"type": b"d"},
                },
            }
        }
    },
)
objc.registerMetaDataForSelector(
    b"OCTestBlock",
    b"getIntBlock",
    {
        "retval": {
            "callable": {
                "retval": {"type": b"i"},
                "arguments": {
                    0: {"type": b"^v"},
                },
            }
        }
    },
)
objc.registerMetaDataForSelector(
    b"OCTestBlock",
    b"getFloatBlock",
    {
        "retval": {
            "callable": {
                "retval": {"type": b"d"},
                "arguments": {
                    0: {"type": b"^v"},
                    1: {"type": b"d"},
                    2: {"type": b"d"},
                },
            }
        }
    },
)
objc.registerMetaDataForSelector(
    b"OCTestBlock",
    b"callOptionalBlock:withValue:",
    {
        "arguments": {
            2: {
                "callable": {
                    "retval": {"type": b"@"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"@"},
                    },
                }
            }
        }
    },
)
objc.registerMetaDataForSelector(
    b"OCTestBlock",
    b"callIntBlock:withValue:",
    {
        "arguments": {
            2: {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"i"},
                    },
                }
            }
        }
    },
)
objc.registerMetaDataForSelector(
    b"OCTestBlock",
    b"callDoubleBlock:withValue:andValue:",
    {
        "arguments": {
            2: {
                "callable": {
                    "retval": {"type": b"d"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"d"},
                        2: {"type": b"d"},
                    },
                }
            }
        }
    },
)
objc.registerMetaDataForSelector(
    b"OCTestBlock",
    b"callStructBlock:a:b:c:d:",
    {
        "arguments": {
            2: {
                "callable": {
                    "retval": {"type": NSRect_tp},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"d"},
                        2: {"type": b"d"},
                        3: {"type": b"d"},
                        4: {"type": b"d"},
                    },
                }
            }
        }
    },
)
objc.registerMetaDataForSelector(
    b"OCTestBlock",
    b"signatureForBlock1:",
    {
        "arguments": {
            2: {
                "type": b"@?",
                "callable": {
                    "retval": {"type": b"d"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"d"},
                        2: {"type": b"d"},
                    },
                },
            }
        }
    },
)
objc.registerMetaDataForSelector(
    b"OCTestBlock",
    b"signatureForBlock2:",
    {
        "arguments": {
            2: {
                "callable": {
                    "retval": {"type": b"@"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"@"},
                    },
                }
            }
        }
    },
)
objc.registerMetaDataForSelector(
    b"OCTestBlock",
    b"signatureForBlock3:",
    {
        "arguments": {
            2: {
                "callable": {
                    "retval": {"type": b"@"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"s"},
                    },
                }
            }
        }
    },
)
objc.registerMetaDataForSelector(
    b"OCTestBlock",
    b"signatureForBlock4:",
    {
        "arguments": {
            2: {
                "callable": {
                    "retval": {"type": b"c"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"i"},
                        2: {"type": b"i"},
                        3: {"type": b"f"},
                    },
                }
            }
        }
    },
)
objc.registerMetaDataForSelector(
    b"NSObject",
    b"processBlock:",
    {
        "retval": {"type": b"d"},
        "arguments": {
            2: {
                "type": b"@?",
                "callable": {
                    "retval": {"type": b"d"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"d"},
                        2: {"type": b"d"},
                    },
                },
            }
        },
    },
)
objc.registerMetaDataForSelector(
    b"NSObject",
    b"callWithCompletion:",
    {
        "arguments": {
            2: {
                "callable": {
                    "type": b"@?",
                    "retval": {"type": b"v"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"@"},
                    },
                }
            }
        }
    },
)
objc.registerMetaDataForSelector(
    b"NSObject",
    b"optionalBlock:",
    {
        "arguments": {
            2: {
                "type": b"@?",
                "callable": {
                    "retval": {"type": b"@"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"@"},
                    },
                },
            }
        }
    },
)


class BlocksHelper(objc.lookUpClass("NSObject")):
    def processBlock_(self, block):
        return -block(2.5, 4.0)

    def optionalBlock_(self, block):
        if block is None:
            return "no block"

        else:
            return block("x")


class BlocksCompletion(objc.lookUpClass("NSObject")):
    def callWithCompletion_(self, completion):
        completion("hello")
        completion("world")


class BlockWithStoredCompletion(objc.lookUpClass("NSObject")):
    def callWithCompletion_(self, completion):
        self.completion = completion

    def performCompletions(self):
        self.completion("hello")
        self.completion("world")


class TestBlocks(TestCase):
    @min_os_level("10.6")
    def testOptionalBlock(self):
        obj = OCTestBlock.alloc().init()

        self.assertEqual(obj.callOptionalBlock_withValue_(None, "hello"), "NOBLOCK")
        self.assertEqual(
            obj.callOptionalBlock_withValue_(lambda x: x + x, "hello"), "hellohello"
        )

    @min_os_level("10.6")
    def testBlockToObjC(self):
        obj = OCTestBlock.alloc().init()

        lst = []

        def callback(v):
            lst.append(v)

        obj.callIntBlock_withValue_(callback, 42)
        self.assertEqual(len(lst), 1)
        obj.callIntBlock_withValue_(callback, 43)
        self.assertEqual(len(lst), 2)

        self.assertEqual(lst, [42, 43])

        class Helper:
            def __init__(self):
                self.values = []

            def callback(self, v):
                self.values.append(v)

        helper = Helper()
        obj.callIntBlock_withValue_(helper.callback, 42)
        self.assertEqual(len(helper.values), 1)
        obj.callIntBlock_withValue_(helper.callback, 43)
        self.assertEqual(len(helper.values), 2)
        self.assertEqual(helper.values, [42, 43])

        class Helper2(objc.lookUpClass("NSObject")):
            def init(self):
                self = objc.super(Helper2, self).init()
                if self is None:
                    return None
                self.values = []
                return self

            def callback_(self, v):
                self.values.append(v)

        helper = Helper2.alloc().init()
        self.assertIsNot(helper, None)
        self.assertEqual(len(helper.values), 0)
        obj.callIntBlock_withValue_(helper.callback_, 42)
        self.assertEqual(len(helper.values), 1)
        obj.callIntBlock_withValue_(helper.callback_, 43)
        self.assertEqual(len(helper.values), 2)
        self.assertEqual(helper.values, [42, 43])

    @min_os_level("10.6")
    def test_block_with_varargs(self):
        obj = OCTestBlock.alloc().init()

        class C:
            def __init__(self):
                self._called = 0

            def callback(*args):
                args[0]._called += 1

        helper = C()
        obj.callIntBlock_withValue_(helper.callback, 43)
        self.assertEqual(helper._called, 1)

        class D:
            def __init__(self):
                self._called = 0

            def callback():
                pass

        helper = D()
        with self.assertRaisesRegex(TypeError, "Method without positional arguments"):
            obj.callIntBlock_withValue_(helper.callback, 43)

    @min_os_level("10.6")
    def testStackBlocksWithDirectUse(self):
        obj = OCTestBlock.alloc().init()
        tester = BlocksCompletion.alloc().init()
        a = []

        obj.callCompletionOn_andArray_withErasedSignature_(tester, a, 0)
        self.assertEqual(a, ["hello", "world"])

        a = []
        obj.callCompletionOn_andArray_withErasedSignature_(tester, a, 1)
        self.assertEqual(a, ["hello", "world"])

    @min_os_level("10.6")
    def testStackBlocksWithIndirectUse(self):
        obj = OCTestBlock.alloc().init()
        tester = BlockWithStoredCompletion.alloc().init()
        a = []

        obj.callCompletionOn_andArray_withErasedSignature_(tester, a, 0)
        self.assertEqual(a, [])

        tester.performCompletions()

        self.assertEqual(a, ["hello", "world"])

        a = []
        obj.callCompletionOn_andArray_withErasedSignature_(tester, a, 1)
        self.assertEqual(a, [])

        tester.performCompletions()

        self.assertEqual(a, ["hello", "world"])

    @min_os_level("10.6")
    def testBlockToObjC2(self):
        obj = OCTestBlock.alloc().init()

        def callback(a, b):
            return a * b

        self.assertEqual(
            obj.callDoubleBlock_withValue_andValue_(callback, 2.0, 3.5), 7.0
        )
        self.assertEqual(
            obj.callDoubleBlock_withValue_andValue_(callback, 2.5, 10), 25.0
        )

    @min_os_level("10.6")
    def testBlockToObjC3(self):
        obj = OCTestBlock.alloc().init()

        def callback(a, b, c, d):
            return ((a, b), (c, d))

        v = obj.callStructBlock_a_b_c_d_(callback, 1.5, 2.5, 3.5, 4.5)
        self.assertEqual(v, ((1.5, 2.5), (3.5, 4.5)))

    @min_os_level("10.6")
    def testBlockFromObjC(self):
        obj = OCTestBlock.alloc().init()

        block = obj.getIntBlock()
        value = block()
        self.assertEqual(value, 42)

        value = block()
        self.assertEqual(value, 42)

    @min_os_level("10.6")
    def testBlockFromObjC2(self):
        obj = OCTestBlock.alloc().init()

        block = obj.getFloatBlock()
        value = block(1, 2)
        self.assertEqual(value, 3.0)

        value = block(2.5, 7.0)
        self.assertEqual(value, 9.5)

    @min_os_level("10.6")
    def testBlockFromObjC3(self):
        obj = OCTestBlock.alloc().init()

        block = obj.getStructBlock()
        v = block(1.5, 2.5, 3.5, 4.5)
        self.assertEqual(v, ((1.5, 2.5), (3.5, 4.5)))

        block2 = obj.getStructBlock()
        self.assertIs(block, block2)

    @min_os_level("10.6")
    def testBlockSignatures(self):
        obj = OCTestBlock.alloc().init()

        block = obj.getFloatBlock()
        sig = objc.splitSignature(objc._block_signature(block))
        self.assertEqual(
            sig, (objc._C_DBL, objc._C_ID + b"?", objc._C_DBL, objc._C_DBL)
        )

        block = obj.getStructBlock()
        sig = objc.splitSignature(objc._block_signature(block))
        self.assertEqual(
            sig,
            (
                NSRect_tp,
                objc._C_ID + b"?",
                objc._C_DBL,
                objc._C_DBL,
                objc._C_DBL,
                objc._C_DBL,
            ),
        )

    @min_os_level("10.6")
    def testBlockArgumentToPython(self):
        obj = OCTestBlock.alloc().init()
        helper = BlocksHelper.alloc().init()
        value = obj.callProcessBlockOn_(helper)
        self.assertEqual(value, -(2.5 * 4.0))

        value = obj.callOptionalBlockOn_(helper)
        self.assertEqual(value, "no block")

    @min_os_level("10.6")
    def testBlocksWithoutMetadata(self):
        obj = OCTestBlock.alloc().init()

        block = obj.getIntBlock2()
        value = block(4)
        self.assertEqual(value, 8)

        block = obj.getIntBlock3()
        value = block(4, 8)
        self.assertEqual(value, 12)

        block = obj.getObjectBlock()
        value = block("hello")
        self.assertEqual(value, 5)

        block = obj.getObjectBlock2()
        value = block("hello", "world")
        self.assertEqual(value, 10)


BLOCK_SELF_TYPE = objc._C_PTR + objc._C_VOID


class TestBlockRuntimeSignature(TestCase):
    def testBlock1(self):
        obj = OCTestBlock.alloc().init()
        signature = obj.signatureForBlock1_(lambda a, b: a * b)
        self.assertEqual(
            signature,
            (objc._C_DBL + BLOCK_SELF_TYPE + objc._C_DBL + objc._C_DBL).decode("utf-8"),
        )

    def testBlock2(self):
        obj = OCTestBlock.alloc().init()
        signature = obj.signatureForBlock2_(lambda a: a)
        self.assertEqual(
            signature, (objc._C_ID + BLOCK_SELF_TYPE + objc._C_ID).decode("utf-8")
        )

    def testBlock3(self):
        obj = OCTestBlock.alloc().init()
        signature = obj.signatureForBlock3_(lambda a: a)
        self.assertEqual(
            signature, (objc._C_ID + BLOCK_SELF_TYPE + objc._C_SHT).decode("utf-8")
        )

    def testBlock4(self):
        obj = OCTestBlock.alloc().init()
        signature = obj.signatureForBlock4_(lambda a, b, c: a)
        self.assertEqual(
            signature,
            (
                objc._C_CHR + BLOCK_SELF_TYPE + objc._C_INT + objc._C_INT + objc._C_FLT
            ).decode("utf-8"),
        )
