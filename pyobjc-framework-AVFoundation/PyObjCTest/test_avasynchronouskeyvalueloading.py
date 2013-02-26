from PyObjCTools.TestSupport import *

import AVFoundation

class AVAsynchronousKeyValueLoadingHelper (AVFoundation.NSObject):
    def statusOfValueForKey_error_(self, a, b):
        pass

    def loadValuesAsynchronouslyForKeys_completionHandler_(self, a, b):
        pass

class TestAVAsynchronousKeyValueLoading (TestCase):

    def test_constants(self):
        self.assertEqual(AVKeyValueStatusUnknown, 0)
        self.assertEqual(AVKeyValueStatusLoading, 1)
        self.assertEqual(AVKeyValueStatusLoaded, 2)
        self.assertEqual(AVKeyValueStatusFailed, 3)
        self.assertEqual(AVKeyValueStatusCancelled, 4)

    def test_prtoocols(self):
        self.assertArgIsOut(AVAsynchronousKeyValueLoadingHelper.statusOfValueForKey_error_, 1)
        self.assertArgIsOut(AVAsynchronousKeyValueLoadingHelper.loadValuesAsynchronouslyForKeys_completionHandler_, 1, 'v')

if __name__ == "__main__":
    main()
