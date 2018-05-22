from PyObjCTools.TestSupport import *

import CoreWLAN

class TestCWNetworkProfile (TestCase):
    @min_os_level('10.7')
    def test_methods10_7(self):
        self.assertResultIsBOOL(CoreWLAN.CWNetworkProfile.isEqualToNetworkProfile_);

    @min_os_level('10.7')
    def testConvenience(self):
       c1 = CoreWLAN.CWNetworkProfile.alloc().init()
       c2 = CoreWLAN.CWNetworkProfile.alloc().init()

       self.assertTrue(c1 == c2)
       self.assertFalse(c1 != c2)

       self.assertFalse(c1 == 42)
       self.assertTrue(c1 != 42)


if __name__ == "__main__":
    main()
