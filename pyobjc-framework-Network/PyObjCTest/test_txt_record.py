from PyObjCTools.TestSupport import TestCase, min_os_level

import Network

nw_txt_record_access_key_t = b"Bn^t@n^vL"
nw_txt_record_access_bytes_t = b"Bn^vL"
nw_txt_record_applier_t = b"Bn^t@n^vL"


class TestTxtRecord(TestCase):
    def test_constants(self):
        self.assertEqual(Network.nw_txt_record_find_key_invalid, 0)
        self.assertEqual(Network.nw_txt_record_find_key_not_present, 1)
        self.assertEqual(Network.nw_txt_record_find_key_no_value, 2)
        self.assertEqual(Network.nw_txt_record_find_key_empty_value, 3)
        self.assertEqual(Network.nw_txt_record_find_key_non_empty_value, 4)

    @min_os_level("10.15")
    def test_functions10_15(self):
        self.assertResultIsRetained(Network.nw_txt_record_create_with_bytes)
        self.assertArgHasType(Network.nw_txt_record_create_with_bytes, 0, b"n^v")
        self.assertArgSizeInArg(Network.nw_txt_record_create_with_bytes, 0, 1)

        self.assertResultIsRetained(Network.nw_txt_record_create_dictionary)
        self.assertResultIsRetained(Network.nw_txt_record_copy)

        self.assertArgHasType(Network.nw_txt_record_find_key, 1, b"n^t")
        self.assertArgIsNullTerminated(Network.nw_txt_record_find_key, 1)

        self.assertArgIsIn(Network.nw_txt_record_access_key, 1)
        self.assertArgIsNullTerminated(Network.nw_txt_record_access_key, 1)
        self.assertArgIsBlock(
            Network.nw_txt_record_access_key, 2, nw_txt_record_access_key_t
        )

        self.assertArgIsIn(Network.nw_txt_record_set_key, 1)
        self.assertArgIsNullTerminated(Network.nw_txt_record_set_key, 1)
        self.assertArgHasType(Network.nw_txt_record_set_key, 2, b"n^v")
        self.assertArgSizeInArg(Network.nw_txt_record_set_key, 2, 3)

        self.assertArgIsIn(Network.nw_txt_record_remove_key, 1)
        self.assertArgIsNullTerminated(Network.nw_txt_record_remove_key, 1)

        Network.nw_txt_record_get_key_count

        self.assertArgIsBlock(
            Network.nw_txt_record_access_bytes, 1, nw_txt_record_access_bytes_t
        )

        self.assertArgIsBlock(Network.nw_txt_record_apply, 1, nw_txt_record_applier_t)

        Network.nw_txt_record_is_equal
        Network.nw_txt_record_is_dictionary
