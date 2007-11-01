"""
Display the useful contents of /var/db/dhcpd_leases

This lets you see what IP addresses are leased out when using
Internet Connection Sharing
"""

from PyObjCTools import AppHelper

# import classes required to start application
import TableModelAppDelegate

# start the event loop
AppHelper.runEventLoop(argv=[], installInterrupt=False)
