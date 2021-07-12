#!/usr/bin/env python
"""
Tells whether the internet is available using the SystemConfiguration
framework.

Usage:
    python internetison [address]
"""
import socket
import sys

from Cocoa import (
    CFRunLoopGetCurrent,
    CFRunLoopRun,
    CFRunLoopStop,
    kCFRunLoopCommonModes,
)
from SystemConfiguration import (
    SCNetworkReachabilityCreateWithAddress,
    SCNetworkReachabilityGetFlags,
    SCNetworkReachabilityScheduleWithRunLoop,
    SCNetworkReachabilitySetCallback,
    kSCNetworkFlagsConnectionAutomatic,
    kSCNetworkFlagsConnectionRequired,
    kSCNetworkFlagsInterventionRequired,
    kSCNetworkFlagsIsDirect,
    kSCNetworkFlagsIsLocalAddress,
    kSCNetworkFlagsReachable,
    kSCNetworkFlagsTransientConnection,
)


def resultAvailable(target, flags, info):
    print(f"got network reachability status for {info}:")

    if flags & kSCNetworkFlagsTransientConnection:
        print("- transient connection")

    if flags & kSCNetworkFlagsReachable:
        print("- reachable")

    if flags & kSCNetworkFlagsConnectionRequired:
        print("- connection required")

    if flags & kSCNetworkFlagsConnectionAutomatic:
        print("- connection automatic")

    if flags & kSCNetworkFlagsInterventionRequired:
        print("- user intervention required")

    if flags & kSCNetworkFlagsIsLocalAddress:
        print("- local interface")

    if flags & kSCNetworkFlagsIsDirect:
        print("- directly attached network")

    # And stop the program:
    loop = CFRunLoopGetCurrent()
    CFRunLoopStop(loop)


def main():
    if len(sys.argv) >= 2:
        addr = socket.gethostbyname(sys.argv[1])
    else:
        addr = "82.94.237.218"  # www.python.org

    loop = CFRunLoopGetCurrent()

    target = SCNetworkReachabilityCreateWithAddress(None, (addr, 80))
    SCNetworkReachabilitySetCallback(target, resultAvailable, addr)

    ok, flags = SCNetworkReachabilityGetFlags(target, None)
    if ok:
        resultAvailable(target, flags, addr)

    else:
        ok = SCNetworkReachabilityScheduleWithRunLoop(
            target, loop, kCFRunLoopCommonModes
        )

        CFRunLoopRun()


if __name__ == "__main__":
    main()
