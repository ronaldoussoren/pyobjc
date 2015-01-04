from PyObjCTools.TestSupport import *

import AVFoundation
import objc

try:
    unicode
except NameError:
    unicode = str

class TestAVAssetResourceLoaderHelper (AVFoundation.NSObject):
    def resourceLoader_shouldWaitForLoadingOfRequestedResource_(self, rl, r): return 1
    def resourceLoader_shouldWaitForRenewalOfRequestedResource_(self, rl, r): return 1
    def resourceLoader_shouldWaitForResponseToAuthenticationChallenge_(self, rl, r): return 1

class TestAVAssetResourceLoader (TestCase):
    @min_os_level('10.9')
    def testProtocols(self):
        objc.protocolNamed('AVAssetResourceLoaderDelegate')

        self.assertResultHasType(TestAVAssetResourceLoaderHelper.resourceLoader_shouldWaitForLoadingOfRequestedResource_)

    @min_os_level('10.10')
    def testProtocols10_10(self):
        self.assertResultHasType(TestAVAssetResourceLoaderHelper.resourceLoader_shouldWaitForRenewalOfRequestedResource_)
        self.assertResultHasType(TestAVAssetResourceLoaderHelper.resourceLoader_shouldWaitForResponseToAuthenticationChallenge_)

    @min_os_level('10.9')
    def testMethods10_8(self):
        self.assertResultIsBOOL(AVFoundation.AVAssetResourceLoadingRequest.isFinished)
        self.assertArgIsBOOL(AVFoundation.AVAssetResourceLoadingRequest.setFinished_, 0)

        self.assertResultIsBOOL(AVFoundation.AVAssetResourceLoadingRequest.isCancelled)
        self.assertArgIsBOOL(AVFoundation.AVAssetResourceLoadingRequest.setCancelled_, 0)

        self.assertResultIsBOOL(AVFoundation.AVAssetResourceLoadingContentInformationRequest.byteRangeAccessSupported)
        self.assertArgIsBOOL(AVFoundation.AVAssetResourceLoadingContentInformationRequest.setByteRangeAccessSupported_, 0)

        self.assertArgIsOut(AVFoundation.AVAssetResourceLoadingRequest.streamingContentKeyRequestDataForApp_contentIdentifier_options_error_, 3)

if __name__ == "__main__":
    main()
