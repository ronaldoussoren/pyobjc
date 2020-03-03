import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAssetCache(TestCase):
    @min_os_level("10.12")
    def testClasses(self):
        AVFoundation.AVAssetCache

    @min_os_level("10.12")
    def testMethods(self):
        self.assertResultIsBOOL(AVFoundation.AVAssetCache.isPlayableOffline)
