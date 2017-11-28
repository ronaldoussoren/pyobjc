from PyObjCTools.TestSupport import *

import Security

class TestSecTransformReadTransform (TestCase):

    @min_os_level('10.7')
    def test_functions10_7(self):
        self.assertResultHasType(Security.SecTransformCreateReadTransformWithReadStream, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecTransformCreateReadTransformWithReadStream)
        self.assertArgHasType(Security.SecTransformCreateReadTransformWithReadStream, 0, objc._C_ID)


if __name__ == "__main__":
    main()
