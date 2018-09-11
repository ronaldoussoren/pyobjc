from PyObjCTools.TestSupport import *

import CoreMedia

class TestCMMemoryPool (TestCase):
    def test_types(self):
        self.assertIsCFType(CoreMedia.CMMemoryPoolRef)

    def test_functions(self):
        CoreMedia.kCMMemoryPoolOption_AgeOutPeriod

        self.assertResultIsCFRetained(CoreMedia.CMMemoryPoolCreate)

        CoreMedia.CMMemoryPoolGetAllocator
        CoreMedia.CMMemoryPoolFlush
        CoreMedia.CMMemoryPoolInvalidate


if __name__ == "__main__":
    main()
