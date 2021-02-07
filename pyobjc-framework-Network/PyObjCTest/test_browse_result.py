from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

import Network

nw_browse_result_enumerate_interface_t = objc._C_BOOL + objc._C_ID


class TestBrowseResult(TestCase):
    def test_constants(self):
        self.assertEqual(Network.nw_browse_result_change_invalid, 0x00)
        self.assertEqual(Network.nw_browse_result_change_identical, 0x01)
        self.assertEqual(Network.nw_browse_result_change_result_added, 0x02)
        self.assertEqual(Network.nw_browse_result_change_result_removed, 0x04)
        self.assertEqual(Network.nw_browse_result_change_interface_added, 0x08)
        self.assertEqual(Network.nw_browse_result_change_interface_removed, 0x10)
        self.assertEqual(Network.nw_browse_result_change_txt_record_changed, 0x20)

    @min_os_level("10.15")
    def test_functions10_15(self):
        self.assertResultIsRetained(Network.nw_browse_result_copy_endpoint)

        Network.nw_browse_result_get_changes
        Network.nw_browse_result_get_interfaces_count

        self.assertResultIsRetained(Network.nw_browse_result_copy_txt_record_object)

        self.assertArgIsBlock(
            Network.nw_browse_result_enumerate_interfaces,
            1,
            nw_browse_result_enumerate_interface_t,
        )
