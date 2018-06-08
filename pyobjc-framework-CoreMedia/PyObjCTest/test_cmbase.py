from PyObjCTools.TestSupport import *

import CoreMedia

class TestCMBase (TestCase):
    def test_constants(self):
        self.assertEqual(CoreMedia.kCMPersistentTrackID_Invalid, 0)

if __name__ == "__main__":
    main()
