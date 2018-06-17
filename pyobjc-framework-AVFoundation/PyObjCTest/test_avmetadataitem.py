from PyObjCTools.TestSupport import *

import AVFoundation


class TestAVMetadataItem (TestCase):
    @min_os_level('10.7')
    def testMethods(self):
        self.assertArgIsOut(AVFoundation.AVMetadataItem.statusOfValueForKey_error_, 1)

        self.assertArgIsBlock(AVFoundation.AVMetadataItem.loadValuesAsynchronouslyForKeys_completionHandler_, 1, b'v')


    @min_os_level('10.11')
    def testMethods(self):
        self.assertArgIsBlock(AVFoundation.AVMetadataItem.metadataItemWithPropertiesOfMetadataItem_valueLoadingHandler_, 1, b'v@')

if __name__ == "__main__":
    main()
