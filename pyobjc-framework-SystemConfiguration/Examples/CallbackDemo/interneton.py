#!/usr/bin/env python
"""
Tells whether the internet is available using the SystemConfiguration
framework.

Usage:
    python internetison [address]
"""
from __future__ import print_function
from SystemConfiguration import kSCNetworkFlagsTransientConnection, kSCNetworkFlagsReachable
from SystemConfiguration import kSCNetworkFlagsConnectionRequired, kSCNetworkFlagsConnectionAutomatic
from SystemConfiguration import kSCNetworkFlagsInterventionRequired, kSCNetworkFlagsIsLocalAddress
from SystemConfiguration import kSCNetworkFlagsIsDirect, SCNetworkReachabilityCreateWithAddress
from SystemConfiguration import SCNetworkReachabilitySetCallback, SCNetworkReachabilityGetFlags
from SystemConfiguration import SCNetworkReachabilityScheduleWithRunLoop
from Cocoa import CFRunLoopGetCurrent, CFRunLoopStop, CFRunLoopRun
import socket, sys

def resultAvailable(target, flags, info):
    print("got network reachability status for %s:"%(info,))

    if flags & kSCNetworkFlagsTransientConnection:
        print("- transient connection")

    if flags &  kSCNetworkFlagsReachable:
        print("- reachable")

    if flags &  kSCNetworkFlagsConnectionRequired:
        print("- connection required")

    if flags &  kSCNetworkFlagsConnectionAutomatic:
        print("- connection automatic")

    if flags &  kSCNetworkFlagsInterventionRequired:
        print("- user intervention required")

    if flags &  kSCNetworkFlagsIsLocalAddress:
        print("- local interface")

    if flags &  kSCNetworkFlagsIsDirect:
        print("- directly attached network")

    # And stop the program:
    loop = CFRunLoopGetCurrent()
    CFRunLoopStop(loop)


def main():
    if len(sys.argv) >= 2:
        addr = socket.gethostbyname(sys.argv[1])
    else:
        addr = "82.94.237.218" # www.python.org

    loop = CFRunLoopGetCurrent()

    target = SCNetworkReachabilityCreateWithAddress(None, (addr, 80))
    SCNetworkReachabilitySetCallback(target, resultAvailable, addr)

    ok, flags = SCNetworkReachabilityGetFlags(target, None)
    if ok:
        resultAvailable(target, flags, addr)

    else:
        ok = SCNetworkReachabilityScheduleWithRunLoop(target,
                loop, kCFRunLoopCommonModes)

        CFRunLoopRun()

if __name__ == "__main__":
    main()
