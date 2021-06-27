"""
Helper script for performing smoke tests on an installed
copy of PyObjC

# NOTE: This file is not yet complete
"""

import platform
from setuptools._distutils.version import LooseVersion

import objc  # noqa: F401
from AddressBook import *  # noqa: F401, F403
from AppleScriptKit import *  # noqa: F401, F403
from AppleScriptObjC import *  # noqa: F401, F403
from ApplicationServices import *  # noqa: F401, F403
from Automator import *  # noqa: F401, F403
from CFNetwork import *  # noqa: F401, F403
from Cocoa import *  # noqa: F401, F403
from CoreData import *  # noqa: F401, F403
from CoreServices import *  # noqa: F401, F403
from DiskArbitration import *  # noqa: F401, F403
from ExceptionHandling import *  # noqa: F401, F403
from GameController import *  # noqa: F401, F403
from HIServices import *  # noqa: F401, F403
from Quartz import *  # noqa: F401, F403

sys_version = LooseVersion(platform.mac_ver()[0])


if sys_version >= LooseVersion("10.5"):
    from CalendarStore import *  # noqa: F401, F403
    from Collaboration import *  # noqa: F401, F403
    from CoreText import *  # noqa: F401, F403
    from DictionaryServices import *  # noqa: F401, F403
    from FSEvents import *  # noqa: F401, F403

if sys_version >= LooseVersion("10.6"):
    from CoreLocation import *  # noqa: F401, F403
    from CoreWLAN import *  # noqa: F401, F403

    from iTunesLibrary import *  # noqa: F401, F403


if sys_version >= LooseVersion("10.7"):
    from AVFoundation import *  # noqa: F401, F403

if sys_version >= LooseVersion("10.8"):
    from Accounts import *  # noqa: F401, F403
    from EventKit import *  # noqa: F401, F403
    from GameCenter import *  # noqa: F401, F403

if sys_version >= LooseVersion("10.9"):
    from AVKit import *  # noqa: F401, F403

if sys_version >= LooseVersion("10.10"):
    from CloudKit import *  # noqa: F401, F403
    from CoreBluetooth import *  # noqa: F401, F403
    from CryptoTokenKit import *  # noqa: F401, F403
    from FinderSync import *  # noqa: F401, F403

if sys_version >= LooseVersion("10.11"):
    from Contacts import *  # noqa: F401, F403
    from ContactsUI import *  # noqa: F401, F403

if sys_version >= LooseVersion("10.12"):
    from Intents import *  # noqa: F401, F403
    from MediaPlayer import *  # noqa: F401, F403

if sys_version >= LooseVersion("10.13"):
    from BusinessChat import *  # noqa: F401, F403
    from ColorSync import *  # noqa: F401, F403
    from CoreML import *  # noqa: F401, F403
    from CoreSpotlight import *  # noqa: F401, F403
    from ExternalAccessory import *  # noqa: F401, F403
    from Vision import *  # noqa: F401, F403

print("")
print("SMOKE TEST PASSED")
print("")
