import dispatch
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestSourceAPI(TestCase):
    def test_types(self):
        self.assertIsOpaquePointer(dispatch.dispatch_source_type_t)

    def test_constants(self):
        self.assertIsInstance(
            dispatch.DISPATCH_SOURCE_TYPE_DATA_ADD, dispatch.dispatch_source_type_t
        )
        self.assertIsInstance(
            dispatch.DISPATCH_SOURCE_TYPE_DATA_OR, dispatch.dispatch_source_type_t
        )
        self.assertIsInstance(
            dispatch.DISPATCH_SOURCE_TYPE_MACH_SEND, dispatch.dispatch_source_type_t
        )
        self.assertIsInstance(
            dispatch.DISPATCH_SOURCE_TYPE_MACH_RECV, dispatch.dispatch_source_type_t
        )
        self.assertIsInstance(
            dispatch.DISPATCH_SOURCE_TYPE_MEMORYPRESSURE,
            dispatch.dispatch_source_type_t,
        )
        self.assertIsInstance(
            dispatch.DISPATCH_SOURCE_TYPE_PROC, dispatch.dispatch_source_type_t
        )
        self.assertIsInstance(
            dispatch.DISPATCH_SOURCE_TYPE_READ, dispatch.dispatch_source_type_t
        )
        self.assertIsInstance(
            dispatch.DISPATCH_SOURCE_TYPE_SIGNAL, dispatch.dispatch_source_type_t
        )
        self.assertIsInstance(
            dispatch.DISPATCH_SOURCE_TYPE_TIMER, dispatch.dispatch_source_type_t
        )
        self.assertIsInstance(
            dispatch.DISPATCH_SOURCE_TYPE_VNODE, dispatch.dispatch_source_type_t
        )
        self.assertIsInstance(
            dispatch.DISPATCH_SOURCE_TYPE_WRITE, dispatch.dispatch_source_type_t
        )

        self.assertEqual(dispatch.DISPATCH_MACH_SEND_DEAD, 0x1)
        self.assertEqual(dispatch.DISPATCH_MEMORYPRESSURE_NORMAL, 0x01)
        self.assertEqual(dispatch.DISPATCH_MEMORYPRESSURE_WARN, 0x02)
        self.assertEqual(dispatch.DISPATCH_MEMORYPRESSURE_CRITICAL, 0x04)

        self.assertEqual(dispatch.DISPATCH_PROC_EXIT, 0x80000000)
        self.assertEqual(dispatch.DISPATCH_PROC_FORK, 0x40000000)
        self.assertEqual(dispatch.DISPATCH_PROC_EXEC, 0x20000000)
        self.assertEqual(dispatch.DISPATCH_PROC_SIGNAL, 0x08000000)

        self.assertEqual(dispatch.DISPATCH_VNODE_DELETE, 0x1)
        self.assertEqual(dispatch.DISPATCH_VNODE_WRITE, 0x2)
        self.assertEqual(dispatch.DISPATCH_VNODE_EXTEND, 0x4)
        self.assertEqual(dispatch.DISPATCH_VNODE_ATTRIB, 0x8)
        self.assertEqual(dispatch.DISPATCH_VNODE_LINK, 0x10)
        self.assertEqual(dispatch.DISPATCH_VNODE_RENAME, 0x20)
        self.assertEqual(dispatch.DISPATCH_VNODE_REVOKE, 0x40)
        self.assertEqual(dispatch.DISPATCH_VNODE_FUNLOCK, 0x100)

        self.assertEqual(dispatch.DISPATCH_TIMER_STRICT, 0x1)

    @min_os_level("10.13")
    def test_constants10_13(self):
        self.assertIsInstance(
            dispatch.DISPATCH_SOURCE_TYPE_DATA_REPLACE, dispatch.dispatch_source_type_t
        )

    @min_os_level("10.6")
    def test_functions(self):
        self.assertResultIsRetained(dispatch.dispatch_source_create)
        self.assertResultHasType(dispatch.dispatch_source_create, objc._C_ID)
        self.assertArgHasType(
            dispatch.dispatch_source_create,
            0,
            dispatch.dispatch_source_type_t.__typestr__,
        )
        self.assertArgHasType(dispatch.dispatch_source_create, 1, objc._C_ULNG)
        self.assertArgHasType(dispatch.dispatch_source_create, 2, objc._C_ULNG)
        self.assertArgHasType(dispatch.dispatch_source_create, 3, objc._C_ID)

        self.assertResultHasType(
            dispatch.dispatch_source_set_event_handler, objc._C_VOID
        )
        self.assertArgHasType(dispatch.dispatch_source_set_event_handler, 0, objc._C_ID)
        self.assertArgIsBlock(dispatch.dispatch_source_set_event_handler, 1, b"v")

        self.assertResultHasType(
            dispatch.dispatch_source_set_event_handler_f, objc._C_VOID
        )
        self.assertArgHasType(
            dispatch.dispatch_source_set_event_handler_f, 0, objc._C_ID
        )
        self.assertArgIsFunction(
            dispatch.dispatch_source_set_event_handler_f, 1, b"v^v", 1
        )

        self.assertResultHasType(
            dispatch.dispatch_source_set_cancel_handler, objc._C_VOID
        )
        self.assertArgHasType(
            dispatch.dispatch_source_set_cancel_handler, 0, objc._C_ID
        )
        self.assertArgIsBlock(dispatch.dispatch_source_set_cancel_handler, 1, b"v")

        self.assertResultHasType(
            dispatch.dispatch_source_set_cancel_handler_f, objc._C_VOID
        )
        self.assertArgHasType(
            dispatch.dispatch_source_set_cancel_handler_f, 0, objc._C_ID
        )
        self.assertArgIsFunction(
            dispatch.dispatch_source_set_cancel_handler_f, 1, b"v^v", 1
        )

        self.assertResultHasType(dispatch.dispatch_source_cancel, objc._C_VOID)
        self.assertArgHasType(dispatch.dispatch_source_cancel, 0, objc._C_ID)

        self.assertResultHasType(dispatch.dispatch_source_testcancel, objc._C_LNG)
        self.assertArgHasType(dispatch.dispatch_source_testcancel, 0, objc._C_ID)

        self.assertResultHasType(dispatch.dispatch_source_get_handle, objc._C_ULNG)
        self.assertArgHasType(dispatch.dispatch_source_get_handle, 0, objc._C_ID)

        self.assertResultHasType(dispatch.dispatch_source_get_mask, objc._C_ULNG)
        self.assertArgHasType(dispatch.dispatch_source_get_mask, 0, objc._C_ID)

        self.assertResultHasType(dispatch.dispatch_source_get_data, objc._C_ULNG)
        self.assertArgHasType(dispatch.dispatch_source_get_data, 0, objc._C_ID)

        self.assertResultHasType(dispatch.dispatch_source_merge_data, objc._C_VOID)
        self.assertArgHasType(dispatch.dispatch_source_merge_data, 0, objc._C_ID)
        self.assertArgHasType(dispatch.dispatch_source_merge_data, 1, objc._C_ULNG)

        self.assertResultHasType(dispatch.dispatch_source_set_timer, objc._C_VOID)
        self.assertArgHasType(dispatch.dispatch_source_set_timer, 0, objc._C_ID)
        self.assertArgHasType(dispatch.dispatch_source_set_timer, 1, objc._C_ULNGLNG)
        self.assertArgHasType(dispatch.dispatch_source_set_timer, 2, objc._C_ULNGLNG)
        self.assertArgHasType(dispatch.dispatch_source_set_timer, 3, objc._C_ULNGLNG)

        self.assertResultHasType(
            dispatch.dispatch_source_set_registration_handler, objc._C_VOID
        )
        self.assertArgHasType(
            dispatch.dispatch_source_set_registration_handler, 0, objc._C_ID
        )
        self.assertArgIsBlock(
            dispatch.dispatch_source_set_registration_handler, 1, b"v"
        )

        self.assertResultHasType(
            dispatch.dispatch_source_set_registration_handler_f, objc._C_VOID
        )
        self.assertArgHasType(
            dispatch.dispatch_source_set_registration_handler_f, 0, objc._C_ID
        )
        self.assertArgIsFunction(
            dispatch.dispatch_source_set_registration_handler_f, 1, b"v^v", 1
        )
