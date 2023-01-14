from CoreFoundation import CFSwapInt16HostToLittle, CFSwapInt16LittleToHost

IOBluetooth = None


def BluetoothCoDMinorPeripheral1(minorClass):
    return minorClass & 0x30


def BluetoothCoDMinorPeripheral2(minorClass):
    return minorClass & 0x0F


def BluetoothGetDeviceClassMajor(inCOD):
    return ((inCOD) & 0x00001F00) >> 8


def BluetoothGetDeviceClassMinor(inCOD):
    return ((inCOD) & 0x000000FC) >> 2


def BluetoothGetSecondsFromSlots(inSlots):
    return inSlots * 0.000625


def BluetoothGetServiceClassMajor(inCOD):
    return ((inCOD) & 0x00FFE000) >> 13


def BluetoothGetSlotsFromSeconds(inSeconds):
    return inSeconds / 0.000625


def BluetoothHCIExtractCommandOpCodeCommand(OPCODE):
    return (OPCODE) & 0x03FF


def BluetoothHCIExtractCommandOpCodeGroup(OPCODE):
    return ((OPCODE) >> 10) & 0x003F


def BluetoothHCIMakeCommandOpCode(GROUP, CMD):
    return (((GROUP) & 0x003F) << 10) | ((CMD) & 0x03FF)


def BluetoothHCIMakeCommandOpCodeEndianSwap(GROUP, CMD):
    return CFSwapInt16HostToLittle(BluetoothHCIMakeCommandOpCode(GROUP, CMD))


def BluetoothHCIMakeCommandOpCodeHostOrder(GROUP, CMD):
    return CFSwapInt16LittleToHost((((GROUP) & 0x003F) << 10) | ((CMD) & 0x03FF))


def BluetoothMakeClassOfDevice(
    inServiceClassMajor, inDeviceClassMajor, inDeviceClassMinor
):
    return (
        (((inServiceClassMajor) << 13) & 0x00FFE000)
        | (((inDeviceClassMajor) << 8) & 0x00001F00)
        | (((inDeviceClassMinor) << 2) & 0x000000FC)
    )


def GET_HEADER_ID_IS_1_BYTE_QUANTITY(HEADER_ID):
    return (HEADER_ID & 0xC0) == 0x80


def GET_HEADER_ID_IS_4_BYTE_QUANTITY(HEADER_ID):
    return (HEADER_ID & 0xC0) == 0xC0


def GET_HEADER_ID_IS_BYTE_SEQUENCE(HEADER_ID):
    return (HEADER_ID & 0xC0) == 0x40


def GET_HEADER_ID_IS_NULL_TERMINATED_UNICODE_TEXT(HEADER_ID):
    return (HEADER_ID & 0xC0) == 0x00


def IS_RESPONSE_CODE_FINAL_BIT_SET(RESPONSE_CODE):
    return RESPONSE_CODE >> 7


def SET_HEADER_ID_IS_1_BYTE_QUANTITY(HEADER_ID):
    return (HEADER_ID & 0x3F) | 0x80


def SET_HEADER_ID_IS_4_BYTE_QUANTITY(HEADER_ID):
    return (HEADER_ID & 0x3F) | 0xC0


def SET_HEADER_ID_IS_BYTE_SEQUENCE(HEADER_ID):
    return (HEADER_ID & 0x3F) | 0x40


def SET_HEADER_ID_IS_NULL_TERMINATED_UNICODE_TEXT(HEADER_ID):
    return HEADER_ID & 0x3F


def STRIP_RESPONSE_CODE_FINAL_BIT(RESPONSE_CODE):
    return RESPONSE_CODE & 0x7F


def IS_REQUEST_PDU(_pduID):
    global IOBluetooth
    if IOBluetooth is None:
        import IOBluetooth
    return (
        (_pduID == IOBluetooth.kBluetoothSDPPDUIDServiceSearchRequest)
        or (_pduID == IOBluetooth.kBluetoothSDPPDUIDServiceAttributeRequest)
        or (_pduID == IOBluetooth.kBluetoothSDPPDUIDServiceSearchAttributeRequest)
    )


def IS_RESPONSE_PDU(_pduID):
    global IOBluetooth
    if IOBluetooth is None:
        import IOBluetooth
    return (
        (_pduID == IOBluetooth.kBluetoothSDPPDUIDErrorResponse)
        or (_pduID == IOBluetooth.kBluetoothSDPPDUIDServiceSearchResponse)
        or (_pduID == IOBluetooth.kBluetoothSDPPDUIDServiceAttributeResponse)
        or (_pduID == IOBluetooth.kBluetoothSDPPDUIDServiceSearchAttributeResponse)
    )


def RFCOMM_CHANNEL_ID_IS_VALID(CHANNEL):
    return (CHANNEL >= 1) and (CHANNEL <= 30)
