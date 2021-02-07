from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

import Network

nw_browser_browse_results_changed_handler_t = b"v@@" + objc._C_BOOL
nw_browser_state_changed_handler_t = b"v@@"


class TestBrowser(TestCase):
    def test_constants(self):
        self.assertEqual(Network.nw_browser_state_invalid, 0)
        self.assertEqual(Network.nw_browser_state_ready, 1)
        self.assertEqual(Network.nw_browser_state_failed, 2)
        self.assertEqual(Network.nw_browser_state_cancelled, 3)
        self.assertEqual(Network.nw_browser_state_waiting, 4)

    @min_os_level("10.15")
    def test_functions10_15(self):
        self.assertResultIsRetained(Network.nw_browser_create)

        Network.nw_browser_set_queue

        self.assertArgIsBlock(
            Network.nw_browser_set_browse_results_changed_handler,
            1,
            nw_browser_browse_results_changed_handler_t,
        )
        self.assertArgIsBlock(
            Network.nw_browser_set_state_changed_handler,
            1,
            nw_browser_state_changed_handler_t,
        )

        Network.nw_browser_start
        Network.nw_browser_cancel

        self.assertResultIsRetained(Network.nw_browser_copy_parameters)
        self.assertResultIsRetained(Network.nw_browser_copy_browse_descriptor)
