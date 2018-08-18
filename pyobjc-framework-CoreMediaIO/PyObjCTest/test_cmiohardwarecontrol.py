from PyObjCTools.TestSupport import *

import CoreMediaIO


class TestCMIOHardwareControl (TestCase):
    def testConstants(self):
        self.assertEqual(CoreMediaIO.kCMIOControlClassID, fourcc(b'actl'))
        self.assertEqual(CoreMediaIO.kCMIOBooleanControlClassID, fourcc(b'togl'))
        self.assertEqual(CoreMediaIO.kCMIOSelectorControlClassID, fourcc(b'slct'))
        self.assertEqual(CoreMediaIO.kCMIOFeatureControlClassID, fourcc(b'ftct'))

        self.assertEqual(CoreMediaIO.kCMIOJackControlClassID, fourcc(b'jack'))
        self.assertEqual(CoreMediaIO.kCMIODirectionControlClassID, fourcc(b'dire'))

        self.assertEqual(CoreMediaIO.kCMIODataSourceControlClassID, fourcc(b'dsrc'))
        self.assertEqual(CoreMediaIO.kCMIODataDestinationControlClassID, fourcc(b'dest'))

        self.assertEqual(CoreMediaIO.kCMIOBlackLevelControlClassID, fourcc(b'bklv'))
        self.assertEqual(CoreMediaIO.kCMIOWhiteLevelControlClassID, fourcc(b'whlv'))
        self.assertEqual(CoreMediaIO.kCMIOHueControlClassID, fourcc(b'hue '))
        self.assertEqual(CoreMediaIO.kCMIOSaturationControlClassID, fourcc(b'satu'))
        self.assertEqual(CoreMediaIO.kCMIOContrastControlClassID, fourcc(b'ctst'))
        self.assertEqual(CoreMediaIO.kCMIOSharpnessControlClassID, fourcc(b'shrp'))
        self.assertEqual(CoreMediaIO.kCMIOBrightnessControlClassID, fourcc(b'brit'))
        self.assertEqual(CoreMediaIO.kCMIOGainControlClassID, fourcc(b'gain'))
        self.assertEqual(CoreMediaIO.kCMIOIrisControlClassID, fourcc(b'iris'))
        self.assertEqual(CoreMediaIO.kCMIOShutterControlClassID, fourcc(b'shtr'))
        self.assertEqual(CoreMediaIO.kCMIOExposureControlClassID, fourcc(b'xpsr'))
        self.assertEqual(CoreMediaIO.kCMIOWhiteBalanceUControlClassID, fourcc(b'whbu'))
        self.assertEqual(CoreMediaIO.kCMIOWhiteBalanceVControlClassID, fourcc(b'whbv'))
        self.assertEqual(CoreMediaIO.kCMIOWhiteBalanceControlClassID, fourcc(b'whbl'))
        self.assertEqual(CoreMediaIO.kCMIOGammaControlClassID, fourcc(b'gmma'))
        self.assertEqual(CoreMediaIO.kCMIOTemperatureControlClassID, fourcc(b'temp'))
        self.assertEqual(CoreMediaIO.kCMIOZoomControlClassID, fourcc(b'zoom'))
        self.assertEqual(CoreMediaIO.kCMIOFocusControlClassID, fourcc(b'fcus'))
        self.assertEqual(CoreMediaIO.kCMIOPanControlClassID, fourcc(b'pan '))
        self.assertEqual(CoreMediaIO.kCMIOTiltControlClassID, fourcc(b'tilt'))
        self.assertEqual(CoreMediaIO.kCMIOOpticalFilterClassID, fourcc(b'opft'))
        self.assertEqual(CoreMediaIO.kCMIOBacklightCompensationControlClassID, fourcc(b'bklt'))
        self.assertEqual(CoreMediaIO.kCMIOPowerLineFrequencyControlClassID, fourcc(b'pwfq'))
        self.assertEqual(CoreMediaIO.kCMIONoiseReductionControlClassID, fourcc(b's2nr'))
        self.assertEqual(CoreMediaIO.kCMIOPanTiltAbsoluteControlClassID, fourcc(b'ptab'))
        self.assertEqual(CoreMediaIO.kCMIOPanTiltRelativeControlClassID, fourcc(b'ptrl'))
        self.assertEqual(CoreMediaIO.kCMIOZoomRelativeControlClassID, fourcc(b'zomr'))

        self.assertEqual(CoreMediaIO.kCMIOControlPropertyScope, fourcc(b'cscp'))
        self.assertEqual(CoreMediaIO.kCMIOControlPropertyElement, fourcc(b'celm'))
        self.assertEqual(CoreMediaIO.kCMIOControlPropertyVariant, fourcc(b'cvar'))

        self.assertEqual(CoreMediaIO.kCMIOBooleanControlPropertyValue, fourcc(b'bcvl'))

        self.assertEqual(CoreMediaIO.kCMIOSelectorControlPropertyCurrentItem, fourcc(b'scci'))
        self.assertEqual(CoreMediaIO.kCMIOSelectorControlPropertyAvailableItems, fourcc(b'scai'))
        self.assertEqual(CoreMediaIO.kCMIOSelectorControlPropertyItemName, fourcc(b'scin'))

        self.assertEqual(CoreMediaIO.kCMIOFeatureControlPropertyOnOff, fourcc(b'fcoo'))
        self.assertEqual(CoreMediaIO.kCMIOFeatureControlPropertyAutomaticManual, fourcc(b'fcam'))
        self.assertEqual(CoreMediaIO.kCMIOFeatureControlPropertyAbsoluteNative, fourcc(b'fcna'))
        self.assertEqual(CoreMediaIO.kCMIOFeatureControlPropertyTune, fourcc(b'fctn'))
        self.assertEqual(CoreMediaIO.kCMIOFeatureControlPropertyNativeValue, fourcc(b'fcnv'))
        self.assertEqual(CoreMediaIO.kCMIOFeatureControlPropertyAbsoluteValue, fourcc(b'fcav'))
        self.assertEqual(CoreMediaIO.kCMIOFeatureControlPropertyNativeRange, fourcc(b'fcnr'))
        self.assertEqual(CoreMediaIO.kCMIOFeatureControlPropertyAbsoluteRange, fourcc(b'fcar'))
        self.assertEqual(CoreMediaIO.kCMIOFeatureControlPropertyConvertNativeToAbsolute, fourcc(b'fn2a'))
        self.assertEqual(CoreMediaIO.kCMIOFeatureControlPropertyConvertAbsoluteToNative, fourcc(b'fa2n'))
        self.assertEqual(CoreMediaIO.kCMIOFeatureControlPropertyAbsoluteUnitName, fourcc(b'fcun'))

        self.assertEqual(CoreMediaIO.kCMIOExposureControlPropertyRegionOfInterest, fourcc(b'eroi'))
        self.assertEqual(CoreMediaIO.kCMIOExposureControlPropertyLockThreshold, fourcc(b'elck'))
        self.assertEqual(CoreMediaIO.kCMIOExposureControlPropertyUnlockThreshold, fourcc(b'eulk'))
        self.assertEqual(CoreMediaIO.kCMIOExposureControlPropertyTarget, fourcc(b'etgt'))
        self.assertEqual(CoreMediaIO.kCMIOExposureControlPropertyConvergenceSpeed, fourcc(b'ecsp'))
        self.assertEqual(CoreMediaIO.kCMIOExposureControlPropertyStability, fourcc(b'esty'))
        self.assertEqual(CoreMediaIO.kCMIOExposureControlPropertyStable, fourcc(b'estb'))
        self.assertEqual(CoreMediaIO.kCMIOExposureControlPropertyIntegrationTime, fourcc(b'eint'))
        self.assertEqual(CoreMediaIO.kCMIOExposureControlPropertyMaximumGain, fourcc(b'emax'))


if __name__== "__main__":
        main()
