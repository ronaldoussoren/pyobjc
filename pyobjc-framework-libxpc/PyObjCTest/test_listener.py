from PyObjCTools.TestSupport import TestCase, min_os_level

import xpc


class TestListener(TestCase):
    @min_os_level("14.4")
    def test_functions(self):
        self.assertArgHasType(
            xpc.xpc_listener_set_peer_code_signing_requirement, 1, b"n^t"
        )
        self.assertArgIsNullTerminated(
            xpc.xpc_listener_set_peer_code_signing_requirement, 1
        )

    @min_os_level("26.0")
    def test_functions26_0(self):
        xpc.xpc_listener_set_peer_requirement
