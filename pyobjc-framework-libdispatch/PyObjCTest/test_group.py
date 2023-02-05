import dispatch
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestGroupAPI(TestCase):
    @min_os_level("10.6")
    def test_functions(self):
        self.assertResultIsRetained(dispatch.dispatch_group_create)
        self.assertResultHasType(dispatch.dispatch_group_create, objc._C_ID)

        self.assertResultHasType(dispatch.dispatch_group_async, objc._C_VOID)
        self.assertArgHasType(
            dispatch.dispatch_group_async, 0, objc._C_ID
        )  # dispatch_group_t
        self.assertArgHasType(
            dispatch.dispatch_group_async, 1, objc._C_ID
        )  # dispatch_queue_t
        self.assertArgIsBlock(dispatch.dispatch_group_async, 2, b"v")

        self.assertResultHasType(dispatch.dispatch_group_async_f, objc._C_VOID)
        self.assertArgHasType(
            dispatch.dispatch_group_async_f, 0, objc._C_ID
        )  # dispatch_group_t
        self.assertArgHasType(
            dispatch.dispatch_group_async_f, 1, objc._C_ID
        )  # dispatch_queue_t
        self.assertArgHasType(dispatch.dispatch_group_async_f, 2, b"^v")
        self.assertArgIsFunction(dispatch.dispatch_group_async_f, 3, b"v^v", 1)

        self.assertResultHasType(dispatch.dispatch_group_wait, objc._C_LNG)
        self.assertArgHasType(
            dispatch.dispatch_group_wait, 0, objc._C_ID
        )  # dispatch_group_t
        self.assertArgHasType(dispatch.dispatch_group_wait, 1, objc._C_ULNGLNG)

        self.assertResultHasType(dispatch.dispatch_group_notify, objc._C_VOID)
        self.assertArgHasType(
            dispatch.dispatch_group_notify, 0, objc._C_ID
        )  # dispatch_group_t
        self.assertArgHasType(
            dispatch.dispatch_group_notify, 1, objc._C_ID
        )  # dispatch_queue_t
        self.assertArgIsBlock(dispatch.dispatch_group_notify, 2, b"v")

        self.assertResultHasType(dispatch.dispatch_group_notify_f, objc._C_VOID)
        self.assertArgHasType(
            dispatch.dispatch_group_notify_f, 0, objc._C_ID
        )  # dispatch_group_t
        self.assertArgHasType(
            dispatch.dispatch_group_notify_f, 1, objc._C_ID
        )  # dispatch_queue_t
        self.assertArgHasType(dispatch.dispatch_group_notify_f, 2, b"^v")
        self.assertArgIsFunction(dispatch.dispatch_group_notify_f, 3, b"v^v", 1)

        self.assertResultHasType(dispatch.dispatch_group_enter, objc._C_VOID)
        self.assertArgHasType(
            dispatch.dispatch_group_enter, 0, objc._C_ID
        )  # dispatch_group_t

        self.assertResultHasType(dispatch.dispatch_group_leave, objc._C_VOID)
        self.assertArgHasType(
            dispatch.dispatch_group_leave, 0, objc._C_ID
        )  # dispatch_group_t
