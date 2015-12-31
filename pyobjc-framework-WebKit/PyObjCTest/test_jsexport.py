from PyObjCTools.TestSupport import *

import JavaScriptCore
import objc

class TestJSExport (TestCase):
    @onlyOn64Bit
    @min_os_level('10.9')
    def test_protocols(self):
        import sysconfig
        target = sysconfig.get_config_var('MACOSX_DEPLOYMENT_TARGET')
        if target in ('10.6', '10.7', '10.9'):
           # The protocol is not available for older binaries...
           return

        self.assertIsInstance(objc.protocolNamed('JSExport'), objc.formal_protocol)

    # XXX: JSExportAs support

if __name__ == "__main__":
    main()
