from PyObjCTools.TestSupport import TestCase, fourcc

import IOBluetooth


class TestOBEXSession(TestCase):
    def test_constants(self):
        self.assertIsEnumType(IOBluetooth.OBEXTransportEventType)
        self.assertEqual(
            IOBluetooth.kOBEXTransportEventTypeDataReceived, fourcc(b"DatA")
        )
        self.assertEqual(IOBluetooth.kOBEXTransportEventTypeStatus, fourcc(b"StaT"))

    def test_methods(self):
        self.assertArgIsIn(
            IOBluetooth.OBEXSession.OBEXConnect_maxPacketLength_optionalHeaders_optionalHeadersLength_eventSelector_selectorTarget_refCon_,
            2,
        )
        self.assertArgSizeInArg(
            IOBluetooth.OBEXSession.OBEXConnect_maxPacketLength_optionalHeaders_optionalHeadersLength_eventSelector_selectorTarget_refCon_,
            2,
            3,
        )

        self.assertArgIsIn(
            IOBluetooth.OBEXSession.OBEXDisconnect_optionalHeadersLength_eventSelector_selectorTarget_refCon_,
            0,
        )
        self.assertArgSizeInArg(
            IOBluetooth.OBEXSession.OBEXDisconnect_optionalHeadersLength_eventSelector_selectorTarget_refCon_,
            0,
            1,
        )

        self.assertArgIsIn(
            IOBluetooth.OBEXSession.OBEXPut_headersData_headersDataLength_bodyData_bodyDataLength_eventSelector_selectorTarget_refCon_,
            1,
        )
        self.assertArgSizeInArg(
            IOBluetooth.OBEXSession.OBEXPut_headersData_headersDataLength_bodyData_bodyDataLength_eventSelector_selectorTarget_refCon_,
            1,
            2,
        )
        self.assertArgIsIn(
            IOBluetooth.OBEXSession.OBEXPut_headersData_headersDataLength_bodyData_bodyDataLength_eventSelector_selectorTarget_refCon_,
            3,
        )
        self.assertArgSizeInArg(
            IOBluetooth.OBEXSession.OBEXPut_headersData_headersDataLength_bodyData_bodyDataLength_eventSelector_selectorTarget_refCon_,
            3,
            4,
        )

        self.assertArgIsIn(
            IOBluetooth.OBEXSession.OBEXGet_headers_headersLength_eventSelector_selectorTarget_refCon_,
            1,
        )
        self.assertArgSizeInArg(
            IOBluetooth.OBEXSession.OBEXGet_headers_headersLength_eventSelector_selectorTarget_refCon_,
            1,
            2,
        )

        self.assertArgIsIn(
            IOBluetooth.OBEXSession.OBEXAbort_optionalHeadersLength_eventSelector_selectorTarget_refCon_,
            0,
        )
        self.assertArgSizeInArg(
            IOBluetooth.OBEXSession.OBEXAbort_optionalHeadersLength_eventSelector_selectorTarget_refCon_,
            0,
            1,
        )

        self.assertArgIsIn(
            IOBluetooth.OBEXSession.OBEXSetPath_constants_optionalHeaders_optionalHeadersLength_eventSelector_selectorTarget_refCon_,
            2,
        )
        self.assertArgSizeInArg(
            IOBluetooth.OBEXSession.OBEXSetPath_constants_optionalHeaders_optionalHeadersLength_eventSelector_selectorTarget_refCon_,
            2,
            3,
        )

        self.assertArgIsIn(
            IOBluetooth.OBEXSession.OBEXConnectResponse_flags_maxPacketLength_optionalHeaders_optionalHeadersLength_eventSelector_selectorTarget_refCon_,
            3,
        )
        self.assertArgSizeInArg(
            IOBluetooth.OBEXSession.OBEXConnectResponse_flags_maxPacketLength_optionalHeaders_optionalHeadersLength_eventSelector_selectorTarget_refCon_,
            3,
            4,
        )

        self.assertArgIsIn(
            IOBluetooth.OBEXSession.OBEXDisconnectResponse_optionalHeaders_optionalHeadersLength_eventSelector_selectorTarget_refCon_,
            1,
        )
        self.assertArgSizeInArg(
            IOBluetooth.OBEXSession.OBEXDisconnectResponse_optionalHeaders_optionalHeadersLength_eventSelector_selectorTarget_refCon_,
            1,
            2,
        )

        self.assertArgIsIn(
            IOBluetooth.OBEXSession.OBEXPutResponse_optionalHeaders_optionalHeadersLength_eventSelector_selectorTarget_refCon_,
            1,
        )
        self.assertArgSizeInArg(
            IOBluetooth.OBEXSession.OBEXPutResponse_optionalHeaders_optionalHeadersLength_eventSelector_selectorTarget_refCon_,
            1,
            2,
        )

        self.assertArgIsIn(
            IOBluetooth.OBEXSession.OBEXGetResponse_optionalHeaders_optionalHeadersLength_eventSelector_selectorTarget_refCon_,
            1,
        )
        self.assertArgSizeInArg(
            IOBluetooth.OBEXSession.OBEXGetResponse_optionalHeaders_optionalHeadersLength_eventSelector_selectorTarget_refCon_,
            1,
            2,
        )

        self.assertArgIsIn(
            IOBluetooth.OBEXSession.OBEXAbortResponse_optionalHeaders_optionalHeadersLength_eventSelector_selectorTarget_refCon_,
            1,
        )
        self.assertArgSizeInArg(
            IOBluetooth.OBEXSession.OBEXAbortResponse_optionalHeaders_optionalHeadersLength_eventSelector_selectorTarget_refCon_,
            1,
            2,
        )

        self.assertArgIsIn(
            IOBluetooth.OBEXSession.OBEXSetPathResponse_optionalHeaders_optionalHeadersLength_eventSelector_selectorTarget_refCon_,
            1,
        )
        self.assertArgSizeInArg(
            IOBluetooth.OBEXSession.OBEXSetPathResponse_optionalHeaders_optionalHeadersLength_eventSelector_selectorTarget_refCon_,
            1,
            2,
        )

        self.assertResultIsBOOL(IOBluetooth.OBEXSession.hasOpenOBEXConnection)

        self.assertArgIsIn(IOBluetooth.OBEXSession.sendDataToTransport_dataLength_, 0)
        self.assertArgSizeInArg(
            IOBluetooth.OBEXSession.sendDataToTransport_dataLength_, 0, 1
        )

        self.assertResultIsBOOL(IOBluetooth.OBEXSession.hasOpenTransportConnection)
