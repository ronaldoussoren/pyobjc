# This file is generated by objective.metadata
#
# Last update: Thu Mar 20 20:29:04 2025
#
# flake8: noqa

import objc, sys
from typing import NewType

if sys.maxsize > 2**32:

    def sel32or64(a, b):
        return b

else:

    def sel32or64(a, b):
        return a


if objc.arch == "arm64":

    def selAorI(a, b):
        return a

else:

    def selAorI(a, b):
        return b


misc = {}
constants = """$BADownloaderPriorityDefault@q$BADownloaderPriorityMax@q$BADownloaderPriorityMin@q$BAErrorDomain$"""
enums = """$BAContentRequestInstall@1$BAContentRequestPeriodic@3$BAContentRequestUpdate@2$BADownloadStateCreated@0$BADownloadStateDownloading@2$BADownloadStateFailed@-1$BADownloadStateFinished@3$BADownloadStateWaiting@1$BAErrorCodeCallFromExtensionNotAllowed@50$BAErrorCodeCallFromInactiveProcessNotAllowed@51$BAErrorCodeCallerConnectionInvalid@56$BAErrorCodeCallerConnectionNotAccepted@55$BAErrorCodeDownloadAlreadyFailed@103$BAErrorCodeDownloadAlreadyScheduled@100$BAErrorCodeDownloadBackgroundActivityProhibited@111$BAErrorCodeDownloadDoesNotExist@113$BAErrorCodeDownloadEssentialDownloadNotPermitted@109$BAErrorCodeDownloadFailedToStart@102$BAErrorCodeDownloadInvalid@0$BAErrorCodeDownloadNotScheduled@101$BAErrorCodeDownloadWouldExceedAllowance@112$BAErrorCodeSessionDownloadAllowanceExceeded@204$BAErrorCodeSessionDownloadDisallowedByAllowance@203$BAErrorCodeSessionDownloadDisallowedByDomain@202$BAErrorCodeSessionDownloadNotPermittedBeforeAppLaunch@206$"""
misc.update(
    {
        "BADownloadState": NewType("BADownloadState", int),
        "BAErrorCode": NewType("BAErrorCode", int),
        "BAContentRequest": NewType("BAContentRequest", int),
    }
)
misc.update(
    {
        "BADownloadState": NewType("BADownloadState", int),
        "BADownloaderPriority": NewType("BADownloaderPriority", int),
    }
)
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b"BADownload", b"isEssential", {"retval": {"type": b"Z"}})
    r(
        b"BADownloadManager",
        b"cancelDownload:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"BADownloadManager",
        b"etchCurrentDownloads:",
        {"arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"BADownloadManager",
        b"fetchCurrentDownloads:",
        {"arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"BADownloadManager",
        b"fetchCurrentDownloadsWithCompletionHandler:",
        {
            "arguments": {
                2: {
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
    r(
        b"BADownloadManager",
        b"performWithExclusiveControl:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"Z"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"BADownloadManager",
        b"performWithExclusiveControlBeforeDate:performHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"Z"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"BADownloadManager",
        b"scheduleDownload:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"BADownloadManager",
        b"startForegroundDownload:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"BAURLDownload",
        b"initWithIdentifier:request:essential:fileSize:applicationGroupIdentifier:priority:",
        {"arguments": {4: {"type": b"Z"}}},
    )
    r(
        b"NSObject",
        b"backgroundDownload:didReceiveChallenge:completionHandler:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"q"},
                            2: {"type": b"@"},
                        },
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"backgroundDownload:failedWithError:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"backgroundDownload:finishedWithFileURL:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"download:didReceiveChallenge:completionHandler:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"q"},
                            2: {"type": b"@"},
                        },
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"download:didWriteBytes:totalBytesWritten:totalBytesExpectedToWrite:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"q"},
                4: {"type": b"q"},
                5: {"type": b"q"},
            },
        },
    )
    r(
        b"NSObject",
        b"download:failedWithError:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"download:finishedWithFileURL:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"downloadDidBegin:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"downloadDidPause:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"downloadsForRequest:manifestURL:extensionInfo:",
        {
            "required": False,
            "retval": {"type": b"@"},
            "arguments": {2: {"type": b"q"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"extensionWillTerminate",
        {"required": False, "retval": {"type": b"v"}},
    )
finally:
    objc._updatingMetadata(False)

objc.registerNewKeywordsFromSelector(
    "BAURLDownload", b"initWithIdentifier:request:applicationGroupIdentifier:"
)
objc.registerNewKeywordsFromSelector(
    "BAURLDownload", b"initWithIdentifier:request:applicationGroupIdentifier:priority:"
)
objc.registerNewKeywordsFromSelector(
    "BAURLDownload",
    b"initWithIdentifier:request:essential:fileSize:applicationGroupIdentifier:priority:",
)
objc.registerNewKeywordsFromSelector(
    "BAURLDownload", b"initWithIdentifier:request:fileSize:applicationGroupIdentifier:"
)
expressions = {}

# END OF FILE
