import dispatch
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestQueueAPI(TestCase):
    def test_constants(self):
        # self.assertFalse(hasattr(dispatch, "DISPATCH_APPLY_AUTO_AVAILABLE"))
        self.assertEqual(dispatch.DISPATCH_APPLY_AUTO, None)

        self.assertEqual(dispatch.DISPATCH_APPLY_AUTO, None)
        self.assertEqual(dispatch.DISPATCH_QUEUE_SERIAL, None)
        self.assertEqual(dispatch.DISPATCH_TARGET_QUEUE_DEFAULT, None)
        self.assertEqual(dispatch.DISPATCH_CURRENT_QUEUE_LABEL, None)

        self.assertEqual(dispatch.DISPATCH_QUEUE_PRIORITY_HIGH, 2)
        self.assertEqual(dispatch.DISPATCH_QUEUE_PRIORITY_DEFAULT, 0)
        self.assertEqual(dispatch.DISPATCH_QUEUE_PRIORITY_LOW, -2)
        self.assertEqual(dispatch.DISPATCH_QUEUE_PRIORITY_BACKGROUND, -(2**15))

        self.assertEqual(dispatch.DISPATCH_AUTORELEASE_FREQUENCY_INHERIT, 0)
        self.assertEqual(dispatch.DISPATCH_AUTORELEASE_FREQUENCY_WORK_ITEM, 1)
        self.assertEqual(dispatch.DISPATCH_AUTORELEASE_FREQUENCY_NEVER, 2)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(dispatch.DISPATCH_QUEUE_CONCURRENT, objc.objc_object)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(dispatch.DISPATCH_QUEUE_SERIAL_INACTIVE, objc.objc_object)
        self.assertIsInstance(
            dispatch.DISPATCH_QUEUE_CONCURRENT_INACTIVE, objc.objc_object
        )
        self.assertIsInstance(
            dispatch.DISPATCH_QUEUE_SERIAL_WITH_AUTORELEASE_POOL, objc.objc_object
        )
        self.assertIsInstance(
            dispatch.DISPATCH_QUEUE_CONCURRENT_WITH_AUTORELEASE_POOL,
            objc.objc_object,
        )

    @min_os_level("10.6")
    def test_functions(self):
        self.assertResultHasType(dispatch.dispatch_async, objc._C_VOID)
        self.assertArgHasType(
            dispatch.dispatch_async, 0, objc._C_ID
        )  # dispatch_queue_t
        self.assertArgIsBlock(dispatch.dispatch_async, 1, b"v")

        self.assertResultHasType(dispatch.dispatch_async_f, objc._C_VOID)
        self.assertArgHasType(
            dispatch.dispatch_async_f, 0, objc._C_ID
        )  # dispatch_queue_t
        self.assertArgHasType(dispatch.dispatch_async_f, 1, objc._C_PTR + objc._C_VOID)
        self.assertArgIsFunction(dispatch.dispatch_async_f, 2, b"v^v", 1)

        self.assertResultHasType(dispatch.dispatch_sync, objc._C_VOID)
        self.assertArgHasType(dispatch.dispatch_sync, 0, objc._C_ID)  # dispatch_queue_t
        self.assertArgIsBlock(dispatch.dispatch_sync, 1, b"v")

        self.assertResultHasType(dispatch.dispatch_sync_f, objc._C_VOID)
        self.assertArgHasType(
            dispatch.dispatch_sync_f, 0, objc._C_ID
        )  # dispatch_queue_t
        self.assertArgHasType(dispatch.dispatch_sync_f, 1, objc._C_PTR + objc._C_VOID)
        self.assertArgIsFunction(dispatch.dispatch_sync_f, 2, b"v^v", 0)

        self.assertResultHasType(dispatch.dispatch_apply, objc._C_VOID)
        self.assertArgHasType(dispatch.dispatch_apply, 0, objc._C_ULNG)
        self.assertArgHasType(
            dispatch.dispatch_apply, 1, objc._C_ID
        )  # dispatch_queue_t
        self.assertArgIsBlock(dispatch.dispatch_apply, 2, b"vQ")

        self.assertResultHasType(dispatch.dispatch_apply_f, objc._C_VOID)
        self.assertArgHasType(dispatch.dispatch_apply_f, 0, objc._C_ULNG)
        self.assertArgHasType(
            dispatch.dispatch_apply_f, 1, objc._C_ID
        )  # dispatch_queue_t
        self.assertArgHasType(dispatch.dispatch_apply_f, 2, objc._C_PTR + objc._C_VOID)
        self.assertArgIsFunction(dispatch.dispatch_apply_f, 3, b"v^vQ", 1)

        self.assertResultHasType(dispatch.dispatch_get_current_queue, objc._C_ID)

        self.assertResultHasType(dispatch.dispatch_get_main_queue, objc._C_ID)

        self.assertResultHasType(dispatch.dispatch_get_global_queue, objc._C_ID)
        self.assertArgHasType(dispatch.dispatch_get_global_queue, 0, objc._C_LNG)
        self.assertArgHasType(dispatch.dispatch_get_global_queue, 1, objc._C_ULNG)

        self.assertResultHasType(dispatch.dispatch_set_target_queue, objc._C_VOID)
        self.assertArgHasType(dispatch.dispatch_set_target_queue, 0, objc._C_ID)
        self.assertArgHasType(dispatch.dispatch_set_target_queue, 1, objc._C_ID)

        self.assertResultHasType(
            dispatch.dispatch_queue_get_label, objc._C_PTR + objc._C_CHAR_AS_TEXT
        )
        self.assertResultIsNullTerminated(dispatch.dispatch_queue_get_label)
        self.assertArgHasType(dispatch.dispatch_queue_get_label, 0, objc._C_ID)

        self.assertResultHasType(dispatch.dispatch_queue_create, objc._C_ID)
        self.assertArgHasType(
            dispatch.dispatch_queue_create,
            0,
            objc._C_IN + objc._C_PTR + objc._C_CHAR_AS_TEXT,
        )
        self.assertArgIsNullTerminated(dispatch.dispatch_queue_create, 0)
        self.assertArgHasType(dispatch.dispatch_queue_create, 1, objc._C_ID)

        self.assertResultHasType(dispatch.dispatch_main, objc._C_VOID)

        self.assertResultHasType(dispatch.dispatch_after, objc._C_VOID)
        self.assertArgHasType(dispatch.dispatch_after, 0, objc._C_ULNGLNG)
        self.assertArgHasType(
            dispatch.dispatch_after, 1, objc._C_ID
        )  # dispatch_queue_t
        self.assertArgIsBlock(dispatch.dispatch_after, 2, b"v")

        self.assertResultHasType(dispatch.dispatch_after_f, objc._C_VOID)
        self.assertArgHasType(dispatch.dispatch_after_f, 0, objc._C_ULNGLNG)
        self.assertArgHasType(
            dispatch.dispatch_after_f, 1, objc._C_ID
        )  # dispatch_queue_t
        self.assertArgHasType(dispatch.dispatch_after_f, 2, objc._C_PTR + objc._C_VOID)
        self.assertArgIsFunction(dispatch.dispatch_after_f, 3, b"v^v", 1)

    @min_os_level("10.7")
    def testFunctions10_7(self):
        self.assertResultHasType(dispatch.dispatch_barrier_async, objc._C_VOID)
        self.assertArgHasType(
            dispatch.dispatch_barrier_async, 0, objc._C_ID
        )  # dispatch_queue_t
        self.assertArgIsBlock(dispatch.dispatch_barrier_async, 1, b"v")

        self.assertResultHasType(dispatch.dispatch_barrier_async_f, objc._C_VOID)
        self.assertArgHasType(
            dispatch.dispatch_barrier_async_f, 0, objc._C_ID
        )  # dispatch_queue_t
        self.assertArgHasType(
            dispatch.dispatch_barrier_async_f, 1, objc._C_PTR + objc._C_VOID
        )
        self.assertArgIsFunction(dispatch.dispatch_barrier_async_f, 2, b"v^v", 1)

        self.assertResultHasType(dispatch.dispatch_barrier_sync, objc._C_VOID)
        self.assertArgHasType(
            dispatch.dispatch_barrier_sync, 0, objc._C_ID
        )  # dispatch_queue_t
        self.assertArgIsBlock(dispatch.dispatch_barrier_sync, 1, b"v")

        self.assertResultHasType(dispatch.dispatch_barrier_sync_f, objc._C_VOID)
        self.assertArgHasType(
            dispatch.dispatch_barrier_sync_f, 0, objc._C_ID
        )  # dispatch_queue_t
        self.assertArgHasType(
            dispatch.dispatch_barrier_sync_f, 1, objc._C_PTR + objc._C_VOID
        )
        self.assertArgIsFunction(dispatch.dispatch_barrier_sync_f, 2, b"v^v", 0)

        self.assertResultHasType(dispatch.dispatch_queue_set_specific, objc._C_VOID)
        self.assertArgHasType(
            dispatch.dispatch_queue_set_specific, 0, objc._C_ID
        )  # dispatch_queue_t
        self.assertArgHasType(
            dispatch.dispatch_queue_set_specific, 1, objc._C_PTR + objc._C_VOID
        )
        self.assertArgHasType(
            dispatch.dispatch_queue_set_specific, 2, objc._C_PTR + objc._C_VOID
        )
        self.assertArgIsFunction(dispatch.dispatch_queue_set_specific, 3, b"v^v", 1)

        self.assertResultHasType(
            dispatch.dispatch_queue_get_specific, objc._C_PTR + objc._C_VOID
        )
        self.assertArgHasType(
            dispatch.dispatch_queue_get_specific, 0, objc._C_ID
        )  # dispatch_queue_t
        self.assertArgHasType(
            dispatch.dispatch_queue_get_specific, 1, objc._C_PTR + objc._C_VOID
        )

        self.assertResultHasType(
            dispatch.dispatch_get_specific, objc._C_PTR + objc._C_VOID
        )
        self.assertArgHasType(
            dispatch.dispatch_get_specific, 0, objc._C_PTR + objc._C_VOID
        )

    @min_os_level("10.10")
    def testFunctions10_10(self):
        self.assertResultHasType(
            dispatch.dispatch_queue_attr_make_with_qos_class, objc._C_ID
        )
        self.assertArgHasType(
            dispatch.dispatch_queue_attr_make_with_qos_class, 0, objc._C_ID
        )
        self.assertArgHasType(
            dispatch.dispatch_queue_attr_make_with_qos_class, 1, objc._C_UINT
        )
        self.assertArgHasType(
            dispatch.dispatch_queue_attr_make_with_qos_class, 2, objc._C_INT
        )

        self.assertResultHasType(dispatch.dispatch_queue_get_qos_class, objc._C_UINT)
        self.assertArgHasType(dispatch.dispatch_queue_get_qos_class, 0, objc._C_ID)
        self.assertArgHasType(
            dispatch.dispatch_queue_get_qos_class,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_INT,
        )

    @min_os_level("10.12")
    def testFunctions10_12(self):
        self.assertResultHasType(
            dispatch.dispatch_queue_attr_make_initially_inactive, objc._C_ID
        )
        self.assertArgHasType(
            dispatch.dispatch_queue_attr_make_initially_inactive, 0, objc._C_ID
        )

        self.assertResultHasType(
            dispatch.dispatch_queue_attr_make_with_autorelease_frequency, objc._C_ID
        )
        self.assertArgHasType(
            dispatch.dispatch_queue_attr_make_with_autorelease_frequency,
            0,
            objc._C_ID,
        )
        self.assertArgHasType(
            dispatch.dispatch_queue_attr_make_with_autorelease_frequency,
            1,
            objc._C_ULNG,
        )

        self.assertResultIsRetained(dispatch.dispatch_queue_create)
        self.assertResultIsRetained(dispatch.dispatch_queue_create_with_target)
        self.assertResultHasType(dispatch.dispatch_queue_create_with_target, objc._C_ID)
        self.assertArgHasType(
            dispatch.dispatch_queue_create_with_target,
            0,
            objc._C_IN + objc._C_PTR + objc._C_CHAR_AS_TEXT,
        )
        self.assertArgIsNullTerminated(dispatch.dispatch_queue_create_with_target, 0)
        self.assertArgHasType(dispatch.dispatch_queue_create_with_target, 1, objc._C_ID)
        self.assertArgHasType(dispatch.dispatch_queue_create_with_target, 2, objc._C_ID)

        self.assertResultHasType(dispatch.dispatch_assert_queue, objc._C_VOID)
        self.assertArgHasType(dispatch.dispatch_assert_queue, 0, objc._C_ID)

        self.assertResultHasType(dispatch.dispatch_assert_queue_barrier, objc._C_VOID)
        self.assertArgHasType(dispatch.dispatch_assert_queue_barrier, 0, objc._C_ID)

        self.assertResultHasType(dispatch.dispatch_assert_queue_not, objc._C_VOID)
        self.assertArgHasType(dispatch.dispatch_assert_queue_not, 0, objc._C_ID)

    @min_os_level("10.14")
    def test_functions10_14(self):
        self.assertResultHasType(dispatch.dispatch_async_and_wait, objc._C_VOID)
        self.assertArgHasType(
            dispatch.dispatch_async_and_wait, 0, objc._C_ID
        )  # dispatch_queue_t
        self.assertArgIsBlock(dispatch.dispatch_async_and_wait, 1, b"v")

        self.assertResultHasType(dispatch.dispatch_async_and_wait_f, objc._C_VOID)
        self.assertArgHasType(
            dispatch.dispatch_async_and_wait_f, 0, objc._C_ID
        )  # dispatch_queue_t
        self.assertArgHasType(
            dispatch.dispatch_async_and_wait_f, 1, objc._C_PTR + objc._C_VOID
        )
        self.assertArgIsFunction(dispatch.dispatch_async_and_wait_f, 2, b"v^v", 1)

        self.assertResultHasType(dispatch.dispatch_barrier_async_and_wait, objc._C_VOID)
        self.assertArgHasType(
            dispatch.dispatch_barrier_async_and_wait, 0, objc._C_ID
        )  # dispatch_queue_t
        self.assertArgIsBlock(dispatch.dispatch_barrier_async_and_wait, 1, b"v")

        self.assertResultHasType(
            dispatch.dispatch_barrier_async_and_wait_f, objc._C_VOID
        )
        self.assertArgHasType(
            dispatch.dispatch_barrier_async_and_wait_f, 0, objc._C_ID
        )  # dispatch_queue_t
        self.assertArgHasType(
            dispatch.dispatch_barrier_async_and_wait_f, 1, objc._C_PTR + objc._C_VOID
        )
        self.assertArgIsFunction(
            dispatch.dispatch_barrier_async_and_wait_f, 2, b"v^v", 1
        )
