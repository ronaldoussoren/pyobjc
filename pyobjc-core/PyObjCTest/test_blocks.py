# Tests for interaction with ObjC "blocks".
#
# These tests are fairly minimal at the moment.

import objc
from PyObjCTest.block import OCTestBlock
from PyObjCTools.TestSupport import TestCase, min_os_level
from .fnd import NSMutableArray

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

# The metadata for this method has been disabled
# intentionally, the compiler adds metadata to the
# runtime.
#
# objc.registerMetaDataForSelector(
#    b"OCTestBlock",
#    b"getIntBlock",
#    {
#        "retval": {
#            "callable": {
#                "retval": {"type": b"i"},
#                "arguments": {
#                    0: {"type": b"^v"},
#                },
#            }
#        }
#    },
# )

# The metadata for this method has been disabled
# intentionally, the compiler adds metadata to the
# runtime
#
# objc.registerMetaDataForSelector(
#    b"OCTestBlock",
#    b"getFloatBlock",
#    {
#        "retval": {
#            "callable": {
#                "retval": {"type": b"d"},
#                "arguments": {
#                    0: {"type": b"^v"},
#                    1: {"type": b"d"},
#                    2: {"type": b"d"},
#                },
#            }
#        }
#    },
# )
objc.registerMetaDataForSelector(
    b"OCTestBlock",
    b"getFloatBlock2",
    {
        "retval": {
            "callable": {
                "retval": {"type": b"d"},
                "arguments": {
                    0: {"type": b"^v"},
                    1: {"type": b"d"},
                    2: {"type": b"X"},
                },
            }
        }
    },
)

objc.registerMetaDataForSelector(
    b"OCTestBlock",
    b"getRaisingBlock",
    {
        "retval": {
            "callable": {
                "retval": {"type": b"v"},
                "arguments": {
                    0: {"type": b"^v"},
                },
            }
        }
    },
)

objc.registerMetaDataForSelector(
    b"OCTestBlock",
    b"getVariadicBlock",
    {
        "retval": {
            "callable": {
                "variadic": True,
                "c_array_delimited_by_null": True,
                "retval": {"type": b"@"},
                "arguments": {
                    0: {"type": b"^v"},
                    1: {"type": b"@"},
                },
            }
        }
    },
)

objc.registerMetaDataForSelector(
    b"OCTestBlock",
    b"getPrintfBlock",
    {
        "retval": {
            "callable": {
                "variadic": True,
                "retval": {"type": b"@"},
                "arguments": {
                    0: {"type": b"^v"},
                    1: {"type": b"@", "printf_format": True},
                },
            }
        }
    },
)

objc.registerMetaDataForSelector(
    b"OCTestBlock",
    b"getPrintfBlock2",
    {
        "retval": {
            "callable": {
                "variadic": True,
                "retval": {"type": b"@"},
                "arguments": {
                    0: {"type": b"^v"},
                    1: {"type": b"o^i"},
                    2: {"type": b"@", "printf_format": True},
                },
            }
        }
    },
)

objc.registerMetaDataForSelector(
    b"OCTestBlock",
    b"getPrintfBlock3",
    {
        "retval": {
            "callable": {
                "variadic": True,
                "retval": {"type": b"@"},
                "arguments": {
                    0: {"type": b"^v"},
                    1: {"type": b"N^i"},
                    2: {"type": b"@", "printf_format": True},
                },
            }
        }
    },
)

objc.registerMetaDataForSelector(
    b"OCTestBlock",
    b"getHugeBlock",
    {
        "retval": {
            "callable": {
                "variadic": True,
                "retval": {"type": b"@"},
                "arguments": {
                    0: {"type": b"^v"},
                    1: {"type": b"@"},
                    2: {"type": b"@"},
                    3: {"type": b"@"},
                    4: {"type": b"@"},
                    5: {"type": b"@"},
                    6: {"type": b"@"},
                    7: {"type": b"@"},
                    8: {"type": b"@"},
                    9: {"type": b"@"},
                    10: {"type": b"@"},
                    11: {"type": b"@"},
                    12: {"type": b"@"},
                    13: {"type": b"@"},
                    14: {"type": b"@"},
                    15: {"type": b"@"},
                    16: {"type": b"@"},
                    17: {"type": b"@"},
                    18: {"type": b"@"},
                    19: {"type": b"@"},
                    20: {"type": b"@"},
                    21: {"type": b"@"},
                    22: {"type": b"@"},
                    23: {"type": b"@"},
                    24: {"type": b"@"},
                    25: {"type": b"@"},
                    26: {"type": b"@"},
                    27: {"type": b"@"},
                    28: {"type": b"@"},
                    29: {"type": b"@"},
                    30: {"type": b"@"},
                    31: {"type": b"@"},
                    32: {"type": b"@"},
                    33: {"type": b"@"},
                    34: {"type": b"@"},
                    35: {"type": b"@"},
                    36: {"type": b"@"},
                    37: {"type": b"@"},
                    38: {"type": b"@"},
                    39: {"type": b"@"},
                    40: {"type": b"@"},
                    41: {"type": b"@"},
                    42: {"type": b"@"},
                    43: {"type": b"@"},
                    44: {"type": b"@"},
                    45: {"type": b"@"},
                    46: {"type": b"@"},
                    47: {"type": b"@"},
                    48: {"type": b"@"},
                    49: {"type": b"@"},
                    50: {"type": b"@"},
                    51: {"type": b"@"},
                    52: {"type": b"@"},
                    53: {"type": b"@"},
                    54: {"type": b"@"},
                    55: {"type": b"@"},
                    56: {"type": b"@"},
                    57: {"type": b"@"},
                    58: {"type": b"@"},
                    59: {"type": b"@"},
                    60: {"type": b"@"},
                    61: {"type": b"@"},
                    62: {"type": b"@"},
                    63: {"type": b"@"},
                    64: {"type": b"@"},
                    65: {"type": b"@"},
                    66: {"type": b"@"},
                    67: {"type": b"@"},
                    68: {"type": b"@"},
                    69: {"type": b"@"},
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
    b"storeBlock:",
    {
        "arguments": {
            2: {
                "callable": {
                    "retval": {"type": b"@"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"@"},
                        2: {"type": b"@"},
                    },
                }
            }
        }
    },
)
objc.registerMetaDataForSelector(
    b"OCTestBlock",
    b"getStoredBlock",
    {
        "retval": {
            "callable": {
                "retval": {"type": b"@"},
                "arguments": {
                    0: {"type": b"^v"},
                    1: {"type": b"@"},
                    2: {"type": b"@"},
                },
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
    b"callCopiedIntBlock:withValue:",
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


class BlockImplementation(objc.lookUpClass("NSObject")):
    @objc.objc_method(signature=b"d@:dd")
    def multiplyX_y_(self, x, y):
        return x * y


class TestBlocks(TestCase):
    @min_os_level("10.6")
    def testOptionalBlock(self):
        obj = OCTestBlock.alloc().init()

        self.assertEqual(obj.callOptionalBlock_withValue_(None, "hello"), "NOBLOCK")
        self.assertEqual(
            obj.callOptionalBlock_withValue_(lambda x: x + x, "hello"), "hellohello"
        )

    def test_block_is_collected(self):

        for use_function in (0, 1):
            with self.subTest(use_function=use_function):
                deleted = False

                if use_function:

                    class Setter:
                        def __del__(self):
                            nonlocal deleted
                            deleted = True

                    def Callable():
                        def result(arg):
                            return [arg]

                        result.attr = Setter()  # noqa: B023
                        return result  # noqa: B023

                else:

                    class Callable:
                        def __call__(self, arg):
                            return [arg]

                        def __del__(self):
                            nonlocal deleted
                            deleted = True

                self.assertFalse(deleted)
                c = Callable()
                del c

                self.assertTrue(deleted)

                deleted = False

                self.assertFalse(deleted)
                with objc.autorelease_pool():
                    obj = OCTestBlock.alloc().init()

                    result = obj.callOptionalBlock_withValue_(Callable(), 42)
                    self.assertEqual(result, [42])

                    del obj

                self.assertTrue(deleted)

    def test_block_is_stored(self):

        for use_function in (0, 1):
            with self.subTest(use_function=use_function):
                deleted = False

                if use_function:

                    class Setter:
                        def __del__(self):
                            nonlocal deleted
                            deleted = True

                    def Callable():
                        def result(arg1, arg2):
                            return [arg1, arg2]

                        result.attr = Setter()  # noqa: B023
                        return result  # noqa: B023

                else:

                    class Callable:
                        def __call__(self, arg1, arg2):
                            return [arg1, arg2]

                        def __del__(self):
                            nonlocal deleted
                            deleted = True

                self.assertFalse(deleted)
                c = Callable()
                del c

                self.assertTrue(deleted)

                deleted = False

                self.assertFalse(deleted)
                with objc.autorelease_pool():
                    obj = OCTestBlock.alloc().init()
                    self.assertIs(obj.getStoredBlock(), None)

                    obj.storeBlock_(Callable())

                    bl = obj.getStoredBlock()
                    v = bl(1, 2)
                    self.assertIsInstance(v, list)
                    self.assertEqual(v, [1, 2])

                    del bl
                    del obj

                self.assertTrue(deleted)

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

        lst = []

        obj.callCopiedIntBlock_withValue_(callback, 142)
        self.assertEqual(len(lst), 1)
        obj.callCopiedIntBlock_withValue_(callback, 143)
        self.assertEqual(len(lst), 2)

        self.assertEqual(lst, [142, 143])

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

        def callback(v1):
            return v1

        with self.assertRaisesRegex(
            ValueError, "did not return None, expecting void return value"
        ):
            obj.callIntBlock_withValue_(callback, 42)

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

        def callback(a, b):
            return

        with self.assertRaisesRegex(ValueError, "returned None, expecting a value"):
            obj.callDoubleBlock_withValue_andValue_(callback, 2.5, 10)

    def test_bound_selector_as_block(self):
        obj = OCTestBlock.alloc().init()
        helper = BlockImplementation()

        self.assertResultHasType(BlockImplementation.multiplyX_y_, objc._C_DBL)
        self.assertArgHasType(BlockImplementation.multiplyX_y_, 1, objc._C_DBL)
        self.assertArgHasType(BlockImplementation.multiplyX_y_, 1, objc._C_DBL)

        self.assertEqual(
            obj.callDoubleBlock_withValue_andValue_(helper.multiplyX_y_, 2.0, 3.5), 7.0
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

        block2 = obj.getIntBlock()
        self.assertIs(block, block2)

    def test_block_multiple_proxy(self):
        obj = OCTestBlock.alloc().init()

        block = obj.getIntBlock()

        a = NSMutableArray.alloc().init()
        a.addObject_(block)
        a.addObject_(block)

        del block

        b1 = a.objectAtIndex_(0)
        b2 = a.objectAtIndex_(1)

        self.assertIs(b1, b2)

        v = b1()
        self.assertEqual(v, 42)

    @min_os_level("10.6")
    def testBlockFromObjC2(self):
        obj = OCTestBlock.alloc().init()

        block = obj.getFloatBlock()
        value = block(1, 2)
        self.assertEqual(value, 4.0)

        value = block(2.5, 7.0)
        self.assertEqual(value, 11.5)

        with self.assertRaisesRegex(ValueError, "depythonifying 'double', got 'str'"):
            block(2.5, "seven")

        with self.assertRaisesRegex(TypeError, "Need 2 arguments, got 3"):
            block(2.5, 7.0, 11.5)

    def test_raising_block(self):
        obj = OCTestBlock.alloc().init()
        block = obj.getRaisingBlock()

        with self.assertRaisesRegex(objc.error, "SimpleException - hello world"):
            block()

    def test_variadic_block(self):
        obj = OCTestBlock.alloc().init()
        block = obj.getVariadicBlock()

        v = block("a", "b", object)
        self.assertEqual(v, ["a", "b", object])

        with self.assertRaisesRegex(
            TypeError, "At most 64 arguments are supported, got 100 arguments"
        ):
            block(*range(100))

        with self.assertRaisesRegex(TypeError, "Need 1 arguments, got 0"):
            block()

    def test_printf_block(self):
        obj = OCTestBlock.alloc().init()
        block = obj.getPrintfBlock()

        v = block("%d %d", 10, 20)
        self.assertEqual(v, "10 20")

        with self.assertRaisesRegex(ValueError, "Too few arguments for format string"):
            block("%d %d", 10)

        with self.assertRaisesRegex(ValueError, "Too many arguments for format string"):
            block("%d %d", 10, 20, 30)

        with self.assertRaisesRegex(TypeError, "Need 1 arguments, got 0"):
            block()

        block = obj.getPrintfBlock2()
        with self.assertRaisesRegex(
            TypeError, "printf format with by-ref args not supported"
        ):
            block(None, "%d", 20)

        block = obj.getPrintfBlock3()
        with self.assertRaisesRegex(
            TypeError, "printf format with by-ref args not supported"
        ):
            block(None, "%d", 20)

    def test_hudge_block(self):
        obj = OCTestBlock.alloc().init()
        block = obj.getHugeBlock()

        with self.assertRaisesRegex(
            TypeError, "At most 64 arguments are supported, got 69 arguments"
        ):
            block(*range(69))

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


class TestInvalidCalling(TestCase):
    def test_wrong_signature(self):
        import objc._convenience as mod

        orig = mod._block_call

        try:

            def faker(*args):
                return orig(*args, 42)

            mod._block_call = faker

            obj = OCTestBlock.alloc().init()
            block = obj.getIntBlock()

            with self.assertRaises(TypeError):
                block()

        finally:
            mod._block_call = orig

    def test_wrong_block_call_invocation(self):
        import objc._convenience as mod

        obj = OCTestBlock.alloc().init()
        block = obj.getIntBlock()

        with self.assertRaisesRegex(TypeError, "not a block"):
            mod._block_call(42, block.__block_signature__, (), {})

        with self.assertRaisesRegex(TypeError, "not a block"):
            mod._block_call(obj, block.__block_signature__, (), {})

        with self.assertRaisesRegex(TypeError, "not a signature"):
            mod._block_call(block, 42, (), {})

        with self.assertRaisesRegex(TypeError, "cannot call block without a signature"):
            mod._block_call(block, None, (), {})

        with self.assertRaisesRegex(TypeError, "Need 0 arguments, got 1"):
            mod._block_call(block, block.__block_signature__, (42,), {})

        with self.assertRaisesRegex(TypeError, "keyword arguments not supported"):
            mod._block_call(block, block.__block_signature__, (), {"a": 42})

        with self.assertRaisesRegex(TypeError, "keyword arguments not supported"):
            mod._block_call(block, block.__block_signature__, (), 42)

    def test_with_bad_signature(self):
        obj = OCTestBlock.alloc().init()
        block = obj.getFloatBlock2()
        with self.assertRaisesRegex(objc.error, "Unhandled type"):
            block(1.0, 2.0)
