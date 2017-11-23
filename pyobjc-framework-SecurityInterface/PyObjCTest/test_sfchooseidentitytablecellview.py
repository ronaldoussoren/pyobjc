from PyObjCTools.TestSupport import *

import SecurityInterface

class TestSFChooseIdentityTableCellView (TestCase):
    @min_os_level('10.13')
    def test_classes(self):
        SecurityInterface.SFChooseIdentityTableCellView

if __name__ == "__main__":
    main()
