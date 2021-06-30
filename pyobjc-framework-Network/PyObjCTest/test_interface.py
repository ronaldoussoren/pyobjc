from PyObjCTools.TestSupport import TestCase

import Network


class TestInterface(TestCase):
    def test_constants(self):
        self.assertEqual(Network.nw_interface_type_other, 0)
        self.assertEqual(Network.nw_interface_type_wifi, 1)
        self.assertEqual(Network.nw_interface_type_cellular, 2)
        self.assertEqual(Network.nw_interface_type_wired, 3)
        self.assertEqual(Network.nw_interface_type_loopback, 4)

        self.assertEqual(Network.nw_interface_radio_type_unknown, 0)
        self.assertEqual(Network.nw_interface_radio_type_wifi_b, 1)
        self.assertEqual(Network.nw_interface_radio_type_wifi_a, 2)
        self.assertEqual(Network.nw_interface_radio_type_wifi_g, 3)
        self.assertEqual(Network.nw_interface_radio_type_wifi_n, 4)
        self.assertEqual(Network.nw_interface_radio_type_wifi_ac, 5)
        self.assertEqual(Network.nw_interface_radio_type_wifi_ax, 6)
        self.assertEqual(Network.nw_interface_radio_type_cell_lte, 0x80)
        self.assertEqual(Network.nw_interface_radio_type_cell_endc_sub6, 0x81)
        self.assertEqual(Network.nw_interface_radio_type_cell_endc_mmw, 0x82)
        self.assertEqual(Network.nw_interface_radio_type_cell_nr_sa_sub6, 0x83)
        self.assertEqual(Network.nw_interface_radio_type_cell_nr_sa_mmw, 0x84)
        self.assertEqual(Network.nw_interface_radio_type_cell_wcdma, 0x85)
        self.assertEqual(Network.nw_interface_radio_type_cell_gsm, 0x86)
        self.assertEqual(Network.nw_interface_radio_type_cell_cdma, 0x87)
        self.assertEqual(Network.nw_interface_radio_type_cell_evdo, 0x88)

    def test_functions(self):
        Network.nw_interface_get_type

        self.assertResultIsNullTerminated(Network.nw_interface_get_name)
        self.assertResultHasType(Network.nw_interface_get_name, b"^t")

        Network.nw_interface_get_index
