
from PyObjCTools.TestSupport import *
from CoreLocation import *

class TestCLLocationManager (TestCase):
    @min_os_level('10.6')
    def testMethods(self):
        self.failUnlessResultIsBOOL(CLLocationManager.locationServicesEnabled)


if __name__ == "__main__":
    main()
