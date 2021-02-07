from PyObjCTools.TestSupport import TestCase

import Network


class TestInterface(TestCase):
    def test_constants(self):
        self.assertEqual(Network.nw_interface_type_other, 0)
        self.assertEqual(Network.nw_interface_type_wifi, 1)
        self.assertEqual(Network.nw_interface_type_cellular, 2)
        self.assertEqual(Network.nw_interface_type_wired, 3)
        self.assertEqual(Network.nw_interface_type_loopback, 4)

    def test_functions(self):
        Network.nw_interface_get_type

        self.assertResultIsNullTerminated(Network.nw_interface_get_name)
        self.assertResultHasType(Network.nw_interface_get_name, b"^t")

        Network.nw_interface_get_index
