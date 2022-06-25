import JavaScriptCore  # noqa: F401
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestJSExport(TestCase):
    @min_os_level("10.9")
    def test_protocols(self):
        self.assertProtocolExists("JSExport")

    # XXX: JSExportAs support
