
from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVPortraitMatte (TestCase):
    @min_os_level('10.14')
    def testMethods(self):
        self.assertArgIsOut(AVFoundation.AVPortraitEffectsMatte.portraitEffectsMatteFromDictionaryRepresentation_error_, 1)
        self.assertArgIsOut(AVFoundation.AVPortraitEffectsMatte.portraitEffectsMatteByReplacingPortraitEffectsMatteWithPixelBuffer_error_, 1)
        self.assertArgIsOut(AVFoundation.AVPortraitEffectsMatte.dictionaryRepresentationForAuxiliaryDataType_, 0)





if __name__ == "__main__":
    main()
