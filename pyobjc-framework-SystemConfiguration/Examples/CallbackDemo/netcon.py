#!/usr/bin/env python
"""
Exercise some API's related to SCNetworkConnection.

NOTE: this example doesn't actually work yet as the author of this script 
doesn't use PPP :-)

Usage:
    python netcon.py
"""
from SystemConfiguration import *

def connectionChanged(connection, status, info):
    print "Status of %s connection changed: %s"(info, status)


def main():
    conn = SCNetworkConnectionCreateWithServiceID(None, 
            "Automatic",
            connectionChanged,
            "foobar")

    print conn
    assert conn is not None

    loop = CFRunLoopGetCurrent()
    SCNetworkConnectionScheduleWithRunLoop(conn, loop, kCFRunLoopCommonModes)
    CFRunLoopRun()

if __name__ == "__main__":
    main()
