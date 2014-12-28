from PyObjCTools.TestSupport import *

import JavaScriptCore
import objc

class TestJSExport (TestCase):
    @onlyOn64Bit
    @min_os_level('10.9')
    def test_protocols(self):
        self.assertIsInstance(objc.protocolNamed('JSExport'), objc.formal_protocol)

if __name__ == "__main__":
    main()
