
from PyObjCTools.TestSupport import *
from SyncServices import *

class TestISyncUIHelper (TestCase):
    @min_os_level('10.5')
    def testProtocols(self):
        self.assertIsInstance(protocols.SyncUIHelperInformalProtocol, objc.informal_protocol)

if __name__ == "__main__":
    main()
