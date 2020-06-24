from PyObjCTools.TestSupport import TestCase, min_os_level

import Network


class TestBrowseDescriptor(TestCase):
    @min_os_level("10.15")
    def test_functions10_15(self):

        self.assertResultIsRetained(Network.nw_browse_descriptor_create_bonjour_service)
        self.assertArgIsIn(Network.nw_browse_descriptor_create_bonjour_service, 0)
        self.assertArgIsNullTerminated(
            Network.nw_browse_descriptor_create_bonjour_service, 0
        )
        self.assertArgIsIn(Network.nw_browse_descriptor_create_bonjour_service, 1)
        self.assertArgIsNullTerminated(
            Network.nw_browse_descriptor_create_bonjour_service, 1
        )

        self.assertResultIsNullTerminated(
            Network.nw_browse_descriptor_get_bonjour_service_type
        )
        self.assertResultIsNullTerminated(
            Network.nw_browse_descriptor_get_bonjour_service_domain
        )
        Network.nw_browse_descriptor_set_include_txt_record
        Network.nw_browse_descriptor_get_include_txt_record
