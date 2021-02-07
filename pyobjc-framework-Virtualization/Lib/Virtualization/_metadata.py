# This file is generated by objective.metadata
#
# Last update: Wed Aug  5 14:49:53 2020
#
# flake8: noqa

import objc, sys

if sys.maxsize > 2 ** 32:

    def sel32or64(a, b):
        return b


else:

    def sel32or64(a, b):
        return a


misc = {}
constants = """$VZErrorDomain$"""
enums = """$VZErrorInternal@1$VZErrorInvalidDiskImage@5$VZErrorInvalidVirtualMachineConfiguration@2$VZErrorInvalidVirtualMachineState@3$VZErrorInvalidVirtualMachineStateTransition@4$VZVirtualMachineStateError@3$VZVirtualMachineStatePaused@2$VZVirtualMachineStatePausing@5$VZVirtualMachineStateResuming@6$VZVirtualMachineStateRunning@1$VZVirtualMachineStateStarting@4$VZVirtualMachineStateStopped@0$"""
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"NSObject",
        b"guestDidStopVirtualMachine:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"listener:shouldAcceptNewConnection:fromSocketDevice:",
        {
            "required": False,
            "retval": {"type": b"Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"virtualMachine:didStopWithError:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"VZDiskImageStorageDeviceAttachment",
        b"initWithURL:readOnly:error:",
        {"arguments": {3: {"type": b"Z"}, 4: {"type_modifier": b"o"}}},
    )
    r(b"VZDiskImageStorageDeviceAttachment", b"isReadOnly", {"retval": {"type": "Z"}})
    r(b"VZFileSerialPortAttachment", b"append", {"retval": {"type": b"Z"}})
    r(
        b"VZFileSerialPortAttachment",
        b"initWithURL:append:error:",
        {"arguments": {3: {"type": b"Z"}, 4: {"type_modifier": b"o"}}},
    )
    r(b"VZMACAddress", b"isBroadcastAddress", {"retval": {"type": b"Z"}})
    r(b"VZMACAddress", b"isLocallyAdministeredAddress", {"retval": {"type": b"Z"}})
    r(b"VZMACAddress", b"isMulticastAddress", {"retval": {"type": b"Z"}})
    r(b"VZMACAddress", b"isUnicastAddress", {"retval": {"type": b"Z"}})
    r(b"VZMACAddress", b"isUniversallyAdministeredAddress", {"retval": {"type": b"Z"}})
    r(
        b"VZVirtioSocketDevice",
        b"connectToPort:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(b"VZVirtualMachine", b"canPause", {"retval": {"type": b"Z"}})
    r(b"VZVirtualMachine", b"canRequestStop", {"retval": {"type": b"Z"}})
    r(b"VZVirtualMachine", b"canResume", {"retval": {"type": b"Z"}})
    r(b"VZVirtualMachine", b"canStart", {"retval": {"type": b"Z"}})
    r(b"VZVirtualMachine", b"isSupported", {"retval": {"type": b"Z"}})
    r(
        b"VZVirtualMachine",
        b"pauseWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"VZVirtualMachine",
        b"requestStopWithError:",
        {"retval": {"type": b"Z"}, "arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"VZVirtualMachine",
        b"resumeWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"VZVirtualMachine",
        b"startWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"VZVirtualMachineConfiguration",
        b"validateWithError:",
        {"retval": {"type": b"Z"}, "arguments": {2: {"type_modifier": b"o"}}},
    )
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
