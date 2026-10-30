import Cocoa  # noqa: F401
import objc
from PyObjCTools import AppHelper
from PyObjCTools.TestSupport import TestCase


class TestAppHelper(TestCase):
    def test_call_after(self):
        pass

    def test_call_later(self):
        pass

    def test_stop_eventloop(self):
        pass

    def test_endsheetmethod(self):
        v = AppHelper.endSheetMethod(lambda x: None)
        self.assertEqual(v.signature, b"v@:@" + objc._C_NSInteger + objc._C_NSInteger)

    def test_run_console_eventloop(self):
        pass

    def test_run_eventloop(self):
        pass
