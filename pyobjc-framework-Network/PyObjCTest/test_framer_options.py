from PyObjCTools.TestSupport import TestCase, min_os_level

import Network

nw_framer_message_dispose_value_t = b"v^v"
nw_framer_start_handler_t = b"i@"
nw_framer_input_handler_t = b"L@"
nw_framer_output_handler_t = b"v@@LB"
nw_framer_wakeup_handler_t = b"v@"
nw_framer_stop_handler_t = b"B@"
nw_framer_cleanup_handler_t = b"v@"
nw_framer_parse_completion_t = b"Ln^vLB"
nw_framer_block_t = b"v"


class TestFramerOptions(TestCase):
    def test_constants(self):
        self.assertEqual(Network.nw_framer_start_result_ready, 1)
        self.assertEqual(Network.nw_framer_start_result_will_mark_ready, 2)

        self.assertEqual(Network.NW_FRAMER_CREATE_FLAGS_DEFAULT, 0x00)

        self.assertEqual(Network.NW_FRAMER_WAKEUP_TIME_FOREVER, 0xFFFFFFFFFFFFFFFF)

    @min_os_level("10.15")
    def test_functions10_15(self):
        self.assertResultIsRetained(Network.nw_framer_protocol_create_message)

        Network.nw_protocol_metadata_is_framer_message

        self.assertResultIsRetained(Network.nw_framer_message_create)

        self.assertArgIsIn(Network.nw_framer_message_set_value, 1)
        self.assertArgIsNullTerminated(Network.nw_framer_message_set_value, 1)
        self.assertArgIsBlock(
            Network.nw_framer_message_set_value, 3, nw_framer_message_dispose_value_t
        )

        self.assertArgIsIn(Network.nw_framer_message_access_value, 1)
        self.assertArgIsNullTerminated(Network.nw_framer_message_access_value, 1)
        self.assertArgIsBlock(Network.nw_framer_message_access_value, 2, b"B^v")

        self.assertArgIsIn(Network.nw_framer_message_set_object_value, 1)
        self.assertArgIsNullTerminated(Network.nw_framer_message_set_object_value, 1)

        self.assertResultIsRetained(Network.nw_framer_message_copy_object_value)

        self.assertResultIsRetained(Network.nw_framer_create_definition)
        self.assertArgIsBlock(
            Network.nw_framer_create_definition, 2, nw_framer_start_handler_t
        )

        self.assertResultIsRetained(Network.nw_framer_create_options)

        self.assertArgIsBlock(
            Network.nw_framer_set_input_handler, 1, nw_framer_input_handler_t
        )

        self.assertArgIsBlock(
            Network.nw_framer_set_output_handler, 1, nw_framer_output_handler_t
        )

        self.assertArgIsBlock(
            Network.nw_framer_set_wakeup_handler, 1, nw_framer_wakeup_handler_t
        )

        self.assertArgIsBlock(
            Network.nw_framer_set_stop_handler, 1, nw_framer_stop_handler_t
        )

        self.assertArgIsBlock(
            Network.nw_framer_set_cleanup_handler, 1, nw_framer_cleanup_handler_t
        )

        Network.nw_framer_mark_ready
        Network.nw_framer_prepend_application_protocol
        Network.nw_framer_mark_failed_with_error

        # self.fail("nw_framer_parse_input: buffer lives longer than call")
        self.assertArgIsIn(Network.nw_framer_parse_input, 3)
        self.assertArgSizeInArg(Network.nw_framer_parse_input, 3, 2)
        self.assertArgIsBlock(
            Network.nw_framer_parse_input, 4, nw_framer_parse_completion_t
        )

        self.assertArgHasType(Network.nw_framer_deliver_input, 1, b"n^v")
        self.assertArgSizeInArg(Network.nw_framer_deliver_input, 1, 2)

        Network.nw_framer_deliver_input_no_copy
        Network.nw_framer_pass_through_input

        # self.fail("nw_framer_parse_output: buffer lives longer than call")
        self.assertArgIsOut(Network.nw_framer_parse_output, 3)
        self.assertArgSizeInArg(Network.nw_framer_parse_output, 3, 2)
        self.assertArgIsBlock(
            Network.nw_framer_parse_output, 4, nw_framer_parse_completion_t
        )

        self.assertArgHasType(Network.nw_framer_write_output, 1, b"n^v")
        self.assertArgSizeInArg(Network.nw_framer_write_output, 1, 2)

        Network.nw_framer_write_output_data
        Network.nw_framer_write_output_no_copy
        Network.nw_framer_pass_through_output
        Network.nw_framer_schedule_wakeup

        self.assertArgIsBlock(Network.nw_framer_async, 1, nw_framer_block_t)

        self.assertResultIsRetained(Network.nw_framer_copy_remote_endpoint)
        self.assertResultIsRetained(Network.nw_framer_copy_local_endpoint)
        self.assertResultIsRetained(Network.nw_framer_copy_parameters)

    @min_os_level("12.3")
    def test_functions12_3(self):
        self.assertArgIsIn(Network.nw_framer_options_set_object_value, 1)
        self.assertArgIsNullTerminated(Network.nw_framer_options_set_object_value, 1)

        self.assertResultIsRetained(Network.nw_framer_options_copy_object_value)
        self.assertArgIsIn(Network.nw_framer_options_copy_object_value, 1)
        self.assertArgIsNullTerminated(Network.nw_framer_options_copy_object_value, 1)

        self.assertResultIsRetained(Network.nw_framer_copy_options)
