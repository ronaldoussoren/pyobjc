import objc
from PyObjCTools.TestSupport import *

class TestProtocols (TestCase):
    def testBasic(self):
        p = objc.protocolNamed('NSObject')
        self.assert_(isinstance(p, objc.formal_protocol))
        #self.assert_(isinstance(p, objc.lookUpClass('Protocol')))

    def testNoProtocol(self):
        self.assertRaises(objc.ProtocolError, objc.protocolNamed, "PyObjCFooBarProtocol")

if __name__ == "__main__":
    main()
