from PyObjCTools.TestSupport import *

import AVFoundation


class TestAVMetadataObject (TestCase):
    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(AVFoundation.AVMetadataFaceObject.hasRollAngle)
        self.assertResultIsBOOL(AVFoundation.AVMetadataFaceObject.hasYawAngle)

    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypeFace, unicode)


if __name__ == "__main__":
    main()
