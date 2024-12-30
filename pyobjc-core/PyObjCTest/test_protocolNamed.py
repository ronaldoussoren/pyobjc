import objc
import objc._objc
from objc._protocols import PROTOCOL_CACHE
from PyObjCTools.TestSupport import TestCase


class TestProtocols(TestCase):
    def testBasic(self):
        PROTOCOL_CACHE.clear()
        p = objc.protocolNamed("NSObject")
        self.assertIsInstance(p, objc.formal_protocol)

    def testNoProtocol(self):
        # XXX: I don't like this exception text, but changing the way the exception
        #      is raised is not backward compatible
        with self.assertRaisesRegex(
            objc.ProtocolError,
            """("protocol 'PyObjCFooBarProtocol' does not exist", 'PyObjCFooBarProtocol')""",
        ):
            objc.protocolNamed("PyObjCFooBarProtocol")

    def testBasic2(self):
        orig_protocolsForProcess = objc._objc.protocolsForProcess
        try:
            objc._objc.protocolsForProcess = lambda: []
            PROTOCOL_CACHE.clear()

            p = objc.protocolNamed("NSObject")
            self.assertIsInstance(p, objc.formal_protocol)

        finally:
            objc._objc.protocolsForProcess = orig_protocolsForProcess

    def test_protocolForClass(self):
        with self.assertRaisesRegex(TypeError, "missing required argument"):
            objc.protocolsForClass()

        result = objc.protocolsForClass(objc.lookUpClass("NSObject"))
        self.assertIsInstance(result, list)
        self.assertNotEqual(len(result), 0)
        for item in result:
            self.assertIsInstance(item, objc.formal_protocol)
