import objc
import unittest

class TestProtocols (unittest.TestCase):
    def testBasic(self):
        p = objc.protocolNamed('NSObject')
        self.assert_(isinstance(p, objc.runtime.Protocol))

    def testNoProtocol(self):
        self.assertRaises(objc.ProtocolError, objc.protocolNamed, "PyObjCFooBarProtocol")

if __name__ == "__main__":
    unittest.main()
