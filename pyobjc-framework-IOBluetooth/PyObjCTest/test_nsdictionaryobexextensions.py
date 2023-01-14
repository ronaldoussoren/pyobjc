from PyObjCTools.TestSupport import TestCase

import IOBluetooth


class TestNSDictionaryOBEXExtensions(TestCase):
    def test_methods(self):
        self.assertArgIsIn(
            IOBluetooth.NSMutableDictionary.dictionaryWithOBEXHeadersData_headersDataSize_,
            0,
        )
        self.assertArgSizeInArg(
            IOBluetooth.NSMutableDictionary.dictionaryWithOBEXHeadersData_headersDataSize_,
            0,
            1,
        )

        self.assertArgIsIn(IOBluetooth.NSMutableDictionary.addTargetHeader_length_, 0)
        self.assertArgSizeInArg(
            IOBluetooth.NSMutableDictionary.addTargetHeader_length_, 0, 1
        )

        self.assertArgIsIn(IOBluetooth.NSMutableDictionary.addHTTPHeader_length_, 0)
        self.assertArgSizeInArg(
            IOBluetooth.NSMutableDictionary.addHTTPHeader_length_, 0, 1
        )

        self.assertArgIsIn(
            IOBluetooth.NSMutableDictionary.addBodyHeader_length_endOfBody_, 0
        )
        self.assertArgSizeInArg(
            IOBluetooth.NSMutableDictionary.addBodyHeader_length_endOfBody_, 0, 1
        )
        self.assertArgIsBOOL(
            IOBluetooth.NSMutableDictionary.addBodyHeader_length_endOfBody_, 2
        )

        self.assertArgIsIn(IOBluetooth.NSMutableDictionary.addWhoHeader_length_, 0)
        self.assertArgSizeInArg(
            IOBluetooth.NSMutableDictionary.addWhoHeader_length_, 0, 1
        )

        self.assertArgIsIn(
            IOBluetooth.NSMutableDictionary.addConnectionIDHeader_length_, 0
        )
        self.assertArgSizeInArg(
            IOBluetooth.NSMutableDictionary.addConnectionIDHeader_length_, 0, 1
        )

        self.assertArgIsIn(
            IOBluetooth.NSMutableDictionary.addApplicationParameterHeader_length_, 0
        )
        self.assertArgSizeInArg(
            IOBluetooth.NSMutableDictionary.addApplicationParameterHeader_length_, 0, 1
        )

        self.assertArgIsIn(
            IOBluetooth.NSMutableDictionary.addByteSequenceHeader_length_, 0
        )
        self.assertArgSizeInArg(
            IOBluetooth.NSMutableDictionary.addByteSequenceHeader_length_, 0, 1
        )

        self.assertArgIsIn(
            IOBluetooth.NSMutableDictionary.addObjectClassHeader_length_, 0
        )
        self.assertArgSizeInArg(
            IOBluetooth.NSMutableDictionary.addObjectClassHeader_length_, 0, 1
        )

        self.assertArgIsIn(
            IOBluetooth.NSMutableDictionary.addAuthorizationChallengeHeader_length_, 0
        )
        self.assertArgSizeInArg(
            IOBluetooth.NSMutableDictionary.addAuthorizationChallengeHeader_length_,
            0,
            1,
        )

        self.assertArgIsIn(
            IOBluetooth.NSMutableDictionary.addAuthorizationResponseHeader_length_, 0
        )
        self.assertArgSizeInArg(
            IOBluetooth.NSMutableDictionary.addAuthorizationResponseHeader_length_, 0, 1
        )

        self.assertArgIsIn(IOBluetooth.NSMutableDictionary.addTimeISOHeader_length_, 0)
        self.assertArgSizeInArg(
            IOBluetooth.NSMutableDictionary.addTimeISOHeader_length_, 0, 1
        )

        self.assertArgIsIn(
            IOBluetooth.NSMutableDictionary.addUserDefinedHeader_length_, 0
        )
        self.assertArgSizeInArg(
            IOBluetooth.NSMutableDictionary.addUserDefinedHeader_length_, 0, 1
        )

        self.assertArgIsIn(
            IOBluetooth.NSMutableDictionary.addImageDescriptorHeader_length_, 0
        )
        self.assertArgSizeInArg(
            IOBluetooth.NSMutableDictionary.addImageDescriptorHeader_length_, 0, 1
        )

        self.assertArgIsIn(
            IOBluetooth.NSMutableDictionary.withOBEXHeadersData_headersDataSize_, 0
        )
        self.assertArgSizeInArg(
            IOBluetooth.NSMutableDictionary.withOBEXHeadersData_headersDataSize_, 0, 1
        )
