
from PyObjCTools.TestSupport import *
from CoreLocation import *

class TestCLLocationManager (TestCase):
    @min_os_level('10.6')
    def testMethods(self):
        self.assertResultIsBOOL(CLLocationManager.locationServicesEnabled)


if __name__ == "__main__":
    main()
