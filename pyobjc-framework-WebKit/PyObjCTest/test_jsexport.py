import JavaScriptCore  # noqa: F401
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestJSExport(TestCase):
    @min_os_level("10.9")
    def test_protocols(self):
        import sysconfig

        target = sysconfig.get_config_var("MACOSX_DEPLOYMENT_TARGET")
        if target in ("10.6", "10.7", "10.9"):
            # The protocol is not available for older binaries...
            return

        self.assertIsInstance(objc.protocolNamed("JSExport"), objc.formal_protocol)

    # XXX: JSExportAs support
