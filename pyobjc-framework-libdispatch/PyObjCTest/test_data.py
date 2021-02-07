import libdispatch
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level

dispatch_data_applier_t = b"B@Ln^vL"


class TestDataAPI(TestCase):
    @min_os_level("10.7")
    def test_constants(self):
        self.assertIsInstance(libdispatch.dispatch_data_empty, objc.objc_object)
        self.assertIsInstance(
            libdispatch.DISPATCH_DATA_DESTRUCTOR_FREE, objc.objc_object
        )

        self.assertIs(libdispatch.DISPATCH_DATA_DESTRUCTOR_DEFAULT, None)

    @min_os_level("10.9")
    def test_constants10_9(self):
        self.assertIsInstance(
            libdispatch.DISPATCH_DATA_DESTRUCTOR_MUNMAP, objc.objc_object
        )

    @min_os_level("10.7")
    def test_functions(self):
        self.assertResultHasType(libdispatch.dispatch_data_create, objc._C_ID)
        self.assertArgHasType(
            libdispatch.dispatch_data_create, 0, objc._C_IN + objc._C_PTR + objc._C_VOID
        )
        self.assertArgSizeInArg(libdispatch.dispatch_data_create, 0, 1)
        self.assertArgHasType(libdispatch.dispatch_data_create, 1, objc._C_ULNG)
        self.assertArgHasType(
            libdispatch.dispatch_data_create, 2, objc._C_ID
        )  # dispatch_queue_t
        self.assertArgIsBlock(libdispatch.dispatch_data_create, 3, b"v")

        self.assertResultHasType(libdispatch.dispatch_data_get_size, objc._C_ULNG)
        self.assertArgHasType(libdispatch.dispatch_data_get_size, 0, objc._C_ID)

        # FIXME: dispatch_data_create_map
        self.assertIsInstance(libdispatch.dispatch_data_create_map, type(id))

        self.assertResultHasType(libdispatch.dispatch_data_create_concat, objc._C_ID)
        self.assertArgHasType(libdispatch.dispatch_data_create_concat, 0, objc._C_ID)
        self.assertArgHasType(libdispatch.dispatch_data_create_concat, 1, objc._C_ID)

        self.assertResultHasType(libdispatch.dispatch_data_create_subrange, objc._C_ID)
        self.assertArgHasType(libdispatch.dispatch_data_create_subrange, 0, objc._C_ID)
        self.assertArgHasType(
            libdispatch.dispatch_data_create_subrange, 1, objc._C_ULNG
        )
        self.assertArgHasType(
            libdispatch.dispatch_data_create_subrange, 2, objc._C_ULNG
        )

        self.assertResultHasType(libdispatch.dispatch_data_apply, objc._C_BOOL)
        self.assertArgHasType(libdispatch.dispatch_data_apply, 0, objc._C_ID)
        self.assertArgIsBlock(
            libdispatch.dispatch_data_apply, 1, dispatch_data_applier_t
        )

        self.assertResultHasType(libdispatch.dispatch_data_copy_region, objc._C_ID)
        self.assertArgHasType(libdispatch.dispatch_data_copy_region, 0, objc._C_ID)
        self.assertArgHasType(libdispatch.dispatch_data_copy_region, 1, objc._C_ULNG)
        self.assertArgHasType(
            libdispatch.dispatch_data_copy_region,
            2,
            objc._C_OUT + objc._C_PTR + objc._C_ULNG,
        )


class TestDataUsage(TestCase):
    def test_basic(self):
        d1 = libdispatch.dispatch_data_create(
            b"hello ", 6, None, libdispatch.DISPATCH_DATA_DESTRUCTOR_DEFAULT
        )
        self.assertIsNot(d1, None)

        d2 = libdispatch.dispatch_data_create(
            b"world", 5, None, libdispatch.DISPATCH_DATA_DESTRUCTOR_DEFAULT
        )
        self.assertIsNot(d2, None)

        self.assertEqual(libdispatch.dispatch_data_get_size(d1), 6)

        d, b, s = libdispatch.dispatch_data_create_map(d1, None, None)
        self.assertIsNot(d, None)
        self.assertIsInstance(b, memoryview)
        self.assertEqual(b.tobytes(), b"hello ")
        self.assertEqual(s, 6)

        con = libdispatch.dispatch_data_create_concat(d1, d2)

        lst = []

        def worker(region, offset, buf, size):
            lst.append((region, offset, buf, size))
            return True

        ok = libdispatch.dispatch_data_apply(con, worker)
        self.assertEqual(ok, True)
        self.assertEqual(len(lst), 2)
        self.assertEqual(lst[0][1:], (0, b"hello ", 6))
        self.assertEqual(lst[1][1:], (6, b"world", 5))

        d, b, s = libdispatch.dispatch_data_create_map(con, None, None)
        self.assertIsNot(d, None)
        self.assertIsInstance(b, memoryview)
        self.assertEqual(b.tobytes(), b"hello world")
        self.assertEqual(s, 11)
