from PyObjCTools.TestSupport import TestCase

import Network

nw_path_monitor_cancel_handler_t = b"v"
nw_path_monitor_update_handler_t = b"v@"


class TestPathMonitor(TestCase):
    def test_functions(self):
        self.assertResultIsRetained(Network.nw_path_monitor_create)

        self.assertResultIsRetained(Network.nw_path_monitor_create_with_type)

        self.assertArgIsBlock(
            Network.nw_path_monitor_set_cancel_handler,
            1,
            nw_path_monitor_cancel_handler_t,
        )

        self.assertArgIsBlock(
            Network.nw_path_monitor_set_update_handler,
            1,
            nw_path_monitor_update_handler_t,
        )

        Network.nw_path_monitor_set_queue
        Network.nw_path_monitor_start
        Network.nw_path_monitor_cancel
