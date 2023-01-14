static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
    p = PyObjC_IdToPython(@protocol(IOBluetoothDeviceAsyncCallbacks));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(IOBluetoothDeviceInquiryDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(IOBluetoothDevicePairDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(IOBluetoothHandsFreeAudioGatewayDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(IOBluetoothHandsFreeDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(IOBluetoothHandsFreeDeviceDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(IOBluetoothL2CAPChannelDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(IOBluetoothRFCOMMChannelDelegate));
    Py_XDECREF(p);
}
