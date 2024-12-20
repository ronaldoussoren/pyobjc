import objc  # noqa: F401
import sys
import sysconfig
from PyObjCTools.TestSupport import TestCase, skipUnless


class TestFreeThreadingBasic(TestCase):
    @skipUnless(
        sysconfig.get_config_var("Py_GIL_DISABLED")
        and sys._xoptions.get("gil", None) != "1",
        "only relevant for the free-threaded build",
    )
    def test_gil_disabled(self):
        # Check that the GIL is actually disabled when importing PyObjC.
        self.assertFalse(sys._is_gil_enabled())
