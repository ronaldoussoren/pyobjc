import objc
from PyObjCTools.TestSupport import *

class TestProtocols (TestCase):
    def testBasic(self):
        p = objc.protocolNamed('NSObject')
        self.assertIsInstance(p, objc.formal_protocol)

    def testNoProtocol(self):
        self.assertRaises(objc.ProtocolError, objc.protocolNamed, "PyObjCFooBarProtocol")

if __name__ == "__main__":
    main()
