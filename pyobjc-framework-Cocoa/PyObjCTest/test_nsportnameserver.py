import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSPortNameServer(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(Foundation.NSPortNameServer.registerPort_name_)
        self.assertResultIsBOOL(Foundation.NSPortNameServer.removePortForName_)

        self.assertResultIsBOOL(Foundation.NSMachBootstrapServer.registerPort_name_)

        self.assertResultIsBOOL(Foundation.NSSocketPortNameServer.registerPort_name_)
        self.assertResultIsBOOL(Foundation.NSSocketPortNameServer.removePortForName_)
        self.assertResultIsBOOL(
            Foundation.NSSocketPortNameServer.registerPort_name_nameServerPortNumber_
        )
