import array

import libdispatch
from PyObjCTools.TestSupport import TestCase
import objc


class TestOnceAPI(TestCase):
    def test_functions(self):
        self.assertResultHasType(libdispatch.dispatch_once, objc._C_VOID)
        self.assertArgHasType(
            libdispatch.dispatch_once, 0, objc._C_INOUT + objc._C_PTR + objc._C_LNG
        )
        self.assertArgIsBlock(libdispatch.dispatch_once, 1, b"v")

        self.assertResultHasType(libdispatch.dispatch_once_f, objc._C_VOID)
        self.assertArgHasType(
            libdispatch.dispatch_once_f, 0, objc._C_INOUT + objc._C_PTR + objc._C_LNG
        )
        self.assertArgHasType(
            libdispatch.dispatch_once_f, 1, objc._C_PTR + objc._C_VOID
        )
        self.assertArgIsFunction(libdispatch.dispatch_once_f, 2, b"v^v", 0)


class TestOnceUsage(TestCase):
    def test_intvar(self):
        pred = 0
        record = []

        def function():
            record.append(None)

        self.assertRaises(TypeError, libdispatch.dispatch_once, pred, function)

    def test_arrayvar(self):
        pred = array.array("l", [0])
        record = []

        def function():
            record.append(None)

        libdispatch.dispatch_once(pred, function)
        libdispatch.dispatch_once(pred, function)

        self.assertEqual(record, [None])
