from PyObjCTools.TestSupport import *

import AVFoundation

try:
    unicode
except NameError:
    unicode = str


class TestAVMetadataObject (TestCase):
    @min_os_level('10.7')
    def testConstants(self):
        self.assertIsInstance(AVFoundation.AVMetadataObjectTypeFace, unicode)

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(AVFoundation.AVMetadataFaceObject.hasRollAngle)
        self.assertResultIsBOOL(AVFoundation.AVMetadataFaceObject.hasYawAngle)


if __name__ == "__main__":
    main()
