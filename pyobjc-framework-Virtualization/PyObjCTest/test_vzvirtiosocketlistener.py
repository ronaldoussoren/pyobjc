from PyObjCTools.TestSupport import TestCase
import Virtualization


class TestVZVirtioSocketListenerHelper(Virtualization.NSObject):
    def listener_shouldAcceptNewConnection_fromSocketDevice_(self, a, b, c):
        return 1


class TestVZVirtioSocketListener(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("VZVirtioSocketListenerDelegate", Virtualization)

    def test_protocol_methods(self):
        self.assertResultIsBOOL(
            TestVZVirtioSocketListenerHelper.listener_shouldAcceptNewConnection_fromSocketDevice_
        )
