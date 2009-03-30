from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSPortNameServer (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSPortNameServer.registerPort_name_)
        self.failUnlessResultIsBOOL(NSPortNameServer.removePortForName_)

        self.failUnlessResultIsBOOL(NSMachBootstrapServer.registerPort_name_)

        self.failUnlessResultIsBOOL(NSSocketPortNameServer.registerPort_name_)
        self.failUnlessResultIsBOOL(NSSocketPortNameServer.removePortForName_)
        self.failUnlessResultIsBOOL(NSSocketPortNameServer.registerPort_name_nameServerPortNumber_)

    

if __name__ == "__main__":
    main()
