from PyObjCTools.TestSupport import *

import CoreServices

class TestTextEncodingPlugin (TestCase):
    def assert_not_wrapped(self, name):
        self.assertTrue(not hasattr(CoreServices, name), "%r exposed in bindings"%(name,))

    def test_not_wrapped(self):
        self.assert_not_wrapped('kTECAvailableEncodingsResType')
        self.assert_not_wrapped('kTECAvailableSniffersResType')
        self.assert_not_wrapped('kTECSubTextEncodingsResType')
        self.assert_not_wrapped('kTECConversionInfoResType')
        self.assert_not_wrapped('kTECMailEncodingsResType')
        self.assert_not_wrapped('kTECWebEncodingsResType')
        self.assert_not_wrapped('kTECInternetNamesResType')
        self.assert_not_wrapped('kTECPluginType')
        self.assert_not_wrapped('kTECPluginCreator')
        self.assert_not_wrapped('kTECPluginOneToOne')
        self.assert_not_wrapped('kTECPluginOneToMany')
        self.assert_not_wrapped('kTECPluginManyToOne')
        self.assert_not_wrapped('kTECPluginSniffObj')
        self.assert_not_wrapped('verUnspecified')
        self.assert_not_wrapped('kTECResourceID')
        self.assert_not_wrapped('TextEncodingRec')
        self.assert_not_wrapped('TECEncodingsListRec')
        self.assert_not_wrapped('TECSubTextEncodingRec')
        self.assert_not_wrapped('TECSubTextEncodingsRec')
        self.assert_not_wrapped('TECEncodingPairRec')
        self.assert_not_wrapped('TECEncodingPairs')
        self.assert_not_wrapped('TECEncodingPairsRec')
        self.assert_not_wrapped('TECLocaleListToEncodingListRec')
        self.assert_not_wrapped('TECLocaleToEncodingsListRec')
        self.assert_not_wrapped('TECInternetNameRec')
        self.assert_not_wrapped('TECInternetNamesRec')
        self.assert_not_wrapped('TECBufferContextRec')
        self.assert_not_wrapped('TECPluginStateRec')
        self.assert_not_wrapped('TECConverterContextRec')
        self.assert_not_wrapped('TECSnifferContextRec')
        self.assert_not_wrapped('kTECPluginDispatchTableVersion1')
        self.assert_not_wrapped('kTECPluginDispatchTableVersion1_1')
        self.assert_not_wrapped('kTECPluginDispatchTableVersion1_2')
        self.assert_not_wrapped('kTECPluginDispatchTableCurrentVersion')
        self.assert_not_wrapped('TECPluginDispatchTable;')

if __name__ == "__main__":
    main()
