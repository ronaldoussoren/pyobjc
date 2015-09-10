from PyObjCTools.TestSupport import *
from WebKit import *

class TestWKScriptMessageHandler (TestCase):
    @onlyOn64Bit
    @min_os_level('10.10')
    def testProtocols10_10(self):
        p = objc.protocolNamed("WKScriptMessageHandler")
        self.assertIsInstance(p, objc.formal_protocol)


if __name__ == "__main__":
    main()
