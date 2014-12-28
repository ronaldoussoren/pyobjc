from PyObjCTools.TestSupport import *
import ServiceManagement

class TestSMLoginItem (TestCase):
    @min_os_level('10.6')
    def testFunctions(self):
        self.assertResultIsBOOL(ServiceManagement.SMLoginItemSetEnabled)
        self.assertArgIsBOOL(ServiceManagement.SMLoginItemSetEnabled, 1)

if __name__ == "__main__":
    main()
