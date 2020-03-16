import libdispatch
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestBlockAPI(TestCase):
    def test_constants(self):
        self.assertEqual(libdispatch.DISPATCH_BLOCK_BARRIER, 0x1)
        self.assertEqual(libdispatch.DISPATCH_BLOCK_DETACHED, 0x2)
        self.assertEqual(libdispatch.DISPATCH_BLOCK_ASSIGN_CURRENT, 0x4)
        self.assertEqual(libdispatch.DISPATCH_BLOCK_NO_QOS_CLASS, 0x8)
        self.assertEqual(libdispatch.DISPATCH_BLOCK_INHERIT_QOS_CLASS, 0x10)
        self.assertEqual(libdispatch.DISPATCH_BLOCK_ENFORCE_QOS_CLASS, 0x20)

    @min_os_level("10.10")
    def test_functions(self):
        self.assertResultIsBlock(libdispatch.dispatch_block_create, b"v")
        self.assertArgHasType(libdispatch.dispatch_block_create, 0, objc._C_ULNG)
        self.assertArgIsBlock(libdispatch.dispatch_block_create, 1, b"v")

        self.assertResultIsBlock(libdispatch.dispatch_block_create_with_qos_class, b"v")
        self.assertArgHasType(
            libdispatch.dispatch_block_create_with_qos_class, 0, objc._C_ULNG
        )
        self.assertArgHasType(
            libdispatch.dispatch_block_create_with_qos_class, 1, objc._C_UINT
        )
        self.assertArgHasType(
            libdispatch.dispatch_block_create_with_qos_class, 2, objc._C_INT
        )
        self.assertArgIsBlock(libdispatch.dispatch_block_create_with_qos_class, 3, b"v")

        self.assertResultHasType(libdispatch.dispatch_block_perform, objc._C_VOID)
        self.assertArgHasType(libdispatch.dispatch_block_perform, 0, objc._C_ULNG)
        self.assertArgIsBlock(libdispatch.dispatch_block_perform, 1, b"v")

        self.assertResultHasType(libdispatch.dispatch_block_wait, objc._C_LNG)
        self.assertArgIsBlock(libdispatch.dispatch_block_wait, 0, b"v")
        self.assertArgHasType(libdispatch.dispatch_block_wait, 1, objc._C_ULNGLNG)

        self.assertResultHasType(libdispatch.dispatch_block_notify, objc._C_VOID)
        self.assertArgIsBlock(libdispatch.dispatch_block_notify, 0, b"v")
        self.assertArgHasType(
            libdispatch.dispatch_block_notify, 1, objc._C_ID
        )  # dispatch_queue_t
        self.assertArgIsBlock(libdispatch.dispatch_block_notify, 2, b"v")

        self.assertResultHasType(libdispatch.dispatch_block_cancel, objc._C_VOID)
        self.assertArgIsBlock(libdispatch.dispatch_block_cancel, 0, b"v")

        self.assertResultHasType(libdispatch.dispatch_block_testcancel, objc._C_LNG)
        self.assertArgIsBlock(libdispatch.dispatch_block_testcancel, 0, b"v")
