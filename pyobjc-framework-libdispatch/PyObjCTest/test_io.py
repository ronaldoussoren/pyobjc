import libdispatch
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level

dispatch_io_handler_t = b"vB@i"


class TestIoAPI(TestCase):
    def test_constants(self):
        self.assertEqual(libdispatch.DISPATCH_IO_STREAM, 0)
        self.assertEqual(libdispatch.DISPATCH_IO_RANDOM, 1)

        self.assertEqual(libdispatch.DISPATCH_IO_STOP, 0x1)

        self.assertEqual(libdispatch.DISPATCH_IO_STRICT_INTERVAL, 0x1)

    @min_os_level("10.7")
    def test_functions(self):
        self.assertResultHasType(libdispatch.dispatch_read, objc._C_VOID)
        self.assertArgHasType(libdispatch.dispatch_read, 0, objc._C_INT)
        self.assertArgHasType(libdispatch.dispatch_read, 1, objc._C_ULNG)
        self.assertArgHasType(
            libdispatch.dispatch_read, 2, objc._C_ID
        )  # dispatch_queue_t
        self.assertArgIsBlock(libdispatch.dispatch_read, 3, b"v@i")

        self.assertResultHasType(libdispatch.dispatch_write, objc._C_VOID)
        self.assertArgHasType(libdispatch.dispatch_write, 0, objc._C_INT)
        self.assertArgHasType(
            libdispatch.dispatch_write, 1, objc._C_ID
        )  # dispatch_data_t
        self.assertArgHasType(
            libdispatch.dispatch_write, 2, objc._C_ID
        )  # dispatch_queue_t
        self.assertArgIsBlock(libdispatch.dispatch_write, 3, b"v@i")

        self.assertResultHasType(libdispatch.dispatch_io_create, objc._C_ID)
        self.assertArgHasType(libdispatch.dispatch_io_create, 0, objc._C_ULNG)
        self.assertArgHasType(libdispatch.dispatch_io_create, 1, objc._C_INT)
        self.assertArgHasType(libdispatch.dispatch_io_create, 2, objc._C_ID)
        self.assertArgIsBlock(libdispatch.dispatch_write, 3, b"v@i")

        self.assertResultHasType(libdispatch.dispatch_io_create_with_path, objc._C_ID)
        self.assertArgHasType(libdispatch.dispatch_io_create_with_path, 0, objc._C_ULNG)
        self.assertArgHasType(
            libdispatch.dispatch_io_create_with_path,
            1,
            objc._C_IN + objc._C_PTR + objc._C_CHAR_AS_TEXT,
        )
        self.assertArgIsNullTerminated(libdispatch.dispatch_io_create_with_path, 1)
        self.assertArgHasType(libdispatch.dispatch_io_create_with_path, 2, objc._C_INT)
        self.assertArgHasType(libdispatch.dispatch_io_create_with_path, 3, objc._C_USHT)
        self.assertArgHasType(libdispatch.dispatch_io_create_with_path, 4, objc._C_ID)
        self.assertArgIsBlock(libdispatch.dispatch_io_create_with_path, 5, b"vi")

        self.assertResultHasType(libdispatch.dispatch_io_create_with_io, objc._C_ID)
        self.assertArgHasType(libdispatch.dispatch_io_create_with_io, 0, objc._C_ULNG)
        self.assertArgHasType(
            libdispatch.dispatch_io_create_with_io, 1, objc._C_ID
        )  # dispatch_io_t
        self.assertArgHasType(
            libdispatch.dispatch_io_create_with_io, 2, objc._C_ID
        )  # dispatch_queue_t
        self.assertArgIsBlock(libdispatch.dispatch_write, 3, b"v@i")

        self.assertResultHasType(libdispatch.dispatch_io_read, objc._C_VOID)
        self.assertArgHasType(
            libdispatch.dispatch_io_read, 0, objc._C_ID
        )  # dispatch_io_t
        self.assertArgHasType(libdispatch.dispatch_io_read, 1, objc._C_LNGLNG)
        self.assertArgHasType(libdispatch.dispatch_io_read, 2, objc._C_ULNG)
        self.assertArgHasType(
            libdispatch.dispatch_io_read, 3, objc._C_ID
        )  # dispatch_queue_t
        self.assertArgIsBlock(libdispatch.dispatch_io_read, 4, dispatch_io_handler_t)

        self.assertResultHasType(libdispatch.dispatch_io_write, objc._C_VOID)
        self.assertArgHasType(
            libdispatch.dispatch_io_write, 0, objc._C_ID
        )  # dispatch_io_t
        self.assertArgHasType(libdispatch.dispatch_io_write, 1, objc._C_LNGLNG)
        self.assertArgHasType(
            libdispatch.dispatch_io_write, 2, objc._C_ID
        )  # dispatch_data_t
        self.assertArgHasType(
            libdispatch.dispatch_io_write, 3, objc._C_ID
        )  # dispatch_queue_t
        self.assertArgIsBlock(libdispatch.dispatch_io_write, 4, dispatch_io_handler_t)

        self.assertResultHasType(libdispatch.dispatch_io_close, objc._C_VOID)
        self.assertArgHasType(
            libdispatch.dispatch_io_close, 0, objc._C_ID
        )  # dispatch_io_t
        self.assertArgHasType(libdispatch.dispatch_io_close, 1, objc._C_ULNG)

        self.assertResultHasType(libdispatch.dispatch_io_barrier, objc._C_VOID)
        self.assertArgHasType(
            libdispatch.dispatch_io_barrier, 0, objc._C_ID
        )  # dispatch_io_t
        self.assertArgIsBlock(libdispatch.dispatch_io_barrier, 1, b"v")

        self.assertResultHasType(libdispatch.dispatch_io_get_descriptor, objc._C_INT)
        self.assertArgHasType(
            libdispatch.dispatch_io_get_descriptor, 0, objc._C_ID
        )  # dispatch_io_t

        self.assertResultHasType(libdispatch.dispatch_io_set_high_water, objc._C_VOID)
        self.assertArgHasType(
            libdispatch.dispatch_io_set_high_water, 0, objc._C_ID
        )  # dispatch_io_t
        self.assertArgHasType(libdispatch.dispatch_io_set_high_water, 1, objc._C_ULNG)

        self.assertResultHasType(libdispatch.dispatch_io_set_low_water, objc._C_VOID)
        self.assertArgHasType(
            libdispatch.dispatch_io_set_low_water, 0, objc._C_ID
        )  # dispatch_io_t
        self.assertArgHasType(libdispatch.dispatch_io_set_low_water, 1, objc._C_ULNG)

        self.assertResultHasType(libdispatch.dispatch_io_set_interval, objc._C_VOID)
        self.assertArgHasType(
            libdispatch.dispatch_io_set_interval, 0, objc._C_ID
        )  # dispatch_io_t
        self.assertArgHasType(libdispatch.dispatch_io_set_interval, 1, objc._C_ULNGLNG)
        self.assertArgHasType(libdispatch.dispatch_io_set_interval, 2, objc._C_ULNG)
