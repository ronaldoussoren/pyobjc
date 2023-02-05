from PyObjCTools.TestSupport import TestCase, min_os_level

import xpc

xpc_session_cancel_handler_t = b"v@"
xpc_session_incoming_message_handler_t = b"v@"
xpc_session_reply_handler_t = b"v@@"


class TestSession(TestCase):
    def test_constants(self):
        self.assertIsEnumType(xpc.xpc_session_create_flags_t)
        self.assertEqual(xpc.XPC_SESSION_CREATE_NONE, 0)
        self.assertEqual(xpc.XPC_SESSION_CREATE_INACTIVE, 1 << 0)
        self.assertEqual(xpc.XPC_SESSION_CREATE_MACH_PRIVILEGED, 1 << 1)

    @min_os_level("13.0")
    def test_functions(self):
        self.assertResultIsNullTerminated(xpc.xpc_session_copy_description)

        self.assertResultIsRetained(xpc.xpc_session_create_xpc_service)
        self.assertArgIsIn(xpc.xpc_session_create_xpc_service, 0)
        self.assertArgIsNullTerminated(xpc.xpc_session_create_xpc_service, 0)
        self.assertArgIsOut(xpc.xpc_session_create_xpc_service, 3)

        self.assertResultIsRetained(xpc.xpc_session_create_mach_service)
        self.assertArgIsIn(xpc.xpc_session_create_mach_service, 0)
        self.assertArgIsNullTerminated(xpc.xpc_session_create_mach_service, 0)
        self.assertArgIsOut(xpc.xpc_session_create_mach_service, 3)

        self.assertArgIsBlock(
            xpc.xpc_session_set_incoming_message_handler,
            1,
            xpc_session_incoming_message_handler_t,
        )
        self.assertArgIsBlock(
            xpc.xpc_session_set_cancel_handler, 1, xpc_session_cancel_handler_t
        )

        self.assertArgIsOut(xpc.xpc_session_activate, 1)

        xpc.xpc_session_cancel

        self.assertResultIsRetained(xpc.xpc_session_send_message)

        self.assertResultIsRetained(xpc.xpc_session_send_message_with_reply_sync)
        self.assertArgIsOut(xpc.xpc_session_send_message_with_reply_sync, 2)

        self.assertArgIsBlock(
            xpc.xpc_session_send_message_with_reply_async,
            2,
            xpc_session_reply_handler_t,
        )
