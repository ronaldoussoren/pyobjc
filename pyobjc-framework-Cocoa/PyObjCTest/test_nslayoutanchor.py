from PyObjCTools.TestSupport import *
from AppKit import *


class TestNSLayoutAnchor(TestCase):
    @min_os_level("10.12")
    def test_methods10_12(self):
        self.assertResultIsBOOL(NSLayoutAnchor.hasAmbiguousLayout)


if __name__ == "__main__":
    main()
