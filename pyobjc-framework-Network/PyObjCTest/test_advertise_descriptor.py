from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

import Network


class TestAdvertiseDescriptor(TestCase):
    def test_functions(self):
        self.assertResultHasType(
            Network.nw_advertise_descriptor_create_bonjour_service, objc._C_ID
        )
        self.assertResultIsRetained(
            Network.nw_advertise_descriptor_create_bonjour_service
        )
        self.assertArgIsIn(Network.nw_advertise_descriptor_create_bonjour_service, 0)
        self.assertArgIsNullTerminated(
            Network.nw_advertise_descriptor_create_bonjour_service, 0
        )
        self.assertArgIsIn(Network.nw_advertise_descriptor_create_bonjour_service, 1)
        self.assertArgIsNullTerminated(
            Network.nw_advertise_descriptor_create_bonjour_service, 1
        )
        self.assertArgIsIn(Network.nw_advertise_descriptor_create_bonjour_service, 2)
        self.assertArgIsNullTerminated(
            Network.nw_advertise_descriptor_create_bonjour_service, 2
        )

        self.assertArgIsIn(Network.nw_advertise_descriptor_set_txt_record, 1)
        self.assertArgSizeInArg(Network.nw_advertise_descriptor_set_txt_record, 1, 2)

        self.assertArgHasType(
            Network.nw_advertise_descriptor_set_no_auto_rename, 1, objc._C_BOOL
        )
        self.assertResultHasType(
            Network.nw_advertise_descriptor_get_no_auto_rename, objc._C_BOOL
        )

    @min_os_level("10.15")
    def test_functions10_15(self):
        Network.nw_advertise_descriptor_set_txt_record_object

        self.assertResultIsRetained(
            Network.nw_advertise_descriptor_copy_txt_record_object
        )

    @min_os_level("11.0")
    def test_functions11_0(self):
        self.assertResultIsRetained(
            Network.nw_advertise_descriptor_copy_txt_record_object
        )
