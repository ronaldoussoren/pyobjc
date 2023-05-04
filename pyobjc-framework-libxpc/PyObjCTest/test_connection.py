from PyObjCTools.TestSupport import TestCase, min_os_level

import xpc
import objc
import platform

xpc_finalizer_t = b"v^v"


class TestConnection(TestCase):
    def test_constants(self):
        self.assertIsInstance(xpc.XPC_ERROR_CONNECTION_INTERRUPTED, objc.objc_object)
        self.assertIsInstance(xpc.XPC_ERROR_CONNECTION_INVALID, objc.objc_object)
        self.assertIsInstance(xpc.XPC_ERROR_TERMINATION_IMMINENT, objc.objc_object)

        self.assertEqual(xpc.XPC_CONNECTION_MACH_SERVICE_LISTENER, 1 << 0)
        self.assertEqual(xpc.XPC_CONNECTION_MACH_SERVICE_PRIVILEGED, 1 << 1)

    @min_os_level("12.0")
    def test_constants12_0(self):
        if (
            platform.mac_ver()[0] != "10.16"
        ):  # Skip test on Python's build with pre-11.0 SDK
            self.assertIsInstance(
                xpc.XPC_ERROR_PEER_CODE_SIGNING_REQUIREMENT, objc.objc_object
            )

    def test_functions(self):
        self.assertResultIsRetained(xpc.xpc_connection_create)
        self.assertArgIsIn(xpc.xpc_connection_create, 0)
        self.assertArgIsNullTerminated(xpc.xpc_connection_create, 0)

        self.assertResultIsRetained(xpc.xpc_connection_create_mach_service)
        self.assertArgIsIn(xpc.xpc_connection_create_mach_service, 0)
        self.assertArgIsNullTerminated(xpc.xpc_connection_create_mach_service, 0)

        self.assertResultIsRetained(xpc.xpc_connection_create_from_endpoint)

        xpc.xpc_connection_set_target_queue

        self.assertArgIsBlock(xpc.xpc_connection_set_event_handler, 1, b"v@")

        xpc.xpc_connection_suspend
        xpc.xpc_connection_resume
        xpc.xpc_connection_send_message
        xpc.xpc_connection_send_barrier

        self.assertArgIsBlock(xpc.xpc_connection_send_message_with_reply, 3, b"v@")

        xpc.xpc_connection_send_message_with_reply_sync
        xpc.xpc_connection_cancel

        self.assertResultIsNullTerminated(xpc.xpc_connection_get_name)

        xpc.xpc_connection_get_euid
        xpc.xpc_connection_get_egid
        xpc.xpc_connection_get_pid
        xpc.xpc_connection_get_asid
        xpc.xpc_connection_set_context
        xpc.xpc_connection_get_context

        self.assertArgIsFunction(
            xpc.xpc_connection_set_finalizer_f, 1, xpc_finalizer_t, True
        )

    @min_os_level("10.12")
    def test_functions10_12(self):
        xpc.xpc_connection_activate

    @min_os_level("12.0")
    def test_functions12_0(self):
        self.assertArgIsIn(xpc.xpc_connection_set_peer_code_signing_requirement, 1)
        self.assertArgIsNullTerminated(
            xpc.xpc_connection_set_peer_code_signing_requirement, 1
        )
