#!/usr/bin/env python
"""
A simple script for toggling the power to the WLAN adaptor

NOTE: Running this script might require administrator
      privileges (depending on the macOS settings)
"""

import sys

import CoreWLAN

iface = CoreWLAN.CWInterface.interface()

ok, error = iface.setPower_error_(not iface.powerOn(), None)
if ok:
    print(
        "Toggled WLAN power, current state is {}".format(
            "on" if iface.powerOn() else "off"
        )
    )

    sys.exit(0)
else:
    print(f"Could not toggle WLAN power: {error.localizedDescription()}")

    sys.exit(1)
