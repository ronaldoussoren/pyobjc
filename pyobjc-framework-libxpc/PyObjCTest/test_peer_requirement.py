from PyObjCTools.TestSupport import TestCase, min_os_level

import xpc


class TestPeerRequirement(TestCase):
    @min_os_level("26.0")
    def test_functions26_0(self):
        self.assertResultIsRetained(xpc.xpc_peer_requirement_create_entitlement_exists)
        self.assertArgHasType(
            xpc.xpc_peer_requirement_create_entitlement_exists, 0, b"n^t"
        )
        self.assertArgIsNullTerminated(
            xpc.xpc_peer_requirement_create_entitlement_exists, 0
        )
        self.assertArgIsOut(xpc.xpc_peer_requirement_create_entitlement_exists, 1)

        self.assertResultIsRetained(
            xpc.xpc_peer_requirement_create_entitlement_matches_value
        )
        self.assertArgHasType(
            xpc.xpc_peer_requirement_create_entitlement_matches_value, 0, b"n^t"
        )
        self.assertArgIsNullTerminated(
            xpc.xpc_peer_requirement_create_entitlement_matches_value, 0
        )
        self.assertArgIsOut(
            xpc.xpc_peer_requirement_create_entitlement_matches_value, 2
        )

        self.assertResultIsRetained(xpc.xpc_peer_requirement_create_team_identity)
        self.assertArgHasType(xpc.xpc_peer_requirement_create_team_identity, 0, b"n^t")
        self.assertArgIsNullTerminated(xpc.xpc_peer_requirement_create_team_identity, 0)
        self.assertArgIsOut(xpc.xpc_peer_requirement_create_team_identity, 1)

        self.assertResultIsRetained(xpc.xpc_peer_requirement_create_platform_identity)
        self.assertArgHasType(
            xpc.xpc_peer_requirement_create_platform_identity, 0, b"n^t"
        )
        self.assertArgIsNullTerminated(
            xpc.xpc_peer_requirement_create_platform_identity, 0
        )
        self.assertArgIsOut(xpc.xpc_peer_requirement_create_platform_identity, 1)

        self.assertResultIsRetained(xpc.xpc_peer_requirement_create_lwcr)
        self.assertArgIsOut(xpc.xpc_peer_requirement_create_lwcr, 1)

        self.assertArgIsOut(xpc.xpc_peer_requirement_match_received_message, 2)
