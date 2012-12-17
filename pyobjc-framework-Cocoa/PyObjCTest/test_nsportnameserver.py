from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSPortNameServer (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSPortNameServer.registerPort_name_)
        self.assertResultIsBOOL(NSPortNameServer.removePortForName_)

        self.assertResultIsBOOL(NSMachBootstrapServer.registerPort_name_)

        self.assertResultIsBOOL(NSSocketPortNameServer.registerPort_name_)
        self.assertResultIsBOOL(NSSocketPortNameServer.removePortForName_)
        self.assertResultIsBOOL(NSSocketPortNameServer.registerPort_name_nameServerPortNumber_)



if __name__ == "__main__":
    main()
