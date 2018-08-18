from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import PhotosUI

    class TestPHProjectTypeDescriptionDataSource (TestCase):
        @min_sdk_level('10.14')
        def testProtocols(self):
            objc.protocolNamed('PHProjectTypeDescriptionDataSource')
            objc.protocolNamed('PHProjectTypeDescriptionInvalidator')


if __name__ == "__main__":
    main()
