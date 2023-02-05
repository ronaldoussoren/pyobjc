import dispatch
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestObjectAPI(TestCase):
    @min_os_level("10.6")
    def test_functions(self):
        self.assertFalse(hasattr(dispatch, "dispatch_retain"))
        self.assertFalse(hasattr(dispatch, "dispatch_release"))

        self.assertResultHasType(
            dispatch.dispatch_get_context, objc._C_PTR + objc._C_VOID
        )
        self.assertArgHasType(dispatch.dispatch_get_context, 0, objc._C_ID)

        self.assertResultHasType(dispatch.dispatch_set_context, objc._C_VOID)
        self.assertArgHasType(dispatch.dispatch_set_context, 0, objc._C_ID)
        self.assertArgHasType(
            dispatch.dispatch_set_context, 1, objc._C_PTR + objc._C_VOID
        )

        self.assertResultHasType(dispatch.dispatch_set_finalizer_f, objc._C_VOID)
        self.assertArgHasType(dispatch.dispatch_set_finalizer_f, 0, objc._C_ID)
        self.assertArgIsFunction(dispatch.dispatch_set_finalizer_f, 1, b"v^v", 1)

        self.assertResultHasType(dispatch.dispatch_suspend, objc._C_VOID)
        self.assertArgHasType(dispatch.dispatch_suspend, 0, objc._C_ID)

        self.assertResultHasType(dispatch.dispatch_resume, objc._C_VOID)
        self.assertArgHasType(dispatch.dispatch_resume, 0, objc._C_ID)

        self.assertFalse(hasattr(dispatch, "dispatch_wait"))
        # Generic function macro, not available as C function
        # self.assertResultHasType(dispatch.dispatch_wait, objc._C_LNG)
        # self.assertArgHasType(dispatch.dispatch_wait, 0, objc._C_ID)
        # self.assertArgHasType(dispatch.dispatch_wait, 1, objc._C_ULNGLNG)

        self.assertFalse(hasattr(dispatch, "dispatch_notify"))
        # Generic function macro, not available as C function
        # self.assertResultHasType(dispatch.dispatch_notify, objc._C_VOID)
        # self.assertArgHasType(dispatch.dispatch_notify, 0, objc._C_ID)
        # self.assertArgHasType(dispatch.dispatch_notify, 1, objc._C_ID) # dispatch_object_t
        # self.assertArgIslock(dispatch.dispatch_notify, 2, b'v')

        self.assertFalse(hasattr(dispatch, "dispatch_cancel"))
        # Generic function macro, not available as C function
        # self.assertResultHasType(dispatch.dispatch_cancel, objc._C_VOID)
        # self.assertArgHasType(dispatch.dispatch_cancel, 0, objc._C_ID)

        self.assertFalse(hasattr(dispatch, "dispatch_testcancel"))
        # Generic function macro, not available as C function
        # self.assertResultHasType(dispatch.dispatch_testcancel, objc._C_LNG)
        # self.assertArgHasType(dispatch.dispatch_testcancel, 0, objc._C_ID)

        self.assertFalse(hasattr(dispatch, "dispatch_debug"))
        self.assertFalse(hasattr(dispatch, "dispatch_debugv"))

    @min_os_level("10.12")
    def test_functions_10_12(self):
        self.assertResultHasType(dispatch.dispatch_activate, objc._C_VOID)
        self.assertArgHasType(dispatch.dispatch_activate, 0, objc._C_ID)

    @min_os_level("10.14")
    def test_functions_10_14(self):
        self.assertResultHasType(dispatch.dispatch_set_qos_class_floor, objc._C_VOID)
        self.assertArgHasType(dispatch.dispatch_set_qos_class_floor, 0, objc._C_ID)
        self.assertArgHasType(dispatch.dispatch_set_qos_class_floor, 1, objc._C_UINT)
        self.assertArgHasType(dispatch.dispatch_set_qos_class_floor, 2, objc._C_INT)
